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

## Validation Requirements

Keep validation lightweight and proportional to the change:
- Inspect the simplest relevant CI or project commands. For code changes, run the affected component's basic compile/build or type/syntax check and relevant unit tests. Use existing commands and environments; install dependencies only if needed.
- For documentation-only changes, check the edited text, links, referenced paths and commands against the repository. No application build or test suite is required unless executable behavior changed.
- Do not automatically run the full CI matrix, integration or end-to-end suites, browser walkthroughs, live smoke tests, security campaigns, packaging or signing. Add a focused check only when a changed behavior or observed failure makes it necessary.
- Inspect command side effects before execution. Use disposable synthetic state when tests write data; do not touch owner state or trigger external operations through a validation command without existing authorization.
- Use available baseline results; if a check fails, distinguish an existing failure from a regression. Fix regressions from this pass. Once the basic checks pass, stop unless new evidence justifies more testing.
- Report the checks actually run and their results, with material untested limits. Do not claim unrun checks passed or equate technical checks with owner acceptance, artifact qualification, or release approval.

## Acceptance Criteria

- README accurately explains what the repo is, how to run it, how to test it, and where deeper docs live.
- Supporting docs are current, consolidated, and useful.
- Broken references are fixed.
- Small repo issues found during doc validation are implemented.
- Relevant tests/checks pass.
- Remaining gaps are clearly identified as follow-up work.

## Final Response

Include:
- Docs added, updated, consolidated, or removed.
- Implementation fixes made while validating docs.
- Commands/checks run and results.
- Behavior documented as an explicit limitation because it could not be verified.
- Follow-up items that require a broader engineering or product decision.
