"""Request gateway that combines policy decisions and audit events."""

from policy_engine.decision import normalize


class SecurityGateway:
    def __init__(self, rules=None, event_store=None):
        self.rules = rules or []
        self.event_store = event_store

    def inspect(self, request):
        decision = self._evaluate(request)
        event = {"request_id": request.get("request_id"), **decision, "tool": request.get("tool"), "agent_id": request.get("agent_id")}
        if self.event_store:
            self.event_store.append(event)
        return event

    def _evaluate(self, request):
        payload = str(request.get("payload", "")).lower()
        for rule in self.rules:
            if any(str(term).lower() in payload for term in rule.get("match", [])):
                return normalize(rule.get("risk", "high"), rule.get("action", "review"), rule.get("id"))
        return normalize("low", "allow")
