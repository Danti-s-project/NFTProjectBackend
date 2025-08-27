# API документация сервиса NFTs

## Оглавление

- [Введение](#введение)
- [Базовая информация](#базовая-информация)
  - [Пагинация](#пагинация)
  - [Форматы запросов и ответов](#форматы-запросов-и-ответов)
- [Коллекции NFT](#коллекции-nft)
- [Модели NFT](#модели-nft)
- [Бекдропы NFT](#бекдропы-nft)
- [Символы NFT](#символы-nft)
- [NFT объекты](#nft-объекты)

## Введение

API сервиса NFTs предоставляет интерфейс для работы с NFT и их компонентами, такими как коллекции, модели, бекдропы и символы.

## Базовая информация

### Пагинация

Все эндпоинты, возвращающие списки, поддерживают пагинацию с использованием параметров `limit` и `offset`:

- `limit` - количество элементов на странице (по умолчанию: 10, максимум: 100)
- `offset` - смещение от начала списка

Пример запроса с пагинацией:
```
GET /api/nfts/collections/?limit=5&offset=10
```

Пример ответа с пагинацией:
```json
{
  "count": 42,
  "next": "http://example.com/api/nfts/collections/?limit=5&offset=15",
  "previous": "http://example.com/api/nfts/collections/?limit=5&offset=5",
  "results": [
    // список объектов
  ]
}
```

### Форматы запросов и ответов

API использует формат JSON для запросов и ответов. При отправке POST, PUT или PATCH запросов, необходимо установить заголовок `Content-Type: application/json`.

## Коллекции NFT

### Получение списка коллекций

```
GET /api/nfts/collections/
```

Параметры запроса:
- `limit` - количество элементов на странице (опционально)
- `offset` - смещение от начала списка (опционально)
- `ordering` - поле для сортировки (по умолчанию: 'name')

Пример ответа:
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "AlphaNFT",
      "alias": "alpha",
      "indexed": 1,
      "quantity": 100
    },
    {
      "name": "BetaNFT",
      "alias": "beta",
      "indexed": 2,
      "quantity": 50
    },
    {
      "name": "GammaNFT",
      "alias": null,
      "indexed": 0,
      "quantity": 25
    }
  ]
}
```

### Получение информации о конкретной коллекции

```
GET /api/nfts/collections/{name}/
```

Пример ответа:
```json
{
  "name": "AlphaNFT",
  "alias": "alpha",
  "indexed": 1,
  "quantity": 100
}
```

### Создание новой коллекции

```
POST /api/nfts/collections/
```

Пример запроса:
```json
{
  "name": "DeltaNFT",
  "alias": "delta",
  "indexed": 3,
  "quantity": 75
}
```

Пример ответа (код 201 Created):
```json
{
  "name": "DeltaNFT",
  "alias": "delta",
  "indexed": 3,
  "quantity": 75
}
```

### Обновление коллекции

```
PUT /api/nfts/collections/{name}/
```

Пример запроса:
```json
{
  "name": "DeltaNFT",
  "alias": "delta-new",
  "indexed": 3,
  "quantity": 80
}
```

Пример ответа:
```json
{
  "name": "DeltaNFT",
  "alias": "delta-new",
  "indexed": 3,
  "quantity": 80
}
```

### Частичное обновление коллекции

```
PATCH /api/nfts/collections/{name}/
```

Пример запроса:
```json
{
  "quantity": 85
}
```

Пример ответа:
```json
{
  "name": "DeltaNFT",
  "alias": "delta-new",
  "indexed": 3,
  "quantity": 85
}
```

### Удаление коллекции

```
DELETE /api/nfts/collections/{name}/
```

Успешный ответ: статус 204 No Content

## Модели NFT

### Получение списка моделей

```
GET /api/nfts/models/
```

Параметры запроса:
- `limit` - количество элементов на странице (опционально)
- `offset` - смещение от начала списка (опционально)
- `ordering` - поле для сортировки (по умолчанию: 'name')

Пример ответа:
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "Classic"
    },
    {
      "name": "Modern"
    },
    {
      "name": "Vintage"
    }
  ]
}
```

### Получение информации о конкретной модели

```
GET /api/nfts/models/{name}/
```

Пример ответа:
```json
{
  "name": "Classic"
}
```

### Создание новой модели

```
POST /api/nfts/models/
```

Пример запроса:
```json
{
  "name": "Futuristic"
}
```

Пример ответа (код 201 Created):
```json
{
  "name": "Futuristic"
}
```

### Обновление модели

```
PUT /api/nfts/models/{name}/
```

Пример запроса:
```json
{
  "name": "Futuristic-V2"
}
```

Пример ответа:
```json
{
  "name": "Futuristic-V2"
}
```

### Удаление модели

```
DELETE /api/nfts/models/{name}/
```

Успешный ответ: статус 204 No Content

## Бекдропы NFT

### Получение списка бекдропов

```
GET /api/nfts/backdrops/
```

Параметры запроса:
- `limit` - количество элементов на странице (опционально)
- `offset` - смещение от начала списка (опционально)
- `ordering` - поле для сортировки (по умолчанию: 'name')

Пример ответа:
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "Desert"
    },
    {
      "name": "Forest"
    },
    {
      "name": "Ocean"
    }
  ]
}
```

### Получение информации о конкретном бекдропе

```
GET /api/nfts/backdrops/{name}/
```

Пример ответа:
```json
{
  "name": "Desert"
}
```

### Создание нового бекдропа

```
POST /api/nfts/backdrops/
```

Пример запроса:
```json
{
  "name": "Mountains"
}
```

Пример ответа (код 201 Created):
```json
{
  "name": "Mountains"
}
```

### Обновление бекдропа

```
PUT /api/nfts/backdrops/{name}/
```

Пример запроса:
```json
{
  "name": "High Mountains"
}
```

Пример ответа:
```json
{
  "name": "High Mountains"
}
```

### Удаление бекдропа

```
DELETE /api/nfts/backdrops/{name}/
```

Успешный ответ: статус 204 No Content

## Символы NFT

### Получение списка символов

```
GET /api/nfts/symbols/
```

Параметры запроса:
- `limit` - количество элементов на странице (опционально)
- `offset` - смещение от начала списка (опционально)
- `ordering` - поле для сортировки (по умолчанию: 'name')

Пример ответа:
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "BTC"
    },
    {
      "name": "ETH"
    },
    {
      "name": "TON"
    }
  ]
}
```

### Получение информации о конкретном символе

```
GET /api/nfts/symbols/{name}/
```

Пример ответа:
```json
{
  "name": "BTC"
}
```

### Создание нового символа

```
POST /api/nfts/symbols/
```

Пример запроса:
```json
{
  "name": "SOL"
}
```

Пример ответа (код 201 Created):
```json
{
  "name": "SOL"
}
```

### Обновление символа

```
PUT /api/nfts/symbols/{name}/
```

Пример запроса:
```json
{
  "name": "SOLANA"
}
```

Пример ответа:
```json
{
  "name": "SOLANA"
}
```

### Удаление символа

```
DELETE /api/nfts/symbols/{name}/
```

Успешный ответ: статус 204 No Content

## NFT объекты

### Получение списка NFT

```
GET /api/nfts/nfts/
```

Параметры запроса:
- `limit` - количество элементов на странице (опционально)
- `offset` - смещение от начала списка (опционально)
- `collection` - фильтр по коллекции (опционально)
- `nft_model` - фильтр по модели (опционально)
- `backdrop` - фильтр по бекдропу (опционально)
- `symbol` - фильтр по символу (опционально)
- `quantity` - фильтр по количеству (опционально)

Пример ответа:
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "collection": "AlphaNFT",
      "owner": "user1",
      "nft_model": "Classic",
      "backdrop": "Desert",
      "symbol": "BTC",
      "issued": 1234
    },
    {
      "id": 2,
      "collection": "BetaNFT",
      "owner": "user2",
      "nft_model": "Modern",
      "backdrop": "Ocean",
      "symbol": "ETH",
      "issued": 5678
    }
  ]
}
```

### Получение информации о конкретном NFT

```
GET /api/nfts/nfts/{id}/
```

Пример ответа:
```json
{
  "id": 1,
  "collection": "AlphaNFT",
  "owner": "user1",
  "nft_model": "Classic",
  "backdrop": "Desert",
  "symbol": "BTC",
  "issued": 1234
}
```

### Создание нового NFT

```
POST /api/nfts/nfts/
```

Пример запроса:
```json
{
  "collection": "GammaNFT",
  "owner": "user3",
  "nft_model": "Vintage",
  "backdrop": "Forest",
  "symbol": "TON",
  "issued": 9012
}
```

Пример ответа (код 201 Created):
```json
{
  "id": 3,
  "collection": "GammaNFT",
  "owner": "user3",
  "nft_model": "Vintage",
  "backdrop": "Forest",
  "symbol": "TON",
  "issued": 9012
}
```

### Обновление NFT

```
PUT /api/nfts/nfts/{id}/
```

Пример запроса:
```json
{
  "collection": "GammaNFT",
  "owner": "user4",
  "nft_model": "Vintage",
  "backdrop": "Forest",
  "symbol": "TON",
  "issued": 9012
}
```

Пример ответа:
```json
{
  "id": 3,
  "collection": "GammaNFT",
  "owner": "user4",
  "nft_model": "Vintage",
  "backdrop": "Forest",
  "symbol": "TON",
  "issued": 9012
}
```

### Частичное обновление NFT

```
PATCH /api/nfts/nfts/{id}/
```

Пример запроса:
```json
{
  "owner": "user5"
}
```

Пример ответа:
```json
{
  "id": 3,
  "collection": "GammaNFT",
  "owner": "user5",
  "nft_model": "Vintage",
  "backdrop": "Forest",
  "symbol": "TON",
  "issued": 9012
}
```

### Удаление NFT

```
DELETE /api/nfts/nfts/{id}/
```

Успешный ответ: статус 204 No Content
