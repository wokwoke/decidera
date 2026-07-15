# Workflow States

## Purpose

This document defines the states of a Decidera workflow during execution.

Workflow states provide visibility into workflow progress, enable reliable coordination, and support future monitoring and recovery mechanisms.

---

## Background

A workflow is not only a sequence of activities.

During execution, a workflow moves through different conditions that represent its current status.

Explicit states allow Decidera to understand, observe, and manage workflow execution consistently.

---

## State Model

A workflow progresses through the following states.

Created

↓

Initialized

↓

Prepared

↓

Running

↓

Validating

↓

Completed

or

Failed

---

## Created

The workflow has been defined but execution has not started.

Characteristics:

- Workflow definition exists.
- Required metadata is available.
- No execution activity has occurred.

---

## Initialized

The workflow execution context has been prepared.

Activities include:

- Loading configuration.
- Resolving workspace context.
- Preparing required resources.

The workflow is ready for preparation.

---

## Prepared

All execution prerequisites have been satisfied.

Activities include:

- Input validation.
- Dependency resolution.
- Environment verification.

The workflow can proceed to execution.

---

## Running

The workflow is actively performing its primary responsibility.

Examples:

- Analyzing discussions.
- Extracting Findings.
- Generating Artifacts.

The workflow remains observable during this state.

---

## Validating

The workflow output is being evaluated.

Validation may include:

- Structure verification.
- Traceability checks.
- Consistency evaluation.

A workflow should not complete without successful validation when validation is required.

---

## Completed

The workflow has successfully finished.

Characteristics:

- Expected outputs exist.
- Results are validated.
- Repository state is consistent.

Completed workflows may become inputs for future workflows.

---

## Failed

The workflow was unable to complete successfully.

Possible causes include:

- Invalid input.
- Missing resources.
- Validation failure.
- External provider failure.

A failed workflow should preserve enough information for diagnosis and recovery.

---

## State Transitions

Valid transitions:

Created → Initialized

Initialized → Prepared

Prepared → Running

Running → Validating

Validating → Completed

Any execution failure may transition:

Any Active State → Failed

Recovery mechanisms may later return a failed workflow to a previous executable state.

---

## State Observability

Workflow states provide visibility into:

- Current execution status.
- Historical progression.
- Failure location.
- Recovery possibilities.

State information may later support:

- User notifications.
- Monitoring systems.
- Audit records.
- Atlas entries.

---

## Design Implications

A defined state model enables:

- Predictable execution.
- Easier debugging.
- Workflow monitoring.
- Future automation.
- Reliable recovery.

---

## Non-Goals

This document does not define:

- Storage format for states.
- Runtime implementation.
- User interface representation.
- Scheduling behavior.

---

## Related Documents

- Workflow Overview
- Workflow Lifecycle
- Workflow Types
- Workflow Coordination
- Workflow Composition
- Workflow Recovery

---

## Summary

Workflow States provide a consistent model for understanding workflow execution.

By defining explicit states and transitions, Decidera can maintain visibility, reliability, and control throughout the engineering process.
