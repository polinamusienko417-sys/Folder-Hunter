#!/usr/bin/env bash
set -euo pipefail

# Creates a virtual environment in .venv and installs requirements
PYTHON=${PYTHON:-python3}
VENV_DIR=".venv"

echo "Creating virtual environment in ${VENV_DIR} using ${PYTHON}..."
${PYTHON} -m venv "${VENV_DIR}"

# Activate and upgrade pip, then install requirements
# Note: on macOS use: source .venv/bin/activate
echo "To activate the venv run: source ${VENV_DIR}/bin/activate"
source "${VENV_DIR}/bin/activate"
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "No requirements.txt found; skipping pip install."
fi

echo "Environment ready. Activate with: source ${VENV_DIR}/bin/activate" 
