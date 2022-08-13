web: gunicorn djangoProject3.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

release: python manage.py makemigrations --no-input
web: python djangoProject3/manage.py runserver 0.0.0.0:$PORT