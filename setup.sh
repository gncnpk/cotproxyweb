#!/usr/bin/env bash

python3 manage.py migrate

python3 manage.py createsuperuser \
   --username admin --email admin@undef.net

python3 manage.py runserver 0:10415

# http://localhost:10415/admin/
