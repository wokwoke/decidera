# Finding

> Status: Draft
>
> Version: 0.1

---

# Purpose

This document defines the Finding domain entity.

A Finding represents validated knowledge discovered during engineering activities.

Findings capture observations, insights, constraints, assumptions, risks, or conclusions that may influence future decisions.

---

# Background

Engineering discussions often generate large amounts of information.

Not every statement deserves to become a decision.

Before making commitments, important knowledge should first be identified, documented, and validated.

The Finding provides this intermediate step.

---

# Definition

A Finding is a structured piece of engineering knowledge.

It summarizes information considered valuable enough to preserve and potentially use when making future decisions.

A Finding may originate from discussions, experiments, reviews, research, testing, or operational experience.

---

# Responsibilities

A Finding is responsible for:

- Preserving engineering knowledge.
- Recording important observations.
- Capturing assumptions.
- Identifying risks.
- Documenting constraints.
- Supporting future decisions.

A Finding does not approve or enforce any action.

---

# Relationships

A Finding belongs to one Workspace.

A Finding may originate from:

- Forums
- Discussions
- Reviews
- Experiments
- External references

A Finding may support one or more Decisions.

Multiple Findings may contribute to the same Decision.

---

# Lifecycle

Typical Finding lifecycle:

Observation

↓

Discussion

↓

Validation

↓

Finding

↓

Referenced by Decisions

↓

Historical Knowledge

Findings remain part of the project's permanent engineering knowledge.

---

# Design Implications

Separating Findings from Decisions improves engineering quality.

Knowledge can be accumulated before commitments are made.

This encourages evidence-based decision making rather than opinion-based development.

---

# Non-Goals

A Finding is not:

- A decision.
- A task.
- A requirement.
- An implementation.

A Finding represents knowledge, not commitment.

---

# Related Documents

- forum.md
- decision.md
- atlas.md
- ../06-decision-model/findings.md

---

# Summary

The Finding captures validated engineering knowledge.

It provides the evidence and understanding required to make informed decisions while preserving valuable project insights for future evolution.
