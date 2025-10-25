#!/usr/bin/env bash
set -euo pipefail

host=${1:-8.8.8.8}
count=${2:-4}

echo "Pinging $host ($count packets)..."
ping -c "$count" "$host"
