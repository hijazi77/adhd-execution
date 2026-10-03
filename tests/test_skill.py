from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "adhd-execution" / "SKILL.md"


class SkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = SKILL.read_text(encoding="utf-8")
        end = cls.text.find("\n---\n", 4)
        cls.frontmatter = cls.text[4:end]
        cls.body = cls.text[end + 5 :]

    def test_spec_clean_frontmatter(self) -> None:
        self.assertTrue(self.text.startswith("---\n"))
        self.assertRegex(self.frontmatter, r"(?m)^name: adhd-execution$")
        self.assertRegex(self.frontmatter, r"(?m)^description: .+$")
        self.assertRegex(self.frontmatter, r"(?m)^license: MIT$")
        for vendor_key in ("disable-model-invocation", "context:", "user-invocable:"):
            self.assertNotIn(vendor_key, self.frontmatter)

    def test_name_matches_directory(self) -> None:
        name = re.search(r"(?m)^name:\s*(.+)$", self.frontmatter).group(1)
        self.assertEqual(name, SKILL.parent.name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

    def test_skill_is_progressively_disclosed(self) -> None:
        self.assertLessEqual(len(self.text.splitlines()), 500)
        self.assertTrue(self.body.strip())

    def test_style_never_overrides_completion_or_safety(self) -> None:
        for phrase in (
            "form, not substance",
            "Safety and destructive actions",
            "Task completeness",
            "Requested output format",
        ):
            self.assertIn(phrase, self.body)

    def test_no_forced_action_or_fake_estimate(self) -> None:
        self.assertIn("Keep simple answers simple", self.body)
        self.assertIn("Estimate only when grounded", self.body)
        self.assertIn("no manufactured steps", self.body)

    def test_execution_checkpoint_is_defined(self) -> None:
        for phrase in (
            "Done: <completed state supported by available evidence>",
            "In progress: <current work or none>",
            "Next: <next action or none>",
        ):
            self.assertIn(phrase, self.body)

    def test_openai_adapter_allows_narrow_implicit_matching(self) -> None:
        adapter = (ROOT / "skills" / "adhd-execution" / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", adapter)

    def test_plugin_brand_asset_exists(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        for key in ("logo", "composerIcon"):
            relative = manifest["interface"][key].removeprefix("./")
            self.assertTrue((ROOT / relative).is_file(), f"missing {key}: {relative}")

    def test_evals_are_unique_and_complete(self) -> None:
        cases = [
            json.loads(line)
            for line in (ROOT / "evals" / "cases.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertGreaterEqual(len(cases), 8)
        self.assertEqual(len(cases), len({case["id"] for case in cases}))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertTrue(case["criteria"])


if __name__ == "__main__":
    unittest.main()
