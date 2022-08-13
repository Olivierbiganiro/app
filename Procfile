web: gunicorn djangoProject3.wsgi --log-file -
web: gunicorn djangoProject3.wsgi
release: python manage.py makemigrations --no-input
web: python djangoProject3/manage.py runserver 0.0.0.0:$PORT