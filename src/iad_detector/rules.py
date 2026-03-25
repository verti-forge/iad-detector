from __future__ import annotations

IRREVERSIBLE_HINTS = {
    "deploy",
    "delete",
    "send",
    "publish",
    "push",
    "merge",
    "write-public",
}

COMPOUND_SEPARATORS = [" and ", " then ", ", and ", ";", " + "]

TOOL_HINTS = {
    "compare": {"diff", "reader", "local.read"},
    "read": {"reader", "local.read", "docs.search", "web.search"},
    "search": {"docs.search", "web.search"},
    "patch": {"editor.patch", "editor.write"},
    "test": {"runner.test", "terminal"},
    "deploy": {"deploy", "terminal"},
}
