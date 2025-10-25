#!/usr/bin/env bash
set -euo pipefail

target_dir=${1:-/var/log}
days_old=${2:-7}

echo "Deleting log files in $target_dir older than $days_old days..."
find "$target_dir" -type f -name '*.log' -mtime "+$days_old" -print -delete
