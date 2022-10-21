# CiPlay Task

- [Зависимости](#requirements)
- [Запуск локально в докере](#local)
- [Запуск тестов](#tests)
- [Документация API](#docs)

<a id="requirements">Зависимости</a>

- [Docker](https://www.docker.com/)
- [docker compose v2](https://docs.docker.com/compose/install/)

<a id="local">Запуск локально в докере</a>

```shell
$ cat .env.example > .env
# Заполнить .env вашими данными

$ docker compose up -d 
```
Команда включает в себя:
- Cборка и запуск докер контейнеров
- Создание таблицы, если не была создана ранее 
- Запуск сервиса


<a id="tests">Запуск тестов</a>
```shell
$ cat .env.example > .env
# Заполнить .env вашими данными

$ <path_to_project>/scripts/start-test.sh
```
Команда включает в себя:
- Удаление текущих контейнеров вместе с volume, если запущены
- Сборка и запуск докер контейнеров
- Форматирование кода (Опционально)
- Удаление скомпилированных python файлов (`__pycache__`)
- Создание таблицы, если не была создана ранее 
- Запуск тестов


<a id="docs">Документация</a>

http://localhost:8000/docs
