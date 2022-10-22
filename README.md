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
- Запуск сервиса 1 сервиса


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

<a id="prod">Запуск в продакшен</a>
```shell
$ docker compose config > docker-stack.yaml
```
* Далее необходимо отредактировать сгенерированный файл `docker-stack.yaml`
* Удалить ключ `name` и добавить вместо него `version="3.9"`
* Привести все `public_port` к типу int
* $ pip install docker-auto-labels
* docker-auto-labels docker-stack.yaml
* docker stack deploy -c docker-stack.yaml `${STACK_NAME?Variable not exists}`


<a id="docs">Документация</a>
https://natours-club.site/docs

                        
