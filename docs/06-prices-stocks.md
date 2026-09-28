# Цены и остатки товаров

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 76. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Обновить количество товаров на складах

## Обновить количество товаров на складах

`POST /v2/products/stocks`

Позволяет изменить информацию о количестве товара в наличии. За один запрос можно изменить наличие для 100 пар товар-склад. С одного аккаунта продавца можно отправить до 80 запросов в минуту. Вы можете задать наличие товара только после того, как его статус сменится на price_sent . Остатки крупногабаритных товаров можно обновлять только на предназначенных для них складах. Если запрос содержит оба параметра — offer_id и product_id , изменения применятся к товару с offer_id . Для избежания неоднозначности используйте только один из параметров.

> **Примечание:** Переданный остаток — количество товара в наличии без учёта

> **Примечание:** зарезервированных товаров. Перед обновлением остатков

> **Примечание:** проверьте количество зарезервированных товаров с помощью

> **Примечание:** метода /v2/product/info/stocks-by-warehouse/fbs.

> **Примечание:** Обновлять остатки у одной пары товар-склад можно только 1 раз

> **Примечание:** в 30 секунд, иначе в параметре result.errors  в ответе будет

```
ошибка TOO_MANY_REQUESTS .
```

**Тело запроса** (`application/json`):
- **stocks** `Array of objects` *обязательный* — Информация о товарах на складах.

**Пример запроса:**

```json
{
  "stocks": [
    {
      "offer_id": "PH11042",
      "product_id": 313455276,
      "stock": 100,
      "warehouse_id": 22142605386000
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество товаров обновлено |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects`
  - **errors** `Array of objects` — Массив ошибок, которые возникли при обработке запроса.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **product_id** `integer <int64>` — Идентификатор товара в системе Ozon — product_id .
  - **updated** `boolean` — Если запрос выполнен успешно и остатки обновлены — true .
  - **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "warehouse_id": 22142605386000,
      "product_id": 118597312,
      "offer_id": "PH11042",
      "updated": true,
      "errors": []
    }
  ]
}
```


---

## Информация о количестве товаров

`POST /v4/product/info/stocks`

Возвращает информацию о ĸоличестве товаров по схемам FBO, FBS, rFBS и FBP: сĸольĸо единиц есть в наличии, сĸольĸо зарезервировано поĸупателями. Чтобы получить аналитику по остаткам по схеме FBO, используйте метод /v1/analytics/stocks.

> **Примечание:** 23 ноября 2026 года отключим параметр total  в ответе метода.

> **Примечание:** Переключитесь на total_items .

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр по товарам.
- **limit** `integer <int32>` *обязательный* — Количество значений на странице. Минимум — 1, максимум — 1000.

**Пример запроса:**

```json
{
  "cursor": "",
  "filter": {
    "offer_id": [
      "1233213232"
    ],
    "product_id": [
      "313455276"
    ],
    "visibility": "ALL",
    "with_quant": {
      "created": true,
      "exists": true
    }
  },
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество товара |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **items** `Array of objects` — Информация о товарах.
- **total** `integer <int32>` — Количество уникальных товаров, для которых выводится информация об остатках.
- **total_items** `integer <int64>` — Количество уникальных товаров, для которых выводится информация об остатках.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "offer_id": "test-offer-123456",
      "product_id": 1000123456,
      "stocks": [
        {
          "sku": 1000123456,
          "type": "fbs",
          "present": 150,
          "reserved": 25,
          "shipment_type": "SHIPMEN"
        },
        {
          "sku": 1000123456,
          "type": "fbo",
          "present": 75,
          "reserved": 10,
          "shipment_type": "SHIPMEN"
        }
      ]
    },
    {
      "offer_id": "test-offer-123457",
      "product_id": 1000123457,
      "stocks": [
        {
          "sku": 1000123457,
          "type": "fbs",
          "present": 45,
          "reserved": 5,
          "shipment_type": "SHIPMEN"
        }
      ]
    }
  ],
  "cursor": "next-cursor-12345",
  "total": 2,
  "total_items": 2
}
```


---

## Получить информацию по остаткам на складе FBS и rFBS

`POST /v1/product/info/warehouse/stocks`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "cursor": "",
  "limit": 10,
  "warehouse_id": 1020003080073000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество товара на складе FBS и rFBS |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных. Если параметр пустой, данных больше нет.
- **has_next** `boolean` — Признак, что в ответе вернули не все товары: true — сделайте повторный запрос с другим значением cursor , чтобы получить остальные значения; false — ответ содержит все значения.
- **stocks** `Array of objects` — Информация об остатках товара.

**Пример ответа (`200`):**

```json
{
  "stocks": [
    {
      "sku": 147035011,
      "product_id": 28743,
      "offer_id": "02105020-35",
      "warehouse_id": 1020003080073000,
      "present": 1000,
      "reserved": 0,
      "free_stock": 1000,
      "updated_at": "2025-09-15T10:36:"
    }
  ],
  "has_next": false,
  "cursor": "147035011"
}
```


---

## Получить информацию об остатках на складах продавца

`POST /v2/product/info/stocks-by-warehouse/fbs`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **limit** `integer <uint64>` *обязательный* — Количество значений в ответе.
- **offer_id** `Array of strings` — Идентификаторы товаров в системе продавца — артикул.
- **sku** `Array of strings <int64>` *обязательный* — Идентификаторы товаров в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "cursor": "string",
  "limit": 0,
  "offer_id": [
    "string"
  ],
  "sku": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество товаров на складах |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **has_next** `boolean` — true , если в ответе вернули не все товары.
- **products** `Array of objects` — Остатки товаров.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "has_next": true,
  "products": [
    {
      "free_stock": 0,
      "offer_id": "string",
      "present": 0,
      "product_id": 0,
      "reserved": 0,
      "sku": 0,
      "warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---

## Информация об остатках на складах продавца (FBS и rFBS)

`POST /v1/product/info/stocks-by-warehouse/fbs`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Передайте в запросе offer_id или sku . Если укажете оба, будет использован только sku .

> **Примечание:** Метод устаревает и будет отключён 7 апреля 2026 года.

> **Примечание:** Переключитесь на /v2/product/info/stocks-by-warehouse/fbs.

**Тело запроса** (`application/json`):
- **sku** `Array of strings <int64>` *обязательный* — Идентификатор товара в системе Ozon — SKU.
- **offer_id** `Array of strings <int64>` — Идентификатор товара в системе продавца — артикул.

**Пример запроса:**

```json
{
  "sku": [
    "string"
  ],
  "offer_id": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество товаров на складах FBS и rFBS |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат работы метода.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
  - **offer_id** `string <int64>` — Идентификатор товара в системе продавца — артикул.
  - **present** `integer <int64>` — Общее количество товара на складе.
  - **product_id** `integer <int64>` — Идентификатор товара в системе Ozon — артикул.
  - **reserved** `integer <int64>` — Количество зарезервированных товаров на складе.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.
  - **warehouse_name** `string` — Название склада.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "sku": 0,
      "offer_id": "string",
      "present": 0,
      "product_id": 0,
      "reserved": 0,
      "warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---

## Обновить цену

`POST /v1/product/import/prices`

Позволяет изменить цену одного или нескольких товаров. Цену каждого товара можно обновлять не больше 10 раз в час. Чтобы сбросить old_price , поставьте 0 у этого параметра. Если у товара установлена минимальная цена и включено автоприменение в акции, отключите его и обновите минимальную цену. Иначе вернётся ошибка Если запрос содержит оба параметра — offer_id и product_id , изменения применятся к товару с offer_id . Для избежания неоднозначности используйте только один из параметров.

```
action_price_enabled_min_price_missing .
```

**Тело запроса** (`application/json`):
- **prices** `Array of objects` — Информация о ценах товаров.

**Пример запроса:**

```json
{
  "prices": [
    {
      "auto_action_enabled": "UNKNOWN",
      "auto_add_to_ozon_actions_list_e \"currency_code": "RUB",
      "declared_price": "1000",
      "manage_elastic_boosting_through \"min_price": "800",
      "min_price_for_auto_actions_enab \"net_price": "650",
      "offer_id": "",
      "old_price": "0",
      "price": "1448",
      "price_strategy_enabled": "UNKNO \"product_id\": 1386",
      "quant_size": 1,
      "vat": "0.1"
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Цена обновлена |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результаты запроса.
  - **errors** `Array of objects` — Массив ошибок, которые возникли при обработке запроса.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **product_id** `integer <int64>` — Идентификатор товара в системе Ozon — product_id .
  - **updated** `boolean` — Если информации о товаре успешно обновлена — true .

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "product_id": 1386,
      "offer_id": "PH8865",
      "updated": true,
      "errors": []
    }
  ]
}
```


---

## Обновление таймера актуальности минимальной цены

`POST /v1/product/action/timer/update`

Минимальная цена действует 30 дней после установки. После этого настройка выключается. Вы можете продлить её: вызовите метод повторно и укажите product_ids .

**Тело запроса** (`application/json`):
- **product_ids** `Array of strings <int64>` — Список идентификаторов товаров в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "product_ids": 88787267123
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

## Получить статус установленного таймера

`POST /v1/product/action/timer/status`

**Тело запроса** (`application/json`):
- **product_ids** `number` — Список идентификаторов товаров в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "product_ids": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статусы |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **statuses** `Array of objects`
  - **expired_at** `string <date-time>` — Время окончания таймера. Если параметр пустой, активного таймера нет.
  - **min_price_for_auto_actions_enabled** `boolean` — true , если Ozon учитывает минимальную цену при добавлении в акции.
  - **product_id** `integer <int64>` — Идентификатор товара в системе Ozon — product_id .

**Пример ответа (`200`):**

```json
{
  "statuses": [
    {
      "expired_at": "2019-08-24T14:15: ",
      "product_id": 0
    }
  ]
}
```


---

## Получить информацию о цене товара

`POST /v5/product/info/prices`

> **Примечание:** 23 ноября 2026 года отключим параметр total  в ответе метода.

> **Примечание:** Переключитесь на total_items .

> **Примечание:** Вы можете посмотреть историю обновления цен только в личном

> **Примечание:** кабинете продавца.

> **Примечание:** Подробнее об истории обновления цен в Базе знаний продавца

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр по товарам.
- **limit** `integer <int32>` *обязательный* — Количество значений на странице.

**Пример запроса:**

```json
{
  "cursor": "",
  "filter": {
    "offer_id": [
      "356792"
    ],
    "product_id": [
      "243686911"
    ],
    "visibility": "ALL"
  },
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о цене товара |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **items** `Array of objects` — Список товаров.
- **total** `integer <int32>` — Количество товаров в списке.
- **total_items** `integer <int64>` — Количество товаров в списке.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "product_id": 1000123456,
      "offer_id": "test-offer-123456",
      "price": {
        "price": 2999.99,
        "old_price": 3499.99,
        "min_price": 2799.99,
        "net_price": 2000,
        "declared_price": {
          "amount": "1000",
          "currency": "RUB"
        },
        "currency_code": "RUB",
        "vat": 0.2,
        "auto_action_enabled": true,
        "auto_add_to_ozon_actions_lis }, \"commissions": {
          "sales_percent_fbo": 15,
          "sales_percent_fbs": 12,
          "fbo_deliv_to_customer_amount \"fbs_deliv_to_customer_amount \"fbo_return_flow_amount": 50,
          "fbs_return_flow_amount": 40
        },
        "price_indexes": {
          "color_index": "GREEN",
          "ozon_index_data": {
            "min_price": 2899.99,
            "min_price_currency": "RU \"price_index_value\": 0.95"
          },
          "external_index_data": {
            "min_price": 2799.99,
            "min_price_currency": "RU \"price_index_value\": 0.93"
          }
        },
        "marketing_actions": {
          "ozon_actions_exist": true,
          "current_period_from": "2026- \"current_period_to\": ",
          "actions": [
            {
              "title": "Скидка 15% н \"value\": 15",
              "date_from": "2026-03- \"date_to\": "
            }
          ]
        },
        "acquiring": 1.5,
        "volume_weight": 0.5
      }
    },
    {
      "product_id": 1000123457,
      "offer_id": "test-offer-123457",
      "price": {
        "price": 5999.99,
        "old_price": 6999.99,
        "min_price": 5499.99,
        "net_price": 4000,
        "currency_code": "RUB",
        "vat": 0.2,
        "auto_action_enabled": false,
        "auto_add_to_ozon_actions_lis }, \"commissions": {
          "sales_percent_fbo": 10,
          "sales_percent_fbs": 8,
          "fbo_deliv_to_customer_amount \"fbs_deliv_to_customer_amount \"fbo_return_flow_amount": 60,
          "fbs_return_flow_amount": 50
        },
        "price_indexes": {
          "color_index": "YELLOW",
          "ozon_index_data": {
            "min_price": 5899.99,
            "min_price_currency": "RU \"price_index_value\": 0.98"
          }
        },
        "marketing_actions": {
          "ozon_actions_exist": false
        },
        "acquiring": 1.8,
        "volume_weight": 0.8
      },
      "cursor": "",
      "total": 2,
      "total_items": 2
    }
  ]
}
```


---

## Узнать информацию об уценке и основном товаре по SKU уценённого товара

`POST /v1/product/info/discounted`

Метод для получения информации о состоянии и дефектах уценённого товара по его SKU. Работает только с уценёнными товарами по схеме FBO. Также метод возвращает SKU основного товара.

**Тело запроса** (`application/json`):
- **discounted_skus** `Array of strings <int64>` *обязательный* — Список SKU уценённых товаров.

**Пример запроса:**

```json
{
  "discounted_skus": [
    "635548518"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об уценке и основном товаре |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **items** `Array of objects` — Информация об уценке и основном товаре.
  - **comment_reason_damaged** `string` — Комментарий к причине повреждения.
  - **condition** `string` — Состояние товара — новый или Б/У.
  - **condition_estimation** `string` — Состояние товара по шкале от 1 до 7: 1 — удовлетворительное, 2 — хорошее, 3 — очень хорошее, 4 — отличное, 5–7 — как новый.
  - **defects** `string` — Дефекты товара.
  - **discounted_sku** `integer <int64>` — SKU уценённого товара.
  - **mechanical_damage** `string` — Описание механического повреждения.
  - **package_damage** `string` — Описание повреждения упаковки.
  - **packaging_violation** `string` — Признак нарушения целостности упаковки.
  - **reason_damaged** `string` — Причина повреждения.
  - **repair** `string` — Признак, что товар отремонтирован.
  - **shortage** `string` — Признак, что товар некомплектный.
  - **sku** `integer <int64>` — SKU основного товара.
  - **warranty_type** `string` — Наличие у товара действующей гарантии.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "discounted_sku": 635548518,
      "sku": 320067758,
      "condition_estimation": "4",
      "packaging_violation": "",
      "warranty_type": "",
      "reason_damaged": "Механическое \"comment_reason_damaged\": ",
      "defects": "",
      "mechanical_damage": "",
      "package_damage": "",
      "shortage": "",
      "repair": "",
      "condition": ""
    }
  ]
}
```


---

## Установить скидку на уценённый товар

`POST /v1/product/update/discount`

Метод для установки размера скидки на уценённые товары, продающиеся по схеме FBS.

**Тело запроса** (`application/json`):
- **discount** `integer <int32>` *обязательный* — Размер скидки: от 3 до 99 процентов.
- **product_id** `integer <int64>` *обязательный* — Идентификатор товара в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "discount": 10,
  "product_id": 876763232
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `boolean` — Результат работы метода. true , если запрос выполнен без ошибок.

**Пример ответа (`200`):**

```json
{
  "result": true
}
```


---
