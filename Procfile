web: gunicorn djangoProject3.wsgi --log-file -
web: gunicorn --pythonpath backend feh.wsgi --log-file - 
web: python project-name/manage.py runserver 0.0.0.0:$PORT