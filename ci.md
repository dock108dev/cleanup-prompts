Review and improve this repository's GitHub Actions CI as a complete engineering system: meaningful quality gates, event-driven workflows, secure execution, useful reporting, and measured reliability.

Implement workflow, supporting-script, test/reporting configuration, and documentation fixes. Do not stop after syntax checks and a few unit tests. Assess correctness, security, compatibility, reproducibility, performance, and operability against the actual project. Comprehensive means each relevant area has a supported check or a specific reason for omission—not that every check runs on every event.

## Scope and working approach

- Read applicable repository instructions, README, active tracker (including a linked Desktop tracker), current candidate identity, maintenance decisions, and Git status before editing. Build on existing work and reconcile stale guidance.
- Preserve unrelated changes, credentials, owner data, evidence, editable masters, frozen builds, and prepared review artifacts. Do not reset, discard, commit, push, publish, or release without existing authorization. Work separately when a review candidate must remain fixed.
- Make routine supported fixes directly. Use audit-only mode only when requested. This prompt authorizes repository-side CI and reporting changes, including suitable open-source tools. New external accounts, installation into an account, uploads of private code/reports to a new service, repository setting changes, and paid plans require existing authorization.
- Use disposable synthetic state for data-writing tests. Live collection, provider spending, owner-data access/migration, signing, and production operations require existing authorization.
- Continue independent work around credential or product-decision blockers. Prepare concrete reviewable configurations and setup instructions for external activation; keep incomplete integrations disabled and clearly labeled.
- Fix CI defects and bounded regressions exposed by checks. Separate broad product rewrites and unrelated upgrades into bounded follow-ups. Never weaken checks merely to make a run green.

## 1. Discover the actual CI contract

Inspect languages, frameworks, package managers, lockfiles, supported runtimes/platforms, entry points, and actual install/check/test/build/package commands. Read every workflow, reusable workflow, custom action, called script, dependency-update configuration, container/service dependency, release configuration, and relevant contributor doc.

If GitHub access is available, inspect required checks, merge-queue configuration, recent run conclusions, timings, failures, and reruns. Use a bounded sample, preferably up to 30 completed runs from the last 30 days; state sample size/window and separate PR from primary-branch evidence. Without access, continue local work and mark hosted history/settings unverified.

Map supported components and critical behavior to checks. Find missing coverage, omitted components, tests that never execute, false-green paths, and commands relying on leftover local files. Reuse prior evidence only when candidate, configuration, environment, and inputs match.

Maintain a concise check map in the existing CI documentation, or `docs/CI.md` if no suitable location exists:

| Area / product risk | Exact workflow / job / command | Event / platform | Required, advisory, scheduled, or N/A | Reason / evidence |
|---|---|---|---|---|

Derive commands and support claims from the repository. Add maintainable scripts/configuration where a necessary check is missing. Explain material omissions.

## 2. Design workflows around events and responsibilities

Use GitHub Actions as an event-driven orchestration platform. There is no requirement to collapse CI into one action, workflow, job, or universal entrypoint. Keep responsibilities readable, parallelize independent work, and express real dependencies with `needs`.

Assess the following event model and implement the parts appropriate to the repository:

| Event / responsibility | Intended checks |
|---|---|
| `pull_request` | Deterministic merge gates: source quality, relevant behavioral suites, builds, security checks, and representative supported platforms. Fork-safe, with useful failure reports. |
| Push to primary or maintained branches | Validate the merged state, broader integration/build checks where justified, and publish comparable baseline reports. Avoid redundant work that adds no distinct assurance. |
| `merge_group` | Required gates for an observed merge queue, using stable check names and the queued candidate. |
| `schedule` | Broader compatibility, dependency/security refresh, deeper tests, benchmarks, and CI-health trend reports. State cadence, UTC timing, default-branch behavior, and freshness limits; schedules are not exact-time guarantees. |
| `workflow_dispatch` | Bounded diagnostics or deeper validation with typed, validated inputs and safe defaults; document what can be requested and any permissions required. |
| Tags/releases/environments | Separate packaging, provenance, signing, deployment, and publishing workflows under existing release authorization and environment controls. Ordinary PR CI must not publish. |

Use reusable workflows (`workflow_call`) for shared multi-job policy, typed inputs, explicit outputs, and narrowly passed secrets. Use composite actions for genuinely repeated step sequences. Do not create abstraction for a one-off command or duplicate policy across workflows. Prefer native job dependencies and artifact handoff over unnecessary chains of `workflow_run`; assess privilege escalation explicitly when cross-workflow triggering is necessary.

Keep distinct workflows discoverable and independently diagnosable. Use stable names, purposeful concurrency groups, realistic timeouts, and trigger/path filters that cannot strand required checks. Include workflow/configuration and shared-library changes in affected-component selection. Document which workflows are merge gates, scheduled assurance, advisory reporting, and release operations. A summary can aggregate results without dictating one execution pipeline.

## 3. Implement meaningful project checks

Assess every category below and implement what applies. Keep inexpensive deterministic gates on PRs; place expensive checks on the appropriate branch, schedule, or manual path without deferring critical merge assurance.

- **Source quality:** formatting in check mode, linting, type checking, compilation, relevant shell/script checks, Actions-aware workflow validation, and generated-file drift. Validate useful executable examples and local documentation references.
- **Behavior:** applicable unit suites and integration/component tests for important boundaries such as persistence, API contracts, authorization, error recovery, and cleanup. Detect unintended zero-test collection, accidental suite exclusions, and missing expected reports.
- **User journeys:** deterministic smoke/end-to-end checks for main supported workflows where available. Assess keyboard/accessibility and representative UI states. Use isolated synthetic inputs; distinguish automated checks from device/native evidence and owner acceptance.
- **Build/distribution:** production builds for supported components, package contents/assets, and fresh-output install/import/start smoke checks where relevant. A clean export or checkout must expose missing tracked inputs. Keep signing/publication separate.
- **Data/services:** disposable databases and services, bounded health checks, deterministic fixtures, relevant supported migration paths, schema/contract checks, and teardown. Never use owner or production state.
- **Security/dependencies:** workflow trust boundaries, secret detection, supported vulnerability scanning, useful language-specific static analysis, and relevant container/IaC checks. Review dependency/license inventories where applicable. Use existing blocking policy; justify defaults for new gates. Suppressions must be narrow, explained, and have a review date. Never print secrets or conceal findings.
- **Performance/size:** representative benchmark, bundle/package size, or memory measurements where meaningful and repeatable. Compare like environments/inputs; begin unbaselined or noisy measurements as advisory and justify blocking budgets. Lab metrics do not prove production performance.
- **Compatibility:** supported runtimes, OSes, architectures, and relevant dependency/service versions. Choose representative PR coverage and broader scheduled coverage deliberately. Explain exclusions instead of adding obsolete combinations to fill a matrix.

Coverage and test counts support behavioral review; they do not replace it. Add tests for important missing behavior or real regressions, not tests that mirror implementation or inflate percentages.

## 4. Make execution secure and reliable

- Use deterministic lockfile installation, correct directories, explicit supported runtimes, and pinned tools/containers. Pin external actions to full commit SHAs with version comments and maintainable updates.
- Set least-privilege permissions per workflow/job. Pass narrowly scoped secrets; avoid blanket inheritance. Treat PR metadata, outputs, reports, artifacts, and contributor-controlled strings as untrusted data. Avoid shell injection and unsafe rendering.
- Inspect `pull_request_target`, `workflow_run`, fork behavior, privileged checkouts, checkout credential persistence, cache/artifact trust, and self-hosted runner exposure. Untrusted PR code must not receive privileged credentials or unsafe access to persistent runners.
- Bound startup polling, network calls, retries, and cleanup. Cancel superseded PR runs without cancelling unrelated work or protected release operations. Make job names and concurrency groups appropriate to event/ref responsibility.
- Key caches by lockfiles, tool/runtime versions, and platform; correctness must not depend on a warm cache. Avoid wasteful matrices, duplicate runs, and unnecessary artifact transfers.
- Verify path filters, `needs`, conditions, matrix results, and any aggregate required gate. Required failure, cancellation, or unexpected skip must not become success. Explain intentional N/A skips. Never blanket-use `continue-on-error`.
- Preserve command exit status through report generation and log pipelines. Applicable reporting/uploads/cleanup should run after failure; they must not mask the original failure. Make required report-generation failures visible. Optional telemetry outages must not erase test results or block unrelated correctness checks.
- Do not change branch protection, rulesets, repository settings, secrets, variables, environments, or external integrations without authorization. Recommend exact setting changes separately from implemented workflow configuration.

## 5. Implement reporting inside CI

Deliver persistent reports in Actions, beyond the engineer's final chat response. Prefer native job summaries through `GITHUB_STEP_SUMMARY`, annotations, and downloadable artifacts. Reuse existing test reporters. Avoid a custom reporting framework when small supported tools suffice.

Each applicable workflow should show:

- Tested SHA/ref, event, run link, platform/runtime, and relevant tool versions. Distinguish PR head, tested merge commit, and merge-queue candidate.
- Concise overall result and actual PASS, FAIL, SKIPPED, CANCELLED, or NOT RUN outcomes with skip/missing-data reasons.
- Passed/failed/skipped test counts and duration, concise failing check/test details, and links to full diagnostics.
- Measured coverage, meaningful comparable deltas, security finding counts by severity, and useful performance/size metrics where applicable.
- Main blocker, next useful action, and retained report links. Keep full logs out of the summary.

Retain machine-readable test results (such as JUnit), supported coverage formats, scan outputs, and applicable build/benchmark reports. Give artifacts unique run/matrix names and explicit reasonable retention. Retain useful failure diagnostics; omit secrets, owner data, unnecessary source archives, and bulky routine recordings. Escape untrusted text and never execute an artifact to render its report.

Where useful, retain a small versioned metrics record with run/candidate identity, timestamps, environment, check outcomes, units, baseline identity, and artifact references. Missing values remain null/unavailable. Missing or malformed required reports are visible failures, not zero findings or a pass.

Provide job/workflow summaries where they help and a consolidated view where it reduces interpretation. Keep independent workflows independent; cross-workflow rollups must identify each run/SHA and cannot treat stale scheduled results as current PR evidence. Verify aggregation using passing, failing, and missing-report synthetic samples.

## 6. Measure quality and CI health

Use metrics already produced by tools first. Capture per-run measurements immediately and historical trends only when comparable evidence exists. Omit irrelevant metrics with a reason.

| Metric | Reporting requirement |
|---|---|
| Tests/coverage | Counts, skips, suite durations, line/branch coverage where supported, changed-code coverage when measurable. State exclusions and baseline; avoid arbitrary universal coverage targets. |
| Reliability | First-attempt pass rate over a stated sample, failure categories, rerun/recovery counts, suspected flakes. Separate cancelled/superseded runs. A successful rerun alone does not establish flakiness. |
| Speed | Elapsed run duration, critical path, queue time; median/p95 only with sufficient timestamp evidence and a stated method. Parallel job durations are not elapsed run time. |
| Security | Counts by tool/severity, new versus baseline findings, exceptions, scan scope, and vulnerability-data freshness. Tool outages mean unavailable evidence. |
| Performance/size | Comparable deltas with units, inputs, variability, and enforced budgets. |
| Resources | Observed runner minutes, artifact/cache sizes/retention, quota data where accessible. Distinguish measurements from estimates and do not invent billing costs. |

Baseline against the primary branch or an explicitly identified comparable candidate. If unavailable, record a first measurement without a trend claim. Do not silently compare different suite scope, tools, or platforms. Do not use retries, exclusions, softened thresholds, or replacement baselines to conceal regressions. Document sampling and retention; do not build an unbounded history crawler.

## 7. Evaluate and prepare useful free integrations

Default to native summaries/artifacts and open-source tools running inside CI. Add services only for a clear unmet need; reuse existing integrations instead of stacking overlapping dashboards. Free tools still consume runner/storage resources.

Verify current official plans/docs at implementation time. For each recommendation, record verification date/source, public/private eligibility, user/LOC/upload limits, relevant features/languages, retention, permissions, external data sent, account/token requirements, and quota-exhaustion behavior. Inspect actual account eligibility when accessible. Free for open source does not imply free for a private repository.

| Candidate | Useful role | Adoption guidance |
|---|---|---|
| GitHub summaries, annotations, artifacts, read-only Actions API | Run reports, diagnostics, bounded history metrics | Default foundation; verify runner/storage allowances. [Summary docs](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary), [billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions). |
| Existing coverage tooling + optional Codecov | Coverage history and changed-code comparisons | Native coverage works without SaaS. Assess current private-repository/user/upload eligibility before activation. [Plans](https://about.codecov.io/pricing/). |
| SonarQube Cloud | Consolidated static analysis and quality trends | Optional if it fills a gap; verify Free/OSS limits and analysis features. [Plan docs](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans). |
| actionlint | Workflow syntax, expressions, action inputs, script checks | Pinned local/CI validator. [Official project](https://github.com/rhysd/actionlint). |
| Gitleaks CLI + OSV-Scanner | Secret and dependency findings | Check scope/ecosystem support; CLI and wrapper Action licensing may differ. [Gitleaks](https://github.com/gitleaks/gitleaks), [OSV-Scanner](https://google.github.io/osv-scanner/). |
| Lighthouse CI | Repeatable web performance/audit reports | Supported isolated web builds; artifact reports without external upload by default. Begin unstable scores as advisory. [Official docs](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md). |

These are candidates, not a mandatory installation list. Check plan eligibility for GitHub code scanning/dependency review rather than assuming private-repo access; prefer suitable CLI alternatives when hosted features require payment. Avoid new self-hosted infrastructure merely for a metrics dashboard.

Implement suitable repository-only options within scope. When a service needs authorization/account activation, prepare reviewed configuration, minimal setup/permissions, verified limits, and a native fallback. Keep it disabled until activation and report its actual status. Do not post PR comments or send notifications without explicit authorization; summaries are the default reporting surface.

## 8. Validate the implemented contract

- Use an Actions-aware validator such as actionlint and inspect event conditions, expressions, paths, inputs, job dependencies, and check names. YAML parsing alone does not validate Actions semantics.
- Run locally reproducible equivalents of applicable required PR gates for affected components, including relevant integration/build/security/reporting checks. Do not reduce validation to a basic compile and a few tests when the contract requires more. Check clean-install/export behavior when dependency, package, or generated-input logic changes.
- Inspect side effects first; use disposable synthetic services/state and finite timeouts. Verify a representative local environment and identify remaining hosted/platform matrix entries. Local runner emulation does not prove GitHub behavior.
- Exercise applicable failure, missing-data, and intentional-skip reporting/gate behavior without touching production. Ensure report generation preserves failures and required missing/skipped checks cannot produce false-green status.
- Distinguish existing failures from regressions; retain sanitized evidence and repair defects introduced by this pass. Do not repeat unchanged passing suites without a reason. Continue independent checks around concrete blockers.
- For documentation/prompt-only edits, inspect consistency, references, links, and the diff; no application suite is needed unless executable behavior changed.
- Review the final diff for scope/security and preserved work. Update existing CI docs and relevant tracker/handoff with workflow responsibilities, commands, gate policy, report locations, baseline rules, integrations, and deferred checks.
- If hosted runs are authorized/available, inspect required checks on the exact final commit. Do not push or activate services simply to obtain hosted evidence without authorization.

## Acceptance and stop conditions

Every relevant category has a supported implementation or a specific omission/blocker. Events and workflow boundaries match their responsibilities. Required checks cover supported components and important behavior, with no concealed configuration defect or false-green route. Applicable local gates pass or unresolved failures are reported explicitly. Summaries, retained reports, and attributable metrics are implemented and failure handling is checked. Integration choices have current eligibility evidence and accurate activation status.

Stop when the CI contract, reporting, relevant validation, documentation, and handoff are complete. Continue independent work around blockers; do not perform unrelated rewrites, endless reruns, external activation, or release operations to claim readiness.

## Final report

Use this structure. Keep the chat report concise and link detailed evidence.

# CI Readiness Report

## Overall status

**Expected pull-request result:** LOCALLY READY — HOSTED UNVERIFIED | HOSTED PASS CONFIRMED | BLOCKED | UNVERIFIED

Explain the result in one paragraph. LOCALLY READY requires applicable locally reproducible required gates to pass, with hosted/platform limits stated. HOSTED PASS CONFIRMED requires observed required checks on the exact final commit: identify tested SHA(s) and run links. BLOCKED means a known required failure/unmet requirement; UNVERIFIED means insufficient evidence for readiness. A prior commit's pass does not qualify changed source.

## Workflow and check map

| Workflow / exact check | Purpose | Event / platform | Required or advisory | Actual or expected result |
|---|---|---|---|---|
| `<name>` | `<behavior>` | `<trigger/matrix>` | `<policy>` | Expected pass / Observed pass / Unverified / Blocked / Intentional skip |

Explain skips and distinguish recommended repository settings from applied configuration.

## Validation performed

| Validation | PASS / FAIL / NOT RUN / N/A | Evidence and candidate |
|---|---|---|
| `<check/suite/build/scan/report/platform>` | `<actual result>` | `<command/run link; SHA or dirty-worktree identity>` |

Separate inspection, local execution, and hosted evidence. Include material omissions; never mark unrun validation PASS.

## Quality and CI health

| Metric | Measured value | Baseline / delta | Evidence / sample / limit |
|---|---|---|---|
| `<useful metric>` | `<units or unavailable>` | `<comparable baseline or none>` | `<report/run link and scope>` |

Link implemented summaries/reports and identify unverified hosted rendering. Do not fill the table with invented measurements.

## Changes and integrations

Summarize what changed, why, and resulting coverage/reporting. State integration status: active and verified, configured but unverified, prepared pending activation, or recommended only. Include verified free-tier limits/source/date, external data sent, and setup still required.

## Remaining work

List material blockers, unverified checks/environments, and up to five prioritized follow-ups with one bounded next action each. State actual commit/push/hosted-run status. Omit speculative backlog; technical CI success is separate from owner acceptance and release approval.
