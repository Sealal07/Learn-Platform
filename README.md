**Установка и запуск
**
1. Клонирование репозитория


git clone https://github.com/yourusername/learn_platform.git
cd learn_platform

2. Создание виртуального окружения (рекомендуется)


python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Установка зависимостей


pip install -r requirements.txt


4. Настройка базы данных


python manage.py migrate

5. Создание суперпользователя


python manage.py createsuperuser

6. Запуск сервера


python manage.py runserver
Откройте в браузере: http://127.0.0.1:8000
