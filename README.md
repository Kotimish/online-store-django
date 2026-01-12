# online-store-django


### Установка

1. **Клонируем репозиторий и переходим в папку проекта**
    - По HTTP
    ```bash
    git clone https://github.com/Kotimish/online-store-django.git
    ```
   - Или по SSH
    ```bash
    git clone git@github.com:Kotimish/online-store-django.git
    ```
    - Переходим в созданную папку проекта
    ```bash
    cd online-store-django
    ```

2. **Создаем виртуальное окружение**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    Примечание: Убедитесь, что ваша версия Python не ниже 3.12.
    При необходимости указывайте явно версию Python при создании окружения.

    К примеру (для Python3.12)
    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

3. **Устанавливаем необходимые пакеты с помощью poetry**
    ```bash
    poetry install
    ```
   Если poetry отсутствует, то установите его по следующей инструкции: [ссылка](https://python-poetry.org/docs/#installation)

4. **Выполняем миграции для БД**
    ```bash
    python manage.py migrate
    ```

5. **Запуск**
    ```bash
    python manage.py runserver
    ```

Примечания:
- Для генерации псевдо-данных доступна следующая команда:
    ```bash
    python manage.py generate_fake_data
    ```