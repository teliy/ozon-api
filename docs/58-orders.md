# Заказы

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 620. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Отменить заказ

`POST /v1/order/cancel`

Отменяет заказ со всеми отправлениями. Используйте идентификатор причины отмены reasons.id из метода /v1/cancel-reason/list-by-order.

**Тело запроса** (`application/json`):
- **order_number** `string` *обязательный* — Номер заказа.
- **reason_id** `integer <int32>` *обязательный* — Идентификатор причины отмены заказа.
- **reason_message** `string` — Причина отмены заказа.

**Пример запроса:**

```json
{
  "order_number": "string",
  "reason_id": 0,
  "reason_message": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заказ отменён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **message** `string` — Статус обработки отмены.

**Пример ответа (`200`):**

```json
{
  "message": "string"
}
```


---

## Проверить возможность отмены заказа

`POST /v1/order/cancel/check`

Возвращает возможность отмены заказа для покупателя.

**Тело запроса** (`application/json`):
- **order_number** `string` *обязательный* — Номер заказа.

**Пример запроса:**

```json
{
  "order_number": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат проверки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cancellable** `boolean` — true , если заказ можно отменить.
- **order_number** `string` — Номер заказа.
- **posting_groups** `Array of objects` — Группы отправлений.
- **postings** `Array of objects` — Информация о возможности отмены отправлений.

**Пример ответа (`200`):**

```json
{
  "cancellable": true,
  "order_number": "string",
  "posting_groups": [
    {
      "posting_numbers": [
        "string"
      ]
    }
  ],
  "postings": [
    {
      "cancellable": true,
      "posting_number": "string",
      "why_not_cancellable": "string"
    }
  ]
}
```


---

## Получить статус отмены заказа

`POST /v1/order/cancel/status`

**Тело запроса** (`application/json`):
- **order_number** `string` *обязательный* — Номер заказа.

**Пример запроса:**

```json
{
  "order_number": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус отмены заказа |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **order_number** `string` — Номер заказа.
- **posting_number** `Array of strings` — Список отправлений в заказе.
- **state** `string` — Статус отмены заказа: Подтверждена , На подтверждении , Отклонена , Ожидает обработки .

**Пример ответа (`200`):**

```json
{
  "order_number": "string",
  "posting_number": [
    "string"
  ],
  "state": "string"
}
```


---

## Создать заказ

`POST /v2/order/create`

Создаёт заказ для покупателя и получателя в системе Ozon. Передайте вариант доставки из ответа метода /v2/delivery/checkout. В ответе могут быть не все отправления. Получите список всех отправлений по номеру заказа order_number методом: Значение параметра delivery_schema должно совпадать с тем, что вы передали в /v2/delivery/checkout.

**Тело запроса** (`application/json`):
- **buyer** `object` *обязательный* — Информация о покупателе.
- **delivery** *обязательный* — Информация о доставке.
- **delivery_schema** `string` *обязательный* — Схема доставки: MIX — на выбор Ozon; FBO — FBO; FBS — FBS.. Enum: `"MIX"`, `"FBO"`, `"FBS"`.
- **recipient** `object` *обязательный* — Информация о получателе.
- **splits** `Array of objects` *обязательный* — Информация об отправлениях в заказе.

**Пример запроса:**

```json
{
  "buyer": {
    "first_name": "string",
    "last_name": "string",
    "middle_name": "string",
    "phone": "string"
  },
  "delivery": {
    "delivery_schema": "MIX",
    "recipient": {
      "recipient_first_name": "string",
      "recipient_last_name": "string",
      "recipient_middle_name": "string",
      "recipient_phone": "string"
    },
    "splits": [
      {
        "delivery_method": {
          "delivery_method_id": 0,
          "delivery_type": "COURIER",
          "logistic_date_range": {
            "from": "2019-08-24T14:15 ",
            "to": "2019-08-24T14:15:2"
          },
          "price": {
            "currency_code": "string",
            "nanos": 0,
            "units": 0
          },
          "timeslot_id": 0
        },
        "items": [
          {
            "offer_id": "string",
            "price": {
              "currency_code": "stri \"nanos\": 0",
              "units": 0
            },
            "quantity": 0,
            "sku": 0
          }
        ],
        "warehouse_id": 0
      }
    ]
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заказ создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **order_number** `string` — Номер заказа.
- **postings** `Array of strings` — Отправления.

**Пример ответа (`200`):**

```json
{
  "order_number": "string",
  "postings": [
    "string"
  ]
}
```


---
