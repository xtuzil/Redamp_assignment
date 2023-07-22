#!/bin/bash

# Check if 'venv' directory exists, if not, create a virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install project dependencies from requirements.txt (replace with your requirements file)
pip install -r requirements.txt

# Optionally, you can add other setup tasks here
# ...

# Deactivate the virtual environment
deactivate
