Documentation and Repository Accuracy Implementation Prompt

You are the engineer assigned to create the project documentation from the current source code and make small repo fixes discovered while validating it.

Treat this as the first documentation pass for the assigned codebase. The docs should teach a new engineer what the system does, how to run it, how to test it, how it is configured, and where important behavior lives. Implement small fixes when validation shows the repo and the intended workflow are out of sync.

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
- Use existing docs as source material after verifying each claim against code, config, scripts, or runnable behavior.
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

Before finishing:
- Run setup, build, lint, type-check, test, or smoke-test commands that the docs tell users to run.
- Fix docs or implementation when documented commands fail.
- Verify internal links, referenced paths, script names, and environment variable names.
- Run enough of the test suite to catch breakage from any implementation changes.
- If a command cannot be run locally, state why and document the correct next validation step.

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
