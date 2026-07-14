"""In-memory approval queue for policy review workflows."""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ApprovalRequest:
    request_id: str
    risk: str
    reason: str
    state: str = "pending"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    reviewer: str | None = None


class ApprovalQueue:
    def __init__(self):
        self.items = {}

    def submit(self, request):
        self.items[request.request_id] = request
        return request

    def decide(self, request_id, state, reviewer):
        if state not in {"approved", "rejected", "expired"}:
            raise ValueError("invalid approval state")
        request = self.items[request_id]
        request.state = state
        request.reviewer = reviewer
        return request

    def pending(self):
        return [item for item in self.items.values() if item.state == "pending"]
