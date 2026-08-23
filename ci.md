Review this repository and ensure its GitHub Actions CI setup is complete, reliable, secure, and appropriate for the actual project.

Your objective is to leave the repository in a state where a normal pull request should pass every required CI check. Do not merely review the workflows: implement necessary fixes unless they require credentials, external infrastructure, destructive changes, or a product decision.

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
- Run all relevant formatting checks, linting, type-checking, unit tests, integration tests, builds, and repository-specific validation.
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

Validation requirements:

1. Validate the workflow YAML and GitHub Actions configuration with the best locally available tools.
2. Run the same install, format-check, lint, type-check, test, build, and other commands that CI will execute.
3. Where practical, test from a clean or disposable environment so untracked files and local caches cannot create a false pass.
4. Confirm that workflow-referenced paths, scripts, action inputs, matrix values, artifact paths, and output names exist and are correct.
5. Review the final diff for accidental scope expansion and security regressions.
6. Never describe a check as passing unless it was actually run successfully.
7. Clearly distinguish:
   - Locally validated checks
   - Configuration-only checks
   - Checks that can run only on GitHub-hosted runners
   - Checks blocked by credentials, infrastructure, platform access, or repository settings

If GitHub access is available, inspect recent Actions runs and required status checks. Do not change branch protection, repository settings, secrets, variables, environments, or external integrations without explicit authorization.

A successful result means:

- The workflow configuration matches the repository.
- Every locally reproducible CI command passes.
- No known configuration error should prevent GitHub-hosted jobs from passing.
- Remaining uncertainty is explicitly identified.
- The final report gives the user a clear picture of what a new pull request should show.

Use this exact final-report structure:

# CI Readiness Report

## Overall status

**Expected pull-request result:** ALL CHECKS PASSING | PASSING WITH EXTERNAL REQUIREMENTS | NOT READY

One concise paragraph explaining the result.

## Expected GitHub checks

| Check | Purpose | Expected result |
|---|---|---|
| `<exact check name>` | `<what it validates>` | Pass |
| `<exact check name>` | `<what it validates>` | Pass |

List the exact check or job names users should expect to see on a pull request. Include expected skipped checks only when the skip is intentional, and explain the triggering condition.

## Validation performed

| Validation | Result | Evidence |
|---|---|---|
| Workflow configuration | PASS/FAIL/NOT RUN | `<tool or inspection performed>` |
| Dependency installation | PASS/FAIL/NOT RUN | `<command and concise result>` |
| Formatting | PASS/FAIL/NOT RUN | `<command and concise result>` |
| Linting | PASS/FAIL/NOT RUN | `<command and concise result>` |
| Type checking | PASS/FAIL/NOT RUN | `<command and concise result>` |
| Tests | PASS/FAIL/NOT RUN | `<command, test count, and concise result>` |
| Build | PASS/FAIL/NOT RUN | `<command and concise result>` |

Add or remove rows to reflect the repository. Never use “PASS” for an unrun validation.

## Changes