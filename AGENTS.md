# Agent Guide

Use this map when maintaining the repository.

## Source of truth

- Canonical behavior: `skills/adhd-execution/SKILL.md`
- Client metadata: `skills/adhd-execution/agents/`, `.claude-plugin/`, `.codex-plugin/`
- Behavior cases: `evals/cases.jsonl`
- Structural validation: `scripts/validate.py` and `tests/test_skill.py`

Do not add client-specific syntax to the canonical `SKILL.md`. Put optional client behavior in sidecar metadata or installation documentation.

## Required invariants

1. The skill remains a style layer and never overrides safety, system instructions, tool rules, output schemas, verification, or completeness.
2. Direct factual questions do not receive artificial steps, checkpoints, or next actions.
3. Time, size, and cost estimates require a stated basis.
4. The five-item limit controls display only; required work is batched, not discarded.
5. No universal medical claims about ADHD.
6. No claim of session persistence unless a specific client adapter guarantees it.
7. Personal names and project-specific ownership labels do not appear in the canonical behavior, except repository authorship metadata.

## Verification

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
skills-ref validate skills/adhd-execution
git diff --check
```

For a release, smoke-test one direct-answer case and one execution case in both Claude Code and Codex. Record the exact model, prompt, and observed output. Do not treat a successful manifest validation as behavior validation.
