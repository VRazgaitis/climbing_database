#!/bin/bash
# Create the virtual environment
python3.10 -m venv venv
# Activate the virtual environment
source myenv/bin/activate
# Install dependencies
pip install -r requirements.txt