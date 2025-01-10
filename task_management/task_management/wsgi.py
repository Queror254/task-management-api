#!/usr/bin/env python3
"""
WSGI config for task_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import django

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')

# Initialize Django
django.setup()

# Get the custom user model
CustomUser = get_user_model()

# Ensure the database is ready
connection.ensure_connection()

# Users data
users = [
    {
        'username': 'admin',
        'password': 'admin',  # 
        'email': 'admin@example.com',
    },
    {
        'username': 'victor',
        'password': 'victor',  
        'email': 'victor@example.com',
    },
]

for user in users:
    # Check if the user exists, create the user if not
    if not CustomUser.objects.filter(username=user['username']).exists():
        CustomUser.objects.create_superuser(
            username=user['username'],
            email=user['email'],
            password=user['password']
        )
        print(f"Superuser {user['username']} created.")
    else:
        print(f"Superuser {user['username']} already exists.")


application = get_wsgi_application()
