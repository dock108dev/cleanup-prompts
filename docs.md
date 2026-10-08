# Documentation and Repository Cleanup Implementation Prompt

Update the project documentation to explain the current software clearly, and clean up repository clutter discovered along the way. Make the changes directly, including small fixes to broken setup instructions, scripts, examples, and configuration.

## Working approach

- Read the README, applicable repository instructions, relevant source and configuration, and Git status. Build on useful existing docs.
- Use judgment about how much to inspect. Focus on what readers need to understand, run, test, and maintain the project.
- Make routine cleanup decisions without asking for confirmation. Leave unrelated code changes alone and flag larger product or architecture decisions briefly.
- Local notes and development artifacts do not need special archival treatment. Clean them up as part of this pass when useful; the maintainer generally handles their ongoing local organization.

## Documentation

- Keep the README concise: purpose, main capabilities, requirements, quickstart, basic testing, and links to useful supporting docs.
- Add or update supporting docs only when the project needs them. Consolidate duplicates and delete obsolete or unnecessary documentation.
- Describe what the software does today using the source, configuration, and existing commands. Correct stale claims and mention meaningful limitations plainly.
- Use portable paths and repository-owned instructions. Remove personal Desktop paths, private tracker references, internal prompts, and unrelated workspace routines.
- Remove task, slice, phase, milestone, and handoff narration from lasting docs and source comments. Rewrite useful explanations around current behavior and design rationale. Keep meaningful domain terms and real API or schema versions.
- Keep useful comments that explain behavior or a non-obvious decision. Remove stale TODOs, coding diaries, and redundant narration.
- Do not create evidence inventories, candidate identity records, acceptance ledgers, or historical archives for this cleanup. Ordinary documentation accuracy does not require proving every sentence through a separate validation exercise.

## Keep GitHub focused on the project

- Keep source, required configuration, dependency manifests and lockfiles, useful tests and fixtures, licenses, and documentation that helps someone use or contribute to the project.
- Remove unnecessary tracked coding notes, task lists, plans, agent handoffs, internal review records, screenshots, logs, compiled outputs, generated reports, and temporary or collected data. Do not relocate these into a public planning or history folder merely to retain them.
- If working material is still useful locally, keep it outside Git tracking and add focused ignore rules. Untrack already tracked local artifacts when appropriate; adding an ignore rule alone is insufficient.
- Delete clearly obsolete or disposable local clutter when appropriate. No comprehensive preservation process or cleanup ledger is needed.
- Check how files are used before removing them. Retain data, fixtures, or generated files required to run, test, build, or distribute the project. Keep credentials and personal data out of GitHub.
- Fix documentation links and script references affected by cleanup. Avoid broad ignore patterns that hide necessary project files.

## Small repository fixes

Fix straightforward problems encountered during the pass: incorrect paths, broken package commands, invalid examples, missing sample environment settings, references to removed files, and minor defects in the documented workflow. Keep larger refactors and new features out of scope.

## Validation

- For documentation and artifact cleanup, check edited text, links, paths, ignore rules, and affected file references. Run a diff whitespace check when Git is available.
- If code or executable configuration changes, run the relevant existing checks or tests. Run a build only when the change warrants it.
- Keep checks proportional. A docs pass does not require a full CI campaign, live service validation, packaging, or new evidence bundles.
- Report actual results honestly and mention significant unresolved problems. Do not commit or push unless requested.

## Final response

Briefly summarize the documentation changes, repository cleanup, small fixes, checks run, and any important remaining issue. Keep the summary practical and short.
