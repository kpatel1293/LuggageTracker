release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn LuggageTrackerMain.wsgi --log-file -
