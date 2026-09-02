#!/usr/bin/env python3
"""Serve a static frontend preview on loopback without third-party packages."""

from __future__ import annotations

import argparse
import functools
import http.server
import sys
from http import HTTPStatus
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    """Static handler with optional HTML fallback for client-side routes."""

    root: Path
    spa_fallback: bool

    def _validated_path(self, candidate: Path) -> Path | None:
        try:
            lexical_path = candidate.relative_to(self.root)
        except ValueError:
            return None

        current = self.root
        for part in lexical_path.parts:
            if part in {".", ".."} or part.startswith("."):
                return None
            current /= part
            if current.is_symlink() or (
                hasattr(current, "is_junction") and current.is_junction()
            ):
                return None

        resolved = candidate.resolve(strict=False)
        try:
            resolved.relative_to(self.root)
        except ValueError:
            return None
        return resolved

    def _safe_candidate(self) -> Path | None:
        request_path = unquote(urlsplit(self.path).path)
        parts = [part for part in PurePosixPath(request_path).parts if part != "/"]
        return self._validated_path(self.root.joinpath(*parts))

    def _host_is_allowed(self) -> bool:
        host_header = self.headers.get("Host", "")
        if not host_header or "@" in host_header or any(char.isspace() for char in host_header):
            return False
        try:
            parsed = urlsplit(f"//{host_header}")
            hostname = (parsed.hostname or "").lower().rstrip(".")
            _ = parsed.port
        except ValueError:
            return False
        return hostname in {"127.0.0.1", "localhost"}

    def _prepare_request(self) -> bool:
        if not self._host_is_allowed():
            self.send_error(HTTPStatus.MISDIRECTED_REQUEST, "Loopback Host header required")
            return False

        candidate = self._safe_candidate()
        if candidate is None:
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return False

        if not self.spa_fallback:
            return True

        accepts_html = "text/html" in self.headers.get("Accept", "")
        request_path = unquote(urlsplit(self.path).path)
        if request_path != "/" and not candidate.exists() and accepts_html:
            self.path = "/index.html"
        return True

    def do_GET(self) -> None:  # noqa: N802 - method name defined by stdlib
        if self._prepare_request():
            super().do_GET()

    def do_HEAD(self) -> None:  # noqa: N802 - method name defined by stdlib
        if self._prepare_request():
            super().do_HEAD()

    def send_head(self):  # type: ignore[no-untyped-def]
        candidate = self._safe_candidate()
        if candidate is None:
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return None

        if candidate.is_dir():
            for index_name in ("index.html", "index.htm"):
                index_candidate = candidate / index_name
                if index_candidate.exists():
                    if self._validated_path(index_candidate) is None:
                        self.send_error(HTTPStatus.NOT_FOUND, "Not found")
                        return None
                    break
        return super().send_head()

    def list_directory(self, path: str):  # type: ignore[no-untyped-def]
        self.send_error(HTTPStatus.NOT_FOUND, "Directory listing is disabled")
        return None

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()

    def log_message(self, message: str, *args: object) -> None:
        print(f"[preview] {self.address_string()} - {message % args}", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve static frontend files on localhost for interactive review."
    )
    parser.add_argument(
        "--root",
        required=True,
        help="Directory containing index.html and its static assets.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=0,
        help="TCP port. Use 0 (the default) to select a free port.",
    )
    parser.add_argument(
        "--spa",
        action="store_true",
        help="Serve index.html for missing browser routes that accept HTML.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        root = Path(args.root).expanduser().resolve(strict=True)
    except FileNotFoundError:
        print(f"error: preview root does not exist: {args.root}", file=sys.stderr)
        return 2

    if not root.is_dir():
        print(f"error: preview root is not a directory: {root}", file=sys.stderr)
        return 2
    if not (root / "index.html").is_file():
        print(f"error: index.html was not found under: {root}", file=sys.stderr)
        return 2
    if (root / "index.html").is_symlink():
        print("error: index.html must not be a symbolic link", file=sys.stderr)
        return 2
    if not 0 <= args.port <= 65535:
        print("error: --port must be between 0 and 65535", file=sys.stderr)
        return 2
    handler_type = type(
        "ConfiguredPreviewHandler",
        (PreviewHandler,),
        {"root": root, "spa_fallback": args.spa},
    )
    handler = functools.partial(handler_type, directory=str(root))

    try:
        server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except OSError as error:
        print(f"error: could not start preview server: {error}", file=sys.stderr)
        return 2

    _, selected_port = server.server_address[:2]
    preview_url = f"http://127.0.0.1:{selected_port}/"

    print(f"PREVIEW_ROOT={root}", flush=True)
    print(f"PREVIEW_URL={preview_url}", flush=True)
    print("Press Ctrl+C to stop the preview.", flush=True)

    try:
        server.serve_forever(poll_interval=0.2)
    except KeyboardInterrupt:
        print("\nPreview stopped.", flush=True)
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
