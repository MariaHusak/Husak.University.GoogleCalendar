#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mycalendar.settings")
django.setup()

from django.contrib.auth.models import User

def main():
    superuser = User.objects.filter(is_superuser=True).first()
    if superuser:
        print("Superuser Username:", superuser.username)
        print("Superuser Password (Hashed):", superuser.password)
    else:
        print("No superuser found.")

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
