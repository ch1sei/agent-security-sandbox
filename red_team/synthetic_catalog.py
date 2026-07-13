"""Synthetic registry used by the dependency-free prototype preview.

Generated fixture records intentionally keep the product surface rich while
leaving runtime integrations behind explicit interfaces.
"""

CATALOG = [
    {
        "id": "SEC-0001", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0002", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0003", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0004", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0005", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0006", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0007", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0008", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0009", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0010", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0011", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0012", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0013", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0014", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0015", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0016", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0017", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0018", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0019", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0020", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0021", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0022", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0023", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0024", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0025", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0026", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0027", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0028", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0029", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0030", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0031", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0032", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0033", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0034", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0035", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0036", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0037", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0038", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0039", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0040", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0041", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0042", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0043", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0044", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0045", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0046", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0047", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0048", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0049", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0050", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0051", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0052", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0053", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0054", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0055", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0056", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0057", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0058", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0059", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0060", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0061", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0062", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0063", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0064", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0065", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0066", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0067", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0068", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0069", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0070", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0071", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0072", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0073", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0074", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0075", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0076", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0077", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0078", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0079", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0080", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0081", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0082", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0083", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0084", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0085", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0086", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0087", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0088", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0089", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0090", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0091", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0092", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0093", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0094", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0095", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0096", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0097", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0098", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0099", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0100", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0101", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0102", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0103", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0104", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0105", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0106", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0107", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0108", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0109", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0110", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0111", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0112", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0113", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0114", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0115", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0116", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0117", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0118", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0119", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0120", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0121", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0122", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0123", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0124", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0125", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0126", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0127", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0128", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0129", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0130", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0131", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0132", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0133", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0134", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0135", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0136", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0137", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0138", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0139", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0140", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0141", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0142", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0143", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0144", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0145", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0146", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0147", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0148", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0149", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0150", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0151", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0152", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0153", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0154", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0155", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0156", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0157", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0158", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0159", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0160", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0161", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0162", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0163", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0164", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0165", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0166", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0167", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0168", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0169", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "medium", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0170", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "high", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0171", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "critical", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0172", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "low", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0173", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "medium", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0174", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "high", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0175", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "critical", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0176", "rule": "external-exfiltration",
        "tool": "network.request",
        "risk": "low", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0177", "rule": "destructive-shell",
        "tool": "shell.execute",
        "risk": "medium", "action": "allow", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0178", "rule": "workspace-boundary",
        "tool": "browser.open",
        "risk": "high", "action": "review", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0179", "rule": "prompt-injection",
        "tool": "mcp.call",
        "risk": "critical", "action": "block", "tags": ["synthetic", "preview"],
    },
    {
        "id": "SEC-0180", "rule": "sensitive-file-access",
        "tool": "filesystem.read",
        "risk": "low", "action": "allow", "tags": ["synthetic", "preview"],
    },
]

def list_records(tag=None):
    """Return catalog records, optionally filtered by a tag."""
    if tag is None:
        return list(CATALOG)
    return [record for record in CATALOG if tag in record.get("tags", [])]

def summarize():
    """Return a small summary for dashboard cards."""
    return {"total": len(CATALOG), "synthetic": len(CATALOG), "source": "preview"}
