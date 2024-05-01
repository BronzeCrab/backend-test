TODO:

- проставь энвы (см. .env.example)
- запусти постгрю (тестилось на 15й версии, но другая тоже подойдет) и создай базу
- прогони миграции
- доделай ручку, к которой написан TODO комментарий

Как запустить приложение, прогнать линтер и миграции - см. Makefile

За помощью обращайся к чему угодно, но начать лучше с документации:

- [poetry](https://python-poetry.org/)
- [yoyo](https://ollycope.com/software/yoyo/latest/)
- [strawberry](https://strawberry.rocks/docs)
- [graphql](https://graphql.org/learn/)
- [fastapi](https://fastapi.tiangolo.com/)
- [asyncpg](https://magicstack.github.io/asyncpg/current/)
- [ruff](https://docs.astral.sh/ruff/)
- [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html)

Мы знаем, что наше тестовое может решить (или помочь решить) ChatGPT.
Мы ок с использованием вспомогательных инструментов для разработки,
но, пожалуйста, не делайте этого бездумно.

А есть ли в коде баги? Кто знает...

## Что я сделал:

0. Добавил `git init`
1. Добавил `docker-compose.yml`
2. Скопировал .env
3. Поставил зависимости, создал окружение: `poetry install`
4. Поднял базу: `sudo docker compose -f docker-compose.yml up -d`
5. Зашел в `dbeaver`, проверил базу
6. Попытался `poetry run python schema.py`, получил ошибку валидации схемы, поправил
7. Запустил снова `poetry run uvicorn schema:app --reload`, сервер поднялся
8. Попробал сделать graphql запрос на книги, получил пустой список
9. Накатил миграции `poetry run python -m yoyo apply -vvv --batch --database "postgresql+psycopg://postgres:postgres@$127.0.0.1:6432/books" ./migrations`, не получилось, поправил, накатил.
10. Поправил ручку `books`, протестил сервис.
