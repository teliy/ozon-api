# Работа с отзывами

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 424. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Оставить комментарий на отзыв

`POST /v1/review/comment/create`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

**Тело запроса** (`application/json`):
- **mark_review_as_processed** `boolean` — Обновление статуса у отзыва: true — статус изменится на Processed . false — статус не изменится.
- **parent_comment_id** `string` — Идентификатор родительского комментария, на который вы отвечаете.
- **review_id** `string` *обязательный* — Идентификатор отзыва.
- **text** `string` *обязательный* — Текст комментария.

**Пример запроса:**

```json
{
  "mark_review_as_processed": true,
  "parent_comment_id": "string",
  "review_id": "string",
  "text": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Комментарий создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **comment_id** `string` — Идентификатор комментария.

**Пример ответа (`200`):**

```json
{
  "comment_id": "string"
}
```


---

## Удалить комментарий на отзыв

`POST /v2/review/comment/delete`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

**Тело запроса** (`application/json`):
- **comment_id** `string` *обязательный* — Идентификатор комментария.
- **sku** `integer <int64>` *обязательный* — Идентификатор товара в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "comment_id": "string",
  "sku": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`400`):**

```json
{
  "code": 0,
  "details": [
    {
      "typeUrl": "string",
      "value": "string"
    }
  ],
  "message": "string"
}
```


---

## Удалить комментарий на отзыв Deprecated

`POST /v1/review/comment/delete`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

> **Примечание:** Метод устаревает. Переключитесь на /v2/review/comment/delete.

**Тело запроса** (`application/json`):
- **comment_id** `string` *обязательный* — Идентификатор комментария.

**Пример запроса:**

```json
{
  "comment_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Комментарий удалён |
| `default` | Ошибка |

**Пример ответа (`200`):**

```json
{}
```


---

## Получить список комментариев на отзыв

`POST /v1/review/comment/list`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro. Метод возвращает информацию по комментариям на отзывы, которые прошли модерацию.

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтры для поиска отзывов.
- **limit** `integer <int32>` *обязательный* — Ограничение значений в ответе. Минимум — 20. Максимум — 100.
- **offset** `integer <int32>` — Количество элементов, которое будет пропущено с начала списка в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **review_id** `string` *обязательный* — Идентификатор отзыва.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию, DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "review_id": "0000-0000",
  "sort_dir": "ASC",
  "filters": {
    "sku": 0,
    "published_from": "2026-03-10T14:08: ",
    "published_to": "2026-03-10T14:08:00"
  },
  "limit": 100,
  "offset": 123
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о комментариях на отзыв |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **comments** `Array of objects` — Информация о комментарии.
- **offset** `integer <int32>` — Количество элементов в выдаче.

**Пример ответа (`200`):**

```json
{
  "comments": [
    {
      "id": "1234-5678",
      "text": "comment text",
      "parent_comment_id": "3333-3333",
      "is_owner": true,
      "is_official": false,
      "is_published": true,
      "is_rejected": true,
      "likes_amount": 0,
      "dislikes_amount": 0,
      "deviation_reason": "string",
      "published_at": "2021-09-03T07:0"
    }
  ],
  "offset": 124
}
```


---

## Изменить статус отзывов

`POST /v2/review/change-status`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

**Тело запроса** (`application/json`):
- **review_ids** `Array of strings` — Список идентификаторов отзывов.
- **status** `string` — Новый статус отзыва: NEW — новый; VIEWED — просмотренный; PROCESSED — обработанный.. Enum: `"NEW"`, `"VIEWED"`, `"PROCESSED"`.

**Пример запроса:**

```json
{
  "status": "NEW",
  "review_ids": [
    "01920411-f6af-7e58-a8a4-63c5cfc007d"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`400`):**

```json
{
  "code": 0,
  "details": [
    {
      "typeUrl": "string",
      "value": "string"
    }
  ],
  "message": "string"
}
```


---

## Изменить статус отзывов Deprecated

`POST /v1/review/change-status`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

> **Примечание:** Метод устаревает. Переключитесь на /v2/review/change-status.

**Тело запроса** (`application/json`):
- **review_ids** `Array of strings` *обязательный* — Массив с идентификаторами отзывов от 1 до 100.
- **status** `string` *обязательный* — Статус отзыва: PROCESSED — обработанный, UNPROCESSED — необработанный.

**Пример запроса:**

```json
{
  "review_ids": [
    "string"
  ],
  "status": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус изменён |
| `default` | Ошибка |

**Пример ответа (`200`):**

```json
{}
```


---

## Получить количество отзывов по статусам

`POST /v2/review/count`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество отзывов по статусам |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **new** `integer <int32>` — Количество новых отзывов.
- **processed** `integer <int32>` — Количество обработанных отзывов.
- **total** `integer <int32>` — Количество всех отзывов.
- **viewed** `integer <int32>` — Количество просмотренных отзывов.

**Пример ответа (`200`):**

```json
{
  "total": 3,
  "processed": 1,
  "new": 1,
  "viewed": 1
}
```


---

## Количество отзывов по статусам Deprecated

`POST /v1/review/count`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

> **Примечание:** Метод устаревает. Переключитесь на /v2/review/count.

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество обработанных и необработанных отзывов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **processed** `integer <int32>` — Количество обработанных отзывов.
- **total** `integer <int32>` — Количество всех отзывов.
- **unprocessed** `integer <int32>` — Количество необработанных отзывов.

**Пример ответа (`200`):**

```json
{
  "processed": 0,
  "total": 0,
  "unprocessed": 0
}
```


---

## Получить информацию по отзыву

`POST /v2/review/info`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

**Тело запроса** (`application/json`):
- **review_id** `string` *обязательный* — Идентификатор отзыва.

**Пример запроса:**

```json
{
  "review_id": "1"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отзыве |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **comments_amount** `integer <int32>` — Количество комментариев к отзыву.
- **dislikes_amount** `integer <int32>` — Количество дизлайков на отзыве.
- **id** `string` — Идентификатор отзыва.
- **is_rating_participant** `boolean` — true , если отзыв участвует в подсчёте рейтинга.
- **likes_amount** `integer <int32>` — Количество лайков на отзыве.
- **order_status** `string` — Статус заказа, на который покупатель оставил отзыв: DELIVERED — доставлен; CANCELLED — отменён.. Enum: `"DELIVERED"`, `"CANCELLED"`.
- **photos** `Array of objects` — Информация об изображениях.
- **photos_amount** `integer <int32>` — Количество изображений у отзыва.
- **published_at** `string <date-time>` — Дата публикации отзыва.
- **rating** `integer <int32>` — Оценка отзыва.
- **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
- **status** `string` — Статус отзыва: NEW — новый; VIEWED — просмотренный; PROCESSED — обработанный.. Enum: `"NEW"`, `"VIEWED"`, `"PROCESSED"`.
- **text** `string` — Текст отзыва.
- **videos** `Array of objects` — Информация о видео.
- **videos_amount** `integer <int32>` — Количество видео у отзыва.

**Пример ответа (`200`):**

```json
{
  "comments_amount": 0,
  "dislikes_amount": 0,
  "id": "string",
  "is_rating_participant": true,
  "likes_amount": 0,
  "order_status": "DELIVERED",
  "photos": [
    {
      "height": 0,
      "url": "string",
      "width": 0
    }
  ],
  "photos_amount": 0,
  "published_at": "2019-08-24T14:15:22Z",
  "rating": 0,
  "sku": 0,
  "status": "NEW",
  "text": "string",
  "videos": [
    {
      "height": 0,
      "preview_url": "string",
      "short_video_preview_url": "stri \"url\": \"string",
      "width": 0
    }
  ],
  "videos_amount": 0
}
```


---

## Получить информацию об отзыве Deprecated

`POST /v1/review/info`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

> **Примечание:** Метод устаревает. Переключитесь на /v2/review/info.

**Тело запроса** (`application/json`):
- **review_id** `string` *обязательный* — Идентификатор отзыва.

**Пример запроса:**

```json
{
  "review_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отзыве |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **comments_amount** `integer <int32>` — Количество комментариев к отзыву.
- **dislikes_amount** `integer <int32>` — Количество дизлайков на отзыве.
- **id** `string` — Идентификатор отзыва.
- **is_rating_participant** `boolean` — true , если отзыв участвует в подсчёте рейтинга.
- **likes_amount** `integer <int32>` — Количество лайков на отзыве.
- **order_status** `string` — Статус заказа, на который покупатель оставил отзыв: DELIVERED — доставлен, CANCELLED — отменён.
- **photos** `Array of objects` — Информация об изображении.
- **photos_amount** `integer <int32>` — Количество изображений у отзыва.
- **published_at** `string <date-time>` — Дата публикации отзыва.
- **rating** `integer <int32>` — Оценка отзыва.
- **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
- **status** `string` — Статус отзыва: UNPROCESSED — не обработан, PROCESSED — обработан.
- **text** `string` — Текст отзыва.
- **videos** `Array of objects` — Информация о видео.
- **videos_amount** `integer <int32>` — Количество видео у отзыва.

**Пример ответа (`200`):**

```json
{
  "comments_amount": 0,
  "dislikes_amount": 0,
  "id": "string",
  "is_rating_participant": true,
  "likes_amount": 0,
  "order_status": "string",
  "photos": [
    {
      "height": 0,
      "url": "string",
      "width": 0
    }
  ],
  "photos_amount": 0,
  "published_at": "2019-08-24T14:15:22Z",
  "rating": 0,
  "sku": 0,
  "status": "string",
  "text": "string",
  "videos": [
    {
      "height": 0,
      "preview_url": "string",
      "short_video_preview_url": "stri \"url\": \"string",
      "width": 0
    }
  ],
  "videos_amount": 0
}
```


---

## Получить список отзывов

`POST /v2/review/list`

Доступно для продавцов с подпиской Управление отзывами или Premium Pro.

**Тело запроса** (`application/json`):
- **filters** `object` — Фильтры для поиска отзывов.
- **last_id** `string` — Идентификатор последнего отзыва в ответе.
- **limit** `integer <int32>` *обязательный* — Количество отзывов в ответе.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filters": {
    "sku": [
      0
    ],
    "order_status": "DELIVERED",
    "status": "NEW",
    "published_from": "2026-03-10T14:08: ",
    "published_to": "2026-03-10T14:08:00"
  },
  "last_id": "string",
  "limit": 0,
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список отзывов |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернули не все отзывы.
- **last_id** `string` — Идентификатор последнего отзыва на странице.
- **reviews** `Array of objects` — Список отзывов.

**Пример ответа (`200`):**

```json
{
  "reviews": [
    {
      "id": "017c0d1c-66d3-b838-3d29-c \"sku\": \"148591503",
      "text": "Не лучший товар",
      "published_at": "2024-10-10T07:2 \"rating\": 2",
      "status": "NEW",
      "comments_amount": 0,
      "photos_amount": 0,
      "videos_amount": 0,
      "order_status": "DELIVERED",
      "is_rating_participant": true
    }
  ],
  "has_next": true,
  "last_id": "017c0d53-a7c8-81ef-53de-7d32"
}
```


---

## Получить список отзывов Deprecated

`POST /v1/review/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Доступно для продавцов с подпиской Управление отзывами или Premium Pro. Метод не возвращает параметры «Достоинства» и «Недостатки», если они есть в отзывах на товар. Эти параметры устарели, в новых отзывах их нет.

> **Примечание:** Метод устаревает. Переключитесь на /v2/review/list.

**Тело запроса** (`application/json`):
- **last_id** `string` — Идентификатор последнего отзыва на странице.
- **limit** `integer <int32>` *обязательный* — Количество отзывов в ответе. Минимум — 20, максимум — 100.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию, DESC — по убыванию.
- **status** `string` — Статусы отзывов: ALL — все, UNPROCESSED — необработанные, PROCESSED — обработанные.

**Пример запроса:**

```json
{
  "last_id": "",
  "limit": 100,
  "sort_dir": "ASC",
  "status": "ALL"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список отзывов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернули не все отзывы.
- **last_id** `string` — Идентификатор последнего отзыва на странице.
- **reviews** `Array of objects` — Информация об отзыве.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "last_id": "string",
  "reviews": [
    {
      "comments_amount": 0,
      "id": "string",
      "is_rating_participant": true,
      "order_status": "string",
      "photos_amount": 0,
      "published_at": "2019-08-24T14:1 \"rating\": 0",
      "sku": 0,
      "status": "string",
      "text": "string",
      "videos_amount": 0
    }
  ]
}
```


---
