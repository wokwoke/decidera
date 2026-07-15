# Registry Types

## Purpose

This document defines the different types of Registry used within Decidera.

Registry Types provide organized discovery mechanisms for different categories of engineering resources while maintaining a consistent Registry Model.

---

## Background

Decidera contains multiple types of resources.

Workflows, capabilities, providers, modules, and templates have different responsibilities but share common discovery requirements.

Registry Types allow these resources to be organized without creating unnecessary coupling.

---

## Workflow Registry

The Workflow Registry contains references to available workflows.

Purpose:

- Discover executable workflows.
- Identify workflow definitions.
- Provide workflow metadata.

Examples:

- Discussion Analysis
- Finding Extraction
- Decision Formation
- Artifact Generation
- Atlas Recording

The registry references workflows but does not execute them.

---

## Capability Registry

The Capability Registry contains references to system capabilities.

Purpose:

- Discover available abilities.
- Describe capability metadata.
- Connect capabilities with workflows and providers.

Examples:

- Text Analysis
- Code Generation
- Document Processing

Capability Registry becomes the foundation for Chapter 08.

---

## Provider Registry

The Provider Registry contains references to external service providers.

Purpose:

- Identify available providers.
- Describe provider capabilities.
- Enable provider abstraction.

Examples:

- AI Provider
- Storage Provider
- Repository Provider

Providers remain replaceable implementations.

---

## Module Registry

The Module Registry contains references to Decidera modules.

Purpose:

- Discover system components.
- Describe module responsibilities.
- Support modular extension.

Examples:

- Registry Module
- Workflow Module
- Atlas Module

---

## Template Registry

The Template Registry contains references to reusable artifact templates.

Purpose:

- Discover generation patterns.
- Standardize artifact creation.
- Maintain template metadata.

Examples:

- Document Template
- Report Template
- Specification Template

---

## Resource Registry

A general Resource Registry may reference other resource categories.

Purpose:

- Provide broad discovery.
- Support relationships between registries.
- Enable ecosystem visibility.

---

## Registry Relationships

Registry Types are connected through references.

Example:

Workflow Registry

↓

Workflow Entry

↓

Capability Reference

↓

Provider Reference

↓

Template Reference

This creates a discoverable ecosystem.

---

## Registry Selection Principles

A new Registry Type should only be introduced when:

- The resource has a distinct responsibility.
- Discovery provides value.
- Existing registries cannot represent it clearly.

Avoid creating registries for every small concept.

---

## Design Implications

Registry Types enable:

- Organized discovery.
- Modular growth.
- Clear ownership.
- Future automation.
- Capability expansion.

---

## Non-Goals

This document does not define:

- Registry implementation.
- Storage format.
- Registry APIs.
- Runtime loading behavior.

---

## Related Documents

- Registry Overview
- Registry Model
- Registry Lifecycle
- Registry Discovery
- Registry Validation
- Registry Evolution

---

## Summary

Registry Types organize the discoverable resources within Decidera.

By separating workflows, capabilities, providers, modules, and templates into clear registry categories, Decidera can scale while maintaining consistency and architectural clarity.
