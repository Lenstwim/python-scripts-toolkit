#!/usr/bin/env bash
set -euo pipefail

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
target=${1:-$HOME}
archive="${HOME}/backup_${timestamp}.tar.gz"

tar -czf "$archive" "$target"
echo "Backup created: $archive"
