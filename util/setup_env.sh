#!/bin/bash
# Create the virtual environment
python3 -m venv myenv
# Activate the virtual environment
source myenv/bin/activate
# Install dependencies
pip install -r requirements.txt