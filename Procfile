web: gunicorn djangoProject3.wsgi --log-file -
web: gunicorn --pythonpath backend feh.wsgi --log-file - 
release: python manage.py makemigrations --no-input
web: python djangoProject3/manage.py runserver 0.0.0.0:$PORT