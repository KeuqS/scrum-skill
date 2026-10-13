#!/usr/bin/env python3
"""Resolve invocation intent only; never execute, install or appoint anyone."""
from __future__ import annotations

import argparse
import json
import re
import shlex
import sys

MODES = {"wizard", "setup", "resume", "plan", "deliver", "review", "retro", "doctor"}
ALIASES = {
    "scrum-master": "scrum-master", "sm": "scrum-master",
    "engineering": "engineering", "engineer": "engineering", "software-engineer": "engineering",
    "design": "design", "ui-ux": "design", "ux": "design",
    "qa": "qa", "security": "security", "legal-counsel": "legal-counsel", "legal": "legal-counsel",
    "privacy-counsel": "privacy-counsel", "privacy": "privacy-counsel",
    "ai": "ai", "operations": "operations", "ops": "operations", "domain-reviewer": "domain-reviewer",
}


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValueError(message)


def resolve(request: str) -> dict:
    lexer = shlex.shlex(request, posix=True)
    lexer.whitespace_split = True
    lexer.commenters = ""
    lexer.escape = ""  # Windows paths and all argument values remain literal data.
    tokens = list(lexer)
    role, mode = "scrum-master", "wizard"
    if tokens and tokens[0] == "role":
        tokens.pop(0)
        if not tokens or tokens[0] not in ALIASES:
            raise ValueError("role requires a known role name; see invocation guide")
        role = ALIASES[tokens.pop(0)]
        if tokens and not tokens[0].startswith("--"):
            mode = tokens.pop(0)
            if mode not in MODES:
                raise ValueError("unknown workflow mode")
    elif tokens and tokens[0] in MODES:
        mode = tokens.pop(0)
    elif tokens:
        if len(tokens) == 1 or any(token.startswith("--") for token in tokens):
            raise ValueError("unknown command; use wizard or a supported workflow mode")
        return {"mode": "natural-language", "role": role, "request": request,
                "intent_resolution_required": True, "executes_actions": False}
    if tokens and not any(token.startswith("--") for token in tokens):
        return {"mode": mode, "role": role, "request": request,
                "intent_resolution_required": True, "executes_actions": False}
    parser = Parser(add_help=False, allow_abbrev=False)
    for field in ("goal", "target", "project", "roles", "cadence", "profile"):
        parser.add_argument("--" + field)
    options = vars(parser.parse_args(tokens))
    if options["roles"] is not None:
        roles = [part.strip() for part in options["roles"].split(",")]
        if any(not re.fullmatch(r"[a-z][a-z0-9-]{0,47}", item) for item in roles) or len(set(roles)) != len(roles):
            raise ValueError("roles must be distinct lowercase slugs")
        options["roles"] = roles
    if options["profile"] and role != "domain-reviewer":
        raise ValueError("custom profile is supported through domain-reviewer")
    return {"mode": mode, "role": role, "options": options,
            "executes_actions": False, "authorization": "use actual user/project instructions"}


if __name__ == "__main__":
    try:
        # One request string avoids shell reconstruction and preserves quoted values.
        if len(sys.argv) > 2:
            raise ValueError("pass one quoted invocation argument string")
        print(json.dumps(resolve(sys.argv[1] if len(sys.argv) == 2 else ""), indent=2))
    except ValueError as error:
        print(f"scrum-skill routing: {error}", file=sys.stderr)
        raise SystemExit(2)
