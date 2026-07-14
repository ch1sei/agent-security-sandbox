"""Conservative secret-pattern scanner for preview policy checks."""

import re


PATTERNS = {
    "private-key": re.compile(r"-----BEGIN [A-Z ]+ PRIVATE KEY-----"),
    "token-assignment": re.compile(r"(?i)(api[_-]?key|token|secret)\s*[:=]\s*[^\s]+"),
    "password-assignment": re.compile(r"(?i)password\s*[:=]\s*[^\s]+"),
}


class SecretScanner:
    def scan(self, text):
        text = text or ""
        findings = []
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append({"type": name, "start": match.start(), "end": match.end(), "action": "redact"})
        return {"detected": bool(findings), "findings": findings, "status": "preview"}

    def redact(self, text):
        result = text or ""
        for pattern in PATTERNS.values():
            result = pattern.sub("[REDACTED]", result)
        return result
