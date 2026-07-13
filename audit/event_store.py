"""In-memory audit event store used by the static security prototype."""


class EventStore:
    def __init__(self):
        self.events = []

    def append(self, event):
        event = dict(event)
        event.setdefault("event_type", "policy.decision")
        event.setdefault("status", "preview")
        self.events.append(event)
        return event

    def list(self, risk=None):
        if risk is None:
            return list(self.events)
        return [event for event in self.events if event.get("risk") == risk]

    def summary(self):
        return {"total": len(self.events), "blocked": len([event for event in self.events if event.get("action") == "block"]), "status": "preview"}
