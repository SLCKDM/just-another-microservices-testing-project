# Проект для проб микросервисов

## Развёртывание проекта

1. Развёрывание PyPI и выгрузка пакетов:

`docker network create shared-net; docker compose -f /path/to/project/Starter/PyPI/docker-compose.yml up --build -d"`

2. Развёртывание основных сервисов (кроль, БД, etc):

`docker compose -f /path/to/project/Starter/core/docker-compose.yml up --build  -d"`

3. Поднятие сервисов:

`docker compose -f /path/to/project/Starter/services/docker-compose.yml up --build -d"`


Для удобства, команды в виде таск находятся в workspace проекта для VS Code. В workspace необходимо заменить пути к проекту на актуальные.
