# API документация сервиса Users

## Оглавление

- [Введение](#введение)
- [Базовая информация](#базовая-информация)
  - [Форматы запросов и ответов](#форматы-запросов-и-ответов)
- [Пользователи](#пользователи)
- [Курсы обучения](#курсы-обучения)
  - [Курс Toncoin](#курс-toncoin)
  - [Курс NFT продаж](#курс-nft-продаж)
  - [Курс P2P](#курс-p2p)
  - [Курс по безопасности (Scam)](#курс-по-безопасности-scam)

## Введение

API сервиса Users предоставляет интерфейс для работы с пользователями и их прогрессом по образовательным курсам.

## Базовая информация

### Форматы запросов и ответов

API использует формат JSON для запросов и ответов. Все эндпоинты поддерживают стандартные HTTP методы (GET, POST, PUT, PATCH, DELETE) в соответствии с принципами REST API.

## Пользователи

### Получение списка пользователей

```
GET /api/v1/users/
```

Пример ответа:
```json
[
  {
    "user_id": 123456789,
    "username": "johndoe",
    "fullname": "John Doe",
    "registration_date": "2025-08-29T15:30:45Z",
    "language": "ru",
    "ref_user": null,
    "is_premium": false,
    "balance": 0.0
  },
  {
    "user_id": 987654321,
    "username": "janedoe",
    "fullname": "Jane Doe",
    "registration_date": "2025-08-28T12:15:30Z",
    "language": "en",
    "ref_user": 123456789,
    "is_premium": true,
    "balance": 100.5
  }
]
```

### Получение информации о конкретном пользователе

```
GET /api/v1/users/{user_id}/
```

Пример ответа:
```json
{
  "user_id": 123456789,
  "username": "johndoe",
  "fullname": "John Doe",
  "registration_date": "2025-08-29T15:30:45Z",
  "language": "ru",
  "ref_user": null,
  "is_premium": false,
  "balance": 0.0
}
```

### Создание нового пользователя

```
POST /api/v1/users/
```

Пример запроса:
```json
{
  "user_id": 123456789,
  "username": "johndoe",
  "fullname": "John Doe",
  "language": "ru",
  "ref_user": null
}
```

Пример ответа (код 201 Created):
```json
{
  "user_id": 123456789,
  "username": "johndoe",
  "fullname": "John Doe",
  "registration_date": "2025-08-30T10:15:30Z",
  "language": "ru",
  "ref_user": null,
  "is_premium": false,
  "balance": 0.0
}
```

### Обновление пользователя

```
PUT /api/v1/users/{user_id}/
```

Пример запроса:
```json
{
  "user_id": 123456789,
  "username": "johndoe",
  "fullname": "John Smith",
  "language": "en",
  "ref_user": 987654321,
  "is_premium": true,
  "balance": 50.0
}
```

Пример ответа:
```json
{
  "user_id": 123456789,
  "username": "johndoe",
  "fullname": "John Smith",
  "registration_date": "2025-08-29T15:30:45Z",
  "language": "en",
  "ref_user": 987654321,
  "is_premium": true,
  "balance": 50.0
}
```

### Частичное обновление пользователя

```
PATCH /api/v1/users/{user_id}/
```

Пример запроса:
```json
{
  "is_premium": true,
  "balance": 75.5
}
```

Пример ответа:
```json
{
  "user_id": 123456789,
  "username": "johndoe",
  "fullname": "John Doe",
  "registration_date": "2025-08-29T15:30:45Z",
  "language": "ru",
  "ref_user": null,
  "is_premium": true,
  "balance": 75.5
}
```

### Удаление пользователя

```
DELETE /api/v1/users/{user_id}/
```

Успешный ответ: статус 204 No Content

## Курсы обучения

API предоставляет эндпоинты для работы с прогрессом пользователей по различным образовательным курсам. Все курсы используют одинаковую структуру и набор эндпоинтов.

### Общая структура объекта курса

```json
{
  "id": 1,
  "user_id": 123456789,
  "chapter": 2,
  "lesson": 3
}
```

Где:
- `id` - уникальный идентификатор записи о прогрессе
- `user_id` - идентификатор пользователя
- `chapter` - номер текущей главы курса
- `lesson` - номер текущего урока в главе

### Курс Toncoin

#### Получение списка прогресса по курсу Toncoin

```
GET /api/v1/toncoin-courses/
```

Пример ответа:
```json
[
  {
    "id": 1,
    "user_id": 123456789,
    "chapter": 1,
    "lesson": 2
  },
  {
    "id": 2,
    "user_id": 987654321,
    "chapter": 3,
    "lesson": 1
  }
]
```

#### Получение прогресса конкретного пользователя по курсу Toncoin

```
GET /api/v1/toncoin-courses/{id}/
```

Пример ответа:
```json
{
  "id": 1,
  "user_id": 123456789,
  "chapter": 1,
  "lesson": 2
}
```

#### Создание записи о прогрессе по курсу Toncoin

```
POST /api/v1/toncoin-courses/
```

Пример запроса:
```json
{
  "user_id": 123456789,
  "chapter": 1,
  "lesson": 1
}
```

Пример ответа (код 201 Created):
```json
{
  "id": 1,
  "user_id": 123456789,
  "chapter": 1,
  "lesson": 1
}
```

#### Обновление прогресса по курсу Toncoin

```
PUT /api/v1/toncoin-courses/{id}/
```

Пример запроса:
```json
{
  "user_id": 123456789,
  "chapter": 2,
  "lesson": 1
}
```

Пример ответа:
```json
{
  "id": 1,
  "user_id": 123456789,
  "chapter": 2,
  "lesson": 1
}
```

#### Частичное обновление прогресса по курсу Toncoin

```
PATCH /api/v1/toncoin-courses/{id}/
```

Пример запроса:
```json
{
  "lesson": 2
}
```

Пример ответа:
```json
{
  "id": 1,
  "user_id": 123456789,
  "chapter": 2,
  "lesson": 2
}
```

#### Удаление записи о прогрессе по курсу Toncoin

```
DELETE /api/v1/toncoin-courses/{id}/
```

Успешный ответ: статус 204 No Content

### Курс NFT продаж

#### Получение списка прогресса по курсу NFT продаж

```
GET /api/v1/nft-sell-courses/
```

Структура запросов и ответов аналогична курсу Toncoin.

#### Получение прогресса конкретного пользователя по курсу NFT продаж

```
GET /api/v1/nft-sell-courses/{id}/
```

#### Создание записи о прогрессе по курсу NFT продаж

```
POST /api/v1/nft-sell-courses/
```

#### Обновление прогресса по курсу NFT продаж

```
PUT /api/v1/nft-sell-courses/{id}/
```

#### Частичное обновление прогресса по курсу NFT продаж

```
PATCH /api/v1/nft-sell-courses/{id}/
```

#### Удаление записи о прогрессе по курсу NFT продаж

```
DELETE /api/v1/nft-sell-courses/{id}/
```

### Курс P2P

#### Получение списка прогресса по курсу P2P

```
GET /api/v1/p2p-courses/
```

Структура запросов и ответов аналогична курсу Toncoin.

#### Получение прогресса конкретного пользователя по курсу P2P

```
GET /api/v1/p2p-courses/{id}/
```

#### Создание записи о прогрессе по курсу P2P

```
POST /api/v1/p2p-courses/
```

#### Обновление прогресса по курсу P2P

```
PUT /api/v1/p2p-courses/{id}/
```

#### Частичное обновление прогресса по курсу P2P

```
PATCH /api/v1/p2p-courses/{id}/
```

#### Удаление записи о прогрессе по курсу P2P

```
DELETE /api/v1/p2p-courses/{id}/
```

### Курс по безопасности (Scam)

#### Получение списка прогресса по курсу Scam

```
GET /api/v1/scam-courses/
```

Структура запросов и ответов аналогична курсу Toncoin.

#### Получение прогресса конкретного пользователя по курсу Scam

```
GET /api/v1/scam-courses/{id}/
```

#### Создание записи о прогрессе по курсу Scam

```
POST /api/v1/scam-courses/
```

#### Обновление прогресса по курсу Scam

```
PUT /api/v1/scam-courses/{id}/
```

#### Частичное обновление прогресса по курсу Scam

```
PATCH /api/v1/scam-courses/{id}/
```

#### Удаление записи о прогрессе по курсу Scam

```
DELETE /api/v1/scam-courses/{id}/
```
