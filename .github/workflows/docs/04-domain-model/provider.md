# Provider

> Status: Draft
>
> Version: 0.1

---

# Purpose

This document defines the Provider domain entity.

A Provider represents an external capability or service that enables Decidera to perform engineering activities.

Providers supply functionality but do not define engineering processes or project knowledge.

---

# Background

Modern engineering projects rely on many external systems.

Examples include Large Language Models, version control systems, file systems, scripting environments, communication platforms, and third-party services.

Decidera treats all of these as Providers.

This abstraction keeps the engineering process independent from specific technologies.

---

# Definition

A Provider is an external capability integrated into a Workspace.

Providers perform specialized tasks on behalf of the engineering process.

A Provider may be local or remote.

A Provider may be replaced without changing the engineering model.

---

# Responsibilities

A Provider is responsible for:

- Executing specialized capabilities.
- Interacting with external systems.
- Producing engineering outputs.
- Supporting automation.
- Extending Workspace functionality.

Providers should remain independent from project knowledge.

---

# Relationships

A Provider belongs to one Workspace.

Providers may interact with:

- Artifacts
- Registries
- Forums
- Atlas
- External Services

Examples include:

- LLM Providers
- Git Providers
- File System Providers
- Shell Providers
- Plugin Providers

---

# Lifecycle

Typical Provider lifecycle:

Registration

↓

Configuration

↓

Validation

↓

Usage

↓

Maintenance

↓

Replacement or Removal

Providers may evolve independently of project artifacts.

---

# Design Implications

By separating Providers from the engineering model, Decidera remains portable across different execution environments.

Changing a Provider should not require redesigning project knowledge or workflows.

---

# Non-Goals

A Provider is not:

- A Workspace.
- A Decision.
- A Registry.
- A Workflow.

Providers supply capabilities rather than engineering knowledge.

---

# Related Documents

- workspace.md
- artifact.md
- registry.md
- ../11-providers/README.md

---

# Summary

A Provider supplies external capabilities to Decidera.

It enables engineering activities while remaining independent from the project's knowledge, decisions, and architecture.
