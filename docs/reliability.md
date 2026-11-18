# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Send 100 concurrent reservations for a session with capacity 10.
- Retry a successful request after a simulated client timeout.
- Kill the outbox publisher between publish and acknowledgement.
- Attempt to cancel another learner’s booking.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- Exactly ten active bookings remain after the capacity test; record conflict responses.
- Retrying a request produces one logical booking, including after a process restart.
- Outbox rows cannot be lost between booking commit and publisher restart; downstream duplicates are documented.
- Authorization tests cover object ownership and admin-only operations.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
