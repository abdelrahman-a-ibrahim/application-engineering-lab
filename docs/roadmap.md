# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Define API resources, conflict/error responses and a booking state machine. Write an ADR comparing a modular monolith with microservices; start with one deployable service.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Implement domain rules and persistence with database migrations. Enforce capacity in a database transaction and use a unique request key for safe retries.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Add authentication and authorization for learner versus administrator operations. Include negative authorization tests, pagination and bounded request sizes.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Implement a transactional outbox and a background publisher. Demonstrate what happens if the process dies after commit but before publishing.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Add integration and concurrency tests, a container build, health/readiness endpoints and an operating runbook. Measure behavior under contention.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- Property-based testing of the booking state machine
- Dependency timeouts and retry budgets
- API compatibility tests and cursor pagination
- Profile database query plans under load

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.
