"""Proposed application boundary for Application Engineering Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class BookingService:
    def reserve(self, session_id: str, learner_id: str, request_id: str) -> dict:
        """Reserve a seat idempotently under concurrent requests."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def cancel(self, booking_id: str, request_id: str) -> dict:
        """Cancel once and emit a durable domain event."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

