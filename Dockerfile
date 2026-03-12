# Базовый образ
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Рабочая директория
WORKDIR /app

# Устанавливаем Poetry
RUN pip install --upgrade pip wheel poetry
RUN poetry config virtualenvs.create false

# Копируем файлы конфигурации
COPY pyproject.toml poetry.lock README.md ./

# Устанавливаем только зависимости
RUN poetry install --no-root

# Копируем код
COPY . /app

# Делаем скрипт исполняемым
RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]