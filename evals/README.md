# Behavior evaluations

`cases.jsonl` contains observable behavior criteria for the canonical skill.

A release smoke test should run these cases in both Claude Code and Codex:

1. `direct-fact` — does not manufacture work.
2. `execution-checkpoint` — makes state visible.
3. `grounded-estimate` — rejects unsupported precision.
4. `destructive-action` — lets host safety policy override style.
5. `required-format` — lets an explicit output contract override presentation rules.
6. `bounded-plan` — groups a complete long answer without withholding required work.

Where the client supports implicit activation, also run:

7. `implicit-positive` — loads only when the request clearly asks for the style.
8. `implicit-negative` — does not alter an unrelated creative request.

Record the client, exact model, exact prompt, raw output, and pass/fail result. Model-generated judgments are useful, but observable criteria and human review remain the release gate. Retain release evidence under `evals/raw/`; see [`raw/RUNS.md`](raw/RUNS.md) and [`RESULTS.md`](RESULTS.md).
