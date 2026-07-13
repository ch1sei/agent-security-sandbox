"""Workspace path boundary for policy simulation."""


class PathGuard:
    def __init__(self, allowed_roots=None, blocked_fragments=None):
        self.allowed_roots = allowed_roots or ["./workspace"]
        self.blocked_fragments = blocked_fragments or [".ssh", "credentials", "id_rsa"]

    def inspect(self, path):
        path = path or ""
        blocked = [fragment for fragment in self.blocked_fragments if fragment in path]
        allowed = any(path.startswith(root) for root in self.allowed_roots)
        return {"path": path, "allowed_root": allowed, "blocked_fragments": blocked, "action": "block" if blocked or not allowed else "allow"}


def explain(result):
    return "blocked by path policy" if result.get("action") == "block" else "path is inside an allowed preview root"
