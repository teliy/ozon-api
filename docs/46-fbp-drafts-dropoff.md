# Работа с FBP-черновиками c доставкой drop-off

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 545. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Создать черновик для доставки в drop- off пункт

## Создать черновик для доставки в drop- off пункт

`POST /v1/fbp/draft/drop-off/create`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **bundle_id** `string` *обязательный* — Идентификатор провалидированного списка товаров.
- **delivery_details** `object` *обязательный* — Детали доставки.
- **package_units_count** `integer <int32>` *обязательный* — Количество грузомест.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада продавца.

**Пример запроса:**

```json
{
  "bundle_id": "string",
  "delivery_details": {
    "drop_off_date": "string",
    "drop_off_point_id": 0,
    "drop_off_province_uuid": "string"
  },
  "package_units_count": 0,
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Черновик создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **draft_id** `integer <int64>` — Идентификатор черновика.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.
- **supply_id** `string` — Идентификатор заявки на поставку.

**Пример ответа (`200`):**

```json
{
  "draft_id": 0,
  "row_version": 0,
  "supply_id": "string"
}
```


---

## Удалить черновик для доставки в drop- off пункт

`POST /v1/fbp/draft/drop-off/delete`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.

**Пример запроса:**

```json
{
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Черновик удалён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cancellation_state** `object` — Статус отмены.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "cancellation_state": {
    "cancellation_error": {
      "error_code": "NO_RESPONSE_FROM_ \"message\": \"string\""
    },
    "cancellation_status": "CONFIRMATION"
  },
  "row_version": 0
}
```


---

## Отредактировать детали доставки для drop-off черновика

`POST /v1/fbp/draft/drop-off/dlv/edit`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **drop_off_date** `string` *обязательный* — Дата доставки.
- **drop_off_point_id** `integer <int64>` *обязательный* — Идентификатор drop-off пункта.
- **drop_off_province_uuid** `string` *обязательный* — Уникальный идентификатор провинции.
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.

**Пример запроса:**

```json
{
  "drop_off_date": "string",
  "drop_off_point_id": 0,
  "drop_off_province_uuid": "string",
  "row_version": 0,
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "row_version": 0
}
```


---

## Перевести черновик в действующую поставку

`POST /v1/fbp/draft/drop-off/registrate`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.

**Пример запроса:**

```json
{
  "row_version": 0,
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error** `object` — Ошибка.
- **is_error** `boolean` — true , если есть ошибка.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "error": {
    "bundle_errors": [
      {
        "errors": [
          "BUNDLE_ITEM_ERROR_UNSPEC ], ",
          "sku",
          0
        ],
        "order_error": "ORDER_ERROR_TYPE_UNS"
      },
      {
        "is_error": true,
        "row_version": 0
      }
    ]
  }
}
```


---

## Получить список провинций

`POST /v1/fbp/draft/drop-off/province/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список провинций |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **provinces** `Array of objects` — Список провинций.
  - **name** `string` — Название провинции.
  - **points_count** `integer <int32>` — Количество пунктов на карте.
  - **province_uuid** `string` — Уникальный идентификатор провинции.

**Пример ответа (`200`):**

```json
{
  "provinces": [
    {
      "name": "string",
      "points_count": 0,
      "province_uuid": "string"
    }
  ]
}
```


---

## Получить список drop-off пунктов в провинции

`POST /v1/fbp/draft/drop-off/point/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **next_page_number** `integer <int32>` — Следующий номер страницы.
- **page_size** `integer <int32>` *обязательный* — Количество элементов на странице.
- **province_uuid** `string` *обязательный* — Уникальный идентификатор провинции.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "next_page_number": 0,
  "page_size": 0,
  "province_uuid": "string",
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список drop-off пунктов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **drop_off_points** `Array of objects` — Список drop-off пунктов.
  - **city** `string` — Город.
  - **drop_off_point_id** `integer <int64>` — Идентификатор drop-off пункта.
  - **nearest_drop_off_date** `string <date-time>` — Ближайшая дата отгрузки.
  - **point_address** `string` — Адрес drop-off пункта.
  - **province_uuid** `string` — Уникальный идентификатор провинции.

**Пример ответа (`200`):**

```json
{
  "drop_off_points": [
    {
      "city": "string",
      "drop_off_point_id": 0,
      "nearest_drop_off_date": "2019-0 \"point_address\": \"string",
      "province_uuid": "string"
    }
  ]
}
```


---

## Получить расписание работы drop-off пункта

`POST /v1/fbp/draft/drop-off/point/timetable`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **drop_off_point_id** `integer <int64>` *обязательный* — Идентификатор drop-off пункта.
- **province_uuid** `string` *обязательный* — Уникальный идентификатор провинции.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "drop_off_point_id": 0,
  "province_uuid": "string",
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Расписание работы |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **calendar** `Array of objects` — Расписание работы drop-off пункта.
  - **calendar_item** `object` — Расписание работы.
  - **day_of_week** `string` — Дни недели: DAY_OF_WEEK_UNSPECIFIED — не определён, MONDAY — понедельник, TUESDAY — вторник, WEDNESDAY — среда, THURSDAY — четверг, FRIDAY — пятница, SATURDAY — суббота, SUNDAY — воскресенье.. Enum: `"DAY_OF_WEEK_UNSPECIFIED"`, `"MONDAY"`, `"TUESDAY"`, `"WEDNESDAY"`, `"THURSDAY"`, `"FRIDAY"`, `"SATURDAY"`, `"SUNDAY"`.

**Пример ответа (`200`):**

```json
{
  "calendar": [
    {
      "calendar_item": {
        "break_hours": {
          "timeslot_end": "string",
          "timeslot_start": "string"
        },
        "is_holiday": true,
        "opening_hours": {
          "timeslot_end": "string",
          "timeslot_start": "string"
        }
      },
      "day_of_week": "DAY_OF_WEEK_UNSP }"
    }
  ]
}
```


---

## Проверить список товаров, которые склад партнёра может принять

`POST /v1/fbp/draft/drop-off/product/validate`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **skus** `Array of objects` *обязательный* — Идентификаторы товаров в системе Ozon — SKU.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "skus": [
    {
      "count": 0,
      "sku": 0
    }
  ],
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат проверки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **approved_items** `Array of objects` — Принятые товары.
- **bundle_generated** `boolean` — true , если создан товарный состав.
- **bundle_id** `string` — Идентификатор провалидированного списка товаров.
- **rejected_items** `Array of objects` — Отклонённые товары.

**Пример ответа (`200`):**

```json
{
  "approved_items": [
    {
      "barcode": "string",
      "icon_name": "string",
      "name": "string",
      "offer_id": "string",
      "quantity": 0,
      "sku": 0,
      "volume": 0
    }
  ],
  "bundle_generated": true,
  "bundle_id": "string",
  "rejected_items": [
    {
      "barcode": "string",
      "icon_name": "string",
      "name": "string",
      "offer_id": "string",
      "quantity": 0,
      "rejection_reasons": [
        "BUNDLE_ITEM_ERROR_UNSPECIFIE ], ",
        "sku",
        0,
        {
          "volume": 0
        }
      ]
    }
  ]
}
```


---
