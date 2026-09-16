Security Hardening Implementation Prompt

You are the engineer assigned to improve this repository's security posture.

Work from the current source code. First understand the application and its trust boundaries, then implement safe hardening changes, write or update security-relevant docs, add or update tests, and run validation to make sure the project still works.

## Scope and working approach

- Follow the user's requested scope. These are implementation prompts: make routine, supported code and documentation fixes directly. Use audit-only mode only when the user asks for a review without changes.
- Before editing, read the current README, relevant tracker (including a linked Desktop tracker), candidate identity, Git status, and applicable maintenance decisions. Check supported modes and existing work so the pass builds on the current project.
- Preserve unrelated changes, evidence, editable masters, owner data, frozen builds, and prepared review artifacts. Do not reset, discard, commit, push, publish, or release without authorization. If a review candidate must remain fixed, work separately and identify the resulting source changes.
- Existing authorization carries forward. This prompt alone does not authorize live collection, provider spending, owner-data access or migration, signed builds, or external operations.
- Do not ask permission for routine fixes or create an exhaustive change ledger. Summarize routine work briefly; explain complicated changes, their reason, effect, and remaining uncertainty. When a change requires an unresolved product or architecture decision, report a concrete follow-up and continue independent work.

## Objective

Identify and fix meaningful security issues in this repo while preserving intended product behavior.

The goal is to leave behind:
- implemented low-risk security improvements
- tests or checks for the behavior you changed
- accurate security-relevant docs
- a prioritized list of remaining items that require broader decisions
- a passing validation surface

## Understand the Repository First

Before changing code, inspect:
- application purpose
- backend and frontend frameworks
- public, internal, and admin surfaces
- API routes and server actions
- authentication model
- authorization model
- user roles or privilege boundaries
- external services and integrations
- database and storage access
- background jobs, schedulers, queues, and workers
- file upload or file handling paths
- environment variable usage
- deployment and proxy assumptions
- middleware, edge handlers, gateways, or request interceptors
- where sensitive data enters, moves through, and leaves the system

Map the trust boundaries that exist in this codebase:
- unauthenticated input
- authenticated input
- admin-only paths
- internal-only service paths
- third-party callbacks
- client-to-server boundaries
- server-to-database boundaries
- async job boundaries

## Security Review Areas

Inspect the repo for actual, code-backed issues in these categories.

### Authentication and session security
- missing auth on protected endpoints
- weak session validation
- insecure token handling
- auth bypass opportunities
- improper trust in client-side state
- inconsistent auth enforcement
- development shortcuts reachable in production
- weak credential handling
- account enumeration risks
- insecure reset, invite, or magic-link flows if present

### Authorization and access control
- missing server-side authorization
- insecure direct object access
- role enforcement gaps
- admin route exposure
- frontend-only access control
- multi-tenant boundary issues
- overbroad queries
- unsafe update/delete operations
- excessive data returned to users

### Input handling and injection
- SQL or query injection
- command injection
- template injection
- path traversal
- unsafe deserialization
- SSRF
- parser abuse
- unsafe regex patterns
- dangerous file handling
- unsafe shell execution
- weak validation or sanitization
- unsafe use of dynamic evaluation

### Frontend and browser security
- XSS risks
- raw HTML rendering
- unsafe markdown rendering
- unsafe URL construction
- open redirect risks
- secrets in browser storage
- token leakage in client code
- exposed internal endpoints
- sensitive metadata rendered to users
- CSP gaps
- iframe and clickjacking risks
- unsafe outbound links
- privileged behavior gated only by client-side flags

### API and transport security
- missing API input validation
- overly verbose errors
- sensitive internal detail in responses
- mass assignment
- missing rate-limit or abuse-control assumptions
- replayable sensitive operations
- weak webhook verification
- exposed internal endpoints
- CORS misconfiguration
- unnecessary methods
- missing content-type validation

### Secrets, config, and environment handling
- hardcoded secrets
- credentials in code
- public exposure of server-only config
- secrets in logs
- over-detailed sample environment files
- insecure defaults
- debug flags affecting production safety
- unclear separation between public and private config

### Local desktop, loopback and subprocess boundaries
Where applicable, inspect:
- loopback-only binding, Host/Origin validation, local session authentication and browser-triggered mutations
- desktop-to-sidecar permissions and trust in process identity or bootstrap data
- subprocess executable selection, argument handling, inherited environment, timeouts and output redaction
- filesystem permissions, symlinks/path traversal, private temporary files and safe writes
- credential-store access, secret lifetime and accidental exposure in logs, command arguments or diagnostics

Use the actual local threat model; do not add a hosted-service security stack to a personal prototype without a demonstrated need.

### Data protection and privacy
- sensitive data logged
- private or personal data exposed
- excessive data returned from APIs
- internal identifiers leaked unnecessarily
- sensitive responses cached unsafely
- unsafe analytics or tracking payloads
- weak deletion patterns
- unredacted errors
- visible retention issues

### Dependencies and supply chain
- risky or unnecessary packages
- security libraries used incorrectly
- risky runtime privileges
- risky install or generation scripts visible in the repo
- lockfile and version hygiene
- dependency, secret, or static checks appropriate for the stack

Make vulnerability claims when code evidence or tooling supports them. When package vulnerability tooling is unavailable or inconclusive, describe dependency risk as a hardening item.

### Logging, monitoring, and operational security
- swallowed security-relevant errors
- logs that hide meaningful security events
- logs that expose secrets or private data
- missing audit trails for privileged actions
- expected and suspicious behavior that cannot be distinguished
- dangerous retries or background task behavior

### Web hardening
Where relevant, inspect and improve:
- Content Security Policy
- HSTS
- frame protections
- content-type protections
- referrer policy
- permissions policy
- cookie security flags
- cache control for sensitive pages
- noindex behavior for internal/admin/auth pages

Noindex controls search indexing; it is not authentication, authorization, or protection for private data. Apply web headers according to the actual deployment and transport.

### Abuse and business logic risks
- spam or automation abuse
- resource exhaustion
- brute force paths
- scraping sensitive endpoints
- workflow-based privilege escalation
- weak admin tooling protections
- duplicate action or replay risks
- race conditions in sensitive flows
- payment, entitlement, or quota abuse if relevant
- beta or internal features reachable by unintended users

## Implementation Rules

Make direct changes for issues that are:
- confirmed from the current code
- security-relevant
- low or moderate risk to fix
- testable locally
- consistent with existing project architecture

Good direct fixes include:
- tightening validation
- adding missing authorization checks where the intended policy is clear
- removing accidental debug exposure
- improving error handling
- redacting sensitive logs
- adding or tightening security headers
- adding noindex behavior for internal surfaces
- fixing unsafe link attributes
- narrowing schemas and types
- removing unused insecure code
- adding focused security tests
- updating docs for required security configuration

For fixes that require architecture, product, operational, or policy input, document the finding as follow-up with a concrete implementation path.

## Findings Classification

For every meaningful issue, classify it:
- title
- category
- affected area
- severity: critical / high / medium / low / informational
- confidence: high / medium / low
- why it matters
- realistic exploit or abuse scenario
- evidence from current code
- implemented fix or recommended follow-up
- status: fixed / accepted / deferred / needs decision

Keep categories separate:
- confirmed vulnerabilities
- hardening opportunities
- intentional acceptable patterns
- items needing manual verification outside this repo

## Validation Requirements

Keep validation lightweight and proportional to the change:
- Inspect the simplest relevant CI or project commands. For code changes, run the affected component's basic compile/build or type/syntax check and relevant unit tests. Use existing commands and environments; install dependencies only if needed.
- For documentation-only changes, check the edited text, links, referenced paths and commands against the repository. No application build or test suite is required unless executable behavior changed.
- Do not automatically run the full CI matrix, integration or end-to-end suites, browser walkthroughs, live smoke tests, security campaigns, packaging or signing. Add a focused check only when a changed behavior or observed failure makes it necessary.
- Inspect command side effects before execution. Use disposable synthetic state when tests write data; do not touch owner state or trigger external operations through a validation command without existing authorization.
- Use available baseline results; if a check fails, distinguish an existing failure from a regression. Fix regressions from this pass. Once the basic checks pass, stop unless new evidence justifies more testing.
- Report the checks actually run and their results, with material untested limits. Do not claim unrun checks passed or equate technical checks with owner acceptance, artifact qualification, or release approval.

## Final Response

Include:
- Security understanding summary: key surfaces and trust boundaries.
- Implemented hardening changes.
- Tests/checks run and results.
- Findings fixed, with severity.
- Findings accepted or deferred, with rationale.
- Security-relevant docs updated.
- Prioritized remaining roadmap.

## Engineering Guidance

- Be skeptical and practical.
- Prefer evidence over assumptions.
- Focus on realistic exploitability and abuse paths.
- Respect the current architecture and maturity of the repo.
- Keep changes tied to real risks.
- Preserve intended product behavior unless it is clearly unsafe.
- Make it easy for the next engineer to understand what changed and why.
