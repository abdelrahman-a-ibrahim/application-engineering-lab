# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
A backend service for organizations that run technical workshops and need consistent seat reservations under concurrent demand. The design centers on transactional capacity checks, request idempotency, ownership-based authorization and an outbox for booking events.

## Target capabilities
- Define API resources, conflict/error responses and a booking state machine. Write an ADR comparing a modular monolith with microservices; start with one deployable service.
- Implement domain rules and persistence with database migrations. Enforce capacity in a database transaction and use a unique request key for safe retries.
- Add authentication and authorization for learner versus administrator operations. Include negative authorization tests, pagination and bounded request sizes.
- Implement a transactional outbox and a background publisher. Demonstrate what happens if the process dies after commit but before publishing.
- Add integration and concurrency tests, a container build, health/readiness endpoints and an operating runbook. Measure behavior under contention.

## Acceptance criteria
- Exactly ten active bookings remain after the capacity test; record conflict responses.
- Retrying a request produces one logical booking, including after a process restart.
- Outbox rows cannot be lost between booking commit and publisher restart; downstream duplicates are documented.
- Authorization tests cover object ownership and admin-only operations.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.
