#!/usr/bin/env bash
set -euo pipefail

uname -a
lsb_release -a 2>/dev/null || echo "lsb_release not available"
