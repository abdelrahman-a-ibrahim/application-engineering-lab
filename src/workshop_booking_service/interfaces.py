"""Initial application boundary for Workshop Booking Service.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class BookingService:
    def reserve(self, session_id: str, learner_id: str, request_id: str) -> dict:
        """Reserve a seat idempotently under concurrent requests."""
        raise NotImplementedError("Runtime implementation is in development.")

    def cancel(self, booking_id: str, request_id: str) -> dict:
        """Cancel once and emit a durable domain event."""
        raise NotImplementedError("Runtime implementation is in development.")
