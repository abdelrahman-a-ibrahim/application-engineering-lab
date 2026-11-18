# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
A backend service for organizations that run technical workshops and need consistent seat reservations under concurrent demand. The design centers on transactional capacity checks, request idempotency, ownership-based authorization and an outbox for booking events.

## Component view
```text
HTTP client -> Booking API -> PostgreSQL
                   |
                   +-> transactional outbox -> event publisher
```

## Design decisions
- Concurrency control: optimistic version versus row lock
- Outbox publication and duplicate handling
- Application boundaries and error contract

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/workshop_booking_service/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
