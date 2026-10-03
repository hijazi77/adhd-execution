# Before and after

These examples demonstrate presentation changes only. The skill must not change facts, safety policy, tool behavior, or task completeness.

## Direct factual question

**Prompt**

> What port does PostgreSQL use by default?

**Before**

> PostgreSQL is a popular relational database system. By default, when installed, it listens for connections on port 5432, although this can be changed in the configuration. Let me know if you want help configuring it.

**After**

> PostgreSQL uses port **5432** by default.

Why: a factual question needs the fact, not a workflow or artificial next action.

## Execution update

**Prompt**

> The schema migration finished. The backfill is running. Integration tests are next. Give me a status update.

**Before**

> We have made good progress on the migration. The schema portion is complete, and the backfill process is currently underway. Once that finishes, we will want to move on to the integration testing phase to make sure everything is working as expected.

**After**

> Backfill is running; integration tests are queued next.
>
> Done: Schema migration finished (reported)
> In progress: Data backfill
> Next: Run integration tests after backfill completion

Why: completed work, current state, and the next gate remain visible without reconstructing earlier messages.

## Complete long plan

A complete nine-action plan is not shortened to five actions. It is presented as two labeled groups, each containing five or fewer actions. The five-item rule controls visual grouping, not completeness.
