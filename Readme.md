python -m venv env
source env/bin/activate
pip install -r requirements.txt
cd core

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver

docs -> http://127.0.0.1:8000/docs/
admin-pannel -> http://127.0.0.1:8000/admin/
