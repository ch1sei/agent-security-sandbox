# Agent Security Sandbox

> Policy gateway, risk dashboard, approval workflow, and audit workspace for agent tool calls.

Agent Security Sandbox is a product-shaped prototype for placing a security decision layer between an agent and the tools it can use. The intended gateway makes sensitive actions inspectable, classifiable, reviewable, and replayable.

```text
Agent -> Security Gateway -> Policy Engine -> Decision + Audit Event
                                  |
                                  v
                      Shell / Files / Browser / Network / MCP
```

## Product Surface

- Tool-call policy evaluation
- Shell command analysis
- Sensitive path detection
- Secret and credential pattern scanning
- Network destination checks
- Prompt-injection and instruction-conflict signals
- Risk scoring and severity bands
- Allow, review, block, and timeout decisions
- Human approval queue
- Full decision audit trail
- Red-team fixture library
- Replayable security incidents
- Workspace and agent policy profiles
- Configuration versioning and policy diffs

## Core Modules

### Policy Engine

The policy engine evaluates a request against ordered rules. Rules can match tool names, command fragments, file paths, network destinations, environment variables, message targets, and request metadata.

Example policy categories include sensitive file access, external exfiltration, destructive shell operations, unapproved browser or messaging actions, workspace escape, and approval conflicts.

### Command Analyzer

The command analyzer is intended to split shell input into executable segments, identify flags, detect redirects, enumerate network targets, and classify filesystem effects.

### Path and Network Guards

The path guard compares requested paths with allowed, restricted, and blocked scopes. The network guard provides a boundary for destination policy, upload verbs, unusual ports, and private network access.

### Secret Scanner

The secret scanner is designed to detect credential-like patterns before tool output is persisted or returned to an agent. Findings should be redacted in logs while preserving review metadata.

### Approval Workflow

High-risk actions can move into a queue with request context, matched rules, risk explanation, requested scope, expiration time, approver identity, final decision, and rationale.

### Audit Logger

Every policy decision should produce a structured record that can be searched, exported, correlated with an agent session, and replayed during an incident review.

## Decision Model

```json
{
  "request_id": "req_01",
  "agent_id": "research-orchestrator",
  "tool": "filesystem.read",
  "risk": "critical",
  "action": "block",
  "matched_rules": ["sensitive-file-access"],
  "reason": "Requested path is inside a restricted credential scope",
  "policy_version": "2025.04"
}
```

Intended actions are `allow`, `review`, `block`, `timeout`, and `redact`.

## Console Areas

### Risk Posture

The risk dashboard summarizes credential access, data exfiltration, destructive actions, prompt injection, unbounded filesystem access, and unapproved network requests.

### Live Decision Stream

The stream presents recent decisions with severity, tool, agent, matched rule, action, and inspection entry point.

### Policy Performance

Policy activity can be grouped by rule, agent, tool, workspace, or time window. Useful signals include match count, block rate, review backlog, false-positive review, and policy coverage.

### Replay and Red Team

The red-team fixture library is intended to cover prompt injection, credential file access, hidden data transfer, shell command chaining, browser submission, unapproved messaging, path traversal, workspace escape, and configuration downgrade attempts.

## Repository Layout

```text
agent-security-sandbox/
├── analyzers/                Command and request analysis contracts
├── audit/                    Audit event boundary
├── config/                   Policy examples and approval settings
├── console/                  Static security operations console
├── policy_engine/            Policy rules and decision contracts
├── red_team/                 Attack fixture boundary
├── replay/                   Incident replay boundary
├── scanners/                 Secret scanner boundary
├── tests/                    Policy regression fixture layout
└── docs/                     Operations notes and roadmap
```

## Configuration

`config/policies.yaml` demonstrates rules for sensitive files, external exfiltration, destructive shell activity, approval severity, and timeout settings.

Production deployments should additionally define workspace roots, read-only mounts, network policy, secret redaction, approval identity, audit retention, access control, and policy rollback behavior.

## Local Preview

No packages are installed and no model files are downloaded.

```bash
conda env create -f environment.yml
conda activate agent-security-sandbox
```

The environment file intentionally declares no dependencies. Open `console/index.html` to preview the static control plane.

## Roadmap

- Define a stable gateway request and decision envelope
- Add policy simulation before enforcement
- Add approval queue state transitions
- Expand command, path, network, and secret analyzers
- Add replayable red-team fixtures
- Add audit export and incident bundles
- Add policy version comparison and rollback previews
- Add integration boundaries for shell, browser, filesystem, and MCP tools

## Prototype Scope

This is an architectural and visual prototype. The console uses synthetic events, policy functions are simplified contracts, and no security enforcement is active.
