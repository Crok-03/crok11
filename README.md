# JSON Records Service

## Требования

- Python 3.10+
- PostgreSQL
- pip

## Установка

1. Клонировать репозиторий

git clone <repository_url>

cd <repo_name>

2. Создать виртуальное окружение

python -m venv venv

Windows:
venv\Scripts\activate

Linux:
source venv/bin/activate

3. Установить зависимости

pip install -r requirements.txt

4. Создать базу данных PostgreSQL

CREATE DATABASE records_db;

5. Указать настройки базы данных в файле

core/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'records_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

6. Выполнить миграции

python manage.py makemigrations

python manage.py migrate

7. Запустить сервер

python manage.py runserver

8. Открыть браузер

http://127.0.0.1:8000