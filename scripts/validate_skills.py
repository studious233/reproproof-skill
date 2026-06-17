#!/usr/bin/env python3
"""Lightweight repository validation for ReproProof Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT
REQUIRED_ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
]
MOJIBAKE_MARKERS = [
    "\u9225",
    "\u9242",
    "\u6402",
    "\u9286",
    "\u7f01",
    "\u9340",
    "\u95ab",
    "\u922b",
    "\u922e",
    "\u9236",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def validate_frontmatter(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        fail(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")

    text = read_text(skill_file)
    if not text.startswith("---\n"):
        fail(f"{skill_file.relative_to(ROOT)} must start with YAML frontmatter")

    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{skill_file.relative_to(ROOT)} has malformed YAML frontmatter")

    frontmatter = match.group(1)
    fields = {}
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{skill_file.relative_to(ROOT)} frontmatter line is invalid: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    allowed = {"name", "description"}
    extra = set(fields) - allowed
    if extra:
        fail(f"{skill_file.relative_to(ROOT)} has unsupported frontmatter fields: {sorted(extra)}")

    for key in sorted(allowed):
        if key not in fields or not fields[key]:
            fail(f"{skill_file.relative_to(ROOT)} is missing frontmatter field: {key}")

    name = fields["name"]
    if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
        fail(f"{skill_file.relative_to(ROOT)} has invalid skill name: {name}")
    if skill_dir.name != name:
        fail(f"{skill_file.relative_to(ROOT)} name does not match folder: {name} != {skill_dir.name}")


def validate_text_files() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".mdc", ".json", ".py", ".txt", ".yaml", ".yml"}:
            continue
        text = read_text(path)
        found = [marker for marker in MOJIBAKE_MARKERS if marker in text]
        if found:
            fail(f"{path.relative_to(ROOT)} contains mojibake markers: {', '.join(found)}")


def main() -> int:
    for filename in REQUIRED_ROOT_FILES:
        if not (ROOT / filename).exists():
            fail(f"missing required root file: {filename}")

    skill_dirs = [ROOT / "reproproof"]
    if not skill_dirs:
        fail("no skills found")

    for skill_dir in skill_dirs:
        validate_frontmatter(skill_dir)

    validate_text_files()

    print(f"OK: validated {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
