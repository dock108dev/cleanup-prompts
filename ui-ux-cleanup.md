Review and improve this product so it takes less reading, less scrolling, and less interpretation to use. Implement a coherent cleanup of the ordinary user experience. Use familiar words and clear sentences. Keep the product's functionality and meaning intact.

## Start with the actual experience

Read the repository instructions, README, current tracker, local design guidance, and working-tree status. Identify the active app and its main user journeys; distinguish development screens and older prototypes from the current product. Preserve existing work and frozen review builds.

Inspect representative screens and their source, including dynamic messages. Use an isolated local preview with synthetic data where supported. Label older screenshots as historical; don't treat them as the current interface. If a preview is unavailable, continue source-supported cleanup and state the visual verification limit.

Identify what the user came to do on each screen, what they need to know now, and the next useful action. Give a short scope summary, then proceed without another routine approval step.

## Make these changes

- **Put the useful part first.** Bring the main result, working area, or task and its next action into the first viewport where practical. Give the primary action clear emphasis. Keep stop, cancel, and recovery controls easy to reach.
- **Write for a person.** Replace internal vocabulary, codes, label chains, vague headings, and repeated status badges with familiar wording. A short sentence can explain a state better than several tags. Use specific action names such as “Choose a game” or “Save changes.” Preserve useful field labels, units, dates, and names; clarity matters more than the smallest word count.
- **Remove repetition.** Cut duplicate titles, introductory filler, obvious instructions, repeated caveats, and decorative category labels. Explain something once, near where it matters. Keep useful domain content, teaching, narrative, and explanations of consequences.
- **Reduce unnecessary scrolling.** Trim oversized headers, excessive card padding, empty space, repeated summaries, and stacks of tiny panels. Group related information; use compact rows or tables for comparison. Keep controls near their result. Preserve reading order on narrow screens and the playable area in games.
- **Reveal detail when needed.** Put advanced setup, full history, diagnostics, identifiers, and lengthy calculation explanations behind clearly named secondary controls. Keep current blockers, important uncertainty, material assumptions, freshness, and consequences visible beside the relevant action or result. Do not collapse everything, add an extra click to every common task, or hide essentials in hover-only tooltips.
- **Make feedback useful.** Loading, empty, failed, unavailable, and successful states should say what happened and what the user can do. Explain disabled actions in context. Preserve distinctions such as unavailable versus zero, requested versus applied, saved versus live, and demonstration versus actual execution.

Retain the existing visual direction and components where they work. Read the shared `ui-templates` requirements if available, or the repository's local copy. When available, start from the [Starter 02 working examples](../ui-templates/index.html) and [matched comparison](../ui-templates/review/starter-02/index.html). Check the app's adoption version: a Starter 01 local copy does not already include these improvements. Adapt the layout to the task; a decorative template must not dictate the amount of chrome.

Do not achieve compactness through tiny type, cramped controls, clipped text, unexplained icons, missing accessible labels, or color alone. Avoid replacing scroll with needless tabs, dialogs, nested scrolling, or fragmented navigation.

## Keep the scope clear

Change copy, presentation, spacing, hierarchy, and local information grouping. Keep calculations, source meaning, eligibility, permissions, gameplay rules, teaching requirements, persistence, and data contracts unchanged. Translate internal values for display rather than renaming stored values unnecessarily.

This pass does not authorize new features, major navigation or workflow redesign, broad refactoring, dependency upgrades, live collection, owner-data access, migrations, or replacement of installed/frozen builds. Carry forward existing authorization; do not commit, push, publish, or release without it. Continue independent cleanup when a larger issue needs a separate decision.

Update existing design notes briefly where needed. Do not create a new documentation system or an exhaustive change ledger.

## Verify the improvement

Compare before and after on the same representative states, data, and viewport. Check the main task and relevant empty, error, disabled, and populated states. For web apps, inspect supported desktop and narrow layouts; for native games, inspect their actual supported window sizes. Check keyboard focus, readable text at increased scale, disclosures, primary actions, and reachable stop/recovery controls.

Show whether the result or action is easier to find and requires less unnecessary reading or scrolling without adding task steps. Use a few matched screenshots and measured observations where possible. Do not invent percentages or use word-count checks as proof of usability.

Run the appropriate existing build/syntax checks and focused tests for affected behavior, plus the relevant visual checks. Repair regressions caused by this pass. Report unrun checks and existing failures accurately. Technical verification is separate from owner acceptance and release qualification.

## Return a short handoff

1. **Changed:** the most useful improvements, with two or three concrete before/after examples and links to reviewable screens or files.
2. **Checked:** what was actually verified and any material limits.
3. **Other suggestions:** up to five prioritized issues outside this cleanup. For each, name the screen or source, the observed problem and user impact, whether it is confirmed or needs verification, why it is outside scope, and one bounded next action. Include real workflow, functionality, consistency, or accessibility concerns when found; do not invent a backlog to fill the list.

Keep the final response concise. Link longer evidence rather than reproducing it. Stop after the agreed presentation cleanup and relevant checks; leave separate suggestions unimplemented.
