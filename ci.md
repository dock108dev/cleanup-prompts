Review this repository and ensure its GitHub Actions CI setup is complete, reliable, secure, and appropriate for the actual project.

Your objective is to leave the repository in a state where a normal pull request should pass every required CI check. Do not merely review the workflows: implement necessary fixes unless they require credentials, external infrastructure, destructive changes, or a product decision.

## Scope and working approach

- Follow the user's requested scope. These are implementation prompts: make routine, supported code and documentation fixes directly. Use audit-only mode only when the user asks for a review without changes.
- Before editing, read the current README, relevant tracker (including a linked Desktop tracker), candidate identity, Git status, and applicable maintenance decisions. Check supported modes and existing work so the pass builds on the current project.
- Preserve unrelated changes, evidence, editable masters, owner data, frozen builds, and prepared review artifacts. Do not reset, discard, commit, push, publish, or release without authorization. If a review candidate must remain fixed, work separately and identify the resulting source changes.
- Existing authorization carries forward. This prompt alone does not authorize live collection, provider spending, owner-data access or migration, signed builds, or external operations.
- Do not ask permission for routine fixes or create an exhaustive change ledger. Summarize routine work briefly; explain complicated changes, their reason, effect, and remaining uncertainty. When a change requires an unresolved product or architecture decision, report a concrete follow-up and continue independent work.

First, inspect:

- The repository structure, languages, frameworks, package managers, lockfiles, build tools, and supported runtime versions.
- Existing contributor documentation and the project’s real commands for installing dependencies, formatting, linting, type-checking, testing, building, packaging, and security scanning.
- Every file under `.github/workflows/` and relevant supporting files such as reusable workflows, custom actions, Dependabot configuration, CODEOWNERS, release configuration, and scripts called by CI.
- The current Git status. Preserve unrelated user changes and do not reset, discard, commit, push, publish, or release anything unless explicitly authorized.

Then evaluate and improve the CI configuration.

The workflow should, where applicable:

- Run on pull requests and pushes to the repository’s primary branch.
- Use the correct package manager, lockfile, runtime, working directory, and project commands.
- Perform clean, deterministic dependency installation.
- Keep ordinary CI proportional to the project: basic compile/build or type checking and unit tests, plus existing checks that serve a demonstrated requirement. Avoid adding a broad validation matrix for completeness alone; do not remove existing required checks merely to reduce local validation work.
- Test the project’s supported runtime or platform matrix without adding obsolete or unsupported combinations.
- Use caching correctly without allowing stale caches to hide failures.
- Set explicit least-privilege `permissions`.
- Pin third-party actions to immutable full commit SHAs where practical, with comments identifying their release versions.
- Avoid exposing secrets to untrusted pull requests or executing unsafe pull-request code with elevated permissions.
- Use timeouts, concurrency controls, and cancellation of superseded runs.
- Upload useful test, coverage, or diagnostic artifacts when appropriate, including on failure where that helps troubleshooting.
- Keep job and check names stable, concise, and suitable for branch-protection rules.
- Avoid redundant jobs and unnecessary CI cost.
- Handle monorepos, generated files, submodules, services, databases, containers, or platform-specific builds correctly when present.
- Keep release, deployment, publishing, signing, and credential-dependent operations separate from ordinary pull-request CI.
- Include dependency-update automation and security checks only when appropriate for the repository.
- Use YAML and expressions that are valid for GitHub Actions.

Do not invent commands or requirements. Derive them from the repository. If the repository lacks a necessary script or configuration, add the smallest maintainable implementation that matches the project’s conventions.

## Validation Requirements

Keep validation lightweight and proportional to the change:
- Inspect the simplest relevant CI or project commands. For code changes, run the affected component's basic compile/build or type/syntax check and relevant unit tests. Use existing commands and environments; install dependencies only if needed.
- For documentation-only changes, check the edited text, links, referenced paths and commands against the repository. No application build or test suite is required unless executable behavior changed.
- Do not automatically run the full CI matrix, integration or end-to-end suites, browser walkthroughs, live smoke tests, security campaigns, packaging or signing. Add a focused check only when a changed behavior or observed failure makes it necessary.
- Inspect command side effects before execution. Use disposable synthetic state when tests write data; do not touch owner state or trigger external operations through a validation command without existing authorization.
- Use available baseline results; if a check fails, distinguish an existing failure from a regression. Fix regressions from this pass. Once the basic checks pass, stop unless new evidence justifies more testing.
- Report the checks actually run and their results, with material untested limits. Do not claim unrun checks passed or equate technical checks with owner acceptance, artifact qualification, or release approval.

For workflow changes, also inspect YAML/expressions with an existing local validator if available and verify changed paths, scripts, action inputs and job names. A disposable environment is useful for install-related changes, not a prerequisite for every pass. Review the final diff for scope and security regressions.

If GitHub access is available, inspect recent Actions runs and required status checks. Do not change branch protection, repository settings, secrets, variables, environments, or external integrations without explicit authorization.

A successful result means:

- The workflow configuration matches the repository.
- The selected basic local checks pass; other checks are explicitly unrun or supported by current hosted evidence.
- No known configuration error should prevent GitHub-hosted jobs from passing.
- Remaining uncertainty is explicitly identified.
- The final report gives the user a clear picture of what a new pull request should show.

Use this exact final-report structure:

# CI Readiness Report

## Overall status

**Expected pull-request result:** LOCALLY READY — HOSTED UNVERIFIED | HOSTED PASS CONFIRMED | BLOCKED

One concise paragraph explaining the result. Local readiness is an expectation, not a hosted pass. Use HOSTED PASS CONFIRMED only for observed required checks on the exact current commit; identify that commit. Do not transfer a prior commit's result to changed source.

## Expected GitHub checks

| Check | Purpose | Expected result |
|---|---|---|
| `<exact check name>` | `<what it validates>` | Expected pass / Unverified / Observed pass / Blocked |
| `<exact check name>` | `<what it validates>` | Expected pass / Unverified / Observed pass / Blocked |

List the exact check or job names users should expect to see on a pull request. Include expected skipped checks only when the skip is intentional, and explain the triggering condition.

## Validation performed

| Validation | Result | Evidence |
|---|---|---|
| Workflow configuration | PASS/FAIL/NOT RUN | `<tool or inspection performed>` |
| Basic compile/build or type check | PASS/FAIL/NOT RUN | `<command and concise result>` |
| Relevant unit tests | PASS/FAIL/NOT RUN | `<command and concise result>` |

Add rows only for additional checks actually relevant to this pass. Never use “PASS” for an unrun validation. State material unrun hosted/platform checks briefly without expanding the local workload.

## Changes

Summarize routine fixes briefly. Explain complicated workflow or supporting-code changes, why they were needed, and their effect on expected checks.

## Remaining limits

List material unverified checks, external requirements, or decisions still needed. Distinguish configuration inspection, local execution, and exact-commit hosted evidence. Omit this section if there are no material limits.
