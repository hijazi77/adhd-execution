# ADHD Execution

An open-format Agent Skill that shapes AI responses for low-friction execution: answer first, bounded steps, visible progress, ranked decisions, and no filler. Release 0.1.0 is runtime-tested in Claude Code and Codex.

It is useful for ADHD readers, but no diagnosis is needed. It is a communication preference—not diagnostic or medical guidance.

## What changes

- The answer, decision, or next action appears first.
- Multi-step work is shown in batches of five or fewer actions.
- Execution updates use `Done / In progress / Next` checkpoints.
- Decisions use ranked options with short trade-offs and a recommendation.
- Estimates require a stated basis; the skill never invents precision.
- Simple questions stay simple, and requested deep explanations stay detailed.

The skill controls presentation only. Safety, system instructions, tool requirements, verification, and task completeness always win.

## Install

The canonical skill is [`skills/adhd-execution/SKILL.md`](skills/adhd-execution/SKILL.md). It follows the open [Agent Skills specification](https://agentskills.io/specification).

### Compatible skills installer

After this repository is published, standards-compatible installers can use:

```bash
npx skills add hijazi77/adhd-execution --skill adhd-execution -g
```

This installer route is documented for convenience but was not part of the 0.1.0 runtime test.

### Manual locations

Copy the whole `skills/adhd-execution` directory into the location your client scans.

**Runtime-tested in 0.1.0:**

- Claude Code: `~/.claude/skills/adhd-execution/`
- Codex: `~/.agents/skills/adhd-execution/`

**Compatibility paths supplied but not runtime-tested in 0.1.0:**

- Hermes: `~/.hermes/skills/adhd-execution/`
- Cursor: `~/.cursor/skills/adhd-execution/`
- GitHub Copilot: `~/.copilot/skills/adhd-execution/` or `~/.agents/skills/adhd-execution/`
- Gemini CLI: `~/.gemini/skills/adhd-execution/`
- OpenCode: `~/.config/opencode/skills/adhd-execution/`

Project-level installation is usually better for teams. Use the equivalent project skill directory documented by the client, and commit the skill with the repository.

## Invoke

Invocation depends on how the skill was installed:

**Tested:**

- Claude Code, manually installed skill: `/adhd-execution`
- Claude Code, repository plugin: `/adhd-execution:adhd-execution`
- Codex: `$adhd-execution`

**Client-dependent and not tested in this release:** select the installed skill using that client's documented skill command, or ask it to use `adhd-execution` for the current conversation.

The Codex adapter permits implicit invocation when the request clearly asks for ADHD-friendly or action-first formatting; explicit `$adhd-execution` invocation is always available. Other clients may use their own matching policy. The skill does not claim persistence beyond what the client guarantees.

## Repository layout

```text
skills/adhd-execution/SKILL.md       Canonical portable behavior
skills/adhd-execution/agents/        Optional client metadata
.claude-plugin/                      Claude Code plugin metadata
.codex-plugin/                       Codex plugin metadata
assets/logo.svg                      Plugin branding asset
examples/before-after.md             Canonical behavior examples
evals/cases.jsonl                    Behavior cases
evals/RESULTS.md                     Release evidence
evals/REVIEW.md                      Independent release verdict
scripts/validate.py                  Dependency-free structural checks
tests/test_skill.py                  Regression checks
```

## Verify

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
skills-ref validate skills/adhd-execution
```

Behavior smoke tests should cover at least Claude Code and Codex before release. See [`evals/cases.jsonl`](evals/cases.jsonl).

## Design notes

This public version was generalized from Muhammed Hijazi's personal `hijazi-adhd-execution` workflow and reviewed with Claude Opus 5. It was also compared with the MIT-licensed [`ayghri/i-have-adhd`](https://github.com/ayghri/i-have-adhd) project to avoid duplicating its weaknesses or distinctive wording. The upstream copyright and MIT notice are retained in [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md).

Key differences from many concise-output prompts:

- It does not force a fake next action after a factual answer.
- It does not manufacture time estimates.
- It does not make universal medical claims about ADHD.
- It does not pretend the harness will preserve the skill forever.
- It preserves completeness and detailed explanations when the task requires them.

## License

MIT © 2026 Muhammed Hijazi. Portions informed by Ayoub Ghriss's MIT-licensed `i-have-adhd`; retained notice is in [`LICENSE`](LICENSE).
