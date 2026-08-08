Repository Cleanup Implementation Prompt

You are the engineer assigned to make this source tree clean, consistent, and easy to maintain.

Work from the code in front of you. Treat this as the first time an engineer will use these docs and the first time the repository is being shaped for day-to-day project work. Implement the cleanup, write the docs needed for the current codebase, run the appropriate checks, and leave the repo in a working state.

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
- Review source files over roughly 500 lines.
- Split or extract when it clearly improves readability or testability.
- Keep cohesive modules together when extraction would make the code harder to follow.
- Leave a short list of any files still over roughly 500 lines and why they were retained.

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
5. Run formatter, linter, type checks, tests, and smoke checks that are appropriate for the repo.
6. Fix breakage caused by the cleanup.
7. Provide a concise final summary of what changed and what remains.

## Acceptance Criteria

- Repo builds or starts using its documented local workflow.
- Relevant tests and checks pass.
- README is lean and points to deeper docs where appropriate.
- Supporting docs are organized, accurate, and useful.
- Unused code, inaccurate comments, and obvious leftovers are removed.
- Large unused blocks and abandoned experiments are removed.
- Source files over roughly 500 lines have a clear reason.
- Formatting and linting pass, or remaining warnings are explained clearly.
- Main user or developer flows still work.

## Final Response

Include:
- Cleanup summary.
- Documentation changes.
- Code structure changes.
- Tests/checks run and results.
- Files still over roughly 500 lines, with reason retained.
- Follow-up work that should be handled separately.
