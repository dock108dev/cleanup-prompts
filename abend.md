Abend Handling Implementation Prompt

You are the engineer assigned to harden error handling for this source tree.

Work from the code in front of you. Build an understanding of how failures move through the application, implement the appropriate changes, write the docs an engineer needs to operate this behavior, and run the relevant validation before handing it back.

## Scope and working approach

- Follow the user's requested scope. These are implementation prompts: make routine, supported code and documentation fixes directly. Use audit-only mode only when the user asks for a review without changes.
- Before editing, read the current README, relevant tracker (including a linked Desktop tracker), candidate identity, Git status, and applicable maintenance decisions. Check supported modes and existing work so the pass builds on the current project.
- Preserve unrelated changes, evidence, editable masters, owner data, frozen builds, and prepared review artifacts. Do not reset, discard, commit, push, publish, or release without authorization. If a review candidate must remain fixed, work separately and identify the resulting source changes.
- Existing authorization carries forward. This prompt alone does not authorize live collection, provider spending, owner-data access or migration, signed builds, or external operations.
- Do not ask permission for routine fixes or create an exhaustive change ledger. Summarize routine work briefly; explain complicated changes, their reason, effect, and remaining uncertainty. When a change requires an unresolved product or architecture decision, report a concrete follow-up and continue independent work.

## Objective

Make production-path error handling explicit, observable, and appropriate.

By the end of this work:
- Deliberate resilience remains in place.
- Risky silent failure paths are tightened.
- Expected non-fatal failures have clear handling, telemetry, and tests where appropriate.
- Production behavior is observable enough for debugging and operations.
- Documentation describes the implemented behavior as the current source of truth.
- The repo builds, tests, and passes relevant checks.

## Scope

Inspect the full repository for patterns including:

### Exception and error handling
- broad catches
- catches that log and continue
- catches that return empty, falsey, default, or cached values
- catches that convert errors into warning/status objects
- catches that suppress known failure modes
- catches with comments like expected, ignore, best effort, non-fatal, fallback, safe to continue, or optional
- API handlers that return generic success or generic failure wrappers
- background jobs, schedulers, and workers that consume failures without escalation

### Logging and observability
- logs downgraded from error to warning/info/debug
- logs emitted only in certain runtime modes
- hidden stack traces
- rate-limited, deduplicated, or disabled logs
- warning and log filters
- telemetry, metrics, or alert suppression
- places where repeated failures are hard to distinguish from success

### Runtime suppression
- warning filters
- lint, type, or static-analysis suppressions
- deprecation suppression
- third-party warning suppression
- no-op behavior
- optional dependency guards

### Resilience and fallback behavior
- retries
- fallback values
- degraded mode paths
- partial success flows
- continue-on-failure paths
- queue/task failure handling
- timeout handling
- circuit breakers
- health checks that treat failures as soft failures

### Cancellation, shutdown and recovery
- cancellation propagation and bounded task/process shutdown
- resource ownership and cleanup failures that can mask the original error
- partial writes, transaction boundaries, crash recovery and duplicate retries
- accurate durable/partial/unknown status after storage failures
- safe error details: preserve useful diagnostics without exposing credentials, private payloads or sensitive subprocess output

Review broad catches in context, including ownership boundaries and existing recovery behavior. Narrow them when that fixes a demonstrated problem; do not remove deliberate handling merely because a catch is broad.

### Environment-specific strictness
- production and non-production behavior differences
- debug-mode checks
- test-mode strictness
- production-mode suppression
- environment flags that change exception handling, validation, observability, or fail-open/fail-closed behavior

## Implementation Requirements

For each meaningful issue you find, implement the most appropriate outcome:

1. Keep healthy resilience
   - Preserve the behavior.
   - Make intent clear with concise comments where helpful.
   - Ensure logs, metrics, or status surfaces make failures visible enough.
   - Add or update tests if behavior is important.

2. Tighten risky handling
   - Narrow broad catches.
   - Re-raise unexpected errors.
   - Fail closed where appropriate.
   - Preserve stack traces in appropriate private diagnostics; redact sensitive content and keep public errors safe.
   - Avoid returning misleading success.
   - Replace silent defaults with explicit errors or typed fallback results.

3. Improve observability
   - Add actionable logging while protecting secrets and private data.
   - Add metrics, counters, status flags, or structured error information where the codebase has a pattern for it.
   - Make repeated failures diagnosable.

4. Remove unused fallback behavior
   - Delete unused suppression paths.
   - Remove no-op code that hides real behavior.
   - Correct comments that describe behavior inaccurately.

5. Document current behavior
   - Write or update README/docs content where this behavior affects setup, operations, production behavior, known limitations, or incident response.
   - Keep documentation factual and tied to implemented behavior.

## Risk Model

Assess each case through these lenses:
- Reliability: can this hide broken behavior or unstable execution?
- Data integrity: can this create bad, partial, duplicated, or missing data without visibility?
- Security: can this hide auth, permission, validation, secret, or audit failures?
- Observability: can this make debugging, alerting, or incident response materially harder?
- Operations: can this create silent degradation, recurring noise, or hard-to-diagnose incidents?

Severity guidance:
- Critical: likely to hide serious production failure, security exposure, or data corruption.
- High: meaningful production risk that should be fixed promptly.
- Medium: acceptable temporarily but should be improved.
- Low: minor blind spot or maintainability issue.
- Note: intentional, low-risk behavior that is clear and acceptable.

## Search Heuristics

Search for patterns and keywords such as:
- try
- except
- catch
- pass
- continue
- return None
- return []
- return {}
- logger
- warning
- suppressed
- ignore
- fallback
- best effort
- non-fatal
- safe to continue
- optional
- timeout
- retry
- default
- noop
- no-op
- silent
- filterwarnings
- ts-ignore
- eslint-disable
- noqa
- pylint disable
- type ignore

Also inspect:
- middleware
- API handlers
- frontend fetch and render flows
- background jobs and workers
- queue consumers
- schedulers
- cron-style tasks
- health checks
- integration clients

## Validation Requirements

Keep validation lightweight and proportional to the change:
- Inspect the simplest relevant CI or project commands. For code changes, run the affected component's basic compile/build or type/syntax check and relevant unit tests. Use existing commands and environments; install dependencies only if needed.
- For documentation-only changes, check the edited text, links, referenced paths and commands against the repository. No application build or test suite is required unless executable behavior changed.
- Do not automatically run the full CI matrix, integration or end-to-end suites, browser walkthroughs, live smoke tests, security campaigns, packaging or signing. Add a focused check only when a changed behavior or observed failure makes it necessary.
- Inspect command side effects before execution. Use disposable synthetic state when tests write data; do not touch owner state or trigger external operations through a validation command without existing authorization.
- Use available baseline results; if a check fails, distinguish an existing failure from a regression. Fix regressions from this pass. Once the basic checks pass, stop unless new evidence justifies more testing.
- Report the checks actually run and their results, with material untested limits. Do not claim unrun checks passed or equate technical checks with owner acceptance, artifact qualification, or release approval.

## Final Response

Include:
- Summary of implemented changes.
- The most important failure-handling issues found and how they were resolved.
- Intentional suppressions retained and why they are acceptable.
- Documentation updates made.
- Tests and checks run, with results.
- Remaining risks or follow-up items that should be handled separately.

## Engineering Guidance

- Distinguish healthy resilience from dangerous silent failure.
- Preserve deliberate resilience where it is correct and observable.
- Prefer narrow, targeted fixes over broad rewrites.
- Follow existing project patterns for logging, errors, telemetry, tests, and docs.
- When a risky behavior needs product or architecture input, record a clear follow-up in the appropriate docs or issue-tracking surface used by the repo.
