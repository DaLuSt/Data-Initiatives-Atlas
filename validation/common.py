"""Shared helpers for the validation/validate_*.py scripts.

Parses entity Markdown+YAML frontmatter and loads the controlled
vocabularies from metadata/schema.json, so each validator only has to
implement its own checks.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "metadata" / "schema.json"

# Top-level directories that hold entity files directly (by type).
FLAT_ENTITY_DIRS = [
    "initiatives", "legislation", "policies", "strategies", "standards",
    "frameworks", "programmes", "organisations", "data-spaces",
    "platforms", "publications", "domains",
]

# Geography roots: entity files here are the anchor entity + index.md only,
# one directory level down (countries/nl/, regions/eu/, international/un/).
GEOGRAPHY_ROOTS = ["countries", "regions", "international"]

# Directories excluded from all validation (illustrative content, not data).
EXCLUDE_DIR_NAMES = {"templates", ".git", ".github", "node_modules"}

# Files that are navigation/documentation, not entities, even though they
# live inside an entity directory.
NON_ENTITY_FILENAMES = {"README.md", "index.md"}

_FRONTMATTER_RE = re.compile(r"^---\n(.*?\n)---\n?(.*)$", re.DOTALL)
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]")


def load_schema() -> dict[str, Any]:
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


@dataclass
class EntityFile:
    path: Path
    frontmatter: dict[str, Any] | None
    body: str
    parse_error: str | None = None
    wikilinks: list[str] = field(default_factory=list)

    @property
    def rel_path(self) -> str:
        return str(self.path.relative_to(REPO_ROOT))


def _is_excluded(path: Path) -> bool:
    return any(part in EXCLUDE_DIR_NAMES for part in path.relative_to(REPO_ROOT).parts)


def iter_markdown_files(entities_only: bool = True):
    """Yield every Markdown file relevant to validation.

    entities_only=True restricts to files expected to carry entity
    frontmatter (used by ID/frontmatter/relationship/source checks).
    entities_only=False also includes index/README docs (used by the
    wikilink checker, since links can be authored there too).
    """
    seen: set[Path] = set()
    dirs = [REPO_ROOT / d for d in FLAT_ENTITY_DIRS]
    dirs += [REPO_ROOT / d for d in GEOGRAPHY_ROOTS]

    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*.md")):
            if _is_excluded(path) or path in seen:
                continue
            seen.add(path)
            if entities_only and path.name in NON_ENTITY_FILENAMES:
                continue
            yield path

    if not entities_only:
        for path in sorted(REPO_ROOT.rglob("*.md")):
            if path in seen or _is_excluded(path):
                continue
            seen.add(path)
            yield path


def parse_entity_file(path: Path) -> EntityFile:
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return EntityFile(path=path, frontmatter=None, body=text,
                           parse_error="No YAML frontmatter block found (expected leading '---' ... '---').")
    raw_fm, body = match.group(1), match.group(2)
    try:
        fm = yaml.safe_load(raw_fm)
    except yaml.YAMLError as exc:
        return EntityFile(path=path, frontmatter=None, body=body, parse_error=f"Malformed YAML: {exc}")
    if not isinstance(fm, dict):
        return EntityFile(path=path, frontmatter=None, body=body, parse_error="Frontmatter did not parse to a mapping.")
    wikilinks = _WIKILINK_RE.findall(text)
    return EntityFile(path=path, frontmatter=fm, body=body, wikilinks=wikilinks)


def load_all_entities(entities_only: bool = True) -> list[EntityFile]:
    return [parse_entity_file(p) for p in iter_markdown_files(entities_only=entities_only)]


def known_ids(entities: list[EntityFile]) -> set[str]:
    return {
        e.frontmatter["id"]
        for e in entities
        if e.frontmatter and isinstance(e.frontmatter.get("id"), str)
    }


class Report:
    """Collects errors/warnings and renders a summary; used by every script."""

    def __init__(self, name: str):
        self.name = name
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def print_and_exit_code(self) -> int:
        print(f"\n== {self.name} ==")
        if not self.errors and not self.warnings:
            print("OK — no issues found.")
            return 0
        for w in self.warnings:
            print(f"  WARN  {w}")
        for e in self.errors:
            print(f"  ERROR {e}")
        print(f"{len(self.errors)} error(s), {len(self.warnings)} warning(s).")
        return 1 if self.errors else 0
