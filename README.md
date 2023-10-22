# KeyValue Store Flask API

## Задачи:
Создать `docker-compose.yml`, разворачивающий приложение на python с простой реализацией REST API. Решение должно состоять из двух контейнеров:
- Любая NoSQL DB.
- Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.
- Создаем значение ключ=значение, изменяем ключ=новое_значение, читаем значение ключа.
- Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.

## Структура проекта
-myapp
|-- model
| `-- model.py
|-- app.py
|-- run.py
docker-compose.yml
Dockerfile
requirements.txt
## Описание

- `model.py`: Класс для работы с базой данных MongoDB. Содержит методы для добавления, получения и обновления значений.

- `app.py`: Основное Flask приложение, которое обрабатывает HTTP запросы для работы с данными в MongoDB.

- `run.py`: Точка входа для запуска Flask приложения.

- `docker-compose.yml`: Описывает сервисы для Docker, чтобы легко развернуть приложение вместе с базой данных MongoDB.

- `Dockerfile`: Инструкции для создания Docker образа нашего приложения.

## Как использовать

1. Клонируйте репозиторий:

\```bash
git clone <URL репозитория>
\```

2. Перейдите в директорию проекта:

\```bash
cd <имя_директории_проекта>
\```

3. Запустите Docker Compose:

\```bash
docker-compose up
\```

После запуска, Flask API будет доступен на порту 8080.

## API методы

- **POST /value**: Добавить пару ключ-значение.
  
- **GET /value?key=<ключ>**: Получить значение по ключу.
  
- **PUT /value**: Обновить значение по ключу.
