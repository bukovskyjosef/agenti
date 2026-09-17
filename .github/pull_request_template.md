## Work contract

Closes #

**Role:** Developer / corrective Developer / contract owner / Integrator / other authorized execution role

**Concurrency class:** PARALLEL_SAFE / COORDINATION_REQUIRED / EXCLUSIVE

> Durable handoff rule: this PR and its GitHub review/test threads are the agent-to-agent communication channel. Do not rely on the human user to relay implementation, review or test reports. See `docs/handoff-protocol.md`.

## What changed

Describe the implemented result briefly. Do not repeat the full Issue specification.

## Scope implemented

- 

## Intentionally out of scope

- 

## Shared-contract impact

- Database/schema/migrations: none / describe
- API/domain contract: none / describe
- Governance/runtime/dependencies: none / describe
- Other shared surfaces: none / describe

If a shared contract changed, link the Issue text/decision that authorized it.

## Acceptance criteria evidence

For each relevant acceptance criterion, provide concrete evidence.

## Validation

- [ ] Required task-specific verification completed
- [ ] Governance consistency check completed when governance surfaces changed
- [ ] Self-review of diff completed
- [ ] No secrets/private data added to code, logs or artifacts

Commands/evidence:

```text
...
```

## Documentation impact

- [ ] Canonical documentation was updated where durable project truth changed.
- [ ] No documentation change is required.

Explain if needed.

## Decision gates

- [ ] This PR introduces no unapproved product/governance/shared-contract decision.

If a decision was discovered or resolved, link the durable decision artifact.

## Risks / follow-up

- 

## Independent Reviewer handoff

Reviewer: before acting, read the linked Issue and relevant Issue comments/decisions, this PR body, actual diff/commits, existing reviews/unresolved threads, tester reports when present, and current checks. Do not rely only on an implementer or human chat summary.

Persist review on this PR using `## AGENT REPORT — REVIEWER` and exactly one outcome:

- `APPROVED`
- `CHANGES_REQUIRED`
- `DECISION_REQUIRED`

For every substantive finding record both:

- **severity:** `BLOCKER` / `MAJOR` / `MINOR` / `NIT`
- **disposition:** `DEFECT` / `DECISION_REQUIRED` / `RECOMMENDATION`

Severity describes impact; it does **not** authorize new implementation. See `docs/review-model.md`.

Reviewer checklist:

- [ ] Linked Issue was Ready and dependencies were satisfied.
- [ ] Acceptance criteria are implemented.
- [ ] Change stays within authorized scope.
- [ ] Shared contracts were not changed without authorization.
- [ ] Declared concurrency/coordination constraints were respected.
- [ ] Tests/checks are meaningful and match the contract.
- [ ] Each substantive finding has evidence, severity and disposition.
- [ ] `RECOMMENDATION` was not converted into mandatory implementation without authorization.
- [ ] `DECISION_REQUIRED` does not prescribe an unapproved solution.
- [ ] No unresolved `DEFECT` or required decision gate remains before APPROVED.

## Tester handoff

If a dedicated Tester/Verifier is required, persist the result on this PR or the contractually specified test artifact using:

```text
## AGENT REPORT — TESTER
Tested head: <SHA/version>
Result: PASS | FAIL | INCONCLUSIVE
```

Include environment/commands, scenarios/evidence and failures. A test result returned only in chat is not a durable handoff.

## Integrator handoff

Integrator must verify the exact head, required control gates, checks, unresolved threads and dependencies before merge/promotion. Persist integration evidence with `## AGENT REPORT — INTEGRATOR`; do not treat a chat approval as a merge gate.
