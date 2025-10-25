#!/usr/bin/env bash
set -euo pipefail

process=${1:?"Usage: $0 <process-name>"}

if pgrep -x "$process" >/dev/null; then
    echo "$process is running"
else
    echo "$process is not running"
fi
