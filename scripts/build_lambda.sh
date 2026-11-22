#!/usr/bin/env bash
# Build backend/build/lambda.zip for AWS Lambda (Python 3.12, Linux x86_64).
# Dependencies are downloaded as Linux wheels so the package runs on Lambda, even from a Mac.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BACKEND="$ROOT/backend"
PKG="$BACKEND/build/pkg"
rm -rf "$BACKEND/build" && mkdir -p "$PKG"
python3 -m pip install --quiet --upgrade \
  --platform manylinux2014_x86_64 --implementation cp --python-version 3.12 \
  --only-binary=:all: -r "$BACKEND/requirements.txt" -t "$PKG"
cp -R "$BACKEND/app" "$BACKEND/data" "$PKG/"
find "$PKG" -name __pycache__ -type d -prune -exec rm -rf {} +
(cd "$PKG" && zip -qr "$BACKEND/build/lambda.zip" .)
echo "built $BACKEND/build/lambda.zip ($(du -h "$BACKEND/build/lambda.zip" | cut -f1))"
