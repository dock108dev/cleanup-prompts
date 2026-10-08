Review and improve this product's interface to a professional standard: visually polished, easy to learn, pleasant to use and coherent enough to present to a prospective customer. Its features may serve the owner's specific needs; its interface must work for someone who has never met the owner, read the repository or used the product. Treat future commercial quality as the design standard, without adding sales, billing or release work.

Use three perspectives together: a graphic designer judging composition and visual character, an interface designer judging controls and behavior, and a new user trying to complete a task. Implement a coherent improvement across appearance, interaction and content. Less reading and scrolling matter, but compactness alone is not success.

## Review the current product

Read repository instructions, the active handoff/tracker, local design guidance and working-tree status. Identify the current app and distinguish source, installed builds and historical screenshots. Preserve existing work, private state and frozen builds.

Choose two or three representative screens or states covering the main journey. Inspect their rendered interface and source, including generated messages. Use an isolated synthetic preview where supported; do not launch live acquisition or access owner data merely to review layout. If rendering is unavailable, make source-supported improvements and report visual verification as incomplete.

For each screen, identify the user's task and the main result or control. Find the largest obstacles to clarity and finish. Establish a brief visual direction appropriate to the product and current requirements: type hierarchy, layout, spacing, surfaces, color and control styles. Give a short scope update and proceed with routine decisions.

## Make it look deliberately designed

- Build a clear composition: a dominant working area, recognizable grouping and a natural reading order. Balance density with breathing room. Space should separate meaningful groups, support scanning or showcase useful imagery; arbitrary gaps and decorative filler should disappear.
- Use a restrained, consistent type hierarchy with readable sizes and line lengths. Align labels, values, icons and controls. Check optical balance as well as shared CSS values. Dense comparison data, conversational text and image collections need different layouts.
- Make color, borders, radii, shadows and iconography feel like one product. Fix mixed component styles and accidental visual inconsistencies. Use emphasis selectively; every panel, button and badge cannot compete for attention. Glass, gradients and animation must serve the chosen direction.
- Give controls a consistent family and clear primary, secondary, selected, disabled, hover and focus states. Use consistent icons with accessible names; reserve destructive emphasis for consequential actions.
- Review the whole screen at actual use sizes. It should feel balanced with real content, long names, missing images and partial data. Responsive layouts must be composed intentionally rather than simply stacking every desktop panel. Do not force unrelated products into the same dashboard template.

## Make interaction understandable

A new user should be able to identify what the product does, where to begin, what a control affects and whether an action succeeded. Use familiar interaction patterns, descriptive labels and a clear path through setup and normal use. Technical expertise is not a prerequisite.

Keep controls with their targets. Make selection and editing evident. Explain a disabled action where the user encounters it. Preserve drafts, selection, focus and useful scroll position during updates. Give immediate, proportionate feedback: routine success should not leave a permanent paragraph; consequential changes and failures need durable, actionable information. Use confirmations for meaningful consequences, not routine harmless actions.

## Rebuild the hierarchy

- Start with the working content: prices, collection, conversation, scene or remote controls. Use a compact heading and task controls. Remove promotional headlines, category eyebrows, introductory paragraphs and repeated titles when the screen already explains itself.
- Give the main action clear emphasis. Keep common controls beside the item they affect. Consolidate duplicate controls and remove unnecessary selection steps when existing behavior supports direct action. Secondary actions should look secondary. Keep Stop, Take control and essential recovery directly reachable.
- Make every visible sentence earn its place. Keep text that identifies content, changes a decision, explains a current blocker or states a consequence. Delete explanations of obvious controls. Put occasional help beside the relevant field or in one clearly named help surface.
- Show the current state, not a catalogue of possible states. Avoid stacks such as “No plan,” “No pending change,” “No attempt” and “Not verified.” Use a coherent idle state; show progress, pending changes and results when relevant. Never suppress actionable errors or material uncertainty.
- Review dynamic copy too: model replies, status builders, validation and success messages. Present the useful answer, current activity or required action first. Put extended rationale and diagnostics in optional detail. Preserve complete records where required; do not blindly truncate meaningful content.

## Remove unnecessary structure and space

- Remove a card, border, heading or divider when ordinary alignment and spacing group the content adequately. Prefer compact rows for repeated records and aligned columns for comparisons. Keep cards when items benefit from distinct identity or independent controls.
- Review the combined height of navigation, heading, description, notices, filters and summaries above the work. Reduce that stack before compressing the work itself. Related facts belong together; each fact does not need its own panel.
- Remove empty placeholders and reserved detail columns that consume useful room without helping orientation. Open existing details when selected without losing the user's context, focus or scroll position.
- Inspect computed spacing and responsive behavior, including accumulated margins, fixed heights, minimum heights and grid stretching. Use a small consistent spacing scale. Avoid equal-height cards that create blank bottoms, oversized empty states and full-width boxes for tiny messages. Preserve space needed for a scene, images, alignment and comfortable reading.
- Keep advanced setup, history and diagnostics secondary. Show setup when needed and reduce its prominence after readiness. Do not put every section in an accordion or move common tasks behind new tabs, dialogs or nested scrolling.

## Preserve meaning and usability

Keep useful names, labels, units, dates and distinctions such as unknown versus zero, saved versus live, requested versus applied and observed versus inferred. Show freshness, material assumptions, costs and consequences where they affect a decision. Explain each shared limitation once; repeat only when needed for an independently viewed item or action.

Follow current local requirements. Preserve useful visual identity while replacing components and patterns that undermine clarity or finish. If available, consult shared `ui-templates/DESIGN_REQUIREMENTS.md` and relevant examples; copy useful patterns, not gallery navigation or sample prose. Templates are references, not required runtime dependencies or proof of app quality.

Do not reduce clutter through tiny type, cramped targets, clipped text, unexplained icons, color alone or hover-only essentials. Preserve accessible names, keyboard order, visible focus and readable contrast.

Visual styling, layout, copy, local regrouping and simplifying access to existing controls are in scope. Make routine design decisions autonomously. Preserve calculations, eligibility, permissions, persistence, source identity, gameplay and required approvals. New capabilities, changed domain behavior, migrations, broad refactoring and publication require separate scope. Carry forward existing authorization; do not replace installed/frozen builds without it.

## Check the actual improvement

Compare matched before/after states, data and supported window sizes. Include a populated state, first use and relevant failure or unavailable states. Check long content, narrow layouts where supported, increased text scale, keyboard use, details and recovery.

Review the result through all three perspectives. Does the composition look finished and consistent? Are controls predictable and feedback clear? Can a new user complete the main task without a narrated walkthrough? Record a few concrete before/after observations about useful content, routine steps, reading and spacing. Fix remaining awkward gaps, competing emphasis and inconsistent controls. Measurements support judgment; word counts alone do not prove usability.

Run existing checks appropriate to the affected behavior. Do not expand a presentation pass into a release campaign. Update existing design notes briefly if needed.

Return a short handoff: two or three concrete improvements to appearance and use, matched screenshots or review links, checks and limits, and at most three consequential issues outside scope if found. State source-only conclusions as provisional. Do not call the UI polished without inspecting it rendered. Engineering checks do not establish new-user testing, owner acceptance or commercial readiness.
