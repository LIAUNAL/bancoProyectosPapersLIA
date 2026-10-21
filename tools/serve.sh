#!/usr/bin/env sh
# Serve the static site locally: ./tools/serve.sh [port]  ->  http://localhost:8000
set -e
cd "$(dirname "$0")/.."
PORT="${1:-8000}"
[ -f docs/index.html ] || uv run --with scikit-learn --with numpy python tools/build_bank.py
echo "Banco LIA en http://localhost:$PORT"
exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory docs
