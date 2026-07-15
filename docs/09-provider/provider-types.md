# Provider Types

## Purpose

This document defines the categories of providers within Decidera.

Provider Types provide a consistent classification system for organizing implementation sources while maintaining separation between capability definitions and provider implementations.

---

## Background

Decidera may integrate with many types of implementation sources.

Without classification, providers become difficult to discover, manage, and evaluate.

Provider Types provide a common vocabulary for describing implementation categories.

---

## Provider Categories

Decidera organizes providers into several logical categories.

---

## AI Providers

AI Providers deliver artificial intelligence related capabilities.

Examples:

- Language Model Provider.
- Embedding Provider.
- Reasoning Provider.
- Analysis Provider.

AI Providers may implement capabilities such as:

- Text Generation.
- Text Analysis.
- Knowledge Extraction.

---

## Repository Providers

Repository Providers provide access to software repositories and version-controlled resources.

Examples:

- Git Repository Provider.
- Source Analysis Provider.
- Repository Synchronization Provider.

They support engineering knowledge and artifact workflows.

---

## Storage Providers

Storage Providers manage persistence and retrieval.

Examples:

- File Storage Provider.
- Database Provider.
- Object Storage Provider.

Storage Providers provide access without owning the stored knowledge.

---

## Communication Providers

Communication Providers enable interaction between users and external systems.

Examples:

- Messaging Provider.
- Notification Provider.
- Email Provider.

They support information delivery.

---

## Execution Providers

Execution Providers provide environments where operations can run.

Examples:

- Local Runtime Provider.
- Container Provider.
- Remote Execution Provider.

They enable capability execution environments.

---

## External Service Providers

External Service Providers connect Decidera with outside systems.

Examples:

- API Provider.
- Third-party Service Provider.
- Integration Provider.

They allow external capabilities to participate in the ecosystem.

---

## Provider Type Selection

A new provider type should only be introduced when:

- The implementation category has distinct responsibility.
- Existing categories cannot represent it clearly.
- Classification improves discovery and management.

Avoid creating provider types based only on vendor names.

---

## Provider Relationships

A provider type describes the implementation category.

Example:

Capability:

Text Generation

Provider Type:

AI Provider

Provider:

Specific AI Implementation

---

## Design Implications

Provider Types enable:

- Better organization.
- Easier discovery.
- Provider comparison.
- Future extension.
- Clear architecture boundaries.

---

## Non-Goals

This document does not define:

- Provider implementations.
- Vendor selection.
- Performance evaluation.
- Runtime behavior.

---

## Related Documents

- Provider Overview
- Provider Model
- Provider Lifecycle
- Provider Discovery
- Provider Selection
- Provider Composition
- Provider Evolution

---

## Summary

Provider Types organize implementation sources within Decidera.

By classifying providers according to their role rather than technology names, Decidera maintains flexibility and avoids unnecessary coupling.
