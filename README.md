Django 3.0 
To run project 
Clone repo: git clone https://github.com/SymbioCode/Pet_Project.git 
Enter to repo: cd django_book_by_book_1 
Create virtual environment: virtualenv -p python3 venv.
Activate virtual environment: source venv/bin/activate.
Install requirements: pip3 install -r requirements.txt.
Run migrations: python3 manage.py migrate.
Run server: python3 manage.py runserver.
Local settings
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'scientia044@gmail.com'
EMAIL_HOST_PASSWORD = '**********'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
