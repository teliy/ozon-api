# Работа с актами FBO

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 589. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Получить информацию об акте

`POST /v1/supply-order/act/summary/get`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **order_id** `integer <int64>` *обязательный* — Идентификатор заявки на поставку из метода /v3/supply- order/list.

**Пример запроса:**

```json
{
  "order_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об акте |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **supplies_acts** `Array of objects` — Список актов.
  - **is_agreement_completed** `boolean` — true , если все акты согласованы.
  - **supply_acts** `Array of objects` — Информация об актах.
  - **supply_id** `integer <int64>` — Идентификатор поставки.

**Пример ответа (`200`):**

```json
{
  "supplies_acts": [
    {
      "is_agreement_completed": true,
      "supply_acts": [
        {
          "act_id": 0,
          "act_number": "string",
          "act_state": "UNSPECIFIED \"created_date\": \"string",
          "deadline_utc": "2019-08- \"summary\": { \"approved_amount\": { \"amount\": { \"amount\": ",
          "currency": "st"
        },
        {
          "amount_vat": {
            "amount": "stri \"currency\": "
          },
          "amount_without_va \"amount": "stri \"currency\": "
        }
      ],
      "approved_quantity": 0,
      "declared_quantity": 0,
      "fact_amount": {
        "amount": {
          "amount": "stri \"currency\": "
        },
        "amount_vat": {
          "amount": "stri \"currency\": "
        },
        "amount_without_va \"amount": "stri \"currency\": "
      }
    },
    {
      "fact_quantity": 0,
      "sku_quantity": 0,
      "unidentified_quantity }, \"type": "UNSPECIFIED"
    }
  ],
  "supply_id": 0
}
```


---

## Получить информацию о товарах в акте

`POST /v1/supply-order/act/product/get`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **supply_id** `integer <int64>` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "supply_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о товарах в акте |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **skus_defects** `Array of objects` — Список товаров с браком.
- **supply_acts** `Array of objects` — Список актов в поставке.
- **supply_id** `integer <int64>` — Идентификатор поставки.

**Пример ответа (`200`):**

```json
{
  "skus_defects": [
    {
      "defect_reasons": [
        "string"
      ],
      "sku": 0
    }
  ],
  "supply_acts": [
    {
      "act_id": 0,
      "items": [
        {
          "approved_amount": {
            "amount": {
              "amount": "string",
              "currency": "strin"
            },
            "amount_vat": {
              "amount": "string",
              "currency": "strin"
            },
            "amount_without_vat": "amount\": \"string",
            "currency": "strin"
          }
        },
        {
          "approved_quantity": 0,
          "declared_quantity": 0,
          "fact_amount": {
            "amount": {
              "amount": "string",
              "currency": "strin"
            },
            "amount_vat": {
              "amount": "string",
              "currency": "strin"
            },
            "amount_without_vat": "amount\": \"string",
            "currency": "strin"
          }
        },
        {
          "fact_quantity": 0,
          "sku_info": {
            "barcode": "string",
            "image_link": "string",
            "name": "string",
            "offer_id": "string",
            "price_without_vat": {
              "amount": "string",
              "currency": "strin"
            },
            "sku": 0,
            "vat": 0
          }
        }
      ],
      "type": "UNSPECIFIED",
      "unidentified_quantity": 0
    }
  ],
  "supply_id": 0
}
```


---

## Согласовать акт

`POST /v1/supply-order/act/accept`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **act_id** `integer <int64>` *обязательный* — Идентификатор акта из методов /v1/supply- order/act/summary/get или /v1/supply-order/act/product/get.

**Пример запроса:**

```json
{
  "act_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акт согласован |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **error_reasons** `Array of strings` — Ошибки при принятии акта: UNSPECIFIED — не определена; INVALID_STATE — некорректный статус; SUPPLY_WITH_UTD — поставка с УПД.. Enum: `"UNSPECIFIED"`, `"INVALID_STATE"`, `"SUPPLY_WITH_UTD"`.
- **operation_id** `string` — Идентификатор операции.

**Пример ответа (`200`):**

```json
{
  "error_reasons": [
    "UNSPECIFIED"
  ],
  "operation_id": "string"
}
```


---

## Получить статус согласования акта

`POST /v1/supply-order/act/accept/status`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции из метода /v1/supply- order/act/accept.

**Пример запроса:**

```json
{
  "operation_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус согласования акта |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **status** `string` — Статус операции: SUCCESS — акт согласован; IN_PROGRESS — согласование в процессе; FAILED — ошибка при согласовании акта.. Enum: `"SUCCESS"`, `"IN_PROGRESS"`, `"FAILED"`.
- **error_message** `string` — Причина ошибки.

**Пример ответа (`200`):**

```json
{
  "status": "SUCCESS",
  "error_message": "string"
}
```


---
