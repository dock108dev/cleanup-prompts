Review and improve this product's backend and data layer at the end of a sprint. Leave the system easier to reason about, reliable under failure and retry, efficient at its expected workload, and maintainable by the next engineer. Implement supported fixes, verify affected behavior, and leave a concise handoff of consequential work that remains.

Use three perspectives together: a backend engineer following requests and jobs, a database engineer checking integrity and access patterns, and an operator diagnosing failures and recovering service. Work from the actual implementation and product requirements. Apply only the sections relevant to this system; a local SQLite application does not need a distributed-service architecture.

## Establish the current system and scope

Read repository instructions, the README, active handoff/tracker, runtime and storage contracts, migration history, maintenance decisions, and working-tree status. Identify supported database engines and versions, entry points, background workers, external integrations, and validation commands. Distinguish source, installed applications, active databases, and frozen review builds.

Trace two or three representative paths through the system, including a critical write and an important read or background job where present. Follow input validation, authorization, domain rules, storage, external effects, and the result exposed to callers. Include a failure or retry path. Review sprint changes and their shared dependencies without limiting the review to changed lines. Give a brief scope update and proceed with routine decisions.

This is an implementation pass unless the user requests audit-only work. Preserve intended domain behavior, public contracts, private state, unrelated changes, and retained evidence. Fix demonstrated bugs and localized maintenance problems directly. For unresolved product decisions, broad architecture changes, or incompatible contract changes, prepare a concrete follow-up and continue independent work. Do not introduce new infrastructure, frameworks, or abstractions merely to satisfy this prompt.

Carry forward existing authorization. This prompt alone does not authorize accessing or modifying owner/production data, running production migrations or maintenance, live collection, provider spending, deployment, or replacing installed/frozen builds. Source-level migration repairs and tests on disposable synthetic databases are in scope. Inspect connection targets and command side effects before running validation. Do not commit or push without authorization.

## Preserve data meaning and integrity

- Check that types, nullability, defaults, keys, uniqueness, foreign keys, and check constraints express the actual domain rules. Validate at system boundaries and enforce invariants in storage where supported. Account for existing records before tightening constraints.
- Preserve distinctions such as unknown versus zero, absent versus empty, stale versus current, requested versus applied, and observed versus inferred. Check units, precision, rounding, timestamps, time zones, identifiers, provenance, and serialization across boundaries. Use exact representations where the domain requires them.
- Identify the authoritative source for each important value. Remove localized duplicated rules and conflicting derived state. Verify that aggregates, caches, summaries, and materialized views stay consistent with their inputs and can be rebuilt where required.
- Check ownership and tenant scoping through reads, writes, joins, bulk operations, and background jobs. Preserve authorization checks across service and storage boundaries. Keep SQL parameterized and dynamic identifiers explicitly constrained.
- Review deletion, cascading effects, archival, and retention against documented requirements. Identify orphaned records, unbounded growth, and incomplete cleanup logic using synthetic cases or already authorized evidence. Do not invent retention periods, discard audit/accounting history, or delete real records as housekeeping.

## Make writes, jobs, and external effects reliable

- Put each atomic business operation inside the appropriate transaction. Check commit/rollback behavior, connection lifecycle, exception paths, and partial writes. Keep transactions short and avoid unnecessary network calls while holding locks.
- Inspect concurrent updates, duplicate submissions, worker overlap, and read-modify-write sequences. Use existing constraints, conditional updates, locking, or version checks to enforce the required behavior. Do not rely solely on an application pre-check for uniqueness.
- Make retryable operations idempotent where required. Check deduplication keys, their scope and lifetime, acknowledgement ordering, checkpoints, and crash recovery. A timed-out external request may have succeeded; preserve uncertain outcomes and reconcile them before retrying a consequential effect. Do not claim exactly-once execution without evidence.
- Bound retries, timeouts, concurrency, and queue growth. Retry only appropriate failures and use the project's backoff conventions. Check cancellation, graceful shutdown, abandoned work, lease expiry, and resumption after interruption. Preserve Stop choices and held/uncertain operations.
- Handle database contention, unavailable dependencies, malformed responses, and partially available data explicitly. Avoid swallowed errors, success responses after failed persistence, and fallback values that conceal missing or invalid data.

## Keep schema changes safe and repeatable

Compare models, schema definitions, migration files, and startup behavior. Verify that a fresh database and upgrades from relevant supported prior schemas reach the intended state. Check migration ordering, version bookkeeping, and concurrent-start behavior where applicable.

Do not rewrite migrations already applied to supported installations. Prefer an additive corrective migration. For changes involving data transformation, constraints, or large tables, consider compatibility during rollout, backfill batching, lock duration, interruption, restart behavior, and validation of the resulting records. Use expand/contract steps when the supported deployment model requires mixed-version compatibility.

Exercise affected migrations with representative synthetic prior data, including nulls, duplicates, and boundary values when relevant. Check that legitimate data survives and invalid data receives an explicit, supported disposition. Do not silently coerce or drop records to make an upgrade pass.

Verify the documented recovery approach for the affected change. A rollback may be a forward repair or restoration from backup; do not add a destructive downgrade just to claim reversibility. Distinguish a tested migration on disposable data from a migration applied to an installed or production database.

## Improve performance with evidence

- Inspect important query shapes for unnecessary scans, N+1 access, repeated computation, excessive round trips, unbounded results, and avoidable loading of large fields. Check stable ordering and pagination, including ties and concurrent changes where the contract requires it.
- Match indexes to actual filters, joins, ordering, and uniqueness requirements. Consider write cost and redundant indexes. Do not add indexes to every column or remove one without checking its role in constraints and supported workloads.
- Use query plans and representative synthetic data to investigate suspected bottlenecks. Prefer nonexecuting plan inspection first; execution-based analysis can run writes, acquire locks, or impose significant load. Run such analysis only on a suitable disposable or explicitly authorized target.
- Measure before and after under matched conditions for a performance fix. Record enough context to interpret the result: engine/version, data size and distribution, query or operation, and relevant timing or plan change. Small fixtures establish correctness, not production-scale performance.
- Review connection pool limits, transaction duration, lock contention, batch size, memory use, and database-specific behavior. Scope settings to the operation or transaction when appropriate. Do not apply global tuning, extend timeouts, or disable safeguards merely to conceal an inefficient path.
- Check cache keys, invalidation, expiry, freshness, and behavior when the cache is unavailable. Introduce caching only for a demonstrated need with a clear consistency contract.

## Tighten backend contracts and structure

Keep transport, orchestration, domain policy, and persistence responsibilities understandable. Reuse established boundaries and shared rules. Extract mixed responsibilities when useful; avoid broad rewrites, generic repository layers, or new service boundaries without a demonstrated need.

Check request/response schemas, validation, error semantics, pagination, and compatibility with existing callers. Make configuration defaults explicit and validate required settings at an appropriate boundary. Ensure startup, readiness, shutdown, and resource cleanup reflect actual dependency and lifecycle requirements.

Remove dead backend paths, stale storage adapters, and unused configuration only after checking supported modes and callers. Keep credentials and personal data out of logs and error responses. Apply localized security fixes supported by evidence; use the dedicated security prompt for a broader security review.

## Make failures diagnosable and recovery credible

Review the signals an engineer needs to distinguish a slow query, blocked transaction, failed migration, retry loop, stale worker, and unavailable dependency. Improve existing logs and metrics where a concrete gap prevents diagnosis. Include useful operation context and correlation identifiers without recording secrets, full sensitive payloads, or high-cardinality metric labels. Avoid noisy logging on every successful row or retry.

Check that existing backup and restore instructions cover the authoritative data and supported engine. Where relevant and feasible, exercise recovery using a disposable synthetic database and verify recovered data, not merely command exit status. Do not copy private databases or schedule new backup infrastructure through this prompt. State clearly when restore capability remains untested.

For recurring maintenance such as pruning, compaction, vacuuming, reindexing, or refreshing derived data, verify the need, target, locking/load implications, and failure behavior. Improve existing scripts and documentation where warranted; do not execute maintenance against active databases simply because it appears on a checklist.

## Verify the affected behavior

Use existing project checks and a disposable synthetic environment. Confirm that database tests cannot resolve to an owner or production target, and that external integrations use fakes unless live use is already authorized. Use the actual supported engine for engine-specific SQL, constraints, transaction behavior, and migrations; an in-memory substitute does not establish those properties.

Run focused checks for changed behavior: successful reads/writes, rejected invalid data, rollback after failure, duplicates/retries, concurrency, migration from supported prior state, or cancellation/restart as applicable. Add regression tests for demonstrated bugs and important invariants. Prefer observable outcomes over tests that merely mirror implementation details.

Run relevant formatting, static checks, and affected tests. Broaden validation when shared contracts, migration behavior, or an observed failure justify it. Do not automatically run every suite or a release campaign. Reuse credible baseline evidence, distinguish existing failures from regressions, and fix regressions introduced by this pass. Never weaken assertions, disable constraints, or increase timeouts solely to get a green result.

For documentation-only changes, check text, links, paths, and commands; no application build is required. If an engine or environment is unavailable, complete independent source-supported fixes and identify the specific unverified behavior. Passing unit tests alone does not establish performance, recovery, or production readiness.

## Leave a maintainable result

Update existing storage/runtime contracts, migration guidance, configuration examples, and operating instructions only where the implementation or findings require it. Keep one current explanation of each rule. Add consequential unfinished work to the existing tracker with a concrete outcome and verification step; do not create a parallel audit backlog or exhaustive checklist report.

Return a short handoff covering:

- The most consequential fixes and the behavior or maintenance burden they improve.
- Checks actually run, the database engine and disposable environment used where relevant, and any matched performance evidence.
- Schema/data compatibility and recovery implications for changes made; state whether any real database was accessed or changed.
- Remaining risks, blocked verification, and concrete follow-ups, prioritized by impact.
- Actual source, commit/push, migration, installation, and deployment status. Technical verification does not establish owner acceptance or release approval.

Call the pass complete only for the reviewed scope and verified outcomes. If nothing warrants changing, say so with the evidence and material limits; do not manufacture cleanup work.
