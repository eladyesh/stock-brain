#!/usr/bin/env bash
# Schedule from a stable authorized host; preserve this checkout's build directory.
set -euo pipefail
stock_brain_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
cd -- "$stock_brain_root"
: "${SEC_USER_AGENT:?Set SEC_USER_AGENT to your identifying application/contact string}"
stock_brain_python=${PYTHON_BIN:-python3}
mkdir -p build/monitoring
# flock prevents overlapping timers on Linux. No background daemon is installed here.
exec 9>build/monitoring/refresh.lock
flock -n 9 || exit 0
"$stock_brain_python" scripts/disclosure_monitor.py --summary build/monitoring/summary.md
"$stock_brain_python" scripts/prepare_updates.py --limit 2
