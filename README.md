# Application Engineering Lab

**Python application design, APIs, persistence and secure software delivery**

> Status: foundation only / implementation not started. Independent educational project by Abdelrahman Ahmed. This repository is not a reconstruction of employer systems, a production deployment or proof of completed work.

## The engineering challenge

Build WorkshopHub, a fictional training-session booking API. Learners reserve seats; concurrent requests must never oversell a session. Use synthetic learners and a payment simulator only.

This is a capstone for an experienced engineer. The goal is to defend tradeoffs, investigate failure and produce reproducible evidence, not just get a happy-path demo running.

**Technical focus:** Software engineering · Python · Web APIs · PostgreSQL · Testing · Application security.

## What exists in this first commit

- A project-specific architecture brief and decision questions.
- Five implementation milestones with explicit review gates.
- Failure experiments and acceptance criteria.
- Typed Python interface scaffolds. Methods deliberately raise `NotImplementedError`.
- One synthetic scenario fixture; it is an input, not a successful output or benchmark.
- Evidence and journal templates, an issue template, and syntax/JSON foundation checks.

## What you will build

1. Define API resources, conflict/error responses and a booking state machine. Write an ADR comparing a modular monolith with microservices; start with one deployable service.
2. Implement domain rules and persistence with database migrations. Enforce capacity in a database transaction and use a unique request key for safe retries.
3. Add authentication and authorization for learner versus administrator operations. Include negative authorization tests, pagination and bounded request sizes.
4. Implement a transactional outbox and a background publisher. Demonstrate what happens if the process dies after commit but before publishing.
5. Add integration and concurrency tests, a container build, health/readiness endpoints and an operating runbook. Measure behavior under contention.

## Start here

1. Read [the architecture brief](docs/architecture.md) and record the first decision in [ADR 0001](docs/adr/0001-system-boundaries.md).
2. Inspect [the synthetic scenario](examples/scenario.json) and [the interface boundary](src/application_engineering_lab/interfaces.py).
3. Run the foundation checks from the repository root:

   ```sh
   python3 tools/check_foundation.py
   ```

   Python 3.9+ is sufficient for these standard-library checks. They parse Python and JSON; they do **not** validate runtime behavior, deployment safety, protocol compliance or completion.
4. Create a feature branch, implement milestone 1 and add behavior tests before adapters.
5. Follow [the milestone backlog](docs/milestones.md). Select and pin implementation dependencies when you introduce them; none are installed by this scaffold.
6. Complete [the failure lab](docs/failure-lab.md), gather [evidence](docs/evidence/README.md) and review [acceptance criteria](docs/acceptance.md).

There is deliberately no `deploy`, `apply`, paid API call, installed cloud SDK or working runtime in this initial commit.

## Architecture at a glance

```text
HTTP client -> Booking API -> PostgreSQL
                   |
                   +-> transactional outbox -> event publisher
```

This is a proposed lab architecture. [The design brief](docs/architecture.md) identifies decisions still to make.

## Learning prerequisites

- None. This is an entry point into the curriculum.

Repositories are separate and can evolve independently. If you connect them later, exchange versioned fixtures or contracts; do not rely on sibling-relative imports. You can implement a standalone synthetic adapter first.

## What makes this substantial

- Concurrency control: optimistic version versus row lock
- Outbox publication and duplicate handling
- Application boundaries and error contract

You must explain what happens on retries, partial failure, concurrent operations and recovery. Record what your test environment cannot prove. No result is accepted simply because a dashboard is green.

## Definition of done

- Exactly ten active bookings remain after the capacity test; record conflict responses.
- Retrying a request produces one logical booking, including after a process restart.
- Outbox rows cannot be lost between booking commit and publisher restart; downstream duplicates are documented.
- Authorization tests cover object ownership and admin-only operations.

Also supply installation/reproduction instructions, dependency versions, meaningful behavior tests, cleanup instructions, an architecture decision log and evidence from a repeatable demonstration. A checklist or syntax check alone does not satisfy completion.

## Advanced extensions

- Property-based testing of the booking state machine
- Dependency timeouts and retry budgets
- API compatibility tests and cursor pagination
- Profile database query plans under load

Extensions follow a working baseline; they are not requirements for the first milestone.

## Boundaries and costs

Use fictional services, synthetic inputs and a disposable sandbox. Do not copy employer repositories, runbooks, tickets, customer data, credentials or internal architecture. Real cloud/provider adapters are future work and may incur costs; [the operations plan](docs/operations.md) must identify account, region, budget, resource inventory and teardown before deployment. Budget alerts notify; they do not constitute a hard spending cap.

## Publishable evidence, when earned

A completed lab may support a portfolio case study labeled **independent project**. Share your original code, sanitized diagrams, measured results and a failure/recovery write-up. Employer experience and personal lab evidence remain separate. Never copy illustrative fixture values into a results claim.

## Primary references

- https://docs.python.org/3/library/unittest.html
- https://www.postgresql.org/docs/current/transaction-iso.html
- https://owasp.org/www-project-api-security/

Read current official documentation when selecting SDKs, images, tool versions and integrations. The scaffold intentionally does not guess compatible version combinations.

## Repository map

- `src/application_engineering_lab/interfaces.py`
- `examples/scenario.json`
- `docs/architecture.md`
- `docs/milestones.md`
- `docs/failure-lab.md`
- `docs/acceptance.md`
- `docs/learning-journal.md`
- `docs/evidence/README.md`
- `docs/operations.md` — local/cloud boundaries and teardown plan.
- `docs/adr/` — decisions and alternatives.
- `tools/check_foundation.py` — syntax and fixture integrity only.

## Working agreement

Keep commits focused: `docs`, `feat`, `test`, `fix`, `ops`. Work on a feature branch and merge only after the milestone review. Consult [CONTRIBUTING.md](CONTRIBUTING.md). No open-source license has been chosen yet; see [NOTICE.md](NOTICE.md).
