# Atlas

> Status: Draft
>
> Version: 0.1

---

# Purpose

This document defines the Atlas domain entity.

An Atlas preserves the evolution of engineering knowledge throughout the lifetime of a Workspace.

Rather than recording every implementation detail, the Atlas captures meaningful milestones, design decisions, discoveries, and project evolution.

---

# Background

Engineering is a continuous learning process.

Projects evolve through discussions, findings, decisions, implementation, validation, and reflection.

While version control systems preserve file history, they do not explain why a project evolved.

The Atlas provides this missing context.

---

# Definition

An Atlas is the engineering memory of a Workspace.

It records significant events that influence the direction of a project.

Each Atlas entry summarizes an important step in the project's evolution.

---

# Responsibilities

An Atlas is responsible for:

- Preserving engineering history.
- Recording important milestones.
- Summarizing design evolution.
- Maintaining project context.
- Supporting future reviews.
- Helping new contributors understand the project.

The Atlas is not intended to replace detailed documentation.

---

# Relationships

An Atlas belongs to one Workspace.

Atlas entries may reference:

- Forums
- Findings
- Decisions
- Artifacts
- ADRs
- Releases

The Atlas connects these entities into a coherent project narrative.

---

# Lifecycle

A Workspace begins with an empty Atlas.

As engineering progresses, significant events produce Atlas entries.

The Atlas grows continuously throughout the project lifecycle and remains part of the project's permanent knowledge.

---

# Design Implications

The Atlas emphasizes knowledge rather than implementation.

Instead of documenting every change, it highlights the events that shaped the project.

This enables future contributors to understand how the project evolved without reading every discussion or commit.

---

# Non-Goals

An Atlas is not:

- A Git history.
- A changelog.
- A task list.
- A project timeline.

Although related to these concepts, the Atlas focuses on engineering knowledge rather than operational records.

---

# Related Documents

- workspace.md
- forum.md
- finding.md
- decision.md
- artifact.md

---

# Summary

The Atlas is the long-term engineering memory of Decidera.

It preserves the story of how a project evolves, providing historical context that complements documentation, source code, and version control.
