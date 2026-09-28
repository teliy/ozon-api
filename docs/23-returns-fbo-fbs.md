# Возвраты товаров FBO и FBS

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 349. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Информация о возвратах FBO и FBS

`POST /v1/returns/list`

Метод для получения информации о возвратах FBO и FBS.

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтры. Используйте только один фильтр в запросе: logistic_return_date , storage_tariffication_start_date или visual_status_change_moment , иначе вернётся ошибка.
- **limit** `integer <int32>` *обязательный* — Количество подгружаемых возвратов. Максимальное значение — 500.
- **last_id** `integer <int64>` — Идентификатор последнего подгруженного возврата.

**Пример запроса:**

```json
{
  "filter": {
    "logistic_return_date": {
      "time_from": "2026-02-01T00:00:0 ",
      "time_to": "2026-03-01T23:59:59Z"
    },
    "order_id": "7000123456",
    "posting_numbers": [
      "789456123-0002-3",
      "123456789-0001-1"
    ],
    "product_name": "Тестовый товар",
    "offer_id": "test-offer-123456",
    "visual_status_name": "ArrivedAtRetu \"warehouse_id\": \"3000007863",
    "barcode": "test-barcode-123456789",
    "return_schema": "FBS"
  },
  "limit": 500,
  "last_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация по возвратам |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **returns** `Array of objects` — Информация о возвратах.
- **has_next** `boolean` — true , если у продавца есть другие возвраты.

**Пример ответа (`200`):**

```json
{
  "returns": [
    {
      "exemplars": [
        {
          "id": "1019562967545956"
        }
      ],
      "id": "1000015552",
      "company_id": "3058",
      "return_reason_name": "Покупател \"type\": \"FullReturn",
      "schema": "Fbs",
      "order_id": "24540784250",
      "order_number": "58544282-0057",
      "place": {
        "id": "23869688194000",
        "name": "СЦ_Львовский_Возврат \"address\": "
      },
      "target_place": {
        "id": "23869688194000",
        "name": "СЦ_Львовский_Возврат \"address\": "
      },
      "storage": {
        "sum": {
          "currency_code": "RUB",
          "price": "1231"
        },
        "tariffication_first_date": " \"tariffication_start_date\": ",
        "arrived_moment": "2024-07-29 \"days\": \"0",
        "utilization_sum": {
          "currency_code": "RUB",
          "price": "1231"
        },
        "utilization_forecast_date": ""
      },
      "product": {
        "sku": "1100526203",
        "offer_id": "81451",
        "name": "Кукла Дотти Плачущий \"price\": { \"currency_code\": \"RUB",
        "price": "3318"
      },
      "price_without_commission": {
        "currency_code": "RUB",
        "price": "3318"
      },
      "commission_percent": "1.2",
      "commission": {
        "currency_code": "RUB",
        "price": "2312"
      },
      "quantity": 1
    },
    {
      "logistic": {
        "technical_return_moment": "2 \"final_moment\": \"2024-07-29T0 \" ll d ith ti ",
        "return_date": "2024-07-29T06 \"barcode\": \"ii5275210303\""
      },
      "visual": {
        "status": {
          "id": 3,
          "display_name": "В пункте \"sys_name\": "
        },
        "change_moment": "2024-07-29T"
      },
      "additional_info": {
        "is_opened": true,
        "is_super_econom": false
      },
      "source_id": "90426223",
      "posting_number": "58544282-0057 \"clearing_id\": \"21190893156000",
      "return_clearing_id": null,
      "compensation_status": {
        "status": {
          "id": 2,
          "display_name": "Вы получ \"sys_name\": \"Received\""
        },
        "change_moment": "2025-11-06T"
      }
    }
  ],
  "has_next": false
}
```


---

## Получить историю изменений автоутилизации

`POST /v1/returns/settings/utilization/history`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | История изменений |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **history** `Array of objects` — История изменений.
  - **descriptions** `Array of strings` — Описание события.
  - **updated_at** `string <date-time>` — Дата обновления.
  - **user_name** `string` — Имя пользователя.

**Пример ответа (`200`):**

```json
{
  "history": [
    {
      "descriptions": [
        "string"
      ],
      "updated_at": "2019-08-24T14:15: \"user_name\": \"string\" }"
    }
  ]
}
```


---

## Получить настройки автоутилизации

`POST /v1/returns/settings/utilization/info`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Настройки автоутилизации |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **min_price** `object` — Минимальная цена товара, с которой можно установить автоутилизацию методом /v1/returns/settings/utilization/update.
- **utilization_settings** `object` — Настройки утилизации.

**Пример ответа (`200`):**

```json
{
  "min_price": {
    "amount": "string",
    "currency": "string"
  },
  "utilization_settings": {
    "utilization_price": {
      "amount": "string",
      "currency": "string"
    },
    "utilization_price_defects": {
      "amount": "string",
      "currency": "string"
    }
  }
}
```


---

## Обновить настройки автоутилизации

`POST /v1/returns/settings/utilization/update`

**Тело запроса** (`application/json`):
- **utilization_price** `object` *обязательный* — Максимальная цена автоутилизации для товаров без дефектов.
- **utilization_price_defects** `object` *обязательный* — Максимальная цена автоутилизации для товаров с дефектами.

**Пример запроса:**

```json
{
  "utilization_price": {
    "enabled": true,
    "value": 0
  },
  "utilization_price_defects": {
    "enabled": true,
    "value": 0
  }
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
