# Release evidence — 2026-10-03

## Behavior result

**PASS:** every explicit behavior category in `evals/cases.jsonl` was exercised in both Claude Code and Codex. The destructive-action category used non-executing evaluation wrappers rather than the literal destructive prompt. Implicit activation is claimed and tested only for the Codex adapter.

Raw final outputs, exact prompts, client/model versions, Codex activation traces, and sanitized Claude loader traces are indexed in [`raw/RUNS.md`](raw/RUNS.md).

| Case | Claude | Codex |
|---|---|---|
| direct-fact | PASS | PASS |
| execution-checkpoint | PASS | PASS |
| grounded-estimate | PASS | PASS |
| ranked-decision | PASS | PASS |
| destructive-action | PASS | PASS |
| deep-explanation | PASS | PASS |
| required-format | PASS | PASS |
| medical-boundary | PASS | PASS |
| error-report | PASS | PASS |
| bounded-plan | PASS | PASS |
| implicit-positive | not claimed | PASS, trace retained |
| implicit-negative | not claimed | PASS, trace retained |

The complete nine-action plan was returned in the same response by both clients, grouped as actions 1–5 and 6–9. The five-item rule controlled visual grouping rather than completeness.

## Installation result

- Claude manual skill invocation `/adhd-execution`: **PASS** — project loader trace retained
- Claude repository plugin invocation `/adhd-execution:adhd-execution`: **PASS** — plugin loader trace retained
- Codex explicit invocation `$adhd-execution`: **PASS**
- Codex narrow implicit match: **PASS**
- Codex unrelated creative prompt did not load the skill: **PASS**
- Published `npx skills add` installation for Claude Code and Codex: **PASS** — installed copies matched the canonical SHA-256; [evidence](raw/installer-smoke.txt)

## Structural validation

- `python3 scripts/validate.py`: **PASS**
- `python3 -m unittest discover -s tests -v`: **9/9 PASS**
- `claude plugin validate .claude-plugin/plugin.json --strict`: **PASS**
- `claude plugin validate .claude-plugin/marketplace.json --strict`: **PASS**
- Official `skills-ref validate`: **Valid skill**
  - validator source: `agentskills/agentskills@69ef37e9424c0a7ea9dd2293b559e43ec8176379`
- JSON and SVG parse checks: **PASS**
- Plugin icon visual check: **PASS** — crisp, high-contrast, unclipped, and recognizable at small size
- Independent release review (`gpt-5.6-sol`, medium): **PASS** — [verdict](REVIEW.md)

## Environment note

Codex `0.151.0` could not use Bubblewrap because this host disallows the required namespace creation. Codex behavior tests therefore ran with `danger-full-access` inside a disposable test repository. Prompts did not authorize state changes; the retained activation traces show only reads of the skill file.
