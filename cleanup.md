Repository Cleanup Implementation Prompt

You are the engineer assigned to make this source tree clean, consistent, and easy to maintain.

Work from the code in front of you. Build on existing documentation and maintenance decisions; reconcile stale guidance instead of restarting a completed cleanup pass. Implement the cleanup, write the docs needed for the current codebase, run the appropriate checks, and leave the repo in a working state.

## Scope and working approach

- Follow the user's requested scope. These are implementation prompts: make routine, supported code and documentation fixes directly. Use audit-only mode only when the user asks for a review without changes.
- Before editing, read the current README, relevant tracker (including a linked Desktop tracker), candidate identity, Git status, and applicable maintenance decisions. Check supported modes and existing work so the pass builds on the current project.
- Preserve unrelated changes, evidence, editable masters, owner data, frozen builds, and prepared review artifacts. Do not reset, discard, commit, push, publish, or release without authorization. If a review candidate must remain fixed, work separately and identify the resulting source changes.
- Existing authorization carries forward. This prompt alone does not authorize live collection, provider spending, owner-data access or migration, signed builds, or external operations.
- Do not ask permission for routine fixes or create an exhaustive change ledger. Summarize routine work briefly; explain complicated changes, their reason, effect, and remaining uncertainty. When a change requires an unresolved product or architecture decision, report a concrete follow-up and continue independent work.

## Objective

Improve maintainability while preserving intended product behavior.

The finished repo should be easier to understand, easier to run, and safer for the next engineer to modify.

## Scope

### Documentation organization
- Keep the root README concise and useful.
- Put supporting documentation in `/docs` when the repo structure supports that convention.
- Write documentation from the current implementation and verified commands.
- Merge overlapping explanations into a single clear source.
- Keep setup, environment, deployment, testing, and operational docs aligned with the implemented repo.
- Create only docs that help an engineer run, test, operate, or modify the project.

### Code quality and readability
- Remove unused code, unused imports, unreachable paths, abandoned experiments, and commented-out blocks.
- Convert useful TODOs into clear, actionable notes in the right place.
- Improve unclear names when the change is localized and low risk.
- Add concise comments where intent is hard to infer from the code.
- Prefer comments that explain why something exists.
- Normalize formatting, imports, and organization according to existing project standards.

### File size and structure
- Prioritize mixed responsibilities, difficult changes, duplicated policy, missing behavioral coverage, and compressed multi-statement code.
- Use roughly 500 lines as a discovery hint, not a target or size limit. Small files can still be hard to maintain.
- Split or extract when it clearly improves readability or testability.
- Keep cohesive modules together when extraction would make the code harder to follow.
- Reuse existing large-file retention decisions when still applicable. Report only newly relevant structural issues or complicated extractions; do not inventory every large file.

### Consistency and standards
- Align folder names, file names, module names, and helper patterns with the rest of the repo.
- Consolidate duplicate utilities where the replacement is straightforward and low risk.
- Verify examples, sample configs, scaffolding, scripts, and environment templates are current and minimal.
- Keep behavior stable unless cleanup exposes a clear bug.

### Tests and project health
- Update tests when cleanup changes module boundaries, names, imports, or expected behavior.
- Remove tests that cover deleted unused code.
- Add focused tests if cleanup fixes a real bug or protects an important behavior.
- Run relevant validation before finishing.

## Implementation Workflow

1. Inventory the project structure, docs, scripts, entry points, and validation commands.
2. Identify cleanup targets: unused code, oversized files, duplication, inaccurate comments, broken references, and inconsistent naming.
3. Make small, coherent edits that preserve behavior.
4. Write or update docs from the implemented repository.
5. Run the basic relevant build/check and unit tests described below.
6. Fix breakage caused by the cleanup.
7. Provide a concise final summary of what changed and what remains.

## Validation Requirements

Keep validation lightweight and proportional to the change:
- Inspect the simplest relevant CI or project commands. For code changes, run the affected component's basic compile/build or type/syntax check and relevant unit tests. Use existing commands and environments; install dependencies only if needed.
- For documentation-only changes, check the edited text, links, referenced paths and commands against the repository. No application build or test suite is required unless executable behavior changed.
- Do not automatically run the full CI matrix, integration or end-to-end suites, browser walkthroughs, live smoke tests, security campaigns, packaging or signing. Add a focused check only when a changed behavior or observed failure makes it necessary.
- Inspect command side effects before execution. Use disposable synthetic state when tests write data; do not touch owner state or trigger external operations through a validation command without existing authorization.
- Use available baseline results; if a check fails, distinguish an existing failure from a regression. Fix regressions from this pass. Once the basic checks pass, stop unless new evidence justifies more testing.
- Report the checks actually run and their results, with material untested limits. Do not claim unrun checks passed or equate technical checks with owner acceptance, artifact qualification, or release approval.

## Acceptance Criteria

- Repo builds or starts using its documented local workflow.
- Relevant tests and checks pass.
- README is lean and points to deeper docs where appropriate.
- Supporting docs are organized, accurate, and useful.
- Unused code, inaccurate comments, and obvious leftovers are removed.
- Large unused blocks and abandoned experiments are removed.
- Structural changes improve maintainability rather than merely reducing line counts.
- Edited code follows existing formatting conventions; relevant basic checks pass or failures are explained.
- Intended behavior is preserved within the scope covered by the basic checks.

## Final Response

Include:
- Cleanup summary.
- Documentation changes.
- Code structure changes.
- Tests/checks run and results.
- Complicated structural changes and any newly relevant retention decisions.
- Follow-up work that should be handled separately.
