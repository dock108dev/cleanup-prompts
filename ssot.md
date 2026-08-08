SSOT Enforcement Implementation Prompt

You are the engineer assigned to identify and enforce the repository's current Single Source of Truth (SSOT) behavior.

Work from the current source code. Identify authoritative code paths, remove conflicting or unused paths, update tests and docs, and validate that the project still works.

## Objective

Make the codebase reflect how the system works today.

The finished repo should have:
- one authoritative implementation per domain
- duplicate policy paths routed through the authoritative implementation
- unused flags, modes, adapters, and fallbacks removed
- tests that protect the authoritative paths
- docs that describe supported behavior
- passing validation

## Operating Principles

1. SSOT wins
   - If two paths implement the same domain differently, keep the current authoritative path and remove or route through it.

2. Current production behavior sets the contract
   - Preserve callers, flags, configs, and modes that are actively required by current production behavior.
   - Remove compatibility layers that serve unsupported behavior.

3. Disabled and unreachable code leaves the tree
   - Feature-flagged-off, permanently env-gated, unused fallback, and unreachable paths count as dead unless current production usage is provable.

4. Unknown usage gets investigated
   - Search call sites, routes, schedulers, scripts, tests, config, and runtime entry points.
   - Remove low-risk paths when production usage cannot be proven.
   - For risky removals, isolate the ambiguity behind an explicit failure or documented follow-up.

## Step 1: Identify Current SSOTs

Inspect the repository and list the authoritative sources for each relevant domain.

Use this format in your working notes and final response:

Domain:
SSOT module/file:
Why this is authoritative:
Known callers:

Examples of domains:
- routing
- configuration
- data ingestion
- scheduling
- persistence
- authentication
- authorization
- feature policy
- client API access
- validation
- rendering/state management

## Step 2: Inventory Conflicting or Unused Constructs

Search for:
- duplicate execution paths
- alternate managers, services, adapters, or wrappers
- flags that are always false or unsupported by current behavior
- environment variable aliases
- compatibility shims
- fallback logic that masks unsupported behavior
- tests that validate unused behavior
- docs that describe unsupported modes
- scripts that call inactive entry points

For each candidate, determine:
- file
- symbol, conditional path, mode, or config
- purpose if clear
- how it relates to the current authoritative path
- whether current production usage is provable
- action: delete, route through SSOT, keep with rationale, or defer with follow-up

## Step 3: Implement SSOT-Only Paths

Make the repo enforce the current authoritative behavior:
- delete unused conditional paths, flags, configs, adapters, and tests
- route duplicate callers through the SSOT implementation
- remove unsupported environment variables from examples and docs
- replace ambiguous silent fallback with explicit failure
- simplify callers after removing compatibility layers
- keep behavior stable for current supported paths

When replacing ambiguous fallback behavior, use a clear project-appropriate error such as:

```python
raise RuntimeError("Unsupported path removed; use the current implementation.")
```

Use the language and error-handling conventions of the repo.

## Step 4: Tests and Assertions

Update the test suite so it reflects current supported behavior:
- remove tests that validate deleted behavior
- update tests to call the SSOT path directly or through supported entry points
- add focused tests that prove authoritative modules are used
- add a guard test or static assertion where practical to prevent unsupported symbols or config names from returning
- update fixtures and examples to use supported modes

## Step 5: Documentation Cleanup

Update documentation after implementation:
- remove references to deleted flags, modes, scripts, and behaviors
- update setup and configuration docs
- update architecture docs to identify authoritative modules
- document unsupported behavior where that helps current users avoid mistakes
- keep compatibility notes only when they help current engineering work

## Validation Requirements

Before finishing:
- run formatter, linter, type checks, tests, and smoke checks relevant to the repo
- run focused searches to ensure deleted symbols, flags, and modes are no longer referenced
- verify main supported flows still work
- explain any checks that cannot be run locally

## Final Response

Include:
- SSOT summary by domain
- paths removed
- duplicate paths routed through SSOT
- tests added, updated, or removed
- documentation updates
- validation commands and results
- retained compatibility paths with rationale
- follow-up items for risky removals that need a separate pass

## Definition of Done

- Current supported behavior is enforced by construction.
- Conflicting logic has been removed or routed through the authoritative implementation.
- Unsupported behavior no longer appears as a working path.
- Tests protect the current behavior.
- Docs match the current repo.
- Validation passes or remaining failures are clearly explained.
