#!/usr/bin/env python3
"""Dependency-free structural validation for the adhd-execution package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "adhd-execution"
SKILL = SKILL_DIR / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter is not closed")
    return text[4:end], text[end + 5 :]


def scalar(block: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", block, re.MULTILINE)
    if not match:
        fail(f"missing frontmatter field: {key}")
    return match.group(1).strip('"\'')


def validate_skill() -> None:
    text = SKILL.read_text(encoding="utf-8")
    fm, body = frontmatter(text)
    name = scalar(fm, "name")
    description = scalar(fm, "description")
    license_name = scalar(fm, "license")

    if name != SKILL_DIR.name:
        fail("skill name must match its parent directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("skill name is not Agent Skills compliant")
    if len(name) > 64:
        fail("skill name exceeds 64 characters")
    if not 1 <= len(description) <= 1024:
        fail("description must contain 1-1024 characters")
    if license_name != "MIT":
        fail("license must be MIT")
    if not body.strip():
        fail("skill body is empty")
    if len(text.splitlines()) > 500:
        fail("SKILL.md exceeds the recommended 500-line limit")

    forbidden = {
        "disable-model-invocation": "Claude-specific frontmatter",
        "CLAUDE_SKILL_DIR": "Claude-specific substitution",
        "$ARGUMENTS": "Claude-specific substitution",
        "hijazi-adhd-execution": "personal source skill name",
        "Dahab": "personal owner label",
    }
    for token, reason in forbidden.items():
        if token in text:
            fail(f"canonical skill contains {reason}: {token}")

    required_phrases = [
        "form, not substance",
        "Done: <completed state supported by available evidence>",
        "Estimate only when grounded",
        "Keep simple answers simple",
        "Task completeness",
        "Requested output format",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"canonical behavior invariant missing: {phrase}")


def validate_json_files() -> None:
    for path in [
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "marketplace.json",
        ROOT / ".codex-plugin" / "plugin.json",
    ]:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_openai_sidecar() -> None:
    path = SKILL_DIR / "agents" / "openai.yaml"
    text = path.read_text(encoding="utf-8")
    if "\t" in text:
        fail("openai.yaml must not contain tabs")
    for required in (
        'display_name: "ADHD Execution"',
        "default_prompt:",
        "allow_implicit_invocation: true",
    ):
        if required not in text:
            fail(f"openai.yaml missing expected adapter setting: {required}")


def validate_evals() -> None:
    path = ROOT / "evals" / "cases.jsonl"
    seen: set[str] = set()
    count = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"invalid eval JSON on line {line_number}: {exc}")
        for key in ("id", "category", "prompt", "criteria", "risk"):
            if key not in case:
                fail(f"eval line {line_number} missing {key}")
        if case["id"] in seen:
            fail(f"duplicate eval id: {case['id']}")
        if not isinstance(case["criteria"], list) or not case["criteria"]:
            fail(f"eval {case['id']} has no criteria")
        seen.add(case["id"])
        count += 1
    if count < 8:
        fail("expected at least eight behavior evals")


def validate_release_evidence() -> None:
    raw = ROOT / "evals" / "raw"
    explicit_cases = (
        "direct",
        "progress",
        "estimate",
        "safety",
        "format",
        "bounded-plan",
        "deep-explanation",
        "ranked-decision",
        "medical-boundary",
        "error-report",
    )
    for client in ("claude", "codex"):
        for case in explicit_cases:
            path = raw / f"{client}-{case}.txt"
            if not path.is_file() or not path.read_text(encoding="utf-8").strip():
                fail(f"missing raw release evidence: {path.relative_to(ROOT)}")

    positive = (raw / "codex-implicit-positive.trace.jsonl").read_text(encoding="utf-8")
    negative = (raw / "codex-implicit-negative.trace.jsonl").read_text(encoding="utf-8")
    if "adhd-execution/SKILL.md" not in positive:
        fail("positive implicit trace does not show a skill read")
    if "adhd-execution/SKILL.md" in negative:
        fail("negative implicit trace unexpectedly shows a skill read")

    manual_trace = (raw / "claude-manual-load.trace.txt").read_text(encoding="utf-8")
    plugin_trace = (raw / "claude-plugin-load.trace.txt").read_text(encoding="utf-8")
    if "project: 1" not in manual_trace:
        fail("Claude manual trace does not show project skill discovery")
    if "Loaded 1 skills from plugin adhd-execution" not in plugin_trace:
        fail("Claude plugin trace does not show plugin skill discovery")
    for filename in ("claude-manual-direct-v2.txt", "claude-plugin-direct.txt"):
        output = (raw / filename).read_text(encoding="utf-8").strip()
        if output not in {"5432", "5432."}:
            fail(f"unexpected Claude invocation output in {filename}: {output!r}")


def main() -> None:
    validate_skill()
    validate_json_files()
    validate_openai_sidecar()
    validate_evals()
    validate_release_evidence()
    print("PASS: local structural invariants, JSON syntax, eval-case shape, and release evidence checked")


if __name__ == "__main__":
    main()
