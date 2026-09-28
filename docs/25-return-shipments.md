# Возвратные отгрузки

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 359. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Количество возвратов FBS

`POST /v1/returns/company/fbs/info`

Метод для получения информации о возвратах FBS и их количестве.

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтры.
- **pagination** `object` *обязательный* — Разделение ответа метода.

**Пример запроса:**

```json
{
  "filter": {
    "place_id": 0
  },
  "pagination": {
    "last_id": 0,
    "limit": 500
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество возвратов FBS |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **drop_off_points** `Array of objects` — Информация о drop-off пунктах.
- **has_next** `boolean` — Признак, есть ли ещё пункты, где продавца ожидают возвраты.

**Пример ответа (`200`):**

```json
{
  "drop_off_points": [
    {
      "address": "string",
      "box_count": 0,
      "id": 0,
      "name": "string",
      "pass_info": {
        "count": 0,
        "is_required": true
      },
      "place_id": 0,
      "returns_count": 0,
      "utc_offset": "string",
      "warehouses_ids": [
        "string"
      ]
    }
  ],
  "has_next": true
}
```


---

## Проверить возможность получения возвратных отгрузок по штрихкоду

`POST /v1/return/giveout/is-enabled`

Если у вас есть доступ, в параметре enabled будет указано значение

```
true .
```

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат проверки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **enabled** `boolean` — true , если вы можете получить возвратную отгрузку по штрихкоду.

**Пример ответа (`200`):**

```json
{
  "enabled": true
}
```


---

## Список возвратных отгрузок

`POST /v1/return/giveout/list`

Метод для получения списка активных возвратов. Возвратная отгрузка становится активной после сканирования штрихкода. После сканирования штрихкода второй раз активная выдача переходит в статус неактивной.

**Тело запроса** (`application/json`):
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.
- **limit** `integer <int64>` *обязательный* — Количество элементов в ответе.

**Пример запроса:**

```json
{
  "last_id": 0,
  "limit": 500
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список возвратных отгрузок |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **giveouts** `Array of objects` — Идентификатор отгрузки.
  - **approved_articles_count** `integer <int32>` — Количество товаров в отгрузке.
  - **created_at** `string <date-time>` — Дата и время.
  - **giveout_id** `integer <int64>` — Идентификатор отгрузки.
  - **giveout_status** `string` — Статусы возвратной отгрузки: GIVEOUT_STATUS_UNSPECIFIED — не определён, напишите в поддержку. GIVEOUT_STATUS_CREATED — создана. GIVEOUT_STATUS_APPROVED — одобрена. GIVEOUT_STATUS_COMPLETED — завершена. GIVEOUT_STATUS_CANCELLED — отменена.
  - **total_articles_count** `integer <int32>` — Общее количество товаров, которые нужно забрать со склада.
  - **warehouse_address** `string` — Адрес склада.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.
  - **warehouse_name** `string` — Название склада.

**Пример ответа (`200`):**

```json
{
  "giveouts": [
    {
      "approved_articles_count": 0,
      "created_at": "2019-08-24T14:15: \"giveout_id\": 0",
      "giveout_status": "string",
      "total_articles_count": 0,
      "warehouse_address": "string",
      "warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---

## Информация о возвратной отгрузке

`POST /v1/return/giveout/info`

Метод для получения информации о возвратной отгрузке. В параметр giveout_id передаётся значение, полученное в методе

**Тело запроса** (`application/json`):
- **giveout_id** `integer <int64>` *обязательный* — Идентификатор отгрузки.

**Пример запроса:**

```json
{
  "giveout_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о возвратной отгрузке |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **articles** `Array of objects` — Артикулы товаров.
- **giveout_id** `integer <int64>` — Идентификатор отгрузки.
- **giveout_status** `string` — Статусы возвратной отгрузки: GIVEOUT_STATUS_UNSPECIFIED — не определён, напишите в поддержку. GIVEOUT_STATUS_CREATED — создана. GIVEOUT_STATUS_APPROVED — одобрена. GIVEOUT_STATUS_COMPLETED — завершена. GIVEOUT_STATUS_CANCELLED — отменена.
- **warehouse_address** `string` — Адрес склада.
- **warehouse_name** `string` — Название склада.

**Пример ответа (`200`):**

```json
{
  "articles": [
    {
      "approved": true,
      "delivery_schema": "string",
      "name": "string",
      "seller_id": 0
    }
  ],
  "giveout_id": 0,
  "giveout_status": "string",
  "warehouse_address": "string",
  "warehouse_name": "string"
}
```


---

## Значение штрихкода для возвратных отгрузок

`POST /v1/return/giveout/barcode`

Используйте этот метод, чтобы получить штрихкод из ответа методов

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Значение штрихкода |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **barcode** `string` — Значение штрихкода в текстовом виде.

**Пример ответа (`200`):**

```json
{
  "barcode": "string"
}
```


---

## Штрихкод для получения возвратной отгрузки в формате PDF

`POST /v1/return/giveout/get-pdf`

Возвращает PDF-файл со штрихкодом. Метод работает только для схемы FBS.

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Штрихкод для возвратной отгрузки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **file_content** `string` — PDF-файл со штрихкодом в кодировке Base64.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "application/pdf",
  "file_name": "string",
  "file_content": "string"
}
```


---

## Штрихкод для получения возвратной отгрузки в формате PNG

`POST /v1/return/giveout/get-png`

Возвращает PNG-файл со штрихкодом.

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Штрихкод для возвратной отгрузки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **file_content** `string` — PNG-файл со штрихкодом в кодировке Base64.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "image/png",
  "file_name": "string",
  "file_content": "string"
}
```


---

## Сгенерировать новый штрихкод

`POST /v1/return/giveout/barcode-reset`

Используйте метод, если ваш штрихкод попал в посторонние руки. Метод возвращает PNG-файл с новым штрихкодом. После использования метода вы не сможете получить возвратную отгрузку по старым штрихкодам. Чтобы получить новый штрихкод в PDF- формате, запросите его методом /v1/return/giveout/get-pdf.

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Новый штрихкод |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **file_content** `string` — Изображение со штрихкодом в бинарном виде.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "image/png",
  "file_name": "string",
  "file_content": "string"
}
```


---
