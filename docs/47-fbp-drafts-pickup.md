# Работа с FBP-черновиками с доставкой pick-up

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 552. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Создать черновик заявки на pick-up поставку

## Создать черновик заявки на pick-up поставку

`POST /v1/fbp/draft/pick-up/create`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **bundle_id** `string` *обязательный* — Идентификатор состава поставки.
- **delivery_details** `object` *обязательный* — Детали доставки.
- **package_units_count** `integer <int32>` *обязательный* — Количество грузомест.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "bundle_id": "string",
  "delivery_details": {
    "address": "string",
    "comment": "string",
    "date": "2019-08-24T14:15:22Z",
    "sender_name": "string",
    "sender_phone": "string"
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
- **draft_id** `integer <int64>` — Идентификатор черновика заявки на поставку.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.
- **supply_id** `string` — Идентификатор поставки.

**Пример ответа (`200`):**

```json
{
  "draft_id": 0,
  "row_version": 0,
  "supply_id": "string"
}
```


---

## Отменить черновик заявки на pick-up поставку

`POST /v1/fbp/draft/pick-up/delete`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Черновик отменён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cancellation_state** `object` — Статус отмены.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "cancellation_state": {
    "cancellation_error": {
      "error_code": "CODE_UNSPECIFIED",
      "message": "string"
    },
    "cancellation_status": "STATUS_UNSPE"
  },
  "row_version": 0
}
```


---

## Изменить черновик заявки на pick-up поставку

`POST /v1/fbp/draft/pick-up/dlv/edit`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **pickup_details** `object` *обязательный* — Детали доставки.
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "pickup_details": {
    "address": "string",
    "comment": "string",
    "date": "2019-08-24T14:15:22Z",
    "sender_name": "string",
    "sender_phone": "string"
  },
  "row_version": 0,
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация отредактирована |
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

## Провалидировать список товаров для pick-up поставки

`POST /v1/fbp/draft/pick-up/product/validate`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **skus** `Array of objects` *обязательный* — Список идентификаторов товаров — SKU.
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
| `200` | Список провалидирован |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **approved_items** `Array of objects` — Подтверждённые товары.
- **bundle_generated** `boolean` — true , если проверенный список товаров создан.
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

## Перевести черновик в действующую поставку

`POST /v1/fbp/draft/pick-up/registrate`

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
