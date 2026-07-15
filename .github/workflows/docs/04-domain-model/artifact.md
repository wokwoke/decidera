# Artifact

> Status: Draft
>
> Version: 0.1

---

# Purpose

This document defines the Artifact domain entity.

An Artifact represents any tangible output produced during the engineering process.

Artifacts transform engineering knowledge into reusable deliverables that can be reviewed, executed, maintained, or shared.

---

# Background

Engineering produces many kinds of outputs.

Some are documentation.

Others are source code, diagrams, configuration files, workflows, tests, or scripts.

Although these outputs differ in format, they all represent engineering work and should be managed consistently.

---

# Definition

An Artifact is a persistent engineering deliverable.

It is created as the result of one or more Decisions and contributes to the implementation or documentation of a project.

Artifacts may be human-readable, machine-readable, or executable.

---

# Responsibilities

An Artifact is responsible for:

- Materializing engineering decisions.
- Preserving implementation results.
- Supporting project evolution.
- Enabling review and validation.
- Providing reusable engineering assets.

Artifacts should remain traceable to the Decisions that produced them.

---

# Relationships

An Artifact belongs to one Workspace.

Artifacts may originate from:

- Decisions
- ADRs
- Design documents
- Generated outputs

Artifacts may include:

- Documentation
- Source code
- Markdown
- Configuration
- Diagrams
- Scripts
- Tests
- Workflows

Multiple Artifacts may originate from a single Decision.

---

# Lifecycle

Typical Artifact lifecycle:

Decision

↓

Creation

↓

Review

↓

Validation

↓

Publication

↓

Maintenance

↓

Retirement

Artifacts evolve throughout the lifetime of a project.

---

# Design Implications

Artifacts are implementation-independent.

Their value comes from preserving engineering knowledge in a reusable form rather than from any particular file format or technology.

Maintaining traceability between Artifacts and Decisions improves long-term maintainability.

---

# Non-Goals

An Artifact is not:

- A discussion.
- A finding.
- A decision.
- A project.

Artifacts represent outputs rather than engineering reasoning.

---

# Related Documents

- decision.md
- atlas.md
- registry.md
- ../10-artifact-engine/README.md

---

# Summary

The Artifact is the tangible outcome of engineering work.

It transforms approved decisions into persistent deliverables while preserving traceability throughout the engineering lifecycle.
