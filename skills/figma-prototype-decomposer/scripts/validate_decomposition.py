#!/usr/bin/env python3
import json
import re
import sys
from collections import Counter
from pathlib import Path


LEVELS = {"E", "L1", "L2", "L3", "S"}
CONFIDENCE = {"fact", "analysis", "hypothesis"}
ACTIONS = {"click", "gesture", "back", "close", "sequence", "generate", "pay", "subscribe", "ad", "unknown"}
PAGE_ID = re.compile(r"^P\d{2,}$")


def fail(message):
    print(f"ERROR: {message}")
    return 1


def main(path_string):
    path = Path(path_string)
    data = json.loads(path.read_text(encoding="utf-8"))
    pages = data.get("pages", [])
    interactions = data.get("interactions", [])
    errors = []

    if not data.get("product"):
        errors.append("missing product")
    if not pages:
        errors.append("pages must not be empty")

    ids = [page.get("id") for page in pages]
    duplicates = [page_id for page_id, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate page ids: {', '.join(map(str, duplicates))}")

    page_by_id = {page.get("id"): page for page in pages}
    for index, page in enumerate(pages):
        label = page.get("id") or f"pages[{index}]"
        if not PAGE_ID.match(str(page.get("id", ""))):
            errors.append(f"{label}: invalid page id")
        if page.get("level") not in LEVELS:
            errors.append(f"{label}: invalid level {page.get('level')!r}")
        if not page.get("module") or not page.get("group"):
            errors.append(f"{label}: module and group are required")
        if page.get("confidence") not in CONFIDENCE:
            errors.append(f"{label}: invalid confidence {page.get('confidence')!r}")
        if page.get("level") == "S" and not page.get("parent"):
            errors.append(f"{label}: S state requires parent")
        if page.get("parent") and page.get("parent") not in page_by_id:
            errors.append(f"{label}: unknown parent {page.get('parent')}")

    hotspot_destinations = {}
    for index, interaction in enumerate(interactions):
        label = f"interactions[{index}]"
        source = interaction.get("from")
        target = interaction.get("to")
        hotspot = interaction.get("hotspot")
        if source not in page_by_id:
            errors.append(f"{label}: unknown source {source}")
        if target not in page_by_id and interaction.get("action") != "unknown":
            errors.append(f"{label}: unknown target {target}")
        if not hotspot:
            errors.append(f"{label}: hotspot is required")
        if interaction.get("action") not in ACTIONS:
            errors.append(f"{label}: invalid action {interaction.get('action')!r}")
        if interaction.get("confidence") not in CONFIDENCE:
            errors.append(f"{label}: invalid confidence {interaction.get('confidence')!r}")
        key = (source, hotspot)
        if key in hotspot_destinations and hotspot_destinations[key] != target:
            errors.append(f"{label}: hotspot {source}/{hotspot} has conflicting destinations")
        hotspot_destinations[key] = target
        if interaction.get("commercial") is True:
            source_page = page_by_id.get(source, {})
            target_page = page_by_id.get(target, {})
            if not source_page.get("commercial") and not target_page.get("commercial"):
                errors.append(f"{label}: commercial interaction has no commercial endpoint metadata")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    module_count = len({page["module"] for page in pages})
    group_count = len({(page["module"], page["group"]) for page in pages})
    commercial_count = sum(bool(page.get("commercial")) for page in pages)
    level_counts = dict(Counter(page["level"] for page in pages))
    print(
        f"OK: {len(pages)} pages, {module_count} modules, {group_count} groups, "
        f"{len(interactions)} interactions, {commercial_count} commercial pages, levels {level_counts}"
    )
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {Path(sys.argv[0]).name} decomposition.json")
    raise SystemExit(main(sys.argv[1]))
