# Runtime State

## Purpose

This document defines the Runtime State Model of Decidera.

Runtime State describes the lifecycle of an execution while it is managed by the Runtime system.

---

## Background

Execution is not a single action.

Every execution progresses through a series of observable states.

Explicit state management improves traceability, recovery, monitoring, and engineering reliability.

---

## Runtime State Definition

A Runtime State represents the current condition of an execution.

Every execution should always be in exactly one runtime state.

State transitions should be explicit and observable.

---

## State Lifecycle

A typical execution progresses through the following states:

Created

↓

Pending

↓

Running

↓

Completed

or

Failed

Additional states may exist when required.

---

## Created

An execution has been initialized.

Responsibilities:

- Create execution identifier.
- Initialize execution context.
- Prepare runtime resources.

Execution has not yet started.

---

## Pending

Execution is waiting to begin.

Possible reasons:

- Waiting for scheduling.
- Waiting for dependencies.
- Waiting for provider availability.

Pending execution performs no work.

---

## Running

Execution is actively performing work.

Examples:

- Executing workflow.
- Resolving capabilities.
- Invoking providers.
- Producing artifacts.

Running represents the active execution phase.

---

## Completed

Execution finished successfully.

Responsibilities:

- Collect results.
- Finalize artifacts.
- Record execution history.
- Release runtime resources.

Completed is a terminal state.

---

## Failed

Execution cannot continue.

Examples:

- Provider unavailable.
- Validation failed.
- Unexpected runtime error.
- Unrecoverable execution problem.

Failure should always be observable.

---

## State Transitions

Runtime controls valid state transitions.

Example:

Created

↓

Pending

↓

Running

↓

Completed


or


Created

↓

Pending

↓

Running

↓

Failed

Unexpected transitions should be rejected.

---

## State Visibility

Runtime State should remain observable.

Execution status may be used by:

- Runtime.
- Monitoring.
- Atlas.
- Engineering reports.

State visibility improves system understanding.

---

## Atlas Integration

Important state transitions may be recorded in Atlas.

Examples:

- Execution started.
- Execution completed.
- Execution failed.
- Recovery performed.

---

## Design Implications

Explicit Runtime State enables:

- Reliable monitoring.
- Better recovery.
- Predictable execution.
- Engineering traceability.
- Operational consistency.

---

## Non-Goals

This document does not define:

- Scheduling policy.
- Retry strategy.
- Distributed execution.
- Infrastructure monitoring.

---

## Related Documents

- Runtime Overview
- Runtime Model
- Runtime Execution
- Runtime Event
- Runtime Orchestration
- Runtime Recovery
- Runtime Evolution

---

## Summary

Runtime State provides an explicit lifecycle for execution.

By managing observable execution states, Decidera improves reliability, traceability, and operational consistency.
