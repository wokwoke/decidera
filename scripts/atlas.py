#!/usr/bin/env python3

import json
import subprocess
from datetime import datetime


def git(command):
    return subprocess.check_output(
        ["git"] + command,
        text=True
    ).strip()


metadata = {
    "version": "1.0",

    "repository": git(["rev-parse", "--show-toplevel"]).split("/")[-1],

    "branch": git(["branch", "--show-current"]),

    "timestamp": datetime.utcnow().isoformat() + "Z",

    "commit": {
        "hash": git(["rev-parse", "HEAD"]),
        "author": git(["log", "-1", "--pretty=%an"]),
        "message": git(["log", "-1", "--pretty=%s"])
    },

    "changes": {
        "files": git(["diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"]).splitlines()
    }
}

print(json.dumps(metadata, indent=2))