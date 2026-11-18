# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- Exactly ten active bookings remain after the capacity test; record conflict responses.
- Retrying a request produces one logical booking, including after a process restart.
- Outbox rows cannot be lost between booking commit and publisher restart; downstream duplicates are documented.
- Authorization tests cover object ownership and admin-only operations.

## Failure coverage
- Send 100 concurrent reservations for a session with capacity 10.
- Retry a successful request after a simulated client timeout.
- Kill the outbox publisher between publish and acknowledgement.
- Attempt to cancel another learner’s booking.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
