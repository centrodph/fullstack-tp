release: cd api && pip install -r requirements.txt && python manage.py migrate
web: gunicorn simpk.wsgi --log-file -