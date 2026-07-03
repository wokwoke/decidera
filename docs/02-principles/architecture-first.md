# Architecture First

> Status: Draft
>
> Version: 0.1

---

# Purpose

This document defines the Architecture First principle of Decidera.

Architecture First establishes that architectural understanding and system design must precede implementation.

The objective is to ensure that implementation reflects intentional design rather than becoming the primary design activity itself.

---

# Background

Many software projects begin by writing code immediately.

As implementation progresses, architecture gradually emerges through accumulated decisions, resulting in inconsistent structures, undocumented assumptions, and increasing technical debt.

Decidera adopts the opposite approach.

Architecture should be designed before implementation begins.

Implementation exists to realize the architecture, not to discover it.

---

# Principle

Architecture defines the structure, responsibilities, boundaries, and relationships of a system.

Before implementation begins, the following questions should be understood:

- What problem is being solved?
- What are the system boundaries?
- Which components are required?
- How do the components communicate?
- What responsibilities belong to each component?
- Which design decisions have already been made?

Only after these questions have been answered should implementation proceed.

---

# Rationale

An architecture-first approach provides several benefits:

- Clear system boundaries.
- Reduced implementation uncertainty.
- Better communication among contributors.
- Lower maintenance costs.
- Improved long-term consistency.
- Easier onboarding for future contributors.

Well-defined architecture also reduces unnecessary redesign during implementation.

---

# Design Implications

Applying this principle means that Decidera encourages creators to produce architectural artifacts before source code.

Examples include:

- Vision documents.
- Domain models.
- System overviews.
- Component diagrams.
- Decision records.
- Design specifications.

These artifacts provide a stable foundation for implementation.

---

# Examples

Example workflow:

Discussion

↓

Findings

↓

Architecture

↓

Design Review

↓

Design Freeze

↓

Implementation

Architecture evolves through discussion and review before any significant implementation begins.

---

# Non-Goals

Architecture First does not require every detail to be finalized before implementation.

Small implementation discoveries are expected.

The principle simply requires that the overall structure and major design decisions are intentionally established before coding begins.

---

# Related Documents

discussion-first.md

design-freeze.md

05-architecture/

06-decision-model/

---

# Summary

Architecture First is one of the foundational principles of Decidera.

By placing architecture before implementation, the framework promotes deliberate engineering decisions, improves long-term maintainability, and reduces unnecessary complexity throughout the software development lifecycle.