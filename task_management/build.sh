#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Apply any outstanding database migrations
python manage.py migrate

# create sample users : 
python manage.py shell < wsgi.py

echo "Build completed and users created 🤝." 
