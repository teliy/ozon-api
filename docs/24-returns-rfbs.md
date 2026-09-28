# Возвраты товаров rFBS

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 355. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Список заявок на возврат

`POST /v2/returns/rfbs/list`

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтр.
- **last_id** `integer <int32>` — Идентификатор последнего значения на странице — return_id . Оставьте это поле пустым при выполнении первого запроса.
- **limit** `integer <int32>` *обязательный* — Количество значений в ответе.

**Пример запроса:**

```json
{
  "filter": {
    "offer_id": "test-offer-123456",
    "posting_number": "789456123-0002-3",
    "group_state": [
      "New",
      "Approved"
    ],
    "created_at": {
      "from": "2026-02-01T00:00:00Z",
      "to": "2026-03-01T23:59:59Z"
    }
  },
  "last_id": 0,
  "limit": 1000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список заявок на возврат |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **returns** `object` — Данные о заявках.
  - **client_name** `string` — Имя покупателя.
  - **created_at** `string <date-time>` — Дата создания заявки.
  - **order_number** `string` — Номер заказа.
  - **posting_number** `string` — Номер отправления.
  - **product** `object` — Данные о товаре.
  - **return_id** `integer <int64>` — Идентификатор заявки на возврат.
  - **return_number** `string` — Номер заявки на возврат.
  - **state** `object` — Статусы заявки и возврата денег.

**Пример ответа (`200`):**

```json
{
  "returns": [
    {
      "return_id": 8000123456,
      "return_number": "RET-2026-00123 \"posting_number\": ",
      "order_number": "123456789",
      "created_at": "2026-02-15T10:30: \"product\": { \"sku\": 1000123456",
      "offer_id": "test-offer-12345 \"name\": \"Тестовый товар 1",
      "price": 2999,
      "currency_code": "RUB"
    },
    {
      "state": {
        "group_state": "New",
        "state": "ON_APPROVAL",
        "state_name": "На проверке"
      }
    }
  ]
}
```


---

## Информация о заявке на возврат

`POST /v2/returns/rfbs/get`

**Тело запроса** (`application/json`):
- **return_id** `integer <int64>` *обязательный* — Идентификатор заявки на возврат. Получите методом /v2/returns/rfbs/list.

**Пример запроса:**

```json
{
  "return_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о заявке |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **returns** `object` — Данные о заявке.
  - **available_actions** `Array of objects` — Данные о доступных действиях с заявкой.
  - **client_name** `string` — Имя покупателя.
  - **client_photo** `Array of strings` — Ссылки на фотографии товара.
  - **client_return_method_type** `object` — Данные о способе возврата.
  - **comment** `string` — Комментарий покупателя.
  - **created_at** `string <date-time>` — Дата создания заявки.
  - **order_number** `string` — Номер заказа.
  - **posting_number** `string` — Номер отправления.
  - **product** `object` — Данные о товаре.
  - **rejection_comment** `string` — Комментарий об отклонении заявки.
  - **rejection_reason** `Array of objects` — Данные о причине отклонения заявки.
  - **return_method_description** `string` — Способ возврата товара.
  - **return_number** `string` — Номер заявки на возврат.
  - **return_reason** `object` — Данные о причине возврата.
  - **ru_post_tracking_number** `string` — Трек-номер почтового отправления.
  - **state** `object` — Данные о статусе возврата.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "returns": {
    "available_actions": [
      {
        "action": {
          "id": 0,
          "name": "string"
        }
      }
    ],
    "client_name": "string",
    "client_photo": [
      "string"
    ],
    "client_return_method_type": {
      "id": 0,
      "name": "string"
    },
    "comment": "string",
    "created_at": "2025-09-04T13:49:20.3 \"order_number\": \"string",
    "posting_number": "string",
    "product": {
      "currency_code": "string",
      "name": "string",
      "offer_id": "string",
      "price": 0,
      "sku": 0
    },
    "rejection_comment": "string",
    "rejection_reason": [
      {
        "hint": "string",
        "id": 0,
        "is_comment_required": true,
        "name": "string"
      }
    ],
    "return_method_description": "string \"return_number\": \"string",
    "return_reason": {
      "id": 0,
      "is_defect": true,
      "name": "string"
    },
    "ru_post_tracking_number": "string",
    "state": {
      "state": "string",
      "state_name": "string"
    },
    "warehouse_id": 0
  }
}
```


---

## Передать доступные действия для rFBS возвратов

`POST /v1/returns/rfbs/action/set`

Метод для передачи действий для возврата rFBS.

**Тело запроса** (`application/json`):
- **comment** `string` — Комментарий продавца. Обязателен для id: -1 и id: -10 .
- **compensation_amount** `number <double>` — Сумма компенсации. Обязательна для id: 1020 .
- **id** `integer <int32>` — Идентификатор действия. Получите доступные действия returns.available_actions методом /v2/returns/rfbs/get.
- **rejection_reason_id** `integer <int32>` — Идентификатор причины отмены. Обязателен для id: -1 и id: -10 . Получите возможные причины отмены returns.rejection_reason методом /v2/returns/rfbs/get.
- **return_for_back_way** `number <double>` — Сумма, возмещаемая покупателю за пересылку товара. Отрицательные значения приравниваются к 0 .
- **return_id** `integer <int64>` *обязательный* — Идентификатор заявки на возврат.

**Пример запроса:**

```json
{
  "comment": "string",
  "compensation_amount": 0,
  "id": 0,
  "rejection_reason_id": 0,
  "return_for_back_way": 0,
  "return_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `default` | Ошибка |

**Пример ответа (`default`):**

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
