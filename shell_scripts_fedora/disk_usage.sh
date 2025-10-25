#!/usr/bin/env bash
set -euo pipefail

df -h --total | awk 'NR==1 || /total/'
