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

2. **Запуск через docker-compose**
    ```bash
    sudo docker compose build
    sudo docker compose up 
    ```

Примечания:
- Для генерации псевдо-данных доступна следующая команда:
    ```bash
    python manage.py generate_fake_data
    ```