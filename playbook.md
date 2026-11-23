# Cleanup harness playbook

## Scope and mode

Treat breadth and permission to edit as separate choices. Carry forward the user's explicit scope and existing authorization.

| Request | Breadth | Action |
| --- | --- | --- |
| “Run the cleanup harness” or “run the relevant cleanup prompts” | Local staged, unstaged, and relevant untracked changes, plus affected callers, contracts, tests, and docs | Implement supported cleanup and verify it |
| “Run cleanup for this branch” | Branch changes against the identified base, plus local changes and affected paths | Implement supported cleanup and verify it |
| “Run broader cleanup” or “clean up the whole repo” | Named subsystem or entire repository, as requested | Implement supported cleanup and verify it |
| “Full audit,” “review only,” or “no edits” | Entire repository for a full audit; otherwise the requested scope | Inspect and report; do not edit source or configuration |
| “Full audit and fix the findings” | Entire repository | Review applicable areas and implement supported in-scope fixes |

An explicitly named prompt, directory, issue, or subsystem narrows the work unless the user says otherwise. A larger scope expands coverage, not permission to change product behavior or perform external actions.

While the owner is the sole customer, UI/UX redesign, visual polish, persona or usability studies, and design acceptance are out of scope unless explicitly requested. Do not revive archived design plans or use them as completion gates. Preserve existing application behavior and verify functional correctness, security, and recovery where the change requires it, including frontend behavior.

For a clean working tree with no requested range, perform a bounded read-only triage of repository instructions, manifests, workflows, documented checks, and obvious inconsistencies. Report that there is no local diff. Do not silently audit the whole repository, select an arbitrary previous commit, or manufacture edits. If evidence identifies a concrete routine cleanup within that triage, explain it and apply it in cleanup mode.

## Establish the starting state

- Resolve the target directory from the request and current workspace. Ask only if the target is genuinely ambiguous. Read applicable `AGENTS.md` files, including nested instructions before touching those paths.
- Inspect branch, status, staged and unstaged diffs, relevant untracked files, and any existing merge/rebase state. Deleted and renamed files count. Record enough of the starting state to distinguish existing work from this pass; do not dump sensitive file contents.
- For branch scope, identify the requested or repository-configured base and merge base. State the exact comparison. Do not assume `HEAD~1`, a branch named `main`, or that the tracking branch is the review base. If no reliable base exists, ask for it while doing independent inspection.
- Read the target's requirements, relevant plan, manifests, scripts, workflows, and available validation evidence. Derive commands from those sources, not from a universal language checklist. Inspect command side effects and runtime targets before running them.
- Identify impacted behavior beyond changed lines without widening the pass to unrelated subsystems. If Git or required evidence is unavailable, describe the limit and use the available files; never present a fabricated diff-based review.

## Route the prompts

Consider every catalog entry for applicability, but read full instructions only for selected prompts. A full audit considers every applicable area, including unchanged implementation. “No diff” is not a reason to skip an area in a full audit.

| Prompt | Select when the scope includes |
| --- | --- |
| [Repository cleanup](cleanup.md) | Structure, readability, oversized files, ignore rules, tracked artifacts, or general code hygiene |
| [Documentation](docs.md) | Changed behavior or commands needing documentation, stale instructions, broken references, or doc organization |
| [Backend and database](backend-db-cleanup.md) | APIs, persistence, transactions, migrations, jobs, data meaning, or backend performance |
| [Error handling](abend.md) | Failure, retry, timeout, cancellation, logging, fallback, or recovery paths |
| [Security](security.md) | Trust boundaries, permissions, input handling, secrets, dependency changes, browser/native boundaries, or security review |
| [Sources of truth](ssot.md) | Duplicated rules/configuration, conflicting ownership, repeated policy, or parallel implementations |
| [Test value, pruning, and selection](testing.md) | Tests or tested behavior affected by the scope, requested pruning, wasteful local execution, test-quality/tooling review, or a full audit; inspect independent contracts, assertion value, and available selection tools |
| [CI design and efficiency](ci.md) | Workflows, build/test tooling, dependency/runtime changes affecting gates, or requested CI review; establish gate authority and measure relevant waste before optimizing |
| [Next Steps](next_steps.md) | An identified Next Steps document whose status or remaining plan needs reconciliation within the request |

Do not route exclusively by filename: follow affected behavior and shared dependencies. Use concrete reasons for skips, such as no persistent store or no identified Next Steps document. Distinguish not applicable from applicable but blocked/unverified.

Choose ordering from dependencies: resolve correctness and shared-contract issues before dependent changes; reconcile docs with the final behavior. Combine duplicate findings and run shared checks once when they cover the same final state.

## Execute a bounded pass

Before editing, identify the concrete issues and observable completion checks for the selected scope. In audit-only mode, investigate those issues and propose fixes without implementing them. Use non-mutating checks; if a check generates outputs, use a disposable location or clearly preserve the target's original state.

In cleanup mode, make evidence-backed repairs directly. Preserve product intent, user data, unrelated edits, staged work, retained evidence, and installed/frozen builds. A dirty tree is expected; do not reset, automatically stash, reformat unrelated files, or stage all changes as preparation.

Shared prompt language about implementation remains bounded by this run's selected scope and audit-only setting. Do not turn a targeted CI change into a new integrations project or a structure review into an architecture rewrite. Record consequential out-of-scope discoveries as bounded follow-ups.

Existing authorization remains valid. The cleanup request alone does not authorize commits, pushes, publishing, production migrations, live provider activity, paid services, or replacing installed builds. Complete independent local work before asking for a genuinely required decision; identify the exact blocked action and reason.

## Verification and stopping

Identify the source and checkpoint of a requirement before treating it as a blocker: observed merge rule, explicit local instruction, product/release requirement, or recommendation. An inherited job or benchmark is not automatically an owner-approved acceptance gate. Preserve active requirements until an authorized policy change; explain which milestone they actually govern. New advisory checks must not silently become completion gates.

Use the target's mandatory checks at their required checkpoint and the selected prompts' applicable verification requirements. For local iteration, discover and prefer supported affected-test/incremental commands using the [test-selection policy](testing.md). Include working-tree changes and transitive dependencies; explain selection and any broader fallback. Do not reproduce full CI locally by default, use changed-file counts as a risk threshold, or treat hosted merge gates as an instruction to rerun them after every edit. Honor explicit local requirements; run consolidated final checks once when required. Documentation-only work generally needs links/consistency checks and `git diff --check`, unless the target requires more.

Reuse trustworthy results for matching relevant inputs across prompts and agents; distinguish cached/reused evidence from newly run checks. Expand to the affected subsystem when selection is uncertain, and to the full suite only for a specific risk, explicit requirement, or necessary selector qualification. Do not weaken gates, claim unselected tests passed, or repeatedly rerun passing suites without changed inputs or new evidence. A broad audit requires broad inspection, not automatically the full runtime CI matrix on the local machine.

Distinguish existing failures, regressions introduced here, and failures of unknown origin. Use available baselines or safe isolated comparisons; do not reset the working tree to establish one. Fix regressions from this pass. Inspect the final diff, including newly created files, for unintended changes and incomplete fixes.

Stop when the selected areas have been covered, supported in-scope repairs are complete, required checks have passed, and no known in-scope blocker remains. Do not start another round looking for increasingly subjective improvements. A verified no-change result is valid.

If an essential command, environment, authorization, or product decision is missing, finish independent work and report the specific gap. Do not loop on an unchanged blocker, silently narrow coverage, or call incomplete work done. Broad audit coverage must identify areas actually inspected, any sampling, and limits; it is not proof of exhaustive correctness.

## Final report

Keep the handoff proportional to the work, with:

- **Scope and status:** target, mode, comparison/range if any, and `complete`, `blocked`, or `unverified`. Complete applies only to the defined cleanup or audit pass, not overall product readiness. An audit can complete with findings when the requested review coverage is complete; unmet required inspection stays blocked/unverified.
- **Routing:** selected prompts and reasons; concise reasons for skipped prompts. Group skips when the same reason applies.
- **Result:** concrete changes, or prioritized audit findings with file/evidence references and practical impact. State explicitly when no changes were warranted.
- **Verification:** lead with the behaviors actually checked, why they matter, actual outcomes, and important evidence limits; then commands/counts as useful detail. Include failures, skipped required checks, and uncertainty about pre-existing failures. When tests were audited, state the inspected scope and remaining gaps.
- **Remaining work:** consequential unresolved items, why each remains, and its next action. Keep source changes, local checks, hosted CI, installation/deployment, and owner acceptance separate.

Report in chat unless the user or target instructions require a durable report. Avoid introducing a new tracker or report directory for every run.
