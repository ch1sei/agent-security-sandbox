"""Policy decision objects for the security gateway preview."""


LEVELS = {"low": 1, "medium": 2, "high": 3, "critical": 4}


def normalize(risk, action, rule_id=None):
    risk = risk if risk in LEVELS else "low"
    action = action if action in {"allow", "review", "block", "redact"} else "review"
    return {"risk": risk, "risk_score": LEVELS[risk], "action": action, "rule_id": rule_id, "status": "preview"}


def requires_approval(decision):
    return decision.get("risk_score", 0) >= LEVELS["high"] and decision.get("action") == "review"
