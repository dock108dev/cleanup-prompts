# Test value audit and efficient execution

Audit whether the tests in scope protect behavior that matters, then improve weak coverage and explain the evidence in plain language. A large passing count is not the outcome: the reader should understand what could break, which test would catch it, and what remains unproven.

Follow the [playbook](playbook.md) for scope, audit-only mode, preservation, authorization, and stopping. Use the [CI prompt](ci.md) when implementing workflow reporting; this prompt owns test-value review. Do not expand a targeted cleanup into an unsolicited rewrite of the entire suite.

## 1. Establish what deserves protection

Read product requirements, supported workflows, relevant implementation, test discovery/configuration, fixtures, assertions, and CI commands. Identify the important user outcomes and engineering contracts in scope: successful journeys, data integrity, permissions, calculations, compatibility, failure handling, and recovery as applicable.

Inventory every in-scope test case, including meaningful parameterized cases. Group cases with the same purpose for reporting, but inspect their assertions and setup rather than inferring value from names. Compare collected tests with the tests CI actually runs; identify disabled, skipped, quarantined, excluded, and never-discovered cases. For a full audit, cover the entire suite. If coverage is sampled or incomplete, state exactly what was reviewed and leave the remainder unverified; do not claim every test was audited.

## 2. Evaluate each case's value

For each case or closely related group, answer:

- **Behavior:** What observable result or supported contract does it check, under which inputs or failure conditions?
- **Importance:** What user problem, data loss, security failure, operational failure, or maintenance risk would a regression cause?
- **Detection:** What plausible defect would make this test fail? Inspect the assertion and the code it exercises. A test name, execution without an exception, or a coverage hit alone is insufficient evidence.
- **Realism and boundary:** Does the setup exercise the relevant implementation? Do mocks replace the behavior being claimed? Distinguish isolated logic, integration, simulated UI, real platform execution, and live-service evidence.
- **Distinct contribution:** Does this case cover a different boundary, input, platform, or regression? Overlap across unit and integration layers can be valuable; similar names do not establish redundancy.
- **Trustworthiness:** Can the assertion pass vacuously, swallow an error, compare a result with itself, copy the implementation's calculation, depend on order/time/network, or accept an overly broad outcome? Could the suite pass with no tests collected?

Assign a supported disposition: **keep**, **strengthen**, **consolidate**, **remove**, or **investigate**. Keep useful regression, compatibility, invariant, and smoke checks even when their value is indirect. Do not remove a test merely because it is old, slow, mocked, or duplicates a code path. Before consolidation/removal, identify the replacement coverage and show that no unique behavior or required contract is lost. Unclear value calls for investigation, not automatic deletion.

Use a compact review map in the existing testing/CI documentation or the requested audit report:

| Behavior / scenario | Test reference(s) | Why it matters / plausible defect | Assertion and boundary evidence | Disposition / gap |
| --- | --- | --- | --- | --- |
| `<observable outcome>` | `<file and case IDs>` | `<consequence and failure caught>` | `<what is asserted; what is mocked>` | `<supported action>` |

Keep identifiers traceable and group rows for readability. Do not introduce a separate tracking system or duplicate the test suite in prose. In audit-only mode, report findings without editing tests or configuration.

## 3. Repair supported weaknesses

Prioritize missing or weak checks for important behavior over increasing test counts. Add or strengthen tests for concrete risks and regressions, using independently justified expected results and assertions on observable outcomes. Include relevant negative, boundary, and recovery cases. Rename vague tests so their scenario and expected result are clear.

For a suspicious or high-value assertion, use a focused negative control or temporary mutation in disposable state when practical: introduce the plausible defect and confirm the intended assertion catches it. A setup/import failure is not proof that the behavioral assertion works. Restore the mutation and verify the final state. Record which cases were exercised this way; inspection alone must not be described as demonstrated defect detection. Whole-suite mutation testing is optional, not a universal gate.

Preserve useful coverage when simplifying redundant setup/cases. Fix unstable dependencies where feasible; do not hide failures with retries, broad skips, relaxed assertions, or threshold changes. Use isolated synthetic data and honor existing limits on external activity.

Choose execution using the policy below and the target's applicable requirements. Verify discovery and skip reasons, and confirm tests exercise the final implementation. Do not add tests that merely mirror the implementation or inflate percentages.

## 4. Select local tests using tools and change impact

Do not default to reproducing the full CI suite locally after each edit or cleanup prompt. Prefer the repository's supported affected-test command, dependency-aware runner, incremental build, and valid result cache. Discover these before manually selecting cases or inventing a selector. The number of changed files is not a risk measure: one shared fixture can affect more tests than nine isolated files.

Distinguish three mechanisms: dependency-based selection chooses tests affected by changed inputs; predictive selection uses historical evidence to estimate useful tests and may miss failures; caching reuses prior results for matching inputs. Agent judgment alone is not a predictive engine. Compilation alone does not establish which behavioral tests can safely be omitted.

### Discover and qualify the available mechanism

Inspect the installed runner/build-tool versions, manifests, scripts, dependency graph, coverage/dependency data, cache configuration, and existing local/CI commands. Use current official documentation and local help to confirm supported flags and interactions. Prefer a working existing integration over a new service or custom framework. Examples to investigate, not commands to install blindly:

| Stack / existing tool | Supported starting point | Important qualification |
| --- | --- | --- |
| Python / pytest | [pytest-testmon](https://www.testmon.org/) with `pytest --testmon` | Records executed-code dependencies; needs an initial full collection run and retained local data. Check plugin compatibility, selector/coverage interactions, and inputs it cannot track. |
| JavaScript / TypeScript with Jest | [Related tests](https://jestjs.io/docs/cli) with `jest --findRelatedTests <source-files>` | Supply the complete relevant change set and account for dependencies outside the runner's graph. |
| JavaScript / TypeScript with Vitest | [Related tests](https://vitest.dev/guide/cli#vitest-related) with `vitest related --run <source-files>` | Static import analysis has limits for dynamically resolved imports and non-imported inputs. |
| Repositories already using Nx | [Affected tasks](https://nx.dev/docs/features/ci-features/affected) | Select impacted projects/tasks through the project graph; verify base/head and inclusion of local edits. Project selection is not necessarily individual-test selection. |
| Gradle / Maven with Develocity | [Predictive Test Selection](https://docs.gradle.com/develocity/predictive-test-selection) | Requires an enabled extension and historical build data; verify existing entitlement, configuration, and local-build support. Do not assume it is available because Gradle is installed. |

Examples checked against official documentation on 2026-11-03; recheck against the target's installed versions. These options are alternatives for different stacks, not a mandatory bundle. For unsupported stacks or unreliable graphs, use existing package/module suites and explicit test references with a documented reason.

### Plan one bounded local run

- Establish the exact comparison and include staged, unstaged, relevant untracked, deleted, and renamed files. Branch scope also includes changes since the identified merge base. A HEAD-only comparison must not silently omit the agent's working changes.
- Select affected tests plus changed/new tests and relevant regression cases. Follow transitive dependents, shared fixtures, test helpers, configuration, generated inputs, schemas/migrations, lockfiles, and external/non-code inputs. Explicitly include changes the tool cannot model.
- During iteration, run the selected checks for the current change. At handoff, consolidate applicable local verification once for the final state. Do not repeat the same suite for each prompt, each report, or each cooperating agent. Reuse existing evidence only when the relevant code, tests, dependencies, configuration, environment, and command inputs match; dirty worktrees need more than a commit SHA. Label cached/reused evidence separately from fresh execution.
- State a short selection rationale before a costly run: affected behavior, selection tool/command, extra checks needed, and why anything broader is necessary. Use observed timings when available; do not fabricate time savings or impose an arbitrary test-count cap.
- Expand first to the affected package/subsystem when the graph is unavailable, stale, incomplete, or cannot explain an empty selection. Expand to the full local suite only for a concrete cross-cutting risk, selector baseline/qualification, explicit local gate, or unresolved impact that cannot be bounded. State that reason; do not silently fall back to full CI just because selection is inconvenient.
- Distinguish a supported “no affected tests” outcome from accidental zero-test collection. No affected tests means no fresh test execution, not a test pass. Ensure changed/new tests were discoverable and handle the runner's documented exit semantics without swallowing genuine failures.
- Keep repository-required merge/release checks intact. A hosted merge gate is not automatically a requirement to run the same suite during every local iteration. If repository instructions explicitly require full local checks, honor them at the required checkpoint and propose a precise policy update if they cause avoidable duplication.

### When an implementation slice is needed

Prompt changes can stop redundant runs and direct agents to existing tools immediately. Reliable automated selection needs a bounded repository change when the tool, dependency data, or command is missing. In an authorized testing/tooling improvement pass, implement a compatible local integration when feasible; otherwise specify one concrete follow-up with commands, inputs, fallback rules, and acceptance checks. Do not claim a selection engine was installed by changing this prompt, or deploy one across unrelated projects.

The implementation should provide a discoverable local affected-test entry point and an explicit full-suite override, with clear first-run behavior, ignored local selection data, safe cache invalidation, and visible selection/fallback reasons. Persist reusable local data where appropriate instead of deleting and rebuilding it on every agent run. Isolate incompatible environments/worktrees; do not reuse history or caches solely because branch names match. Installing new tools follows the target's dependency policy; new accounts, uploads, and paid services follow existing authorization.

Qualify the selector with bounded disposable examples: a leaf change, a shared dependency/fixture change, a new test, a deleted/renamed input, a non-code/configuration change, and missing/stale selection data. Verify that relevant tests run, genuine failures remain failures, and uncertain selection broadens visibly. Compare selected runs with full-run evidence for representative changes before relying on the integration. Retain full required CI checks while proving local selection, and use existing periodic/full runs to detect missed failures; do not run a full suite after every selected run, which defeats the optimization. Historical misses and measured time savings must be reported honestly.

## 5. Explain results at a glance

When CI is in scope, implement the [CI summary requirements](ci.md) in the actual workflow/reporting path. A chat explanation alone does not satisfy a request for CI summaries. Lead with **What was tested and why it matters**, before counts and coverage:

| Behavior checked | Actual result | Why it matters | Evidence / limit |
| --- | --- | --- | --- |
| `<plain-language scenario and expected outcome>` | `<PASS / FAIL / SKIPPED / CANCELLED / NOT RUN>` | `<consequence prevented>` | `<test/report link; important boundary>` |

Use a handful of meaningful groups, with detail available in linked results. Derive outcomes from the current run's reports or exact check outcomes; descriptions explain purpose but cannot establish a pass. If only suite-level evidence exists, report at that level and label it. A group with failed, skipped, missing, or unrun required cases must not appear as an unqualified PASS. Static analysis and builds remain separate from behavioral tests.

Include a short **Gaps and limits** section for important untested behavior, skipped cases and reasons, simulated boundaries, and environments not exercised. Keep detailed counts, coverage, timing, and diagnostics below the behavior summary. Never translate a mocked or offline pass into a claim about live operation or overall product readiness.

For selected runs, add **Why these tests ran**: change scope/base, selection mechanism, affected behavior, executed versus reused results, intentionally unselected suites, and any fallback reason. Distinguish not selected from a runner skip and from a failure to discover tests. Link selection details where available; do not list every omitted case in the overview or present a selected pass as a full-suite pass. For example: “Import logic changed; the dependency-aware runner selected importer and storage checks. UI tests were not selected. Full merge CI remains pending.” Use only actual evidence for counts and saved time.

## Acceptance and handoff

The defined scope is inspected, each reviewed case has a defensible purpose or a specific finding, important gaps are visible, supported in-scope repairs are verified, and any requested CI summary is implemented. Report audit coverage, meaningful behaviors protected, changes and reasons, actual checks/results, and remaining gaps. Separate local evidence from hosted CI and owner acceptance. Passing text checks on this prompt do not prove that a future agent will perform the audit correctly.
