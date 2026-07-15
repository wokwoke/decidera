# Registry Model

## Purpose

This document defines the conceptual model of Registry in Decidera.

The Registry Model describes how resources are represented, identified, and referenced without becoming the owner of the resources themselves.

---

## Background

Registry provides discoverability across the Decidera ecosystem.

To support different resource types consistently, Registry requires a common representation model.

This model establishes the foundation for all Registry implementations.

---

## Registry Entry

A Registry Entry is a structured reference to a resource.

A Registry Entry describes a resource through metadata while keeping the actual resource content separate.

---

## Entry Structure

A Registry Entry consists of several conceptual fields.

### Identity

Identity provides a unique reference for the resource.

Examples:

- Identifier
- Name
- Version
- Type

Identity allows resources to be referenced consistently.

---

### Description

Description explains the purpose of the registered resource.

It provides human-readable context for discovery.

---

### Location

Location identifies where the actual resource can be found.

Examples:

- Repository path
- External reference
- Provider location

Registry stores the reference, not the resource itself.

---

### Metadata

Metadata provides additional information needed for discovery.

Examples:

- Tags
- Status
- Owner
- Dependencies
- Compatibility information

---

### Relationships

Registry Entries may reference relationships with other resources.

Examples:

- Workflow uses Capability.
- Capability requires Provider.
- Artifact uses Template.

Relationships help Decidera understand the resource ecosystem.

---

## Registry Entry Lifecycle

A Registry Entry follows a general lifecycle.

Create

↓

Register

↓

Discover

↓

Validate

↓

Update

↓

Retire

Each stage represents a different condition of registry management.

---

## Registry Ownership

Registry owns metadata about resources.

Registry does not own:

- Source code.
- Workflow logic.
- Provider implementation.
- Artifact content.

Ownership remains with the original resource.

---

## Registry and Identity

Stable identity is essential.

A Registry Entry should have:

- Unique identification.
- Predictable naming.
- Version awareness.
- Traceable history.

Stable identity enables reliable references across the system.

---

## Registry Relationships

Registry connects different parts of Decidera.

Example:

Workflow Registry

↓

Workflow Entry

↓

Capability Reference

↓

Provider Reference

This creates discoverability without creating direct coupling.

---

## Design Implications

A consistent Registry Model enables:

- Multiple registry types.
- Resource discovery.
- Future automation.
- Better traceability.
- Easier system evolution.

---

## Non-Goals

This document does not define:

- Database schema.
- File format.
- Registry APIs.
- Runtime implementation.

---

## Related Documents

- Registry Overview
- Registry Types
- Registry Lifecycle
- Registry Discovery
- Registry Validation
- Registry Evolution

---

## Summary

The Registry Model defines how Decidera represents resources through structured references.

By separating metadata ownership from resource ownership, Registry provides a flexible foundation for discovery, extension, and long-term system evolution.
