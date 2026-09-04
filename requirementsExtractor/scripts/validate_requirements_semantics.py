"""Validate cross-references that standard JSON Schema cannot express.

Run this after structural validation against extracted_requirements.schema.json.
The validator has no third-party dependencies and never mutates the input.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


ARTIFACT_COLLECTIONS = (
    "functional_requirements",
    "non_functional_requirements",
    "business_rules",
    "assumptions",
    "constraints",
    "dependencies",
)
ID_COLLECTIONS = ("sources", "stakeholders", *ARTIFACT_COLLECTIONS, "open_items", "conflicts")
EVIDENCE_COLLECTIONS = (
    "stakeholders",
    "functional_requirements",
    "non_functional_requirements",
    "business_rules",
    "assumptions",
    "constraints",
    "dependencies",
)


def _items(data: dict[str, Any], collection: str, errors: list[str]) -> list[dict[str, Any]]:
    value = data.get(collection, [])
    if not isinstance(value, list):
        errors.append(f"{collection}: expected an array")
        return []
    objects: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        if isinstance(item, dict):
            objects.append(item)
        else:
            errors.append(f"{collection}[{index}]: expected an object")
    return objects


def _check_evidence(
    evidence: Any,
    path: str,
    source_ids: set[str],
    errors: list[str],
) -> None:
    if not isinstance(evidence, dict):
        errors.append(f"{path}: expected an evidence object")
        return
    source_id = evidence.get("source_id")
    if source_id not in source_ids:
        errors.append(f"{path}.source_id: unknown source {source_id!r}")


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    repeated: set[str] = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return repeated


def validate_semantics(data: Any) -> list[str]:
    """Return deterministic semantic errors; an empty list means success."""
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["root: expected an object"]

    collections = {name: _items(data, name, errors) for name in ID_COLLECTIONS}
    identified: list[tuple[str, str]] = []
    for name, entries in collections.items():
        for index, entry in enumerate(entries):
            entry_id = entry.get("id")
            if isinstance(entry_id, str):
                identified.append((entry_id, f"{name}[{index}].id"))
            else:
                errors.append(f"{name}[{index}].id: missing or non-string")

    for duplicate in sorted(_duplicates(item[0] for item in identified)):
        locations = ", ".join(path for item_id, path in identified if item_id == duplicate)
        errors.append(f"duplicate id {duplicate!r}: {locations}")

    source_ids = {item.get("id") for item in collections["sources"] if isinstance(item.get("id"), str)}
    artifacts = {
        item["id"]: item
        for name in ARTIFACT_COLLECTIONS
        for item in collections[name]
        if isinstance(item.get("id"), str)
    }
    open_items = {
        item["id"]: item
        for item in collections["open_items"]
        if isinstance(item.get("id"), str)
    }

    for collection in EVIDENCE_COLLECTIONS:
        for index, item in enumerate(collections[collection]):
            evidence_list = item.get("evidence", [])
            if not isinstance(evidence_list, list):
                errors.append(f"{collection}[{index}].evidence: expected an array")
                continue
            for evidence_index, evidence in enumerate(evidence_list):
                _check_evidence(
                    evidence,
                    f"{collection}[{index}].evidence[{evidence_index}]",
                    source_ids,
                    errors,
                )

    for conflict_index, conflict in enumerate(collections["conflicts"]):
        statements = conflict.get("statements", [])
        if not isinstance(statements, list):
            errors.append(f"conflicts[{conflict_index}].statements: expected an array")
            continue
        for statement_index, statement in enumerate(statements):
            if not isinstance(statement, dict):
                errors.append(
                    f"conflicts[{conflict_index}].statements[{statement_index}]: expected an object"
                )
                continue
            _check_evidence(
                statement.get("evidence"),
                f"conflicts[{conflict_index}].statements[{statement_index}].evidence",
                source_ids,
                errors,
            )

    functional = {
        item["id"]: item
        for item in collections["functional_requirements"]
        if isinstance(item.get("id"), str)
    }
    for requirement_id, requirement in functional.items():
        if requirement.get("level") == "global":
            if "parent_id" in requirement:
                errors.append(f"{requirement_id}.parent_id: a global requirement cannot have a parent")
            continue
        if requirement.get("level") != "detallado":
            continue
        parent_id = requirement.get("parent_id")
        parent = functional.get(parent_id)
        if parent is None:
            errors.append(f"{requirement_id}.parent_id: unknown functional requirement {parent_id!r}")
        elif parent.get("level") != "global":
            errors.append(f"{requirement_id}.parent_id: {parent_id!r} is not global")

    for name in ("open_items", "conflicts"):
        for index, item in enumerate(collections[name]):
            target_ids = item.get("target_ids", [])
            if not isinstance(target_ids, list):
                errors.append(f"{name}[{index}].target_ids: expected an array")
                continue
            if not target_ids:
                errors.append(f"{name}[{index}].target_ids: at least one artifact is required")
            for target_id in target_ids:
                if target_id not in artifacts:
                    errors.append(f"{name}[{index}].target_ids: unknown artifact {target_id!r}")

    derived_ids: set[str] = set()
    for artifact_id, artifact in artifacts.items():
        if artifact.get("origin") == "derivado":
            derived_ids.add(artifact_id)
            if artifact.get("status") != "pendiente_validacion":
                errors.append(f"{artifact_id}: a derived artifact must remain pendiente_validacion")
            if not isinstance(artifact.get("derivation"), str) or not artifact["derivation"].strip():
                errors.append(f"{artifact_id}: a derived artifact requires a derivation")
            evidence = artifact.get("evidence")
            evidence_entries = evidence if isinstance(evidence, list) else []
            distinct_locations = {
                (entry.get("source_id", "").strip(), entry.get("locator", "").strip())
                for entry in evidence_entries
                if isinstance(entry, dict)
                and isinstance(entry.get("source_id"), str)
                and isinstance(entry.get("locator"), str)
            }
            if not isinstance(evidence, list) or len(distinct_locations) < 2:
                errors.append(
                    f"{artifact_id}: a derived artifact requires at least two distinct evidence locations"
                )

    for assumption in collections["assumptions"]:
        if (
            assumption.get("basis") == "hipotesis_analista"
            and assumption.get("status") != "pendiente_validacion"
        ):
            errors.append(
                f"{assumption.get('id')}: an analyst hypothesis must remain pendiente_validacion"
            )

    unresolved_targets = {
        target_id
        for item in collections["open_items"]
        if item.get("status") in {"abierto", "diferido"}
        for target_id in item.get("target_ids", [])
    }
    for artifact_id, artifact in artifacts.items():
        if artifact.get("status") == "TBD" and artifact_id not in unresolved_targets:
            errors.append(f"{artifact_id}: TBD requires a linked unresolved open item")

    coverage = data.get("coverage_control")
    if not isinstance(coverage, dict):
        errors.append("coverage_control: expected an object")
        return errors

    reviewed = set(coverage.get("reviewed_source_ids", []))
    pending = set(coverage.get("pending_source_ids", []))
    for source_id in sorted((reviewed | pending) - source_ids):
        errors.append(f"coverage_control: unknown source {source_id!r}")
    for source_id in sorted(source_ids - (reviewed | pending)):
        errors.append(f"coverage_control: source {source_id!r} is neither reviewed nor pending")
    for source_id in sorted(reviewed & pending):
        errors.append(f"coverage_control: source {source_id!r} cannot be reviewed and pending")

    declared_derived = set(coverage.get("derived_pending_ids", []))
    for artifact_id in sorted(declared_derived - derived_ids):
        errors.append(f"coverage_control.derived_pending_ids: {artifact_id!r} is not derived")
    for artifact_id in sorted(derived_ids - declared_derived):
        errors.append(f"coverage_control.derived_pending_ids: missing {artifact_id!r}")

    blocking_open_ids = {
        item_id
        for item_id, item in open_items.items()
        if item.get("blocking") is True and item.get("status") in {"abierto", "diferido"}
    }
    declared_blocking = set(coverage.get("blocking_tbd_ids", []))
    for item_id in sorted(declared_blocking - blocking_open_ids):
        errors.append(
            f"coverage_control.blocking_tbd_ids: {item_id!r} is not an unresolved open blocker"
        )
    for item_id in sorted(blocking_open_ids - declared_blocking):
        errors.append(f"coverage_control.blocking_tbd_ids: missing {item_id!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate semantic references in a requirements register JSON"
    )
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[ERROR] Cannot read requirements JSON: {exc}", file=sys.stderr)
        return 1

    errors = validate_semantics(data)
    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 2
    print("[OK] Requirements semantic references are consistent.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
