#!/bin/bash
source /home/deploy/.virtualenvs/hackathon/bin/activate
cd /home/deploy/redwire
exec gunicorn -c gunicorn_settings.py hackathon.wsgi:application
