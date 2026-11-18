# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
A backend service for organizations that run technical workshops and need consistent seat reservations under concurrent demand. The design centers on transactional capacity checks, request idempotency, ownership-based authorization and an outbox for booking events.

## Questions
- Concurrency control: optimistic version versus row lock
- Outbox publication and duplicate handling
- Application boundaries and error contract

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.
