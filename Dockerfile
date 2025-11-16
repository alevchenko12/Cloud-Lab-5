FROM python:3.11-slim

# Робоча директорія всередині контейнера
WORKDIR /app

# Спочатку копіюємо тільки requirements.txt для кешування залежностей
COPY requirements.txt .

# Ставимо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі інші файли проєкту
COPY . .

# Відкриваємо порт 7777 всередині контейнера
EXPOSE 7777

# Команда запуску сервісу всередині контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]
