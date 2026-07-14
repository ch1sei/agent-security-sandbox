"""Command-line entry point for a local security decision preview."""

import argparse
import json
from audit.event_store import EventStore
from policy_engine.gateway import SecurityGateway


def main(argv=None):
    parser = argparse.ArgumentParser(prog="security-sandbox")
    parser.add_argument("payload", nargs="?", default="browser.search")
    args = parser.parse_args(argv)
    store = EventStore()
    gateway = SecurityGateway(rules=[{"id": "sensitive-file-access", "match": [".ssh", "id_rsa"], "risk": "critical", "action": "block"}], event_store=store)
    print(json.dumps(gateway.inspect({"request_id": "cli-001", "agent_id": "local-preview", "tool": "shell.execute", "payload": args.payload}), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
