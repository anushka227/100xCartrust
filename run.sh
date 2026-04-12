#!/bin/sh
set -e
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required (install Xcode CLI tools, Homebrew Python, or pyenv)." >&2
  exit 1
fi
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -U pip >/dev/null
pip install -r requirements.txt
exec python app.py
