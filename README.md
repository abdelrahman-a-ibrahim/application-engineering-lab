# Workshop Booking Service

A capacity-aware booking API with transactional reservations, cancellation workflows and durable event publication.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

A backend service for organizations that run technical workshops and need consistent seat reservations under concurrent demand. The design centers on transactional capacity checks, request idempotency, ownership-based authorization and an outbox for booking events.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Transactional seat reservations with capacity enforcement and idempotent request handling.
- Booking cancellation and ownership-based access controls.
- Durable booking events through a transactional outbox.
- Versioned API contracts, database migrations and bounded queries.
- Containerized delivery with health checks and concurrency verification.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
HTTP client -> Booking API -> PostgreSQL
                   |
                   +-> transactional outbox -> event publisher
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

Software engineering · Python · Web APIs · PostgreSQL · Testing · Application security.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/workshop-booking-service.git
cd workshop-booking-service
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/workshop_booking_service/interfaces.py`](src/workshop_booking_service/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- Exactly ten active bookings remain after the capacity test; record conflict responses.
- Retrying a request produces one logical booking, including after a process restart.
- Outbox rows cannot be lost between booking commit and publisher restart; downstream duplicates are documented.
- Authorization tests cover object ownership and admin-only operations.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/workshop_booking_service/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://docs.python.org/3/library/unittest.html
- https://www.postgresql.org/docs/current/transaction-iso.html
- https://owasp.org/www-project-api-security/
