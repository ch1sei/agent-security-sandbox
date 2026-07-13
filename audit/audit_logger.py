"""Audit event schema for gateway decisions."""


def record(request, decision):
    return {"event_type": "policy.decision", "request": request, "decision": decision, "preview": True}
