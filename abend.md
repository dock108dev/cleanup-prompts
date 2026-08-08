Abend Handling Implementation Prompt

You are the engineer assigned to harden error handling for this source tree.

Work from the code in front of you. Build an understanding of how failures move through the application, implement the appropriate changes, write the docs an engineer needs to operate this behavior, and run the relevant validation before handing it back.

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
   - Preserve stack traces.
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

Before finishing:
- Run the relevant formatter, linter, type checks, unit tests, integration tests, and smoke tests available in the repo.
- If the repo has no clear validation command, inspect package scripts, task runners, CI configuration, Makefiles, or project docs and run the closest appropriate checks.
- Add or update tests for any behavior you change.
- Verify your changes introduce no new warnings or failures.
- If a check cannot be run locally, explain exactly why and what should be run elsewhere.

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
