Clean up the specified Next Steps document in Desktop

Keep this pass scoped to that document and its associated repository documentation.

The intended structure is:
- **Repository docs explain what exists:** completed work, decisions, operating instructions, limitations, and verification evidence.
- **Next Steps explains what remains:** every slice needed to reach the defined completion goal and the engineer type responsible for executing it.

Read the project’s repository instructions, current requirements, active plan, implementation status, and relevant evidence before editing. Establish the completion goal from those sources and preserve the agreed scope.

**1. Move completed work into repository docs**

For each completed slice, move its useful information into the appropriate existing repository documentation. Create a document only when no suitable destination exists.

Preserve relevant decisions, usage instructions, and limitations. Once that information is properly documented, remove the completed slice from Next Steps.

Resolve duplicated, stale, and superseded material.

If implementation is finished but required verification remains, document the completed implementation in the repo and keep only the outstanding verification work in Next Steps.

**2. Rewrite Next Steps as the complete remaining execution plan**

Include:
- The defined completion goal.
- A brief, evidence-backed current status.
- Every remaining slice required to reach that goal, in dependency order.
- The first executable slice and any actual blocker.

For each remaining slice, specify:
- **Slice ID and name**
- **Outcome:** the concrete result it delivers.
- **Engineer type:** the specialty responsible for execution, such as frontend, backend, native macOS, integration, QA, security, or release engineering.
- **Scope:** the work required.
- **Dependencies or blockers**
- **Completion checks:** observable conditions that establish the slice is finished.
- **Deliverables:** code, documentation, or evidence required at closeout.

Preserve existing slice IDs where practical. Include all required implementation, integration, verification, and delivery work through the defined goal. Put optional future ideas in the repository backlog. Assign owner feedback and acceptance actions to the owner.

**3. Handle a project with no remaining engineering work**

When all required engineering work is complete, reduce Next Steps to a short status such as:

“All implementation and required engineering verification are complete against the defined requirements. Awaiting your feedback.”

Link to the relevant requirements, verification, and review instructions. If a specific owner acceptance or release decision remains, state that action precisely.

Use completion language supported by the evidence. Record unresolved discrepancies explicitly.

**4. Finish the cleanup**

Check document links, consistency, and any existing documentation validation. Keep this pass focused on documentation.

Report:
- Which documents changed.
- Where completed material now lives.
- Remaining slices and their assigned engineer types.
- Whether the project is awaiting only owner feedback or decisions.
- Any unresolved discrepancy.

The cleaned Next Steps document should answer: “What remains to reach the agreed goal, who executes it, and how do we know it is finished?”