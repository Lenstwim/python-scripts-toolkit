#!/usr/bin/env bash
set -euo pipefail

path=${1:-.}
size=${2:-100M}

echo "Searching for files larger than $size in $path"
find "$path" -type f -size "+$size" -print
