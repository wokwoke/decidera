# Layers

## Purpose

This document defines the architectural layers of Decidera.

Layers establish clear boundaries between responsibilities, allowing the system to remain modular, maintainable, and implementation-independent.

Each layer has a distinct purpose and communicates with adjacent layers through well-defined responsibilities.

---

## Background

The Domain Model defines the engineering concepts.

The System Overview defines the major architectural components.

The Layered Architecture defines how those components are organized into coherent responsibilities.

---

## Layered Architecture

Decidera is organized into five logical layers.

Presentation

↓

Application

↓

Domain

↓

Infrastructure

↓

External Providers

Each layer depends only on the layer directly below it.

---

## Presentation Layer

The Presentation Layer provides interfaces through which users interact with Decidera.

Examples include:

- Command Line Interface (CLI)
- Web Interface
- API
- Automation workflows

Responsibilities:

- Receive user input
- Display results
- Trigger application workflows

The Presentation Layer contains no business rules.

---

## Application Layer

The Application Layer coordinates engineering workflows.

Responsibilities include:

- Executing use cases
- Orchestrating processes
- Managing workflow execution
- Coordinating repositories
- Invoking providers

This layer does not contain engineering knowledge itself.

---

## Domain Layer

The Domain Layer is the core of Decidera.

It contains the engineering concepts defined by the Domain Model.

Examples include:

- Workspace
- Forum
- Finding
- Decision
- Artifact
- Atlas
- Registry

Business rules belong exclusively in this layer.

---

## Infrastructure Layer

The Infrastructure Layer provides technical capabilities required by the system.

Examples include:

- Repository access
- File management
- Configuration
- Persistence
- Logging

Infrastructure supports the Domain but does not define it.

---

## External Provider Layer

External Providers supply capabilities beyond the local system.

Examples include:

- AI services
- Version control platforms
- Cloud storage
- External APIs

Providers remain replaceable through abstraction.

---

## Dependency Rules

The architecture follows these dependency rules.

- Presentation depends on Application.
- Application depends on Domain.
- Infrastructure supports Domain and Application.
- Providers are accessed through abstractions.
- Domain never depends on external implementations.

These rules preserve long-term maintainability.

---

## Design Implications

The layered architecture enables:

- Independent evolution
- Easier testing
- Provider replacement
- Stable domain logic
- Clear responsibility boundaries

---

## Non-Goals

This document does not define:

- Specific frameworks
- Programming languages
- API specifications
- Database technologies

---

## Related Documents

- System Overview
- Components
- Data Flow
- Runtime
- Extensibility

---

## Summary

The Layered Architecture organizes Decidera into clear responsibility boundaries.

By separating presentation, application, domain, infrastructure, and external providers, the architecture remains modular, traceable, and adaptable while protecting the engineering knowledge contained within the Domain Layer.
