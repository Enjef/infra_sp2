# Проект: запуск docker-compose

### Описание
После выполнения установки в трёх docker-контейнерах будет развёрнут проект YaMDb.
Проект YaMDb собирает оценки и отзывы пользователей на произведения(книги, фильмы, музыка и пр.).

### Технологии
- Python 3.8.5
- django 3.0.5
- docker-compose 3.8
- postgres:12.4

### Запуск проекта
Выполните команды:
```
docker-compose up -d --build
docker-compose exec web python manage.py makemigrations api --noinput
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py loaddata fixtures.json
docker-compose exec web python manage.py createsuperuser
```
### DockerHub
Образ YaMDb доступен на DockerHub: enjefd/yamdb:v1

### Переменные окружения

| Переменная | Описание |
| ------ | ------ |
| DB_ENGINE | указываем, что работаем с postgresql |
| DB_NAME | имя базы данных |
| POSTGRES_USER | логин для подключения к базе данных |
| POSTGRES_PASSWORD | пароль для подключения к БД |
| DB_HOST | название сервиса (контейнера) |
| DB_PORT | порт для подключения к БД |
