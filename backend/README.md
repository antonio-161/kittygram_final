# Kittygram Backend

Kittygram — это сервис для любителей кошек, где пользователи могут добавлять карточки своих питомцев, делиться фотографиями и просматривать анкеты других котиков.

## Описание проекта

Данный репозиторий содержит backend-часть приложения Kittygram, реализованную на Django и Django REST Framework. Сервис предоставляет API для работы с карточками котов, их цветами, достижениями и фотографиями.

## Основные возможности

- Регистрация и аутентификация пользователей
- Добавление, редактирование и удаление карточек котов
- Загрузка фотографий котов
- Просмотр карточек других пользователей
- Фильтрация и поиск по цвету и достижениям

## Технологии

- Python 3.8+
- Django 3.x
- Django REST Framework
- PostgreSQL
- Docker, Docker Compose
- Gunicorn
- Nginx

## Быстрый старт

### Клонирование репозитория

```sh
git clone https://github.com/yandex-praktikum/kittygram_backend.git
cd kittygram_backend
```

### Локальный запуск (без Docker)

1. Создайте и активируйте виртуальное окружение:
    - Linux/macOS:
      ```sh
      python3 -m venv env
      source env/bin/activate
      ```
    - Windows:
      ```sh
      python -m venv env
      source env/scripts/activate
      ```

2. Установите зависимости:
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

3. Выполните миграции:
    ```sh
    python3 manage.py migrate
    ```

4. Запустите сервер разработки:
    ```sh
    python3 manage.py runserver
    ```

### Запуск с помощью Docker

1. Соберите и запустите контейнеры:
    ```sh
    docker-compose up --build
    ```

2. Приложение будет доступно по адресу: http://localhost:8000/

## Переменные окружения

Для настройки проекта используйте файл `.env` (пример — `.env.example`).

## Документация API

После запуска проекта документация доступна по адресу:  
`/api/docs/` (если настроено в проекте)

## Контакты

- Автор: [Антон Степанов]
- Email: [antonstepanov@yandex.ru]