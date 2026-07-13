# Agent Security Sandbox

Policy gateway and audit console for agent tool calls.

This repository is a visual and architectural prototype. It intentionally contains no installed packages, no downloaded models, and no claim of production enforcement. Rules, policy decisions, and events are represented as deterministic mock contracts for demonstration.

## Product Modules

Policy engine, command analyzer, path guard, network guard, secret scanner, approval workflow, audit logger, risk dashboard, replay engine, and red-team test suite.

## Local Environment

```bash
conda env create -f environment.yml
conda activate agent-security-sandbox
```

The environment declares no packages. Open `console/index.html` to preview the control plane.
