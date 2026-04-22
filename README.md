# llm-p — FastAPI + JWT + OpenRouter

##  Описание проекта

Данный проект представляет собой серверное приложение на **FastAPI**, предоставляющее защищённый API для взаимодействия с большой языковой моделью (LLM) через сервис OpenRouter.

### Основные возможности:

* Регистрация и аутентификация пользователей (JWT)
* Авторизация через Swagger (OAuth2)
* Работа с LLM (чат)
* Хранение истории сообщений
* Очистка истории
* SQLite база данных
* Чистая архитектура (API → UseCases → Repositories → DB/Services)

---

## Технологии

* FastAPI
* SQLAlchemy (async)
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)
* OpenRouter API
* uv (управление зависимостями)

---

## Установка и запуск

### 1. Установка uv

```bash
pip install uv
```

---

### 2. Инициализация проекта

```bash
uv init
```

---

### 3. Создание виртуального окружения

```bash
uv venv
```

---

### 4. Активация

```bash
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate.bat # Windows
```

---

### 5. Установка зависимостей

```bash
uv pip install -r <(uv pip compile pyproject.toml)
```

---

## Настройка .env

В файле `.env.example` найдите строчку OPENROUTER_API_KEY вставьте туда ваш API ключ, который можно получить здесь: https://openrouter.ai/, затем переименуйте `.env.example` в   `.env`

---

## Запуск приложения

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Swagger

После запуска откройте:

```
http://localhost:8000/docs
```

---

## Демонстрация работы API

---

### Регистрация пользователя

```

```

---

### Логин и получение JWT

```

```

---

### Авторизация в Swagger

Нажать кнопку **Authorize** и вставить:

```
Bearer <ваш_токен>
```

```

```

---

### POST /chat

Отправка запроса к LLM:


```

```

---

### GET /chat/history

Получение истории сообщений:

```

```

---

### DELETE /chat/history

Очистка истории:

```

```

---

## Примечание

В проекте использован openrouter/free, который автоматически выбирает самую доступную из бесплатных моделей. В процессе работы над проектом stepfun/step-3.5-flash перестала быть бесплатной, поэтому было решено использовать другие модели.

```

```

---

