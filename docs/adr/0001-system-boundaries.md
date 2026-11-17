# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Build WorkshopHub, a fictional training-session booking API. Learners reserve seats; concurrent requests must never oversell a session. Use synthetic learners and a payment simulator only.

## Decision questions
- Concurrency control: optimistic version versus row lock
- Outbox publication and duplicate handling
- Application boundaries and error contract

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
