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

Use the actual language, framework and file responsibility to judge size. Read existing lint settings and documented structural decisions first. Keep stricter applicable project limits; do not raise them to fit current files. Where no relevant policy exists, use these maintenance defaults. These are cleanup thresholds, not claims of universal industry standards or ideal target sizes.

| Authored file type / role | Review above | Split or justify retention above | Useful extraction boundary |
| --- | ---: | ---: | --- |
| UI components: `.tsx`, `.jsx`, `.vue`, `.svelte`, Angular component `.ts` | 250 lines | 500 lines | Independent component, stateful behavior, data access or domain logic |
| JavaScript / TypeScript modules: `.js`, `.mjs`, `.cjs`, `.ts`, `.mts`, `.cts` | 300 | 600 | Feature, service, validation, transformation or transport |
| Python: `.py`, `.pyw` | 500 | 1,000 | Domain module, storage, provider adapter, orchestration or CLI |
| Swift: `.swift` | 400 | 1,000 | View, model, service or cohesive type responsibility |
| C#, Java, Kotlin: `.cs`, `.java`, `.kt`, `.kts` | 400 | 800 | Primary type or distinct responsibility within a large type |
| Go, Rust, C / C++: `.go`, `.rs`, `.c`, `.h`, `.cc`, `.cpp`, `.hpp` | 400 | 800 | Cohesive package module, subsystem or implementation responsibility |
| Godot scripts: `.gd` | 300 | 600 | Scene controller, gameplay system, UI or resource logic |
| Shell: `.sh`, `.bash`, `.zsh`, extensionless shell launchers | 100 | 200 | Thin entry point plus reusable operations; review whether complex logic belongs in an existing structured-language module |
| PowerShell: `.ps1`, `.psm1` | 200 | 400 | Command, reusable function group or module |
| Styles: `.css`, `.scss`, `.sass`, `.less` | 300 | 600 | Tokens, shared primitives, component or page styles |
| Markup / templates: `.html`, `.htm`, `.jinja`, `.jinja2`, `.j2`, `.hbs`, `.ejs` | 250 | 500 | Reusable partial, page section or layout; separate substantial script/style logic |
| Authored SQL logic: `.sql` | 300 | 600 | Distinct query, procedure or independently deployable operation |

Classify by role before extension: a UI component in `.ts` uses the component row; a Python file embedding a whole web UI needs review of its HTML, CSS and JavaScript responsibilities as well. Use shebangs or build configuration for extensionless files. For unlisted stacks, choose and briefly explain comparable thresholds using project conventions and current official tooling; do not silently apply a blanket 500-line rule.

The reference points differ: [ESLint `max-lines`](https://eslint.org/docs/latest/rules/max-lines) defaults to 300 when the rule is enabled; [Pylint `max-module-lines`](https://pylint.pycqa.org/en/stable/user_guide/configuration/all-options.html) defaults to 1,000; [SwiftLint `file_length`](https://realm.github.io/SwiftLint/file_length.html) defaults to warning at 400 and error at 1,000. [Google's shell guide](https://google.github.io/styleguide/shellguide.html#when-to-use-shell) recommends reconsidering the language beyond 100 lines or with complicated control flow. These references inform the table; the remaining numbers and earlier review triggers are explicit maintenance choices. They do not authorize a language migration. [Angular's guide](https://angular.dev/style-guide#one-concept-per-file) also favors one concept per file, with small related declarations allowed together.

- **At the review threshold:** inspect cohesion, dependency direction, oversized functions/types, nesting, duplicated policy and difficulty testing or changing the file. Split mixed responsibilities now; being below a threshold is not a reason to retain them.
- **At the upper threshold:** perform a coherent extraction within scope, or retain the file only with a concrete explanation of its single responsibility and why extraction would worsen maintainability or violate a real constraint. “Existing,” “working,” and “scripting language” are not sufficient reasons. An unresolved architecture decision becomes a bounded follow-up, not a misleading cleanup-complete claim.
- Split by responsibility, not equal-sized chunks. Use meaningful module names and explicit interfaces; avoid `part1`/`part2`, catch-all utilities, import cycles, hidden shared state and chains of tiny forwarding files. Preserve public imports, entry points, resource paths and side effects; check the affected behavior after extraction.
- Count physical lines under the existing readable formatting, including comments and blanks, unless the configured tool explicitly uses another metric; state that difference when relevant. Do not compress code, delete useful comments or change formatting to pass a count. Inspect dense one-line templates, embedded languages and long functions even when their file count is small.
- Test source uses its language/role thresholds; split by tested feature or behavior while keeping fixtures and shared setup usable. Generated code, vendored files, lockfiles, snapshots, bulk data and generated fixtures are excluded from mechanical splitting. Review their authored generators or surrounding logic instead. Do not rewrite applied migrations or split configs, schemas or notebooks that a consumer requires as one artifact; review their authored logic and supported composition mechanisms.
- Reuse prior retention decisions only while their responsibility, constraints and size assumptions still apply. Renew the review after material growth or added responsibilities. Keep explanations in existing maintenance notes or the short handoff; do not create an inventory of every large file or install a new linter merely to enforce this prompt.

### Consistency and standards
- Align folder names, file names, module names, and helper patterns with the rest of the repo.
- Consolidate duplicate utilities where the replacement is straightforward and low risk.
- Verify examples, sample configs, scaffolding, scripts, and environment templates are current and minimal.
- Keep behavior stable unless cleanup exposes a clear bug.

### Git ignores and tracked artifacts
- Review the current ignore rules and tracked files for generated test evidence, debug screenshots, recordings, logs, caches, build output, temporary files, and redundant source snapshots. Updating `.gitignore` alone does not remove already tracked files.
- Check how candidate files are used before removing them from tracking. Preserve required test/replay fixtures, runtime assets, editable source art, authored build tools, and frozen builds used by supported launchers. Do not blanket-ignore image, data, or build directories that contain authored inputs.
- Update ignore rules to cover disposable output, using narrow exceptions for required inputs and safe environment templates. Keep credentials and local owner state excluded.
- Remove unnecessary tracked artifacts from the Git index while preserving existing local copies and retained evidence. Do not delete local evidence or alter a frozen candidate to tidy the remote tree.
- Keep cleanup changes separate from unrelated staged or unfinished work. Commit and push only with existing authorization; when remote cleanup is requested and authorized, complete the push and verify the remote branch contains the cleanup.
- Normal removal affects the current remote tree, not older commits or historical repository size. Do not rewrite history, force-push, or purge retained artifacts without separate explicit authorization.
- Verify removed files remain locally available, are no longer tracked, and match the intended ignore rules. Check that required source and fixtures remain tracked. Where removal could affect execution, run focused checks from a clean export or checkout so leftover local files cannot hide missing dependencies.
- Keep historical report references truthful: identify evidence that is now local-only and fix active setup or test instructions that would otherwise require untracked files.

### Tests and project health
- Update tests when cleanup changes module boundaries, names, imports, or expected behavior.
- Remove tests that cover deleted unused code.
- Add focused tests if cleanup fixes a real bug or protects an important behavior.
- Run relevant validation before finishing.

## Implementation Workflow

1. Inventory the project structure, docs, scripts, entry points, and validation commands.
2. Identify cleanup targets: unused code, oversized files, duplication, inaccurate comments, broken references, inconsistent naming, stale ignore rules, and unnecessary tracked artifacts.
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
- Ignore rules cover generated output; unnecessary tracked artifacts are untracked with local copies preserved, while required inputs remain available in a fresh checkout.
- Large unused blocks and abandoned experiments are removed.
- Structural changes improve maintainability rather than merely reducing line counts. Reviewed cleanup targets use the applicable stack/role thresholds; files above the upper threshold are coherently split or have a supported retention decision or explicit unresolved follow-up.
- Edited code follows existing formatting conventions; relevant basic checks pass or failures are explained.
- Intended behavior is preserved within the scope covered by the basic checks.

## Final Response

Include:
- Cleanup summary.
- Documentation changes.
- Code structure changes.
- Tests/checks run and results.
- Repository hygiene changes, local-copy preservation, and actual commit/push status; distinguish current-tree removal from history cleanup.
- Complicated structural changes and any newly relevant retention decisions.
- Follow-up work that should be handled separately.
