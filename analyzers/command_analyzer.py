"""Command analysis interface. Real parsing is intentionally deferred."""


def analyze(command):
    return {"command": command, "segments": [], "network_targets": [], "filesystem_targets": []}
