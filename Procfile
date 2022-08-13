web: gunicorn djangoProject3.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
web: gunicorn djangoProject3.wsgi
release: python manage.py makemigrations --no-input
