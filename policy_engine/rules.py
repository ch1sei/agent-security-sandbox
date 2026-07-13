"""Policy rule contracts used by the security gateway preview."""

RULES = [
    {"id": "sensitive-file-access", "pattern": r"\.ssh|id_rsa|credentials", "risk": "critical", "action": "block"},
    {"id": "external-exfiltration", "pattern": r"curl|wget|upload", "risk": "high", "action": "review"},
]


def evaluate(tool_name, payload):
    return {"tool": tool_name, "risk": "low", "action": "allow", "matched_rules": []}
