# CI that gives trustworthy answers with less repeated work

Improve this repository's GitHub Actions CI so a change gets useful, trustworthy feedback sooner, with measured use of compute. Implement supported workflow, script, reporting, and documentation repairs. Establish the behavior and current contract, measure where work goes, then remove unnecessary work before tuning what remains.

Follow the [playbook](playbook.md) for scope, audit-only mode, preservation, authorization, and stopping. Use [testing.md](testing.md) for test quality, pruning, local selection, and verification methods. A targeted CI repair is not permission for a repository-wide test campaign. Relevant quality areas need supported checks or explicit omissions; they do not all need to run on every event or after every edit.

## 1. Establish the contract and who requires it

Read applicable instructions, product requirements, README, active tracker, maintenance decisions, candidate identity, and Git status. Inspect relevant manifests, lockfiles, supported platforms, workflows, reusable workflows, custom actions, called scripts, test discovery, build/package commands, dependency-update and release configuration. Trace actual commands rather than assuming a standard language checklist.

When GitHub access is available, inspect current required checks, rulesets, merge-queue settings, and relevant run evidence. Otherwise continue repository-side work and mark settings/history unverified. Keep a concise map in existing CI documentation, or `docs/CI.md` when needed:

| Behavior / risk | Exact workflow, job, command | Event / platform / checkpoint | Required, advisory, scheduled, or N/A | Authority / evidence |
| --- | --- | --- | --- | --- |
| `<observable contract>` | `<executable check>` | `<where it governs>` | `<current status>` | `<ruleset, instruction, product requirement, or recommendation; source>` |

Distinguish an observed repository merge requirement, an explicit local checkpoint, a product/release requirement, an inherited workflow convention, and an engineering recommendation. A job existing in YAML does not establish that the owner made it a release gate. An active required check still governs current merges even if it looks redundant: preserve it until an authorized change to that contract is made. Explain the impact of any requirement that blocks completion or review.

This prompt authorizes scoped repository-side CI/tooling/reporting fixes. Existing authorization carries forward; it does not by itself authorize commits, pushes, publishing, releases, account installation, new external uploads, paid services, repository settings, secrets, variables, environments, signing, production operations, or provider spending. Use disposable synthetic state for data-writing checks. Preserve unrelated dirty work, owner data, credentials, retained evidence, editable masters, and frozen candidates. Prepare concrete configurations around external blockers and continue independent engineering.

## 2. Measure a baseline and choose useful changes

Use existing reports and a bounded sample: normally up to 30 recent runs from the last 30 days, with sample size/window stated. Include failed, cancelled, timed-out, and rerun work; separate PR, primary-branch, scheduled, and release workloads. Report incomplete observations explicitly. Do not crawl unlimited history or wait weeks for a baseline before fixing a demonstrated defect.

Inspect job and matrix entries, not just workflow duration. For expensive or repeated paths, capture available evidence for:

- Invocations per event/revision, duplicate triggers, superseded attempts, retries, and review-bot starts.
- Queue time, elapsed critical path, runner class/platform, summed runner execution minutes, and useful work completed. Parallel job minutes are not wall-clock duration or necessarily billable minutes.
- Checkout, dependency restore/install, build, service/fixture setup, test execution, and report/upload time. Missing phase timings remain unavailable until measured.
- Test scope, shard imbalance, worker count, memory/OOM evidence, cache hits and actual restore benefit, and artifact sizes/retention where material.

Rank bounded changes by demonstrated waste, feedback benefit, correctness risk, and effort. Typical opportunities are weak or duplicate tests, repeated event/review work, overbroad selection, setup larger than the selected task, then poor shard packing or runner sizing. Investigate the measured bottleneck rather than installing a fashionable runner, selector, or dashboard.

Compare equivalent inputs and report both feedback time and compute use. A smaller runner may cost less while delaying dependent work; more shards may finish sooner while repeating setup. Account for workload changes. Distinguish actual charges, measured usage, and estimates at dated published prices; sponsored capacity is not a paid bill. Do not promise another project's percentage saving or attribute a mixed before/after trend to one change. A missing baseline permits a first measurement, not an invented delta.

Implement changes in reviewable slices, using current evidence to decide the next slice. Stop when the requested scope is complete; do not turn the baseline into a new observability platform.

## 3. Decide what must run before expensive fanout

Reuse the stack's supported task graph, affected-test command, and existing CI classification. A small repository may need only straightforward job conditions. Add a shared planning step only when it removes meaningful repetition or makes selection safer; do not build a custom scheduler by default.

For a selector or planner, establish these contracts:

1. **Exact inputs.** Identify base, head, tested merge/queue candidate, event, policy version, and complete changed paths, including additions, deletions and renames. Account for API pagination/truncation, missing history and merge-base failures. Local commands also include staged, unstaged, and relevant untracked inputs under [testing.md](testing.md).
2. **Explainable ownership.** Include changed/new tests, affected owners and transitive consumers, shared fixtures/helpers, configuration, schemas, generated inputs, lockfiles and non-code dependencies. Missing static imports do not establish independence. Workflow, selector and policy changes receive their own coverage and the scope they can affect.
3. **Retained obligations.** Add applicable mandatory checks and critical smoke contracts independently of a narrowed test list. Select each test under its actual runtime/configuration; a filename alone is not an executable plan.
4. **Explicit outcomes.** Distinguish selected work, supported no-impact/N/A, reused results, and uncertainty. A malformed plan, missing owner, unrecognized input, failed diff, stale graph or unexplained empty selection must broaden visibly to an adequate subsystem/full run or fail planning. It cannot default to an empty green matrix. Configuration changes that invalidate the graph require broader coverage.
5. **Traceable reasons.** Retain enough candidate identity, inventory, selected commands and reasons to explain a surprising inclusion or omission. Validate plan data as data; never turn contributor-supplied strings into shell commands.

Dependency selection, predictive ranking and result caching are different mechanisms. Prefer deterministic supported ownership/dependency selection for omission decisions. A prediction's confidence is not dependency evidence. Qualify new selectors using the bounded cases in [testing.md](testing.md), including relevant historical regressions when available: demonstrate that the needed test is selected and that its behavioral assertion catches the defect. Record misses and repair the rule or widen the fallback.

Start unqualified omission policies in shadow mode: freeze the proposed subset before an already-planned broader run, then compare omitted failures without changing that run. State what would permit promotion, who owns that policy, and how to force broader execution. Retain existing required gates during qualification. Do not run the full suite after every selected local run; use representative qualification and existing broader runs to detect misses. Shadow mode records a proposal; it does not establish safe production selection.

### Keep the required result dependable

Where fanout is conditional, use a stable required result that evaluates the plan and all expected job outcomes, or an equally explicit existing mechanism. Ensure it is emitted for each required event/candidate. Top-level path filters must not strand a required check in pending state. Conditional jobs reporting success are not proof that required work ran; see [GitHub's required-check guidance](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).

An aggregate that uses `needs` must still inspect failed/skipped dependencies, for example through an appropriate `always()` condition. Its decision must require a valid plan and successful expected work. Only explicitly planned N/A work may be absent. Required failure, cancellation, unexpected skip, zero-test collection, missing shard, malformed/missing required report, or planner failure cannot yield an unqualified pass. A wholly cancelled workflow may produce no final summary; absence is not success.

Do not rename/remove active required statuses or change branch rules as an incidental optimization. Prepare any required settings migration, including the safe transition order, under existing authorization.

## 4. Put assurance at the right checkpoint

Keep workflows independently understandable, parallelize independent work, and use `needs` only for real dependencies. There is no requirement for one universal workflow or command.

| Event / responsibility | Appropriate work |
| --- | --- |
| `pull_request` | Fork-safe deterministic merge assurance for the change: applicable source quality, behavior, security, builds and representative supported platforms. Run cheap useful checks before expensive work where that reduces waste. |
| Push to maintained/primary branch | Verify the merged state and distinct integration/regression obligations; avoid repeating identical work with no additional assurance. |
| `merge_group` | Existing merge-queue requirements on the queued candidate, using stable names. |
| `schedule` | Broader compatibility, full/regression assurance, security-data refresh and measured benchmarks where justified. Record tested revision, cadence, freshness limit and failure owner. UTC schedules are not exact-time guarantees. |
| `workflow_dispatch` | Bounded diagnostics/full overrides with typed validated inputs and safe defaults. Document side effects and permissions. |
| Release/tag/environment | Exact-version packaging, provenance, signing, publishing and deployment under existing release authorization; separate from ordinary PR execution. |

Moving a check from PRs to background changes when defects are detected. Preserve active requirements; otherwise explain the risk, responsible repair path, freshness expectation and authorized policy before moving it. Scheduled green evidence for an older revision cannot qualify a newer release. A background failure must remain visible and actionable.

Cancel superseded PR work with event/ref-specific concurrency without cancelling unrelated or protected release work. Consider coalescing noisy updates only when cancellation/setup measurements justify it; do not add arbitrary sleeps that occupy runners. Retain distinct automatic reviews where policy requires them. Avoid repeating a full model review merely to reproduce earlier findings: reuse prior findings and review changed inputs on the current candidate. Local review still uses whatever model service it invokes and is not automatically offline or free.

Use `workflow_call` for genuine shared multi-job policy with typed inputs and narrowly passed secrets; composite actions for repeated step sequences. Avoid abstraction for one command, blanket secret inheritance, and unnecessary `workflow_run` chains. Keep event-specific differences explicit.

## 5. Protect behavior and the verification policy

Map applicable areas to meaningful checks; explain omissions rather than filling a matrix for appearance:

- **Source quality:** format in check mode, lint, types/compile, shell/script checks, Actions-aware validation, generated drift, useful executable examples and local links.
- **Behavior and journeys:** important logic, persistence, API/auth boundaries, calculations, failures/recovery, and affected supported user flows. Choose focused, integration, real-flow, property or differential checks under [testing.md](testing.md). Simulated UI is not native/device evidence; offline tests are not live-provider evidence.
- **Build/distribution/data:** production builds and relevant package contents, fresh-output install/import/start smoke, disposable services, supported schema/migration paths, deterministic fixtures and teardown. Clean checkout/export must not depend on leftover files. Keep signing/publication separate.
- **Security:** secret detection, relevant dependency/static analysis and container/IaC checks; narrow explained suppressions with review dates. Use current blocking policy and supported tool scope. Scanning unavailable is not zero findings.
- **Performance/compatibility:** repeatable representative size, latency or resource checks with comparable inputs, plus supported runtime/OS/architecture/service coverage. Start noisy or unbaselined new budgets as advisory; justify enforcement. Lab numbers do not establish production behavior.

Audit test value within the requested scope. Inspect assertions, fixtures, mock boundaries and plausible regressions; consolidate or prune supported waste without discarding unique protection. State sampling. A CI repair does not implicitly require a case-by-case whole-suite audit or a new test for each prompt sentence.

Keep established acceptance/review policy from the trusted base or default revision when judging a proposed policy change. Identify that policy revision separately from the code under test. A PR can propose better tests and rules, but cannot make its own removal of a guard the sole reason it passes. This does not mean running only old tests: exercise new/changed tests on the candidate and compare material weakenings against the established contract. Reading trusted instructions is not permission to execute untrusted code in a privileged context.

For selector, gate or policy changes, derive the validation obligation from trusted prior policy/classification or force an independently selected broader validation path. Candidate planner output cannot be the sole authority for omitting the checks that judge that planner. Run candidate code and tests without privileged credentials.

For new heuristic/model checks or noisy performance budgets, record false positives and missed defects before making them blocking. Replay relevant known failures and clean controls where practical; distinguish a useful finding from a nit or a pre-existing issue. Retain existing deterministic gates. New enforcement needs a supported product/repository/user policy, not an agent's wish to add a gate. Refine one useful verification loop before adding redundant reviewers. Persist a diff-triggered incident rule only when it adds distinct value; remove obsolete rules instead of growing a permanent checklist.

## 6. Reduce execution cost without weakening isolation

- Use deterministic lockfile installation, explicit supported runtimes, correct working directories and pinned tools/containers. Pin external actions to full commit SHAs with version comments and maintainable updates. A faster replacement tool needs equivalent relevant diagnostics/coverage before displacing an established check; keep a fallback when compatibility is incomplete.
- Measure cache restore and remaining install time. Key compatible dependency/build outputs by their actual lockfiles, runtime, platform, configuration and other relevant inputs. Correctness must survive a cold cache. Result reuse needs matching evidence inputs and must be labeled separately from fresh execution.
- Share builds/setup only when compatible and useful. Keep dependency restoration, artifact transport and result reuse distinct. Prefer the smallest needed artifacts and checkout scope, while retaining complete comparison inputs. A shallow checkout that cannot identify the base is not a safe optimization.
- Balance shards using observed durations and setup cost rather than equal file counts alone. Bound workers to available CPU/memory and measure OOM/retry behavior. Compare representative packing/runner changes before broad adoption; fewer jobs or larger machines are not objectives by themselves.
- Use least-privilege job permissions and narrowly scoped secrets. Disable unnecessary persisted checkout credentials. Treat PR metadata, workflow outputs, plans, reports, caches and artifacts as untrusted. Avoid shell injection and unsafe report rendering.
- Inspect fork behavior, `pull_request_target`, `workflow_run`, self-hosted persistence and cache/artifact trust. Untrusted code must not run with privileged credentials or unsafe persistent-runner access. Do not grant untrusted jobs trusted cache-writing privileges. Follow current [GitHub security guidance](https://docs.github.com/en/actions/reference/security/secure-use) for the actual event and permissions.
- Bound service startup, network calls, retries and cleanup. Preserve exit status through log/report pipelines; cleanup and applicable uploads should run after failure without masking it. Missing/malformed required reports are failures. Optional telemetry outages do not erase correctness results or block unrelated checks.
- Repair flakes and CI defects rather than rerunning to green, widening assertions, blanket-skipping or applying `continue-on-error`. A rerun alone does not prove flakiness. Any quarantine/removal follows the test-value policy and leaves the coverage gap visible.

## 7. Report what ran, what it protects, and what it cost

Implement reports in the actual Actions path, not only in the final chat. Prefer `GITHUB_STEP_SUMMARY`, annotations, existing reporters, downloadable JUnit/coverage/scan/build artifacts, and small supported scripts over a new reporting framework or service.

Lead with **What was tested and why it matters**:

| Behavior checked | Actual result | Why it matters | Evidence / limit |
| --- | --- | --- | --- |
| `<scenario and expected outcome>` | `<PASS / FAIL / SKIPPED / CANCELLED / NOT RUN>` | `<consequence prevented>` | `<current-run test/suite/report; mocked or untested boundary>` |

Use a handful of plain-language groups with detail linked. Derive outcomes from actual current-run IDs or reports; static suite descriptions are not execution evidence. If only suite-level evidence exists, label it. Mixed failed/skipped/missing required cases cannot produce an unqualified group PASS. Distinguish lint/build/security outcomes from behavioral evidence. Include **Gaps and limits** immediately below the table: important untested scenarios, skip reasons and environments/boundaries not exercised.

Then include:

- Run link, tested SHA/ref, event, platform/runtime/tool versions and relevant policy/plan identity. Distinguish PR head, tested merge and queue candidate. An earlier commit's result is not the final commit's result.
- **Why these tests ran** when selection/reuse applies: comparison, mechanism, selected behavior, retained obligations, intentional omissions, fallback and reused versus freshly executed results. Not selected, cached, runner-skipped, zero discovered and failed are different states. No fresh execution is not a fresh pass.
- Actual pass/fail/skip counts, durations, concise failures and useful diagnostics. Missing values remain unavailable, not zero.
- Applicable coverage/changed-code evidence, security severity/scope/freshness, comparable performance/size deltas, first-attempt reliability and observed compute/critical-path data. State sample, units, method and baseline; use median/p95 only with adequate comparable observations. Do not invent billing or savings.
- Main blocker and next useful action. Explain what a passing run does and does not establish.

Retain useful machine-readable results and failure traces/screenshots with unique run/matrix names and reasonable retention. Omit secrets, owner data, unnecessary source archives and bulky routine recordings. Escape untrusted text and never execute artifacts to render them. Keep independent workflows independent; a cross-workflow rollup must identify each run/candidate and cannot borrow stale scheduled success for a PR.

Use native/offline tooling first. Investigate an external service only for an identified unmet need. Before recommending activation, verify current official eligibility, public/private limits, retention, permissions, data sent, account/token requirements, pricing/quota behavior and a native fallback. Prepare configuration disabled where activation is still unauthorized. No PR comments or external notifications without explicit authorization. Report integration status as active and verified, configured but unverified, prepared pending activation, or recommendation only.

## 8. Validate the decision paths and finish

Match checks to the change. Run Actions-aware validation such as actionlint for workflow changes; YAML parsing alone is insufficient. Exercise selected local checks and applicable final local requirements under [testing.md](testing.md), reusing matching evidence across agents/prompts. An observed hosted gate is not a demand to reproduce the whole matrix after each local edit. Verify clean install/export when packaging, dependencies or generated inputs changed.

For a changed planner/aggregate/reporting path, exercise bounded synthetic cases: successful selected work; meaningful failure; planner failure/malformed output; missing history/unknown input; supported no-impact; unexpected empty collection; expected job skipped/cancelled; missing shard/report; and a changed workflow/shared fixture. Confirm selection and final status preserve the intended result. Include a relevant regression replay when available. Actionlint and a green happy path cannot prove these branches.

Verify policy changes against established policy and retain candidate identity. If hosted execution is authorized and available, inspect required results on the exact final commit; otherwise state the limit. Local runner emulation does not prove GitHub's event/permission behavior. Do not push or activate a service just to obtain evidence without authorization.

When a check fails, distinguish a new regression, pre-existing failure and unknown origin. Use a concrete hypothesis and a bounded discriminating check before rerunning. Repeated unchanged failure calls for different evidence or a specific blocker, not an unlimited retry loop. Complete independent in-scope fixes before requesting owner review. Never weaken an assertion/gate to end the loop.

For prompt/documentation-only changes, validate links, consistency and text hygiene plus repository-mandated checks; no application or hosted matrix is implied. Describe a realistic request and expected do/skip/report behavior; exercise a disposable fixture when practical. Text validation alone cannot establish agent compliance.

Review the final diff, preserve prior work, and update existing CI docs with commands, responsibilities, authority, selection/fallback, reports, baseline and activation status. Stop after supported in-scope repairs, integration and required verification are complete or a precise external blocker remains. No endless optimization or speculative integration backlog.

## Handoff

Lead with the concrete result and material gaps. Use **LOCALLY VERIFIED — HOSTED UNVERIFIED**, **HOSTED PASS CONFIRMED**, **BLOCKED**, or **UNVERIFIED**, scoped to the work performed. Local verification requires the applicable local contract; hosted confirmation requires observed required checks on the exact final commit. A selected test pass alone is not full CI readiness, product acceptance or release approval.

Explain what changed and why; show the decisive workflow/script branch where meaningful. Link the check/authority map and implemented behavior summaries. Report actual validation, pruning/selection scope, any remaining defect or platform gap, and comparable feedback/compute evidence or its absence. State commit/push/hosted/activation status explicitly. Identify the source and milestone effect of any remaining required work; give one bounded next action per material blocker.

## Design references

[Vincent Koc's CI case study](https://vincent.build/openclaw-ci-cost-reduction/) and [the Claude Code team's verification article](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/) informed this revision. They are case studies, not authority to copy another repository's tools, deletion targets, gate exceptions or release policy. Apply the target's measured needs and governing contract.
