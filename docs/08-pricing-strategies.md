# Стратегии ценообразования

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 114. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Список конкурентов

`POST /v1/pricing-strategy/competitors/list`

Метод для получения списка конкурентов — продавцов с похожими товарами в других интернет-магазинах и маркетплейсах.

**Тело запроса** (`application/json`):
- **page** `integer <int64>` *обязательный* — Страница списка, с которой нужно выгрузить конкурентов. Минимальное значение — 1 .
- **limit** `integer <int64>` *обязательный* — Максимальное количество конкурентов на странице. Допустимы значения от 1 до 50 .

**Пример запроса:**

```json
{
  "page": 1,
  "limit": 20
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список конкурентов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **competitor** `Array of objects` — Список конкурентов.
- **total** `integer <int32>` — Общее количество конкурентов.

**Пример ответа (`200`):**

```json
{
  "competitor": [
    {
      "id": 7820251,
      "name": "grenmarketshop.ru"
    }
  ],
  "total": 33
}
```


---

## Список стратегий

`POST /v1/pricing-strategy/list`

**Тело запроса** (`application/json`):
- **page** `integer <int64>` *обязательный* — Страница списка, с которой нужно выгрузить стратегии. Минимальное значение — 1 .
- **limit** `integer <int64>` *обязательный* — Максимальное количество стратегий на странице. Допустимые значения — от 1 до 50 .

**Пример запроса:**

```json
{
  "page": 1,
  "limit": 20
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список стратегий |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **strategies** `Array of objects` — Список стратегий.
- **total** `integer <int32>` — Общее количество стратегий.

**Пример ответа (`200`):**

```json
{
  "strategies": [
    {
      "id": "2fb3e6a3-3db5-4bb4-8430-b \"name\": \"стратегия_от_CID7",
      "type": "COMP_PRICE",
      "update_type": "strategyEnabled",
      "updated_at": "2024-05-02 14:47: \"products_count\": 1",
      "competitors_count": 1,
      "enabled": true
    }
  ],
  "total": 5
}
```


---

## Создать стратегию

`POST /v1/pricing-strategy/create`

**Тело запроса** (`application/json`):
- **competitors** `Array of objects` *обязательный* — Список конкурентов.
- **strategy_name** `string` *обязательный* — Название стратегии.

**Пример запроса:**

```json
{
  "strategy_name": "Новая стратегия",
  "competitors": [
    {
      "competitor_id": 1008426,
      "coefficient": 1
    },
    {
      "competitor_id": 204,
      "coefficient": 1
    },
    {
      "competitor_id": 91,
      "coefficient": 1
    },
    {
      "competitor_id": 48,
      "coefficient": 1
    }
  ],
  "company_id": 7
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Стратегия создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **strategy_id** `string` — Идентификатор стратегии.

**Пример ответа (`200`):**

```json
{
  "result": {
    "id": "4f3a1d4c-5833-4f04-b69b-495cb"
  }
}
```


---

## Информация о стратегии

`POST /v1/pricing-strategy/info`

**Тело запроса** (`application/json`):
- **strategy_id** `string` *обязательный* — Идентификатор стратегии.

**Пример запроса:**

```json
{
  "strategy_id": "2fb3e6a3-3db5-4bb4-8430"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о стратегии |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **competitors** `Array of objects` — Список конкурентов.
  - **enabled** `boolean` — Статус стратегии: true — включена, false — отключена.
  - **name** `string` — Название стратегии.
  - **type** `string` — Тип стратегии: MIN_EXT_PRICE — системная стратегия, COMP_PRICE — пользовательская стратегия.
  - **update_type** `string` — Тип последнего изменения стратегии: strategyEnabled — возобновлена, strategyDisabled — остановлена, strategyChanged — обновлена, strategyCreated — создана, strategyItemsListChanged — изменён набор товаров в стратегии.

**Пример ответа (`200`):**

```json
{
  "result": {
    "strategy_name": "стратегия_от_CID7",
    "enabled": true,
    "update_type": "strategyItemsListCha \"type\": \"COMP_PRICE",
    "competitors": [
      {
        "competitor_id": 204,
        "coefficient": 1
      },
      {
        "competitor_id": 1008426,
        "coefficient": 1
      }
    ]
  }
}
```


---

## Обновить стратегию

`POST /v1/pricing-strategy/update`

Можно обновить все стратегии кроме системной.

**Тело запроса** (`application/json`):
- **competitors** `Array of objects` *обязательный* — Список конкурентов.
- **strategy_id** `string` *обязательный* — Идентификатор стратегии.
- **strategy_name** `string` *обязательный* — Название стратегии.

**Пример запроса:**

```json
{
  "strategy_id": "a3de1826-9c54-40f1-bb6d \"strategy_name\": \"Новая стратегия",
  "competitors": [
    {
      "competitor_id": 1008426,
      "coefficient": 1
    },
    {
      "competitor_id": 204,
      "coefficient": 1
    },
    {
      "competitor_id": 91,
      "coefficient": 1
    },
    {
      "competitor_id": 48,
      "coefficient": 1
    },
    {
      "competitor_id": 45,
      "coefficient": 1
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Стратегия обновлена |
| `default` | Ошибка |

**Пример ответа (`200`):**

```json
{}
```


---

## Добавить товары в стратегию

`POST /v1/pricing-strategy/products/add`

**Тело запроса** (`application/json`):
- **product_id** `Array of strings <int64>` *обязательный* — Список идентификаторов товаров в системе Ozon — product_id . Максимальное количество — 50.
- **strategy_id** `string` *обязательный* — Идентификатор стратегии.

**Пример запроса:**

```json
{
  "product_id": [
    "29209"
  ],
  "strategy_id": "e29114f0-177d-4160-8d06"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Ошибки при добавлении товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **errors** `Array of objects` — Товары с ошибками.
  - **failed_product_count** `integer <int32>` — Количество товаров с ошибками.

**Пример ответа (`200`):**

```json
{
  "result": {
    "failed_product_count": 0
  }
}
```


---

## Список идентификаторов стратегий

`POST /v1/pricing-strategy/strategy-ids-by-product-ids`

**Тело запроса** (`application/json`):
- **product_id** `Array of strings <int64>` *обязательный* — Список идентификаторов товаров в системе Ozon — product_id . Максимальное количество — 50.

**Пример запроса:**

```json
{
  "product_id": [
    "29209"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список идентификаторов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **products_info** `Array of objects` — Информация о товаре.

**Пример ответа (`200`):**

```json
{
  "result": {
    "products_info": [
      {
        "product_id": 29209,
        "strategy_id": "b7cd30e6-5667 }"
      }
    ]
  }
}
```


---

## Список товаров в стратегии

`POST /v1/pricing-strategy/products/list`

**Тело запроса** (`application/json`):
- **strategy_id** `string` *обязательный* — Идентификатор стратегии.

**Пример запроса:**

```json
{
  "strategy_id": "b7cd30e6-5667-424d-b105"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Список товаров.
  - **product_id** `Array of strings <int64>` — Идентификатор товара в системе Ozon — product_id .

**Пример ответа (`200`):**

```json
{
  "result": {
    "product_id": [
      "29209"
    ]
  }
}
```


---

## Цена товара у конкурента

`POST /v1/pricing-strategy/product/info`

Если вы добавили товар в стратегию ценообразования, метод вернёт цену и ссылку на товар у конкурента.

**Тело запроса** (`application/json`):
- **product_id** `integer <int64>` *обязательный* — Идентификатор товара в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "product_id": 7856197312
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Цена товара у конкурента |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **strategy_id** `string` — Идентификатор стратегии.
  - **is_enabled** `boolean` — true , если товар участвует в стратегии ценообразования.
  - **strategy_product_price** `integer <int32>` — Цена по стратегии.
  - **price_downloaded_at** `string` — Дата установки цены по стратегии.
  - **strategy_competitor_id** `integer <int64>` — Идентификатор конкурента.
  - **strategy_competitor_product_url** `string` — Ссылка на товар конкурента.

**Пример ответа (`200`):**

```json
{
  "result": {
    "strategy_id": "b7cd30e6-5667-424d-b \"is_enabled\": true",
    "strategy_product_price": 500,
    "price_downloaded_at": "2022-11-17T1 \"strategy_competitor_id\": ",
    "strategy_competitor_product_url": ""
  }
}
```


---

## Удалить товары из стратегии

`POST /v1/pricing-strategy/products/delete`

**Тело запроса** (`application/json`):
- **product_id** `Array of strings <int64>` *обязательный* — Список идентификаторов товаров в системе Ozon — product_id . Максимальное количество — 50.

**Пример запроса:**

```json
{
  "product_id": [
    "29209"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Ошибки при удалении товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **failed_product_count** `integer <int32>` — Количество товаров с ошибками.

**Пример ответа (`200`):**

```json
{
  "result": {
    "failed_product_count": 2
  }
}
```


---

## Изменить статус стратегии

`POST /v1/pricing-strategy/status`

Можно изменить статус любой стратегии кроме системной.

**Тело запроса** (`application/json`):
- **enabled** `boolean` — Статус стратегии: true — включена, false — отключена.
- **strategy_id** `string` *обязательный* — Идентификатор стратегии.

**Пример запроса:**

```json
{
  "strategy_id": "c7516438-7124-4e2c-85d3 \"enabled\": true"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус стратегии изменён |
| `default` | Ошибка |

**Пример ответа (`200`):**

```json
{}
```


---

## Удалить стратегию

`POST /v1/pricing-strategy/delete`

Можно удалить любую стратегию кроме системной.

**Тело запроса** (`application/json`):
- **strategy_id** `string` *обязательный* — Идентификатор стратегии.

**Пример запроса:**

```json
{
  "strategy_id": "b7cd30e6-5667-424d-b105"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Стратегия удалена |
| `default` | Ошибка |

**Пример ответа (`200`):**

```json
{}
```


---
