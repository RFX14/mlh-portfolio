#!/bin/bash
flask db migrate
flask db upgrade
gunicorn wsgi:app -w 1 -b :80 --capture-output --log-level debug
