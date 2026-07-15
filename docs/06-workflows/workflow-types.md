# Workflow Types

## Purpose

This document classifies the engineering workflows supported by Decidera.

Workflow types provide a common taxonomy for engineering processes while allowing new workflows to be introduced without changing the overall architecture.

---

## Background

Engineering activities serve different purposes.

Some workflows analyze information, others generate artifacts, validate engineering outputs, or maintain project knowledge.

Classifying workflows improves discoverability, composition, and long-term maintainability.

---

## Workflow Categories

Decidera organizes workflows into several logical categories.

Each category represents a distinct engineering responsibility.

---

## Analysis Workflows

Analysis workflows examine engineering information.

Examples include:

- Discussion analysis
- Requirement analysis
- Specification review
- Knowledge extraction

Outputs typically become Findings or engineering insights.

---

## Decision Workflows

Decision workflows transform validated knowledge into engineering commitments.

Responsibilities include:

- Evaluating Findings
- Recording Decisions
- Preserving engineering rationale

Decision workflows establish the basis for future artifact generation.

---

## Generation Workflows

Generation workflows produce engineering artifacts.

Examples include:

- Documentation generation
- Specification generation
- Blueprint generation
- Source code generation
- Configuration generation

Generated artifacts should remain traceable to their originating Decisions.

---

## Validation Workflows

Validation workflows evaluate engineering quality.

Examples include:

- Consistency verification
- Traceability validation
- Documentation review
- Structural validation

Validation workflows improve engineering confidence before outputs become permanent.

---

## Registry Workflows

Registry workflows maintain discoverability across the project.

Responsibilities include:

- Registering resources
- Updating indexes
- Resolving identifiers
- Maintaining references

Registries improve navigation rather than storing engineering knowledge.

---

## Atlas Workflows

Atlas workflows preserve engineering evolution.

Responsibilities include:

- Recording milestones
- Capturing engineering progression
- Linking related activities
- Maintaining engineering history

Atlas complements repository history by preserving engineering context.

---

## Maintenance Workflows

Maintenance workflows keep the engineering environment healthy.

Examples include:

- Repository cleanup
- Documentation synchronization
- Reference updates
- Integrity verification

These workflows support long-term sustainability.

---

## Workflow Composition

Complex engineering activities may combine multiple workflow types.

For example:

Analysis

↓

Decision

↓

Generation

↓

Validation

↓

Atlas

Composition enables reusable engineering processes while preserving modularity.

---

## Design Principles

Workflow types should remain:

- Independent
- Reusable
- Discoverable
- Composable
- Traceable

New workflow types should extend the taxonomy rather than replace existing categories.

---

## Non-Goals

This document does not define:

- Individual workflow implementations
- Runtime scheduling
- Provider behavior
- User interfaces

---

## Related Documents

- Workflow Overview
- Workflow Lifecycle
- Workflow Coordination
- Workflow States
- Workflow Composition
- Workflow Recovery

---

## Summary

Workflow Types classify engineering processes according to their primary responsibilities.

This taxonomy provides a stable foundation for organizing current and future workflows while preserving consistency, modularity, and engineering traceability.
