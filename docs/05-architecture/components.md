# Components

## Purpose

This document defines the primary architectural components of Decidera.

Components represent the major building blocks of the system and describe how responsibilities are distributed throughout the architecture.

Each component should have a single, well-defined responsibility.

---

## Background

The Layered Architecture defines responsibility boundaries.

Components provide the concrete realization of those responsibilities within the system architecture.

Together they form the structural blueprint of Decidera.

---

## Architectural Components

The architecture is composed of several core components.

Each component collaborates with others while maintaining clear separation of concerns.

---

## Workspace Manager

The Workspace Manager provides access to the engineering workspace.

Responsibilities include:

- Opening workspaces
- Managing project context
- Resolving repository locations
- Providing workspace configuration

---

## Forum Manager

The Forum Manager organizes engineering discussions.

Responsibilities include:

- Managing discussion sessions
- Recording conversations
- Preparing discussions for knowledge extraction

---

## Finding Engine

The Finding Engine transforms discussions into validated Findings.

Responsibilities include:

- Collecting evidence
- Organizing engineering knowledge
- Producing traceable Findings

---

## Decision Engine

The Decision Engine converts Findings into engineering Decisions.

Responsibilities include:

- Evaluating supporting Findings
- Recording engineering commitments
- Maintaining decision traceability

---

## Artifact Generator

The Artifact Generator produces engineering artifacts from Decisions.

Artifacts may include:

- Documentation
- Specifications
- Templates
- Source code
- Configuration
- Reports

Generation should remain deterministic whenever possible.

---

## Atlas Manager

The Atlas Manager records engineering evolution.

Responsibilities include:

- Tracking generated artifacts
- Recording engineering history
- Maintaining project evolution

Atlas represents engineering knowledge rather than source control history.

---

## Registry Manager

The Registry Manager provides discovery services.

Responsibilities include:

- Registering resources
- Resolving identifiers
- Supporting lookup operations

The Registry references resources without storing their complete contents.

---

## Provider Gateway

The Provider Gateway abstracts external capabilities.

Responsibilities include:

- AI providers
- Repository providers
- Storage providers
- External services

Provider implementations remain interchangeable.

---

## Repository Manager

The Repository Manager coordinates interaction with the repository.

Responsibilities include:

- Reading documentation
- Writing generated artifacts
- Managing project structure
- Supporting repository-centric workflows

The repository remains the Single Source of Truth.

---

## Component Relationships

Components cooperate according to the engineering workflow.

Workspace

↓

Forum

↓

Finding Engine

↓

Decision Engine

↓

Artifact Generator

↓

Repository

↓

Atlas

Registry and Provider Gateway support the workflow without becoming part of the engineering knowledge flow itself.

---

## Design Implications

Component separation enables:

- Independent development
- Easier testing
- Replaceable implementations
- Clear ownership
- Predictable evolution

---

## Non-Goals

This document does not define:

- Internal APIs
- Runtime scheduling
- Process execution
- Provider implementations

---

## Related Documents

- System Overview
- Layers
- Data Flow
- Runtime
- Extensibility

---

## Summary

Architectural components divide Decidera into focused responsibilities.

Each component contributes to the Decision-to-Artifact workflow while preserving modularity, traceability, and repository-centric engineering.
