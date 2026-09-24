Documentation and Repository Accuracy Implementation Prompt

You are the engineer assigned to create the project documentation from the current source code and make small repo fixes discovered while validating it.

Build on the existing documentation and maintenance decisions. Reconcile stale claims instead of recreating a completed documentation pass. The docs should teach a new engineer what the system does, how to run it, how to test it, how it is configured, and where important behavior lives. Implement small fixes when validation shows the repo and the intended workflow are out of sync.

## Scope and working approach

- Follow the user's requested scope. These are implementation prompts: make routine, supported code and documentation fixes directly. Use audit-only mode only when the user asks for a review without changes.
- Before editing, read the current README, relevant tracker (including a linked Desktop tracker), candidate identity, Git status, and applicable maintenance decisions. Check supported modes and existing work so the pass builds on the current project.
- Preserve unrelated changes, evidence, editable masters, owner data, frozen builds, and prepared review artifacts. Do not reset, discard, commit, push, publish, or release without authorization. If a review candidate must remain fixed, work separately and identify the resulting source changes.
- Existing authorization carries forward. This prompt alone does not authorize live collection, provider spending, owner-data access or migration, signed builds, or external operations.
- Do not ask permission for routine fixes or create an exhaustive change ledger. Summarize routine work briefly; explain complicated changes, their reason, effect, and remaining uncertainty. When a change requires an unresolved product or architecture decision, report a concrete follow-up and continue independent work.

## Objective

Leave the repository in a state where:
- A new engineer can understand what the system does.
- Setup and test instructions work.
- Docs describe implemented behavior.
- README, core docs, and source comments make sense without knowing the project's internal tasks, slices, phases, or implementation history.
- Examples, paths, and commands are verified.
- Small repo defects discovered while validating docs are corrected.
- The test/build surface still passes.

## Scope

Review the full repository, including:
- source directories such as `/src`, `/app`, `/services`, `/api`, or equivalents
- entry points
- scripts and task runners
- schedulers, workers, and background jobs
- data models, schemas, and migrations
- external integrations
- environment variables and runtime configuration
- local development workflow
- deployment and operational assumptions
- CI or local validation configuration
- existing README or docs content, if present

Build an accurate model of:
- what the system does today
- how to run it locally
- how to test it
- what is production-relevant
- what is intentionally unsupported
- what code paths are unused or experimental and should be removed, renamed, or clearly marked

## Implementation Requirements

### Documentation creation and updates
- Keep root-level docs limited to critical information, usually the README and any standard project files.
- Put supporting detail in `/docs` when the repo uses or should use that structure.
- Check relevant existing claims against code, config, scripts, or available evidence. Preserve valid ownership and maintenance decisions; do not repeat a whole-repo verification campaign for unrelated text.
- Reconcile current instructions with linked trackers, including Desktop trackers. Clearly distinguish current checkout status from historical candidate evidence; do not rewrite historical results as current qualification.
- Merge overlapping explanations into the clearest canonical location.
- Rewrite inaccurate sections to match current code and configuration.
- Add docs for important implemented behavior.
- Keep docs explicit and operational: commands, environment variables, services, data flows, and known limitations.
- Create docs that directly help engineers run, test, operate, or modify the project.

### Keep development history out of lasting documentation

Prepare the documentation for readers of `main`: users, contributors, reviewers, and external tools should learn what exists today without reconstructing how the team built it. Apply this during ordinary documentation cleanup and before a merge; this prompt does not itself authorize merging.

- Inspect the README, core setup/architecture/API/testing/operations docs, docstrings, source comments, examples, and explanatory text in scripts and tests for internal planning language. Look for numbered slices, phases, tasks, ranks, milestones, work packets, and shorthand such as `B2`, `B9`, or `T1/T2`, as well as handoff narratives and stale next-task instructions. Search by context; these terms can also describe legitimate product concepts.
- Rewrite affected passages around the current feature, responsibility, contract, constraint, or reason. Remove progress narration such as “added in Slice 8,” “Phase 2 complete,” “for Task 4,” and “the next engineer should implement B3.” Do not simply strip the label and leave an unclear sentence.
- Keep useful technical detail: behavior, assumptions, invariants, design rationale, compatibility requirements, known limitations, and operational instructions. Comments should explain the code and why a decision matters now. Replace completed TODOs; move planning-only follow-ups to the designated tracker while retaining any current limitation where readers need it.
- Keep working plans, task breakdowns, handoffs, acceptance records, and historical evidence in an existing designated location such as `docs/planning/`, `docs/history/`, or clearly named engineering tracker/record files. A file being under `docs/` does not by itself make it a history file: core docs still need to stand on their own. Prefer the repo's established locations and avoid creating a second tracker or an exhaustive migration ledger.
- Consolidate scattered planning narrative into that location only when it is still useful and editable. Preserve immutable evidence, historical results, exact candidate identities, and frozen review artifacts unchanged. Fix links when moving editable material; link to retained records where needed instead of copying their chronology into core docs.
- State current support and release limitations plainly. For example, describe a locally delivered build and its pending owner review without requiring readers to understand “B9/B10.” Keep precise build identifiers and evidence links where they establish which artifact a claim concerns. Removing planning jargon must never turn technical verification into owner acceptance or release approval.
- Use descriptive headings and link labels in the README and core docs. A reader should be able to complete setup, understand behavior, and find limitations without opening an internal task tracker. Link to engineering history only where useful; do not make it the main product explanation.
- Do not perform a blind repository-wide replacement. Preserve meaningful domain terms such as a scheduler task, game phase, or array slice, along with real release/schema/API versions, issue references that explain a current constraint, and necessary provenance. Do not rename public APIs, persisted fields, migrations, fixture IDs, evidence paths, or hashed content just to remove planning labels. If these require broader migration work, record that separately; clean up surrounding prose now.
- Treat user-visible messages or generated documentation containing the same jargon as cleanup candidates too. If changing them affects executable behavior or contracts, use the repository-fix and proportional-validation rules below.

Examples of the intended rewrite (verify the underlying facts first):
- “Slice 8 matching layer” → “Matches venue markets using authoritative snapshots.”
- “B2 adds the bounded Mario conversation and custom-plan flow” → “Supports Mario conversations and custom plans within the documented editing limits.”
- “B1–B9 technically complete; B10 pending” → describe the available functionality, the exact delivered build where relevant, and the outstanding owner review in ordinary language.

### Repository fixes
When doc validation reveals small repo problems, fix them directly:
- broken scripts
- package commands that no longer match the source tree
- invalid examples
- missing sample environment keys
- config references that point at the wrong source
- incorrect paths
- references to removed files
- documented behavior that is intended but trivially broken

When a fix requires broader product or architecture direction, document the gap clearly with a concrete follow-up.

### Accuracy rules
- Every factual statement in docs should be verifiable from code, config, scripts, or executable behavior.
- Claims that cannot be verified should become explicit limitations or follow-up items.
- Separate automatic behavior from manual workflows.
- Separate production behavior from local development behavior.
- Call out intentional non-support where it matters.
- Prefer concrete descriptions over vague intent.

## Suggested Documentation Structure

Use the files the repo actually needs.

Root:
- `README.md`

Potential `/docs` files:
- `local-development.md`
- `testing.md`
- `deployment.md`
- `env-and-config.md`
- `architecture.md`
- `data-models.md`
- `integrations.md`
- `scheduler-and-jobs.md`
- `known-limitations.md`
- `operations.md`

Each doc should have a clear job for the engineer who will use it.
Keep internal plans and history in a clearly designated subsection or files, separate from these current-behavior references.

## Validation Requirements

Keep validation lightweight and proportional to the change:
- Inspect the simplest relevant CI or project commands. For code changes, run the affected component's basic compile/build or type/syntax check and relevant unit tests. Use existing commands and environments; install dependencies only if needed.
- For documentation-only changes, check the edited text, links, referenced paths and commands against the repository. No application build or test suite is required unless executable behavior changed.
- Repeat a targeted search of current-facing docs, comments, and explanatory text for planning labels and progress narratives. Review remaining matches in context, confirm they are meaningful domain/version/provenance references or belong in designated planning/history records, and check that rewritten passages preserve the actual behavior and limitations. Do not require zero keyword matches across the repo.
- Do not automatically run the full CI matrix, integration or end-to-end suites, browser walkthroughs, live smoke tests, security campaigns, packaging or signing. Add a focused check only when a changed behavior or observed failure makes it necessary.
- Inspect command side effects before execution. Use disposable synthetic state when tests write data; do not touch owner state or trigger external operations through a validation command without existing authorization.
- Use available baseline results; if a check fails, distinguish an existing failure from a regression. Fix regressions from this pass. Once the basic checks pass, stop unless new evidence justifies more testing.
- Report the checks actually run and their results, with material untested limits. Do not claim unrun checks passed or equate technical checks with owner acceptance, artifact qualification, or release approval.

## Acceptance Criteria

- README accurately explains what the repo is, how to run it, how to test it, and where deeper docs live.
- Supporting docs are current, consolidated, and useful.
- README, core docs, and source comments describe the product and code directly, without scattered task/slice/phase chronology or unexplained internal milestone labels.
- Useful planning history remains in designated records; evidence, technical rationale, exact artifact identity, and current limitations are preserved.
- Broken references are fixed.
- Small repo issues found during doc validation are implemented.
- Relevant tests/checks pass.
- Remaining gaps are clearly identified as follow-up work.

## Final Response

Include:
- Docs added, updated, consolidated, or removed.
- Briefly state where planning/history is retained and any material exceptions still requiring follow-up; do not reproduce the task-by-task history in the summary.
- Implementation fixes made while validating docs.
- Commands/checks run and results.
- Behavior documented as an explicit limitation because it could not be verified.
- Follow-up items that require a broader engineering or product decision.
