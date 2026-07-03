# Core Components

> Status: Draft
>
> Version: 0.1

---

# Purpose

This document introduces the core components of Decidera and summarizes the primary responsibility of each component.

It provides a conceptual overview without describing implementation details.

---

# Background

Decidera is composed of multiple independent components.

Each component has a clearly defined responsibility and collaborates with other components through structured workflows.

This separation enables modularity, maintainability, and long-term evolution.

---

# Specification

The Decidera core consists of several primary components.

Each component performs a single major responsibility while contributing to the overall engineering workflow.

Together they transform discussions into executable project artifacts.

---

# Component Overview

## Workspace

The Workspace represents the project environment.

It organizes project files, documentation, discussions, generated artifacts, metadata, and project history.

---

## Forum

The Forum facilitates structured discussions.

It enables ideas, alternatives, and perspectives to be explored before engineering decisions are made.

---

## Atlas

Atlas captures and preserves project knowledge.

It records findings, observations, risks, opportunities, and other information discovered throughout discussions.

---

## Decision Model

The Decision Model evaluates findings and transforms them into documented engineering decisions.

It establishes the reasoning that guides future implementation.

---

## Registry

The Registry maintains structured relationships between project entities.

It enables traceability across discussions, findings, decisions, documents, and generated artifacts.

---

## Artifact Engine

The Artifact Engine converts approved decisions into project artifacts.

Artifacts may include:

- Documentation
- Source code
- Configuration files
- Shell scripts
- Git operations
- Diagrams

---

## Providers

Providers connect Decidera with external systems and capabilities.

Examples include:

- AI providers
- Git
- Shell
- Filesystem
- Plugins

Providers extend the framework without becoming part of its architectural core.

---

# Component Relationships

Each component contributes to a continuous engineering workflow.

Workspace

↓

Forum

↓

Atlas

↓

Decision Model

↓

Artifact Engine

↓

Registry

Providers support multiple stages of this workflow whenever external capabilities are required.

---

# Design Implications

Every component follows the Single Responsibility Principle.

Components communicate through clearly defined boundaries.

No component should assume the responsibilities of another.

This separation improves modularity, simplifies maintenance, and supports future extensibility.

---

# Examples

A creator starts a discussion inside the Forum.

Atlas records the findings.

The Decision Model evaluates the findings.

The Artifact Engine generates the required outputs.

The Registry preserves the relationships between all resulting artifacts.

The Workspace organizes everything within the project.

---

# Non-Goals

This document does not define internal architecture or implementation details.

Detailed specifications for each component are provided in later chapters.

---

# Related Documents

ecosystem.md

lifecycle.md

04-domain-model/

05-architecture/

---

# Summary

The Decidera core is built from independent components with clearly defined responsibilities.

Together they provide a structured engineering workflow while remaining modular, traceable, and evolvable.