#!/usr/bin/env python3
"""Upstream Source Checker for Humanizer Skill.

Verifies the state and detects changes across all upstream sources defined in skills-lock.json:
- zed-industries/zed (.factory/skills/humanizer/SKILL.md)
- vercel/eve (.agents/skills/technical-writing/SKILL.md)
- humanizerai/agent-skills (skills/humanize/SKILL.md)
- momo2young/humanize-academic-writing (SKILL.md)
- factory-ai/factory-plugins (plugins/droid-evolved/skills/human-writing/SKILL.md)

Supports:
- Checking remote commit SHA and file SHA256 via GitHub REST API / raw content
- Checking against local cache in .agents/skills/
- Offline mode for airgapped or test environments
- Updating skills-lock.json with new computed hashes when requested (--update-lock)
- Outputting human-readable reports or structured JSON (--json)

Zero external dependencies (uses Python standard library).
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class UpstreamCheckResult:
    """Result of checking an upstream skill source."""

    skill_name: str
    source_repo: str
    skill_path: str
    lock_hash: str
    local_hash: Optional[str]
    remote_hash: Optional[str]
    remote_blob_sha: Optional[str]
    latest_commit: Optional[str]
    latest_commit_date: Optional[str]
    status: str  # UP_TO_DATE, CHANGED, LOCAL_ONLY, ERROR, NOT_FOUND
    message: str
    downloaded_content: Optional[str] = None


def find_lockfile(start_path: Optional[Path] = None) -> Optional[Path]:
    """Find skills-lock.json starting from current directory or parent paths."""
    search_dir = (start_path or Path.cwd()).resolve()
    for directory in [search_dir, *search_dir.parents]:
        lock_candidate = directory / "skills-lock.json"
        if lock_candidate.is_file():
            return lock_candidate
    return None


def compute_sha256(data: bytes) -> str:
    """Compute standard hex SHA-256 digest of bytes."""
    return hashlib.sha256(data).hexdigest()


def get_local_cache_content(repo_root: Path, skill_name: str) -> Optional[Tuple[bytes, str]]:
    """Retrieve content and hash of local cached skill in .agents/skills/."""
    candidates = [
        repo_root / ".agents" / "skills" / skill_name / "SKILL.md",
        repo_root / ".agents" / "skills" / skill_name / "skill.md",
    ]
    for cand in candidates:
        if cand.is_file():
            content = cand.read_bytes()
            return content, compute_sha256(content)
    return None


def fetch_github_content(
    source_repo: str,
    skill_path: str,
    token: Optional[str] = None,
    timeout: int = 8,
) -> Tuple[Optional[bytes], Optional[str], Optional[str], Optional[str]]:
    """Fetch file content, blob SHA, latest commit SHA and date from GitHub API.

    Returns:
        (content_bytes, blob_sha, latest_commit_sha, latest_commit_date)
    """
    headers = {
        "User-Agent": "Antigravity-Humanizer-Sync/1.0",
        "Accept": "application/vnd.github.v3+json",
    }
    if token:
        headers["Authorization"] = f"token {token}"

    content_bytes: Optional[bytes] = None
    blob_sha: Optional[str] = None
    commit_sha: Optional[str] = None
    commit_date: Optional[str] = None

    # 1. Fetch file contents and blob sha
    content_url = f"https://api.github.com/repos/{source_repo}/contents/{skill_path}"
    try:
        req = urllib.request.Request(content_url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                body = json.loads(resp.read().decode("utf-8"))
                blob_sha = body.get("sha")
                raw_b64 = body.get("content", "")
                if raw_b64:
                    content_bytes = base64.b64decode(raw_b64)
    except urllib.error.HTTPError as e:
        if e.code == 403 and "rate limit" in str(e).lower():
            pass  # Fallback to raw below
        elif e.code == 404:
            pass
    except Exception:
        pass

    # 2. If content API failed, fallback to raw.githubusercontent.com
    if content_bytes is None:
        raw_branches = ["HEAD", "main", "master"]
        for branch in raw_branches:
            raw_url = f"https://raw.githubusercontent.com/{source_repo}/{branch}/{skill_path}"
            try:
                req = urllib.request.Request(raw_url, headers={"User-Agent": headers["User-Agent"]})
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    if resp.status == 200:
                        content_bytes = resp.read()
                        break
            except Exception:
                continue

    # 3. Fetch latest commit metadata for the path
    commit_url = f"https://api.github.com/repos/{source_repo}/commits?path={skill_path}&per_page=1"
    try:
        req = urllib.request.Request(commit_url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                commits = json.loads(resp.read().decode("utf-8"))
                if commits and isinstance(commits, list):
                    latest = commits[0]
                    commit_sha = latest.get("sha")
                    commit_date = latest.get("commit", {}).get("committer", {}).get("date")
    except Exception:
        pass

    return content_bytes, blob_sha, commit_sha, commit_date


def check_source(
    skill_name: str,
    skill_info: Dict[str, Any],
    repo_root: Path,
    offline: bool = False,
    token: Optional[str] = None,
    timeout: int = 8,
) -> UpstreamCheckResult:
    """Check a single upstream skill entry from skills-lock.json."""
    source_repo = skill_info.get("source", "")
    skill_path = skill_info.get("skillPath", "")
    lock_hash = skill_info.get("computedHash", "")

    # Local cache check
    local_info = get_local_cache_content(repo_root, skill_name)
    local_bytes, local_hash = local_info if local_info else (None, None)

    if offline:
        if local_hash:
            matches = (local_hash == lock_hash)
            status = "UP_TO_DATE" if matches else "CHANGED"
            msg = "Local cache verified (offline mode)"
        else:
            status = "NOT_FOUND"
            msg = "No local cache found in .agents/skills/ (offline mode)"
        return UpstreamCheckResult(
            skill_name=skill_name,
            source_repo=source_repo,
            skill_path=skill_path,
            lock_hash=lock_hash,
            local_hash=local_hash,
            remote_hash=None,
            remote_blob_sha=None,
            latest_commit=None,
            latest_commit_date=None,
            status=status,
            message=msg,
        )

    # Remote check via GitHub
    try:
        content_bytes, blob_sha, commit_sha, commit_date = fetch_github_content(
            source_repo, skill_path, token=token, timeout=timeout
        )
    except Exception as e:
        return UpstreamCheckResult(
            skill_name=skill_name,
            source_repo=source_repo,
            skill_path=skill_path,
            lock_hash=lock_hash,
            local_hash=local_hash,
            remote_hash=None,
            remote_blob_sha=None,
            latest_commit=None,
            latest_commit_date=None,
            status="ERROR",
            message=f"Network error: {e}",
        )

    if content_bytes is None:
        # Fallback to local if remote unreachable
        if local_hash:
            matches = (local_hash == lock_hash)
            return UpstreamCheckResult(
                skill_name=skill_name,
                source_repo=source_repo,
                skill_path=skill_path,
                lock_hash=lock_hash,
                local_hash=local_hash,
                remote_hash=None,
                remote_blob_sha=None,
                latest_commit=None,
                latest_commit_date=None,
                status="LOCAL_ONLY" if matches else "CHANGED",
                message="Remote unreachable (rate-limit/network); verified via local cache",
            )
        return UpstreamCheckResult(
            skill_name=skill_name,
            source_repo=source_repo,
            skill_path=skill_path,
            lock_hash=lock_hash,
            local_hash=None,
            remote_hash=None,
            remote_blob_sha=None,
            latest_commit=None,
            latest_commit_date=None,
            status="ERROR",
            message="Unable to fetch remote file and no local cache available",
        )

    remote_hash = compute_sha256(content_bytes)
    # Check if up to date: matches lock hash or matches local hash
    if remote_hash == lock_hash or (local_hash and remote_hash == local_hash and lock_hash == local_hash):
        status = "UP_TO_DATE"
        msg = "Remote matches lockfile and local source."
    else:
        status = "CHANGED"
        msg = f"Remote content updated (remote: {remote_hash[:8]} vs lock: {lock_hash[:8]})"

    return UpstreamCheckResult(
        skill_name=skill_name,
        source_repo=source_repo,
        skill_path=skill_path,
        lock_hash=lock_hash,
        local_hash=local_hash,
        remote_hash=remote_hash,
        remote_blob_sha=blob_sha,
        latest_commit=commit_sha,
        latest_commit_date=commit_date,
        status=status,
        message=msg,
        downloaded_content=content_bytes.decode("utf-8", errors="replace"),
    )


def check_all_upstreams(
    lock_path: Path,
    offline: bool = False,
    token: Optional[str] = None,
    timeout: int = 8,
) -> List[UpstreamCheckResult]:
    """Check all upstreams defined in skills-lock.json."""
    if not lock_path.is_file():
        raise FileNotFoundError(f"skills-lock.json not found at {lock_path}")

    lock_data = json.loads(lock_path.read_text(encoding="utf-8"))
    skills = lock_data.get("skills", {})
    repo_root = lock_path.parent

    results: List[UpstreamCheckResult] = []
    for skill_name, info in skills.items():
        res = check_source(
            skill_name=skill_name,
            skill_info=info,
            repo_root=repo_root,
            offline=offline,
            token=token,
            timeout=timeout,
        )
        results.append(res)
    return results


def update_lockfile_hashes(lock_path: Path, results: List[UpstreamCheckResult]) -> int:
    """Update computedHash in skills-lock.json for changed skills. Returns count of updated entries."""
    if not lock_path.is_file():
        return 0

    lock_data = json.loads(lock_path.read_text(encoding="utf-8"))
    updated_count = 0

    for res in results:
        target_hash = res.remote_hash or res.local_hash
        if target_hash and target_hash != res.lock_hash:
            if res.skill_name in lock_data.get("skills", {}):
                lock_data["skills"][res.skill_name]["computedHash"] = target_hash
                updated_count += 1

    if updated_count > 0:
        lock_path.write_text(json.dumps(lock_data, indent=2) + "\n", encoding="utf-8")

    return updated_count


def sync_local_cache(repo_root: Path, results: List[UpstreamCheckResult]) -> int:
    """Sync downloaded remote content into .agents/skills/{name}/SKILL.md. Returns count of written files."""
    synced_count = 0
    for res in results:
        if res.downloaded_content and res.status == "CHANGED":
            target_file = repo_root / ".agents" / "skills" / res.skill_name / "SKILL.md"
            target_file.parent.mkdir(parents=True, exist_ok=True)
            target_file.write_text(res.downloaded_content, encoding="utf-8")
            synced_count += 1
    return synced_count


def format_report(results: List[UpstreamCheckResult], lock_path: Path) -> str:
    """Format human-readable CLI report."""
    lines: List[str] = [
        "=" * 80,
        "VERIFICACION DE FUENTES UPSTREAM - SKILL HUMANIZER",
        f"Lockfile: {lock_path}",
        "=" * 80,
        f"{'SKILL':<26} {'ESTADO':<14} {'LOCK HASH':<10} {'REMOTE/LOCAL':<12} {'DETALLES'}",
        "-" * 80,
    ]

    has_changes = False
    for r in results:
        cur_hash = (r.remote_hash or r.local_hash or "N/A")[:8]
        lock_short = r.lock_hash[:8] if r.lock_hash else "N/A"
        status_disp = r.status
        if r.status == "CHANGED":
            has_changes = True
            status_disp = "MODIFICADO"
        elif r.status in ("UP_TO_DATE", "LOCAL_ONLY"):
            status_disp = "AL DIA"
        elif r.status == "ERROR":
            status_disp = "ERROR"

        details = r.message
        if r.latest_commit:
            details += f" (commit {r.latest_commit[:7]})"

        lines.append(f"{r.skill_name:<26} {status_disp:<14} {lock_short:<10} {cur_hash:<12} {details}")

    lines.append("-" * 80)
    if has_changes:
        lines.append("[!] Se detectaron diferencias o actualizaciones en las fuentes upstream.")
        lines.append("    Ejecuta con `--update-lock` y `--sync-cache` para sincronizar la configuracion.")
    else:
        lines.append("[OK] Todas las fuentes upstream estan sincronizadas con la configuracion actual.")
    lines.append("=" * 80)
    return "\n".join(lines)


def main() -> int:
    """CLI entry point."""
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        description="Verifica y sincroniza fuentes upstream de la skill humanizer."
    )
    parser.add_argument(
        "--lock-file",
        type=Path,
        default=None,
        help="Ruta a skills-lock.json (por defecto busca en el árbol de directorios).",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Modo offline: verifica únicamente la caché local en .agents/skills/.",
    )
    parser.add_argument(
        "--update-lock",
        action="store_true",
        help="Actualiza skills-lock.json con los nuevos hashes detectados.",
    )
    parser.add_argument(
        "--sync-cache",
        action="store_true",
        help="Descarga y sincroniza los contenidos remotos en .agents/skills/.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emite el resultado en formato JSON estructurado.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=8,
        help="Tiempo de espera en segundos para consultas HTTP (por defecto 8s).",
    )
    parser.add_argument(
        "--token",
        type=str,
        default=os.environ.get("GITHUB_TOKEN"),
        help="Token de GitHub para autenticar peticiones a la API (o env GITHUB_TOKEN).",
    )

    args = parser.parse_args()

    lock_path = args.lock_file or find_lockfile()
    if not lock_path or not lock_path.is_file():
        print("Error: No se encontró skills-lock.json en el repositorio.", file=sys.stderr)
        return 1

    try:
        results = check_all_upstreams(
            lock_path=lock_path,
            offline=args.offline,
            token=args.token,
            timeout=args.timeout,
        )
    except Exception as err:
        print(f"Error fatal durante la verificación: {err}", file=sys.stderr)
        return 1

    if args.sync_cache:
        synced = sync_local_cache(lock_path.parent, results)
        if not args.json:
            print(f"Se sincronizaron {synced} archivos en .agents/skills/.")

    if args.update_lock:
        updated = update_lockfile_hashes(lock_path, results)
        if not args.json:
            print(f"Se actualizaron {updated} entradas en {lock_path.name}.")

    if args.json:
        payload = {
            "lockfile": str(lock_path),
            "total_sources": len(results),
            "has_changes": any(r.status == "CHANGED" for r in results),
            "results": [asdict(r) for r in results],
        }
        print(json.dumps(payload, indent=2))
    else:
        print(format_report(results, lock_path))

    return 0


if __name__ == "__main__":
    sys.exit(main())
