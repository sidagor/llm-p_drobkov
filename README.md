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
### Эндпоинты

```
<img width="965" height="489" alt="эндпоинты" src="https://github.com/user-attachments/assets/a3b0dcc8-5b77-4b21-92d7-e7b4b00db36d" />

```
---

### Регистрация пользователя

```
<img width="939" height="443" alt="регистрация" src="https://github.com/user-attachments/assets/cf7e2ce8-3959-4a0e-837d-071b55ab3e4b" />
```
---

### Логин и получение JWT

```
<img width="942" height="355" alt="Авторизация" src="https://github.com/user-attachments/assets/7a7a0993-8f56-451a-9709-70e435c65716" />
```
---

### Авторизация в Swagger
```
<img width="429" height="358" alt="авторизация swagger1" src="https://github.com/user-attachments/assets/77fa4c15-8756-4288-9048-fc45f98a5892" />
```

```
<img width="424" height="312" alt="авторизация swagger" src="https://github.com/user-attachments/assets/9210b0bd-d612-40e1-9c7c-21fa9b31c6b7" />

```
---

### POST /chat

Отправка запроса к LLM:
```
<img width="705" height="409" alt="ответ нейросети" src="https://github.com/user-attachments/assets/1c58a47f-0ce9-42ab-8ce9-09d0f63ef953" />
```
---

### GET /chat/history

Получение истории сообщений:
```
<img width="704" height="403" alt="получение истории чата" src="https://github.com/user-attachments/assets/ba91fcc0-2be1-430c-9d70-558a0585f64e" />
```
---

### DELETE /chat/history

Очистка истории:

```
<img width="707" height="242" alt="очистка истории" src="https://github.com/user-attachments/assets/22e50866-17a8-4d2f-bdbf-1565405de90d" />

```
---

## Примечание

В проекте использован openrouter/free, который автоматически выбирает самую доступную из бесплатных моделей. В процессе работы над проектом stepfun/step-3.5-flash перестала быть бесплатной, поэтому было решено использовать другие модели.

```
<img width="718" height="133" alt="нейросеть" src="https://github.com/user-attachments/assets/41264557-565e-4c5d-a5be-129924855e3f" />

```
---

