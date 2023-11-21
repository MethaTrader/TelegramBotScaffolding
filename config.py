import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Телеграм токен
TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# URL базы данных
DATABASE_URL = os.getenv("DATABASE_URL")

# Другие настройки
OTHER_SECRET_KEY = os.getenv("OTHER_SECRET_KEY")
