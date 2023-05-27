#!/bin/bash

# making virtual environment
python3.8 -m venv venv

# activate virtual environment
source venv/bin/activate

# set up the project
pip install -r requirements.txt
python manage.py migrate
