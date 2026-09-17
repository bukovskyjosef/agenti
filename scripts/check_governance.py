#!/usr/bin/env python3
"""Validate structural invariants of the Agenti reference governance model.

This checker intentionally validates only deterministic repository structure and
cross-file markers. It does not attempt to decide product semantics or replace
human/independent review.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "docs" / "README.md",
    ROOT / "docs" / "governance.md",
    ROOT / "docs" / "roles.md",
    ROOT / "docs" / "workflow.md",
    ROOT / "docs" / "issue-standard.md",
    ROOT / "docs" / "review-model.md",
    ROOT / "docs" / "handoff-protocol.md",
    ROOT / "docs" / "automation-model.md",
    ROOT / "docs" / "context-policy.md",
    ROOT / "docs" / "repository-structure.md",
    ROOT / "docs" / "adoption-guide.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "work-item.yml",
    ROOT / ".github" / "pull_request_template.md",
    ROOT / ".github" / "workflows" / "governance.yml",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def text(path: Path) -> str:
    if not path.is_file():
        fail(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(path: Path, *needles: str) -> str:
    content = text(path)
    missing = [needle for needle in needles if needle not in content]
    if missing:
        fail(
            f"{path.relative_to(ROOT)} missing required marker(s): "
            + ", ".join(missing)
        )
    return content


def main() -> int:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED_FILES if not p.is_file()]
    if missing:
        fail("Missing governance file(s): " + ", ".join(missing))

    docs_map = require(
        ROOT / "docs" / "README.md",
        "handoff-protocol.md",
        "automation-model.md",
        "issue-standard.md",
        "review-model.md",
    )
    if docs_map.count("handoff-protocol.md") < 2:
        fail("docs/README.md must both own and route to the handoff protocol")
    if docs_map.count("automation-model.md") < 2:
        fail("docs/README.md must both own and route to the automation model")

    require(
        ROOT / "docs" / "roles.md",
        "## Orchestrátor",
        "## Analytik",
        "## Asistentka",
        "## Vývojář",
        "## Tester",
        "## Reviewer",
        "## Integrátor",
    )

    issue_standard = require(
        ROOT / "docs" / "issue-standard.md",
        "PARALLEL_SAFE",
        "COORDINATION_REQUIRED",
        "EXCLUSIVE",
        "Shared surfaces / coordination rule",
        "Decision gates",
        "Changes Required",
        "Approved",
        "Done",
    )
    for state in (
        "Intake",
        "Analysis",
        "Blocked",
        "Ready",
        "In Progress",
        "In Review",
        "Changes Required",
        "Approved",
        "Done",
    ):
        if state not in issue_standard:
            fail(f"issue-standard.md missing lifecycle state: {state}")

    require(
        ROOT / "docs" / "review-model.md",
        "BLOCKER",
        "MAJOR",
        "MINOR",
        "NIT",
        "DEFECT",
        "DECISION_REQUIRED",
        "RECOMMENDATION",
        "Severity sama nikdy neuděluje",
    )

    require(
        ROOT / "docs" / "handoff-protocol.md",
        "NOT PERSISTED — HANDOFF INCOMPLETE",
        "AGENT REPORT — REVIEWER",
        "AGENT REPORT — TESTER",
        "AGENT REPORT — INTEGRATOR",
        "člověk nebyl message bus",
    )

    require(
        ROOT / "docs" / "automation-model.md",
        "Trigger není autorita",
        "Least privilege",
        "Idempotence",
        "Durable success i durable failure",
        "Provider adapters",
        "Human decision interrupt",
    )

    issue_template = require(
        ROOT / ".github" / "ISSUE_TEMPLATE" / "work-item.yml",
        "Concurrency class",
        "PARALLEL_SAFE",
        "COORDINATION_REQUIRED",
        "EXCLUSIVE",
        "Shared surfaces / coordination rule",
        "Decision gates",
        "Integrator",
    )
    if "Required control gates" not in issue_template:
        fail("work-item template must declare required control gates")

    require(
        ROOT / ".github" / "pull_request_template.md",
        "AGENT REPORT — REVIEWER",
        "BLOCKER",
        "MAJOR",
        "MINOR",
        "NIT",
        "DEFECT",
        "DECISION_REQUIRED",
        "RECOMMENDATION",
        "AGENT REPORT — TESTER",
        "AGENT REPORT — INTEGRATOR",
    )

    require(
        ROOT / "AGENTS.md",
        "docs/handoff-protocol.md",
        "docs/automation-model.md",
        "Severity nálezu sama není oprávnění",
    )

    workflow = require(
        ROOT / ".github" / "workflows" / "governance.yml",
        "python scripts/check_governance.py",
    )
    if "pull_request" not in workflow or "push" not in workflow:
        fail("governance workflow must run for pull requests and pushes")

    print(
        "Governance consistency OK: canonical-map=OK, lifecycle=OK, "
        "concurrency=OK, review-authority=OK, durable-handoff=OK, automation-model=OK"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Governance consistency FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
