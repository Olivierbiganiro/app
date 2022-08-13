web: gunicorn djangoProject3.wsgi --log-file -
web: gunicorn --pythonpath backend feh.wsgi --log-file - 
release: python backend/manage.py makemigrations --no-input
web: python project-name/manage.py runserver 0.0.0.0:$PORT