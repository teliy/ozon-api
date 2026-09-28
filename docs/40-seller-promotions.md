# Акции продавца

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 485. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

Как работать с акциями продавца

Подробнее об акциях продавца в Базе знаний продавца

## Создать акцию с механикой «Скидка»

`POST /v1/seller-actions/create/discount`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

> **Примечание:** Недоступен для продавцов из СНГ.

**Тело запроса** (`application/json`):
- **date_end** `string <date-time>` *обязательный* — Дата и время окончания акции.
- **date_start** `string <date-time>` *обязательный* — Дата и время начала акции.
- **min_action_percent** `number <double>` *обязательный* — Минимальный процент скидки.
- **title** `string` — Название акции.

**Пример запроса:**

```json
{
  "date_end": "2019-08-24T14:15:22Z",
  "date_start": "2019-08-24T14:15:22Z",
  "min_action_percent": 0,
  "title": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акция создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **action_id** `integer <uint64>` — Идентификатор акции.

**Пример ответа (`200`):**

```json
{
  "action_id": 0
}
```


---

## Создать акцию с механикой «Скидка от суммы заказа»

`POST /v1/seller-actions/create/discount-with-condition`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date_end** `string <date-time>` *обязательный* — Дата и время окончания акции.
- **date_start** `string <date-time>` *обязательный* — Дата и время начала акции.
- **discount_type** `string` *обязательный* — Тип скидки: PERCENT — скидка в процентах; CURRENCY — скидка в валюте.. Enum: `"PERCENT"`, `"CURRENCY"`.
- **discount_value** `number <float>` *обязательный* — Размер скидки.
- **min_order_amount** `number <double>` *обязательный* — Сумма заказа, с которой действует скидка.
- **title** `string` — Название акции.

**Пример запроса:**

```json
{
  "date_end": "2019-08-24T14:15:22Z",
  "date_start": "2019-08-24T14:15:22Z",
  "discount_type": "PERCENT",
  "discount_value": 0,
  "min_order_amount": 0,
  "title": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акция создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **action_id** `integer <uint64>` — Идентификатор акции.

**Пример ответа (`200`):**

```json
{
  "action_id": 0
}
```


---

## Создать акцию с механикой «Беспроцентная рассрочка»

`POST /v1/seller-actions/create/installment`

Период рассрочки — 6 месяцев. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date_start** `string <date-time>` *обязательный* — Дата и время начала акции.
- **title** `string` *обязательный* — Название акции.

**Пример запроса:**

```json
{
  "date_start": "2019-08-24T14:15:22Z",
  "title": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акция создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **action_id** `integer <uint64>` — Идентификатор акции.

**Пример ответа (`200`):**

```json
{
  "action_id": 0
}
```


---

## Создать акцию с механикой «Многоуровневая скидка от суммы»

`POST /v1/seller-actions/create/multi-level-discount`

Товары в акцию добавляются автоматически, использовать метод Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date_end** `string <date-time>` *обязательный* — Дата и время окончания акции.
- **date_start** `string <date-time>` *обязательный* — Дата и время начала акции.
- **discount_levels** `Array of objects` *обязательный* — Уровни скидки.
- **discount_type** `string` *обязательный* — Тип скидки: PERCENT — скидка в процентах; CURRENCY — скидка в валюте.. Enum: `"PERCENT"`, `"CURRENCY"`.
- **is_legal_entities_segment** `boolean` — true , если акция только для юридических лиц.
- **title** `string` — Название акции.

**Пример запроса:**

```json
{
  "date_end": "2019-08-24T14:15:22Z",
  "date_start": "2019-08-24T14:15:22Z",
  "discount_levels": [
    {
      "discount_value": 0,
      "order_amount": 0
    },
    {
      "discount_value": 0,
      "order_amount": 0
    }
  ],
  "discount_type": "PERCENT",
  "is_legal_entities_segment": true,
  "title": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акция создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **action_id** `integer <uint64>` — Идентификатор акции.

**Пример ответа (`200`):**

```json
{
  "action_id": 0
}
```


---

## Создать акцию с механикой «Скидка по промокоду»

`POST /v1/seller-actions/create/voucher`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **budget** `integer <int64>` *обязательный* — Бюджет акции. Если бюджет закончится, акция остановится.
- **date_end** `string <date-time>` *обязательный* — Дата и время окончания акции.
- **date_start** `string <date-time>` *обязательный* — Дата и время начала акции.
- **discount_type** `string` *обязательный* — Тип скидки: PERCENT — скидка в процентах; CURRENCY — скидка в валюте.. Enum: `"PERCENT"`, `"CURRENCY"`.
- **discount_value** `number <double>` *обязательный* — Размер скидки.
- **title** `string` *обязательный* — Название акции.
- **user_ids** `Array of strings <uint64>` — Идентификаторы пользователей, которым доступен промокод.
- **voucher_parameters** `object` *обязательный* — Параметры промокодов.

**Пример запроса:**

```json
{
  "budget": 0,
  "date_end": "2019-08-24T14:15:22Z",
  "date_start": "2019-08-24T14:15:22Z",
  "discount_type": "PERCENT",
  "discount_value": 0,
  "title": "string",
  "user_ids": [
    "string"
  ],
  "voucher_parameters": {
    "count_codes": 0,
    "is_private": true,
    "type": "ONE"
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акция создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **action_id** `integer <uint64>` — Идентификатор акции.

**Пример ответа (`200`):**

```json
{
  "action_id": 0
}
```


---

## Обновить акцию с механикой «Скидка»

`POST /v1/seller-actions/update/discount`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

> **Примечание:** Недоступен для продавцов из СНГ.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **action_parameters** `object` — Параметры акции.

**Пример запроса:**

```json
{
  "action_id": 0,
  "action_parameters": {
    "date_end": "2019-08-24T14:15:22Z",
    "date_start": "2019-08-24T14:15:22Z",
    "title": "string"
  }
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

## Обновить акцию с механикой «Скидка от суммы заказа»

`POST /v1/seller-actions/update/discount-with-condition`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **action_parameters** `object` — Параметры акции.

**Пример запроса:**

```json
{
  "action_id": 0,
  "action_parameters": {
    "date_end": "2019-08-24T14:15:22Z",
    "date_start": "2019-08-24T14:15:22Z",
    "discount_value": 0,
    "min_order_amount": 0,
    "title": "string"
  }
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

## Обновить акцию с механикой «Беспроцентная рассрочка»

`POST /v1/seller-actions/update/installment`

Период рассрочки — 6 месяцев. Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **action_parameters** `object` — Параметры акции.

**Пример запроса:**

```json
{
  "action_id": 0,
  "action_parameters": {
    "date_start": "2019-08-24T14:15:22Z",
    "title": "string"
  }
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

## Обновить акцию с механикой «Многоуровневая скидка от суммы»

`POST /v1/seller-actions/update/multi-level-discount`

Товары в акцию добавляются автоматически, вызывать метод Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **action_parameters** `object` — Параметры акции.

**Пример запроса:**

```json
{
  "action_id": 0,
  "action_parameters": {
    "date_end": "2019-08-24T14:15:22Z",
    "date_start": "2019-08-24T14:15:22Z",
    "discount_levels": [
      {
        "discount_value": 0,
        "order_amount": 0
      },
      {
        "discount_value": 0,
        "order_amount": 0
      }
    ],
    "is_legal_entities_segment": true,
    "title": "string"
  }
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

## Обновить акцию с механикой «Скидка по промокоду»

`POST /v1/seller-actions/update/voucher`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **action_parameters** `object` — Параметры акции.

**Пример запроса:**

```json
{
  "action_id": 0,
  "action_parameters": {
    "budget": 0,
    "date_end": "2019-08-24T14:15:22Z",
    "date_start": "2019-08-24T14:15:22Z",
    "discount_value": 0,
    "title": "string",
    "user_ids": [
      "string"
    ]
  }
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

## Добавить товары в акцию

`POST /v1/seller-actions/products/add`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **products** `Array of action_price (object) or discount_percent (object)`
  - **items** *обязательный* — Информация о товарах.

**Пример запроса:**

```json
{
  "action_id": 0,
  "products": [
    {}
  ]
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

## Получить список доступных для акции товаров

`POST /v1/seller-actions/products/candidates`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **cursor** `integer <uint64>` — Указатель для выборки следующих данных.
- **limit** `integer <int64>` *обязательный* — Максимальное количество элементов в ответе.

**Пример запроса:**

```json
{
  "action_id": 0,
  "cursor": 0,
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `integer <uint64>` — Указатель для выборки следующих данных.
- **has_next** `boolean` — Признак, что в ответе вернулась только часть значений: true — сделайте повторный запрос с новым параметром cursor для получения остальных значений; false — ответ содержит все значения.
- **products** `Array of objects` — Информация о товарах.

**Пример ответа (`200`):**

```json
{
  "cursor": 0,
  "has_next": true,
  "products": [
    {
      "action_price": 0,
      "base_price": 0,
      "currency": "string",
      "discount_percent": 0,
      "is_active": true,
      "min_seller_price": 0,
      "name": "string",
      "offer_id": "string",
      "price": 0,
      "product_id": 0,
      "quant_size": 0,
      "quant_type": "UNSPECIFIED",
      "sku": [
        "string"
      ]
    }
  ]
}
```


---

## Удалить товары из акции

`POST /v1/seller-actions/products/delete`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **skus** `Array of strings <uint64>` *обязательный* — Идентификаторы товаров в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "action_id": 0,
  "skus": [
    "string"
  ]
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

## Получить список участвующих в акции товаров

`POST /v1/seller-actions/products/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **cursor** `integer <uint64>` — Указатель для выборки следующих данных.
- **limit** `integer <int64>` *обязательный* — Максимальное количество элементов в ответе.

**Пример запроса:**

```json
{
  "action_id": 0,
  "cursor": 0,
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `integer <uint64>` — Указатель для выборки следующих данных.
- **has_next** `boolean` — Признак, что в ответе вернулась только часть значений: true — сделайте повторный запрос с новым параметром cursor для получения остальных значений; false — ответ содержит все значения.
- **products** `Array of objects` — Информация о товарах.

**Пример ответа (`200`):**

```json
{
  "cursor": 0,
  "has_next": true,
  "products": [
    {
      "action_price": 0,
      "base_price": 0,
      "currency": "string",
      "discount_percent": 0,
      "is_active": true,
      "min_seller_price": 0,
      "name": "string",
      "offer_id": "string",
      "price": 0,
      "product_id": 0,
      "quant_size": 0,
      "quant_type": "UNSPECIFIED",
      "sku": [
        "string"
      ]
    }
  ]
}
```


---

## Перенести акцию в архив

`POST /v1/seller-actions/archive`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.

**Пример запроса:**

```json
{
  "action_id": 0
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

## Включить или выключить акцию

`POST /v1/seller-actions/change-activity`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.
- **is_turn_on** `boolean` *обязательный* — true , чтобы включить акцию.

**Пример запроса:**

```json
{
  "action_id": 0,
  "is_turn_on": true
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

## Получить список акций

`POST /v1/seller-actions/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_ids** `Array of strings <uint64>` — Идентификаторы акций.
- **action_type** `Array of strings` — Механика акции: DISCOUNT — скидка; VOUCHER_DISCOUNT — скидка по промокоду; DISCOUNT_WITH_CONDITION — скидка от суммы заказа; INSTALLMENT — беспроцентная рассрочка; INDIVIDUAL_DISCOUNT_BY_PRODUCTS — бонусы продавца; OZON_ACCOUNT_DISCOUNT — повышенная скидка с картой Ozon Банка; MULTI_LEVEL_DISCOUNT_ON_AMOUNT — многоуровневая скидка от суммы.. Enum: `"DISCOUNT"`, `"VOUCHER_DISCOUNT"`, `"DISCOUNT_WITH_CONDITION"`, `"INSTALLMENT"`, `"INDIVIDUAL_DISCOUNT_BY_PRODUCTS"`, `"OZON_ACCOUNT_DISCOUNT"`, `"MULTI_LEVEL_DISCOUNT_ON_AMOUNT"`.
- **limit** `integer <uint64>` *обязательный* — Количество значений на странице.
- **offset** `integer <uint64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **search** `string` — Поиск по названию акции.
- **status** `Array of strings` — Статус акции: ACTIVE — активна; ENDED — завершена; PLANNED — запланирована; PAUSED — приостановлена.. Enum: `"ACTIVE"`, `"ENDED"`, `"PLANNED"`, `"PAUSED"`.

**Пример запроса:**

```json
{
  "action_ids": [
    "string"
  ],
  "action_type": [
    "DISCOUNT"
  ],
  "limit": 1,
  "offset": 0,
  "search": "string",
  "status": [
    "ACTIVE"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список акций |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **actions** `Array of objects` — Список акций.
- **total** `integer <uint64>` — Общее количество акций.

**Пример ответа (`200`):**

```json
{
  "actions": [
    {
      "action_id": 0,
      "action_parameters": {
        "addresses": [
          "string"
        ],
        "auto_stop_action_reason": "U \"budget\": 0",
        "budget_spent": 0,
        "date_end": "2019-08-24T14:15 ",
        "date_start": "2019-08-24T14: \"discount_levels\": [ { \"discount_value\": 0",
        "order_amount": 0
      },
      "discount_type": "UNSPECIFIED \"discount_value\": 0",
      "is_legal_entities_segment": "min_action_percent",
      "min_order_amount": 0,
      "picked_segments": [
        {
          "segments": [
            {
              "description": "id",
              "name": "string \"type\": "
            }
          ]
        }
      ],
      "status": "ACTIVE",
      "title": "string",
      "type": "DISCOUNT",
      "voucher_parameters": {
        "count_codes": 0,
        "is_private": true,
        "type": "UNSPECIFIED"
      },
      "warehouses": [
        "string"
      ]
    },
    {
      "allow_delete": true,
      "highlight_url": "string",
      "is_editable": true,
      "is_participated": true,
      "is_turn_on": true,
      "sku_count": 0
    }
  ],
  "total": 0
}
```


---

## Получить файл с промокодами в формате CSV

`POST /v1/seller-actions/voucher/get`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите значение параметра методом /v1/seller-actions/list.

**Пример запроса:**

```json
{
  "action_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Файл с промокодами |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **file** `string` — Ссылка на CSV-файл с промокодами.

**Пример ответа (`200`):**

```json
{
  "file": "string"
}
```


---
