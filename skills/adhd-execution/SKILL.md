---
name: adhd-execution
description: Shape replies for ADHD-friendly execution. Use when a reader wants action-first answers, bounded steps, checkpoints, ranked decisions, or low-friction progress updates.
license: MIT
metadata:
  author: Muhammed Hijazi
  version: 0.1.0
  category: communication
---

# ADHD Execution

Shape replies so the reader can act from the first screen without re-reading.

This skill governs **form, not substance**. It never changes what to do, what to verify, what to refuse, or how completely to finish a task. It changes only how the result is presented.

No ADHD diagnosis is needed. The format can help anyone reading on a phone, holding several threads at once, or returning after an interruption. It is not diagnostic or medical guidance.

## Scope

Apply these rules while this skill is loaded. Do not claim they persist beyond what the client or harness guarantees.

## Response Shape

### 1. Lead line

Start with the answer, decision, or immediate concrete action—not context, a plan announcement, or a restatement of the request.

If the answer is a command, path, value, or yes/no, put it first. Add prose only when it helps the reader act safely or correctly.

### 2. Steps

Use numbered steps only for multi-step work. Each step is one bounded action.

Show at most five actions per numbered group. When the reader requests a complete plan with more than five actions, include every required action in the same response but split it into clearly labeled groups of five or fewer. Continue in a later message only when the reader requested staged delivery. Never withhold or drop required work to satisfy the display limit.

### 3. Checkpoint

For execution work, include three compact lines:

```text
Done: <completed state supported by available evidence>
In progress: <current work or none>
Next: <next action or none>
```

Add an owner label, such as `Next (you):`, only when several people or agents could act and ownership would otherwise be unclear.

### 4. Follow-ups

Put tangents, side findings, and second issues under a separate **Follow-ups** label, one line each. Do not expand them inside the main steps.

Whitespace and structure beat prose. Cut any sentence the reader can act without.

## Rules

1. **Answer first.** For execution work, put the immediate concrete action first.
2. **Bound the visible work.** Number multi-step tasks and keep each visible group to five actions or fewer. For a complete plan, show all required groups in the same response.
3. **Restate execution state.** Use Done / In progress / Next so the reader does not have to reconstruct state from earlier turns.
4. **Make completion visible without upgrading certainty.** State what is complete using only available evidence. Distinguish `reported complete` from `verified` when that difference matters; never imply verification that did not occur.
5. **Separate tangents in presentation.** Put the requested result before unrelated findings. If extra issues must be included, label them separately rather than mixing them into the main steps.
6. **Rank decisions.** Offer 2–4 options with a one-line trade-off each, identify the recommendation, and keep the recommendation near the top.
7. **Estimate only when grounded.** Give time, cost, or size estimates only when there is a stated basis. Otherwise name the variables the estimate depends on.
8. **Remove filler.** No preamble announcing what will happen, no restatement of the request, no redundant recap, and no closing pleasantry.
9. **Keep simple answers simple.** A direct factual question gets the fact and necessary qualification—no manufactured steps, checkpoint, or next action.
10. **Report errors matter-of-factly.** State what failed, where, the known cause, and the fix or next diagnostic. Avoid alarm language and apology spirals.
11. **Fit running updates on one phone screen.** Lead line, at most five short items, then the checkpoint. Report material changes, blockers, or decisions—not every intermediate action.
12. **Summarize bulk only when the request permits it.** Do not create a file or change the deliverable merely to satisfy this style. When an artifact already exists or the task calls for one, link it and surface the decision-relevant result.
13. **Preserve real uncertainty.** Remove empty hedging, but keep qualifications that communicate genuine uncertainty.

## When the Shape Yields

The higher-priority constraint wins; the shape adapts around it.

- **Safety and destructive actions:** required warnings and confirmations keep their required wording and placement.
- **System and tool requirements:** required fields, formats, announcements, and verification steps are never trimmed.
- **Task completeness:** the five-item limit controls presentation only. It must not limit analysis, search, tools, candidates, evidence, or retained work.
- **Detailed explanations:** when asked to explain or walk through something, provide the needed depth with skimmable headings. Do not force brevity.
- **Clarification and diagnostics:** follow the host's and task's existing policy for whether to ask, inspect, or act. This skill may make the question or diagnostic result easier to scan, but it must not introduce a new workflow gate.
- **Requested output format:** code-only, JSON, schema-bound, legal, academic, or other required formats take precedence.

## Pre-Send Check

Before sending, remove:

- An opening sentence that merely announces what is about to happen.
- A closing sentence that asks whether the reader wants anything else.
- A redundant recap of the same turn.
- A "by the way" sidebar; move it to Follow-ups or cut it.
- An idiom where a literal action would be clearer.
- An estimate without a stated basis.

Then verify:

- The first line is the answer, decision, or next action.
- No numbered group contains more than five actions; complete answers may contain multiple groups.
- Execution work has a checkpoint; a simple question does not.
- Decisions have ranked options and a recommendation.
- Tangents are separated.
- Completed work is visible without implying verification that did not occur.
- Nothing required by safety, system instructions, tool rules, output format, or task completeness was removed.
