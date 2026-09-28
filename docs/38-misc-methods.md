# Прочие методы

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 441. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Получить информацию о стоках на складах FBO

## Получить информацию о стоках на складах FBO

`POST /v1/product/info/stocks-by-warehouse/fbo`

Передайте в запросе offer_ids или skus . Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **limit** `integer <uint64>` *обязательный* — Количество значений в ответе.
- **offer_ids** `Array of strings` — Идентификатор товаров в системе продавца — артикул.
- **skus** `Array of strings <int64>` — Идентификатор товаров в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "cursor": "string",
  "limit": 0,
  "offer_ids": [
    "string"
  ],
  "skus": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о стоках. |
| `default` | Ошибка. |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **has_next** `boolean` — true , если в ответе вернулись не все значения.
- **products** `Array of objects` — Остатки товаров FBO.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "has_next": true,
  "products": [
    {
      "offer_id": "string",
      "present": 0,
      "product_id": 0,
      "reserved": 0,
      "sku": 0,
      "warehouse_id": 0
    }
  ]
}
```


---

## Управление остатками

`POST /v1/analytics/manage/stocks`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Используйте метод, чтобы узнать, сколько товаров осталось на складах FBO. Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

> **Примечание:** 22 января 2026 года метод будет отключён. Переключитесь на

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтр.
- **limit** `integer <int32>` — Количество значений в ответе.
- **offset** `integer <int32>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , ответ начнётся с 11-го найденного элемента.

**Пример запроса:**

```json
{
  "filter": {
    "skus": [
      "string"
    ],
    "stock_types": [
      "STOCK_TYPE_VALID"
    ],
    "warehouse_ids": [
      "string"
    ]
  },
  "limit": 1,
  "offset": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об остатках |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **items** `Array of objects` — Товары.
  - **defect_stock_count** `integer <int64>` — Остаток дефектного товара, шт.
  - **expiring_stock_count** `integer <int64>` — Остаток товара с истекающим сроком годности, шт.
  - **name** `string` — Название товара.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
  - **valid_stock_count** `integer <int64>` — Остаток товара, доступного для продажи.
  - **waitingdocs_stock_count** `integer <int64>` — Остаток товара, ожидающего документы.
  - **warehouse_name** `string` — Название склада.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "defect_stock_count": 0,
      "expiring_stock_count": 0,
      "name": "string",
      "offer_id": "string",
      "sku": 0,
      "valid_stock_count": 0,
      "waitingdocs_stock_count": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---

## Получить отчёт о списанных товарах

`POST /v1/analytics/decommissioned-goods`

Соответствует разделу FBO → Списанные товары в личном кабинете. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **filter** `object` *обязательный* — Фильтры.
- **page** `integer <int32>` *обязательный* — Номер страницы, возвращаемой в запросе.
- **page_size** `integer <int32>` *обязательный* — Количество элементов на странице.
- **sort_by** `string` — Тип сортировки: DATE — по дате; DISPOSAL_FEE — по начислению.. Enum: `"DATE"`, `"DISPOSAL_FEE"`.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию, DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filter": {
    "compensation": [
      "NO_COMPENSATION"
    ],
    "date_from": "2019-08-24T14:15:22Z",
    "date_to": "2019-08-24T14:15:22Z",
    "delivery_schema": "FBO",
    "dispose_reasons": [
      "ECONOM_UTILIZATION"
    ],
    "posting_number": "string",
    "skus": [
      "string"
    ],
    "supply_id": 0
  },
  "page": 0,
  "page_size": 1,
  "sort_by": "DATE",
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт о списанных товарах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **items** `Array of objects` — Информация о товарах.
- **total_count** `integer <int32>` — Количество оставшихся товаров, которые можно получить в ответе.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "compensation_price": 0,
      "compensation_type": "NO_COMPENS ",
      "date": "2019-08-24T14:15:22Z",
      "delivery_schema": "FBO",
      "disposal_fee": 0,
      "dispose_reason": "ECONOM_UTILIZ \"posting_number\": \"string",
      "quantity": 0,
      "sku": 0,
      "supply_id": 0
    }
  ],
  "total_count": 0
}
```


---

## Получить информацию о сравнении категорий

`POST /v1/analytics/category/comparison`

Соответствует разделу Аналитика → Категории в личном кабинете. Метод доступен продавцам с подпиской Premium Pro. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтр.
- **group** `string` — Группировка данных в ответе: CATEGORY_3 — по категории 3-го уровня; SOURCE — по источнику продаж; SELLER — по продавцу; BRAND — по бренду; CLUSTER — по кластеру отгрузки; PRICE_BOUNDARY — по ценовому сегменту.. Enum: `"CATEGORY_3"`, `"SOURCE"`, `"SELLER"`, `"BRAND"`, `"CLUSTER"`, `"PRICE_BOUNDARY"`.
- **limit** `integer <uint64>` — Количество значений в ответе.
- **metric** `string` — Фильтр по метрикам: GMV — объём продаж в денежном выражении; GMV_GROWTH — объём продаж в процентах по сравнению с предыдущим периодом; ITEMS — количество проданных товаров; AIV — средняя стоимость одного проданного товара; AIV_GROWTH — рост средней стоимости товара в процентах; SELLERS — количество уникальных продавцов в категории или сегменте; BRANDS — количество уникальных брендов в категории или сегменте; CLUSTERS — кластры, регионы или города с похожими характеристиками продаж; CATEGORY_SHARE — доля категории в общем объёме продаж; LEADER_SHARE — доля лидера по продажам; BUYOUT — процент выкупа товаров.. Enum: `"GMV"`, `"GMV_GROWTH"`, `"ITEMS"`, `"AIV"`, `"AIV_GROWTH"`, `"SELLERS"`, `"BRANDS"`, `"CLUSTERS"`, `"CATEGORY_SHARE"`, `"LEADER_SHARE"`, `"BUYOUT"`.
- **offset** `integer <uint64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **period** `string` *обязательный* — Период: WEEK — неделя, MONTH — месяц, QUARTER — квартал, YEAR — год.. Enum: `"WEEK"`, `"MONTH"`, `"QUARTER"`, `"YEAR"`.
- **sort** `string` *обязательный* — Направление сортировки: ASC — по возрастанию, DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filter": {
    "brand_ids": [
      "string"
    ],
    "category": {
      "category_id": 0,
      "category_type": "CATEGORY_3",
      "is_own": true
    },
    "clothing_for": [
      "MALE"
    ],
    "price_segment": {
      "from": 1,
      "to": 1
    },
    "seller_ids": [
      "string"
    ]
  },
  "group": "CATEGORY_3",
  "limit": 0,
  "metric": "GMV",
  "offset": 0,
  "period": "WEEK",
  "sort": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о сравнении категорий |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернулись не все значения.
- **items** `Array of objects` — Массив данных.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "items": [
    {
      "id": "string",
      "label": "string",
      "max_rating": 0,
      "metric_aiv": 0,
      "metric_aiv_growth": 0,
      "metric_brands": 0,
      "metric_buyout": 0,
      "metric_category_share": 0,
      "metric_clusters": 0,
      "metric_gmv": 0,
      "metric_gmv_growth": 0,
      "metric_items": 0,
      "metric_leader_share": 0,
      "metric_sellers": 0,
      "rating": 0
    }
  ]
}
```


---

## Отчёт по вывозу и утилизации с поставки FBO

`POST /v1/removal/from-supply/list`

Метод соответствует разделу FBO → Вывоз и утилизация в личном кабинете. Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date_from** `string` *обязательный* — Дата начала отчётного периода в формате YYYY-MM-DD .
- **date_to** `string` *обязательный* — Дата окончания отчётного периода в формате YYYY-MM-DD .
- **last_id** `string` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.
- **limit** `integer <int32>` *обязательный* — Количество элементов в ответе.

**Пример запроса:**

```json
{
  "date_from": "2025-03-01",
  "date_to": "2025-03-30",
  "last_id": "",
  "limit": 500
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт по вывозу и утилизации с поставки FBO |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **last_id** `string` — Идентификатор последнего значения на странице.
- **returns_summary_report_rows** `Array of objects` — Информация о товарах.

**Пример ответа (`200`):**

```json
{
  "returns_summary_report_rows": [
    {
      "name": "Шурупы",
      "offer_id": "Шуруп-0001",
      "sku": "12314324",
      "barcode": "",
      "quantity_for_return": 1,
      "quant_count": 0,
      "box_id": "202501272",
      "return_id": "934457",
      "stock_type": "Излишек",
      "return_created_at": "2025-03-13 \"is_auto_return\": false",
      "clearing_warehouse_name": "ХОРУ \"return_state\": ",
      "delivery_type": "Вывоз с ПВЗ/СЦ \"preliminary_delivery_price\": 15 \"box_length\": 0.1",
      "box_width": 0.1,
      "box_height": 0.1,
      "box_volume": 34,
      "box_weight": 0.01,
      "box_state": "Доступно к вывозу",
      "destination_warehouse_name": "Р \"destination_warehouse_address\": ",
      "delivery_date": "2025-03-13T06: \"given_out_date\": ",
      "utilization_date": "2025-03-13T"
    }
  ],
  "last_id": "whcReturnId:934457_boxId:202"
}
```


---

## Отчёт по вывозу и утилизации со стока FBO

`POST /v1/removal/from-stock/list`

Метод соответствует разделу FBO → Вывоз и утилизация в личном кабинете. Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date_from** `string` *обязательный* — Дата начала отчётного периода в формате YYYY-MM-DD .
- **date_to** `string` *обязательный* — Дата окончания отчётного периода в формате YYYY-MM-DD .
- **last_id** `string` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.
- **limit** `integer <int32>` *обязательный* — Количество элементов в ответе.

**Пример запроса:**

```json
{
  "date_from": "2025-03-01",
  "date_to": "2025-03-30",
  "last_id": "",
  "limit": 500
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт по вывозу и утилизации со стока FBO |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **last_id** `string` — Идентификатор последнего значения на странице.
- **returns_summary_report_rows** `Array of objects` — Информация о товарах.

**Пример ответа (`200`):**

```json
{
  "returns_summary_report_rows": [
    {
      "name": "Шурупы",
      "offer_id": "Шуруп-0001",
      "sku": "12314324",
      "barcode": "",
      "quantity_for_return": 1,
      "quant_count": 0,
      "box_id": "202501272",
      "return_id": "934457",
      "stock_type": "Излишек",
      "return_created_at": "2025-03-13 \"is_auto_return\": false",
      "clearing_warehouse_name": "ХОРУ \"return_state\": ",
      "delivery_type": "Вывоз с ПВЗ/СЦ \"preliminary_delivery_price\": 15 \"box_length\": 0.1",
      "box_width": 0.1,
      "box_height": 0.1,
      "box_volume": 34,
      "box_weight": 0.01,
      "box_state": "Доступно к вывозу",
      "destination_warehouse_name": "Р \"destination_warehouse_address\": ",
      "delivery_date": "2025-03-13T06: \"given_out_date\": ",
      "utilization_date": "2025-03-13T"
    }
  ],
  "last_id": "whcReturnId:934457_boxId:202"
}
```


---

## Управлять скидкой от количества

`POST /v1/product/stairway-discount/by-quantity/set`

Устанавливает или удаляет скидку на товар в зависимости от его количества в заказе. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **stairways** `Array of objects` *обязательный* — Информация о скидке от количества по товарам.
- **suppress_warnings** `boolean` — Передайте true , чтобы игнорировать предупреждения и установить скидку.

**Пример запроса:**

```json
{
  "stairways": [
    {
      "enabled": true,
      "sku": 0,
      "stairway": {
        "steps": [
          {
            "discount": 0,
            "quantity": 0,
            "step": 0
          }
        ]
      }
    }
  ],
  "suppress_warnings": true
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Настройки скидки изменены |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **accepted** `boolean` — true , если запрос принят. Используйте метод /v1/product/stairway-discount/by-quantity/get, чтобы узнать результат изменения скидки.
- **errors** `Array of objects` — Описание ошибок.
- **warnings** `Array of objects` — Описание предупреждения.

**Пример ответа (`200`):**

```json
{
  "accepted": true,
  "errors": [
    {
      "data": [
        {
          "code": "string",
          "field": "string",
          "message": "string",
          "step": 0,
          "value": "string"
        }
      ],
      "sku": 0
    }
  ],
  "warnings": [
    {
      "data": [
        {
          "code": "string",
          "field": "string",
          "message": "string",
          "step": 0,
          "value": "string"
        }
      ],
      "sku": 0
    }
  ]
}
```


---

## Получить информацию о скидке от количества

`POST /v1/product/stairway-discount/by-quantity/get`

Возвращает информацию о скидке на товар в зависимости от его количества в заказе. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **skus** `Array of strings <int64>` *обязательный* — Список идентификаторов товара в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "skus": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация получена |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **stairways** `Array of objects` — Информация о скидке от количества по конкретному товару.
  - **enabled** `boolean` — true , если скидка от количества включена.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
  - **stairway** `object` — Информация об уровне скидки от количества.
  - **status** `string` — Статус изменения скидки от количества. Возможные значения: ERROR — ошибка при изменении скидки. Вызовите метод /v1/product/stairway- discount/by-quantity/set ещё раз. IN_PROCESS — изменение в процессе. SUCCESS — изменение скидки применено к товару.. Enum: `"IN_PROCESS"`, `"ERROR"`, `"SUCCESS"`.

**Пример ответа (`200`):**

```json
{
  "stairways": [
    {
      "enabled": true,
      "sku": 0,
      "stairway": {
        "steps": [
          {
            "discount": 0,
            "quantity": 0,
            "step": 0
          }
        ]
      },
      "status": "IN_PROCESS"
    }
  ]
}
```


---

## Получить отчёт о балансе

`POST /v1/finance/balance`

Соответствует разделу Финансы → Баланс в личном кабинете. Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date_from** `string <date-time>` *обязательный* — Дата начала отчётного периода в формате YYYY-MM-DD .
- **date_to** `string <date-time>` *обязательный* — Дата окончания отчётного периода в формате YYYY-MM-DD . Максимальный период между date_from и date_to — 30 дней.

**Пример запроса:**

```json
{
  "date_from": "2019-08-24",
  "date_to": "2019-09-24"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт о балансе |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cashflows** `object` — Информация о доходах и расходах.
- **total** `object` — Общие данные по балансу за период.

**Пример ответа (`200`):**

```json
{
  "cashflows": {
    "returns": {
      "amount": {
        "currency_code": "string",
        "value": 0
      },
      "amount_details": {
        "partner_programs": {
          "currency_code": "string",
          "value": 0
        },
        "points_for_discounts": "stri \"revenue\": { \"currency_code\": \"string\" \"value\": 0 }"
      },
      "fee": {
        "currency_code": "string",
        "value": 0
      }
    },
    "sales": {
      "amount": {
        "currency_code": "string",
        "value": 0
      },
      "amount_details": {
        "partner_programs": {
          "currency_code": "string",
          "value": 0
        },
        "points_for_discounts": "stri \"revenue\": { \"currency_code\": \"string\" \"value\": 0 }"
      },
      "fee": {
        "currency_code": "string",
        "value": 0
      }
    },
    "services": [
      {
        "amount": {
          "currency_code": "string",
          "value": 0
        },
        "name": "string"
      }
    ]
  },
  "total": {
    "accrued": {
      "currency_code": "string",
      "value": 0
    },
    "closing_balance": {
      "currency_code": "string",
      "value": 0
    },
    "opening_balance": {
      "currency_code": "string",
      "value": 0
    },
    "payments": [
      {
        "currency_code": "string",
        "value": 0
      }
    ]
  }
}
```


---

## Получить список заявок на скидку

`POST /v2/actions/discounts-task/list`

Возвращает список товаров, которые покупатели хотят купить со скидкой. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. При первом запросе оставьте это поле пустым.
- **limit** `integer <int64>` — Максимальное количество заявок на странице.
- **status** `string` — Статус заявки на скидку: ALL — все статусы, NEW — новая, APPROVED — одобренная, DECLINED — отклонённая.. Enum: `"ALL"`, `"NEW"`, `"APPROVED"`, `"DECLINED"`.

**Пример запроса:**

```json
{
  "last_id": 0,
  "limit": 50,
  "status": "ALL"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список заявок |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **tasks** `Array of objects` — Список заявок.
  - **approved_discount** `number <double>` — Скидка в рублях, которую одобрил продавец. Передайте значение 0 , если продавец не одобрил заявку.
  - **approved_price** `number <double>` — Одобренная цена.
  - **approved_quantity_max** `integer <uint64>` — Максимальное одобренное количество товаров.
  - **auto_moderated_info** `object` — Информация об автоматической модерации заявки.
  - **created_at** `string <date-time>` — Дата создания заявки.
  - **edited_till** `string <date-time> YYYY-MM-DD` — Время для изменения решения.
  - **edited_till_duration** `integer <uint64>` — Время для изменения решения в секундах.
  - **email** `string` — Электронный адрес сотрудника продавца, который обработал заявку.
  - **end_at** `string <date-time>` — Время окончания действия заявки.
  - **end_at_duration** `integer <uint64>` — Время окончания действия заявки в секундах.
  - **first_name** `string` — Имя сотрудника продавца, который обработал заявку.
  - **id** `integer <uint64>` — Идентификатор заявки.
  - **is_auto_moderated** `boolean` — true , если модерация была автоматической.
  - **last_name** `string` — Фамилия сотрудника продавца, который обработал заявку.
  - **min_auto_price** `number <double>` — Минимальное значение цены после автоприменения скидок и акций.
  - **moderated_at** `string <date-time>` — Дата модерации: просмотра, одобрения или отклонения заявки.
  - **name** `string` — Название товара.
  - **original_price** `number <double>` — Цена товара до всех скидок.
  - **patronymic** `string` — Отчество сотрудника продавца, который обработал заявку.
  - **reduction_factor** `number <double>` — Разница между ценой пользователя и продавца в момент создания заявки.
  - **requested_discount** `number <double>` — Скидка в процентах.
  - **requested_price** `number <double>` — Цена по заявке.
  - **requested_quantity_max** `integer <uint64>` — Запрошенное максимальное количество товаров.
  - **sku** `integer <uint64>` — Идентификатор товара в системе Ozon — SKU.
  - **status** `string` — Статус заявки на скидку: ALL — все статусы, NEW — новая, APPROVED — одобренная, DECLINED — отклонённая.. Enum: `"ALL"`, `"NEW"`, `"APPROVED"`, `"DECLINED"`.

**Пример ответа (`200`):**

```json
{
  "tasks": [
    {
      "approved_discount": 0,
      "approved_price": 0,
      "approved_quantity_max": 0,
      "auto_moderated_info": {
        "max_percent": 0,
        "max_price": 0,
        "min_percent": 0,
        "min_price": 0
      },
      "created_at": "2019-08-24T14:15: ",
      "edited_till": "2019-08-24T14:15 \"edited_till_duration\": 0",
      "email": "string",
      "end_at": "2019-08-24T14:15:22Z",
      "end_at_duration": 0,
      "first_name": "string",
      "id": 0,
      "is_auto_moderated": true,
      "last_name": "string",
      "min_auto_price": 0,
      "moderated_at": "2019-08-24T14:1 \"name\": \"string",
      "original_price": 0,
      "patronymic": "string",
      "reduction_factor": 0,
      "requested_discount": 0,
      "requested_price": 0,
      "requested_quantity_max": 0,
      "sku": 0,
      "status": "ALL"
    }
  ]
}
```


---

## Настроить видимость товара на витрине Ozon и Ozon Селект

`POST /v1/product/visibility/set`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

> **Примечание:** Метод доступен продавцам, которые подключены к Ozon Селект

> **Примечание:** или Ozon Доставке.

**Тело запроса** (`application/json`):
- **item_placement** `Array of objects` *обязательный* — Информация о видимости товара.

**Пример запроса:**

```json
{
  "item_placement": [
    {
      "placement": "OZON",
      "sku": 0
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Видимость товара настроена |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **items** `Array of objects` — Информация о видимости товаров.
- **items_errors** `Array of objects` — Товары с ошибками.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "select_permission": "UNSPECIFIE \"seller_item_placement\": ",
      "seller_item_placement_list": [
        "UNSPECIFIED"
      ],
      "showcases_visibility": "UNSPECI \"showcases_visibility_list\": [ \"UNSPECIFIED\" ]",
      "sku": 0,
      "warnings": [
        "string"
      ]
    }
  ],
  "items_errors": [
    {
      "code": "string",
      "sku": 0
    }
  ]
}
```


---

## Получить список отправлений

`POST /v2/posting/digital/list`

Возвращает список отправлений, по которым нужно загрузить коды цифровых товаров. Метод доступен только продавцам, которые работают с цифровыми товарами. Чтобы получить список отправлений в любом статусе, используйте метод /v3/posting/fbo/list. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр для поиска отправлений.
- **limit** `integer <int64>` — Количество значений в ответе.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "sort_dir": "asc",
  "filter": {
    "posting_numbers": [
      "42776709-0200-5"
    ],
    "order_numbers": [
      "12345-1"
    ],
    "since": "2025-05-10T06:49:21.122Z",
    "to": "2025-12-10T06:49:21.122Z"
  },
  "limit": 100,
  "cursor": "",
  "with": {
    "analytics_data": false,
    "financial_data": true,
    "legal_info": true
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список отправлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **has_next** `boolean` — true , если в ответе вернулись не все отправления.
- **postings** `Array of objects` — Список отправлений.

**Пример ответа (`200`):**

```json
{
  "postings": [
    {
      "order_id": 29137896277,
      "order_number": "42776709-0200",
      "posting_number": "42776709-0200 \"status\": \"delivered",
      "cancel_reason_id": 0,
      "created_at": "2025-05-10T06:49: ",
      "in_process_at": "2025-05-10T06: \"legal_info\": { \"company_name\": ",
      "inn": "770123456789",
      "kpp": "770101001"
    },
    {
      "products": [
        {
          "sku": 1624109204,
          "name": "Слипоны демисезо \"offer_id\": \"S5257022-30\" \"price\": { \"amount\": \"1461.00",
          "currency": "RUB"
        },
        {
          "quantity": 1
        }
      ],
      "analytics_data": {
        "city": "",
        "delivery_type": "",
        "is_premium": false,
        "payment_type_group_name": "",
        "warehouse_id": null,
        "warehouse_name": "",
        "is_legal": false
      },
      "financial_data": {
        "products": [
          {
            "product_id": 16241092,
            "commission": {
              "amount": 0,
              "percent": 0,
              "currency": "RUB"
            },
            "payout": 0,
            "old_price": 1461,
            "price": 1461,
            "total_discount_value": "actions",
            "quantity": 1
          }
        ],
        "cluster_from": "Екатеринбург \"cluster_to\": \"Екатеринбург\""
      },
      "cancellation": {
        "cancellation_type": "Client",
        "cancellation_initiator": "Кл"
      },
      "external_order": {
        "is_external": false,
        "platform_name": ""
      },
      "additional_data": []
    }
  ],
  "has_next": false,
  "cursor": ""
}
```


---

## Получить начисления по отправлениям

`POST /v1/finance/accrual/postings`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **posting_numbers** `Array of strings` *обязательный* — Номера отправлений.

**Пример запроса:**

```json
{
  "posting_numbers": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Начисления по отправлениям |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **posting_accruals** `Array of objects` — Список начислений по отправлениям.
  - **accruals** `Array of objects` — Список начислений.
  - **posting_number** `string` — Номер отправления.

**Пример ответа (`200`):**

```json
{
  "posting_accruals": [
    {
      "accruals": [
        {
          "accrual_date": "string",
          "accrued": {
            "amount": "string",
            "currency": "string"
          },
          "quantity": 0,
          "seller_price": {
            "amount": "string",
            "currency": "string"
          },
          "sku": 0,
          "type_id": 0
        }
      ],
      "posting_number": "string"
    }
  ]
}
```


---

## Получить справочник начислений

`POST /v1/finance/accrual/types`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Справочник начислений |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **accrual_types** `Array of objects` — Информация о начислениях.
  - **description** `string` — Описание начисления.
  - **id** `integer <int32>` — Идентификатор начисления.
  - **name** `string` — Название начисления.

**Пример ответа (`200`):**

```json
{
  "accrual_types": [
    {
      "description": "string",
      "id": 0,
      "name": "string"
    }
  ]
}
```


---

## Получить начисления за день

`POST /v1/finance/accrual/by-day`

Если укажете last_id в запросе, передайте значение date из предыдущего запроса, иначе вернётся ошибка 400 Bad Request . Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **date** `string YYYY-MM-DD` *обязательный* — Дата начислений. Самая ранняя — 1 января 2022 года. Если укажете last_id , передайте значение date из предыдущего запроса.
- **last_id** `string` *обязательный* — Идентификатор последнего значения на странице. При первом запросе оставьте это поле пустым. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса. Срок жизни идентификатора — 15 минут.

**Пример запроса:**

```json
{
  "date": "string",
  "last_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Начисления за день |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **accruals** `Array of objects` — Список начислений по отправлению.
- **last_id** `string` — Идентификатор последнего значения на странице. Срок жизни идентификатора — 15 минут.

**Пример ответа (`200`):**

```json
{
  "accruals": [
    {
      "accrued_category": "UNSPECIFIED \"container_fees\": { \"fees\": [ { \"accrued\": { \"amount\": \"string\" \"currency\": "
    },
    {
      "type_id": 0
    }
  ],
  "date": "string",
  "item_fees": {
    "fees": [
      {
        "fees": [
          {
            "accrued": {
              "amount": " \"currency\":"
            },
            "type_id": 0
          }
        ],
        "sku": 0
      }
    ]
  },
  "non_item_fee": {
    "accrued": {
      "amount": "string",
      "currency": "string"
    },
    "type_id": 0
  },
  "posting": {
    "delivery_schema": "string",
    "delivery_speed": 0,
    "products": [
      {
        "commission": {
          "bonus": {
            "amount": "stri \"currency\": "
          },
          "coinvestment": {
            "amount": "stri \"currency\": "
          },
          "commission": {
            "amount": "stri \"currency\": "
          },
          "commission_ratio": "sale_amount",
          "amount": "stri \"currency\": "
        },
        "sale_commission": "amount\": \"stri \"currency\": "
      },
      {
        "sale_price": {
          "amount": "stri \"currency\": "
        },
        "seller_price": {
          "amount": "stri \"currency\": "
        }
      },
      {
        "delivery": {
          "services": [
            {
              "accrued": "amount "
            },
            {
              "type_id": ""
            }
          ],
          "total_accrued": {
            "amount": "stri \"currency\": "
          }
        },
        "sku": 0
      }
    ]
  },
  "total_amount": {
    "amount": "string",
    "currency": "string"
  },
  "accrual_id": 0,
  "unit_number": "string"
}
```


---

## Получить информацию о видимости товара

`POST /v1/product/visibility/info`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **skus** `Array of strings <int64>` — Идентификаторы товаров в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "skus": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о видимости товара |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **items** `Array of objects` — Список товаров.
  - **showcases_visibility** `string` — На каких витринах показывается товар: UNSPECIFIED — не определено; OZON — только на Ozon; SELECT — только на Селект; OZON_SELECT — на Селект и Ozon; NONE — товар скрыт везде.. Enum: `"UNSPECIFIED"`, `"OZON"`, `"SELECT"`, `"OZON_SELECT"`, `"NONE"`.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "showcases_visibility": "UNSPECI \"sku\": 0 }"
    }
  ]
}
```


---

## Получить информацию об отправлении по идентификатору

`POST /v1/posting/fbp/get`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Идентификатор отправления.

**Пример запроса:**

```json
{
  "posting_number": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отправлении |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **posting** `object` — Информация об отправлении.
  - **analytics_data** `object` — Данные аналитики.
  - **cancellation** `object` — Информация об отмене.
  - **financial_data** `object` — Финансовые данные.
  - **in_process_at** `string <date-time>` — Дата и время начала обработки отправления.
  - **order_date** `string <date-time>` — Дата создания заказа.
  - **order_id** `integer <int64>` — Идентификатор заказа, к которому относится отправление.
  - **order_number** `string` — Номер заказа, к которому относится отправление.
  - **posting_number** `string` — Идентификатор отправления.
  - **products** `Array of objects` — Список товаров в отправлении.
  - **status** `integer <int64>` — Статус отправления.
  - **substatus** `string` — Подстатус отправления.
  - **tpl_provider_id** `integer <int64>` — Идентификатор провайдера доставки.

**Пример ответа (`200`):**

```json
{
  "posting": {
    "analytics_data": {
      "city": "string",
      "delivery_date_begin": "2019-08- \"delivery_date_end\": ",
      "delivery_type": "string",
      "region": "string",
      "warehouse_id": 0
    },
    "cancellation": {
      "cancel_reason": "string",
      "cancel_reason_id": 0,
      "cancellation_initiator": "strin \"cancellation_type\": \"string\""
    },
    "financial_data": {
      "cluster_from": "string",
      "cluster_to": "string",
      "delivery_amount": 0,
      "products": [
        {
          "actions": [
            {
              "action_id": 0,
              "action_type": "st \"date_from\": ",
              "date_to": "2019-0 \"description\": \"st \"discount_percent",
              "discount_value": ""
            }
          ],
          "commissions_price": {
            "amount": "string",
            "currency": "string"
          },
          "customer_price": {
            "amount": "string",
            "currency": "string"
          },
          "old_price": 0,
          "posting_commission": {
            "amount": 0,
            "payout": 0,
            "percent": 0
          },
          "quantity": 0,
          "return_commission": {
            "amount": 0,
            "payout": 0,
            "percent": 0
          },
          "seller_price": {
            "amount": "string",
            "currency": "string"
          },
          "sku": 0,
          "total_discount_percent": "total_discount_value"
        }
      ]
    }
  },
  "in_process_at": "2019-08-24T14:15:2 ",
  "order_date": "2019-08-24T14:15:22Z",
  "order_id": 0,
  "order_number": "string",
  "posting_number": "string",
  "products": [
    {
      "has_imei": true,
      "marketplace_seller_price": {
        "amount": "string",
        "currency": "string"
      },
      "name": "string",
      "offer_id": "string",
      "quantity": 0,
      "sku": 0,
      "weight_max": 0
    }
  ],
  "status": 0,
  "substatus": "string",
  "tpl_provider_id": 0
}
```


---

## Получить позаказный отчёт о реализации товаров

`POST /v1/report/realization/posting/create`

Отчёт о реализации доставленных и возвращённых товаров с детализацией по каждому заказу. Не включает отмены и невыкупы. Отчёт доступен с настоящего времени по август 2023 года включительно. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **month** `integer <int32>` *обязательный* — Месяц.
- **year** `integer <int32>` *обязательный* — Год.

**Пример запроса:**

```json
{
  "month": 0,
  "year": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Позаказный отчёт о реализации |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **code** `string` — Уникальный идентификатор отчёта. Получите отчёт методом /v1/report/info.

**Пример ответа (`200`):**

```json
{
  "code": "string"
}
```


---

## Получить параметры для создания сертификата качества

`POST /v2/product/certification/options`

Используйте информацию о параметрах в запросе метода Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Параметры для создания сертификата |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **option** `Array of objects` — Параметры для создания сертификата.
  - **name** `string` *обязательный* — Название параметра сертификата: NAME — название; CERTIFICATE_TYPE — тип; NUMBER — номер; FILES — файл с сертификатом в кодировке Base64; CERTIFICATE_COUNTRY — страна выдачи; ACCORDANCE_TYPE — стандарт сертификации; SKUS — список идентификаторов товара в системе Ozon, SKU; ISSUE_DATE — дата выпуска; EXPIRED_DATE — дата истечения; LINK_TO_REGISTRY — ссылка на государственный реестр; PRODUCT_TYPE — тип товаров; INFINITE — бессрочность. true , если параметр обязательный.

**Пример ответа (`200`):**

```json
{
  "option": [
    {
      "name": "string",
      "required": true
    }
  ]
}
```


---

## Получить обязательные параметры для создания сертификата качества

`POST /v2/product/certification/params`

Используйте информацию о параметрах в запросе метода Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **params** `object` — Параметры для создания сертификата.

**Пример запроса:**

```json
{
  "params": {
    "accordance_type": "UNKNOWN",
    "certificate_country": "st",
    "certificate_type": "UNKNOWN",
    "expired_date": {
      "date": {
        "day": 0,
        "month": 0,
        "year": 0
      },
      "infinite": true
    },
    "files": [
      {
        "file_content": "string",
        "name": "string"
      }
    ],
    "issue_date": "2019-08-24T14:15:22Z",
    "link_to_registry": "string",
    "name": "string",
    "number": "string",
    "product_type": "UNKNOWN",
    "skus": [
      "string"
    ]
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Обязательные параметры для создания сертификата |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **params** `Array of objects` — Параметры для создания сертификата.
  - **name** `string` *обязательный* — Название параметра сертификата: NAME — название; CERTIFICATE_TYPE — тип; NUMBER — номер; FILES — файл с сертификатом в кодировке Base64; CERTIFICATE_COUNTRY — страна выдачи; ACCORDANCE_TYPE — стандарт сертификации; SKUS — список идентификаторов товара в системе Ozon, SKU; ISSUE_DATE — дата выпуска; EXPIRED_DATE — дата истечения; LINK_TO_REGISTRY — ссылка на государственный реестр; PRODUCT_TYPE — тип товаров; INFINITE — бессрочность. true , если параметр обязательный.

**Пример ответа (`200`):**

```json
{
  "params": [
    {
      "name": "string",
      "required": true
    }
  ]
}
```


---

## Создать сертификат качества

`POST /v2/product/certificate/create`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **params** `object` — Параметры для создания сертификата.

**Пример запроса:**

```json
{
  "params": {
    "accordance_type": "SAFETY_DATA_SHEE \"certificate_country\": \"RU",
    "certificate_type": "SAFETY_DATA_SHE \"expired_date\": { \"date\": { \"day\": 1",
    "month": 1,
    "year": 2027
  },
  "infinite": false,
  "files": [
    {
      "file_content": "string",
      "name": "file.pdf"
    }
  ],
  "issue_date": "2019-08-24T14:15:22Z",
  "link_to_registry": "string",
  "name": "string",
  "number": "string",
  "product_type": "UNKNOWN",
  "skus": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Сертификат создан |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **certificate_id** `integer <int64>` — Идентификатор сертификата. Если null , сертификат создать не удалось.
- **params** `Array of objects` — Информация о параметрах в запросе.
- **status** `string` — Статус сертификата: INCOMPLETE — не загружен, некоторые параметры переданы некорректно; COMPLETED — загружен.. Enum: `"INCOMPLETE"`, `"COMPLETED"`.

**Пример ответа (`200`):**

```json
{
  "certificate_id": 0,
  "params": [
    {
      "error": "string",
      "name": "string",
      "state": "VALID"
    }
  ],
  "status": "INCOMPLETE"
}
```


---

## Получить зависимые характеристики

`POST /v1/description-category/dependent-attributes`

Возвращает пары идентификаторов родительской и дочерней характеристик. Получите возможные значения дочерней характеристики для значений родительской методом /v1/description- category/dependent-attributes/values. Характеристика с parent_attribute_id = 8229 — это идентификатор типа товара type_id . Не указывайте её в параметре items.attributes.id в запросах к методам /v3/product/import и Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **description_category_id** `integer <int64>` *обязательный* — Идентификатор категории из метода /v1/description- category/tree.
- **type_id** `integer <int64>` — Идентификатор типа товара из метода /v1/description-category/tree.

**Пример запроса:**

```json
{
  "description_category_id": 234123,
  "type_id": 123123
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Зависимые характеристики |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Информация о зависимых характеристиках.
  - **child_attribute_id** `integer <int64>` — Идентификатор дочерней характеристики.
  - **parent_attribute_id** `integer <int64>` — Идентификатор родительской характеристики.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "child_attribute_id": 4812,
      "parent_attribute_id": 8229
    }
  ]
}
```


---

## Получить возможные значения дочерней характеристики

`POST /v1/description-category/dependent-attributes/values`

Возвращает возможные значения дочерней характеристики для значений родительской. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **child_attribute_id** `integer <int64>` *обязательный* — Идентификатор дочерней характеристики.
- **cursor** `string` — Указатель для выборки следующих данных.
- **description_category_id** `integer <int64>` — Идентификатор категории из метода /v1/description- category/tree.
- **limit** `integer <int64>` — Количество значений в ответе.
- **parent_attribute_id** `integer <int64>` *обязательный* — Идентификатор родительской характеристики.
- **type_id** `integer <int64>` — Идентификатор типа товара из метода /v1/description-category/tree.

**Пример запроса:**

```json
{
  "parent_attribute_id": 8229,
  "child_attribute_id": 23348,
  "description_category_id": 234123,
  "type_id": 123123,
  "limit": 4,
  "cursor": ""
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Возможные значения дочерней характеристики |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **result** `Array of objects` — Информация о зависимых характеристиках.
  - **children** `Array of objects` — Информация о дочерних характеристиках.
  - **parent_value** `string` — Значение родительской характеристики.
  - **parent_value_id** `integer <int64>` — Идентификатор значения родительской характеристики.

**Пример ответа (`200`):**

```json
[
  {
    "cursor": "eyJwYXJlbnRfdmFsdWVfaWQiOjEwM \"result\": [ { \"parent_value_id\": 1001",
    "parent_value": "Лада",
    "children": [
      {
        "child_value_id": 2001,
        "child_value": "Гранта"
      },
      {
        "child_value_id": 2002,
        "child_value": "Приора"
      },
      {
        "child_value_id": 2003,
        "child_value": "Веста"
      }
    ]
  },
  {
    "parent_value_id": 1002,
    "parent_value": "Тойота",
    "children": [
      {
        "child_value_id": 2004,
        "child_value": "Королла"
      }
    ]
  }
]
```


---

## Получить общую информацию о локальности продаж

`POST /v1/analytics/local-sale/total`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **overpayment_items** `object` — Товары с наибольшей переплатой.
- **period** `object` — Период.

**Пример запроса:**

```json
{
  "overpayment_items": {
    "count": 0,
    "with_top_overpayment_items": true
  },
  "period": {
    "from": "string",
    "to": "string"
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о локальности продаж |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **fbo_quantity** `integer <int64>` — Количество товаров, которые продаются по схеме FBO.
- **local_data** `object` — Информация о локальных продажах.
- **overpayment** `object` — Информация о переплате по логистике.
- **overpayment_items** `Array of objects` — Товары с наибольшей переплатой.
- **overpayment_reasons** `Array of objects` — Причины переплат за логистику.

**Пример ответа (`200`):**

```json
{
  "fbo_quantity": 0,
  "local_data": {
    "index": 0,
    "local_quantity": 0,
    "total_quantity": 0
  },
  "overpayment": {
    "delta": 0,
    "non_local_delivery": 0,
    "total": 0
  },
  "overpayment_items": [
    {
      "delivery_schema": [
        "FBO"
      ],
      "image": "string",
      "name": "string",
      "offer_id": "string",
      "sku": 0,
      "total_overpayment": 0
    }
  ],
  "overpayment_reasons": [
    {
      "amount": 0,
      "quantity": 0,
      "reason": "NO_SUPPLIES_TO_CLUSTE }"
    }
  ]
}
```


---

## Получить информацию о локальности продаж по кластерам

`POST /v1/analytics/local-sale/clusters-items/info`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество товаров в ответе.
- **offset** `integer <int64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **sort_by** `string` — Параметр, по которому будут отсортированы товары: IMPACT_SHARE — доля влияния на переплату; LOCALITY — доля локальных продаж; OVERPAYMENT_TOTAL — общая переплата за логистику; OVERPAYMENT_NON_LOCAL — наценка за нелокальную продажу; OVERPAYMENT_DELTA — разница с тарифом для локальной продажи.. Enum: `"IMPACT_SHARE"`, `"LOCALITY"`, `"OVERPAYMENT_TOTAL"`, `"OVERPAYMENT_NON_LOCAL"`, `"OVERPAYMENT_DELTA"`.
- **sort_dir** `string` — Направление сортировки: ASC — во возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filter": {
    "delivery_schema": "ALL",
    "description_categories": [
      {
        "category_id": 0,
        "children_category_id": 0,
        "type_id": 0
      }
    ],
    "macrolocal_cluster_from_ids": [
      "string"
    ],
    "macrolocal_cluster_to_ids": [
      "string"
    ],
    "overpayment_reasons": [
      "NO_SUPPLIES_TO_CLUSTER"
    ],
    "period": {
      "from": "string",
      "to": "string"
    },
    "skus": [
      "string"
    ],
    "supply_period": "ONE_WEEK"
  },
  "limit": 1,
  "offset": 0,
  "sort_by": "IMPACT_SHARE",
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о локальности продаж по кластерам |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **items** `Array of objects` — Список товаров.
- **total** `integer <int64>` — Общее количество товаров.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "cluster_to_id": 0,
      "item": {
        "delivery_schemas": [
          "FBO"
        ],
        "image": "string",
        "name": "string",
        "offer_id": "string",
        "sku": 0
      },
      "metrics": {
        "attention_level": "LOW",
        "impact_share": 0,
        "local_data": {
          "index": 0,
          "local_quantity": 0,
          "total_quantity": 0
        },
        "overpayment": {
          "delta": 0,
          "non_local_delivery": 0,
          "total": 0
        },
        "overpayment_reasons": [
          {
            "amount": 0,
            "quantity": 0,
            "reason": "NO_SUPPLIES"
          }
        ],
        "price": 0,
        "recommended_supply": 0
      }
    }
  ],
  "total": 0
}
```


---

## Получить информацию о локальности продаж товара по кластерам

`POST /v1/analytics/local-sale/items-clusters/info`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество товаров в ответе.
- **offset** `integer <int64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **sort_by** `string` — Параметр, по которому будут отсортированы товары: IMPACT_SHARE — доля влияния на переплату; LOCALITY — доля локальных продаж; OVERPAYMENT_TOTAL — общая переплата за логистику; OVERPAYMENT_NON_LOCAL — наценка за нелокальную продажу; OVERPAYMENT_DELTA — разница с тарифом для локальной продажи.. Enum: `"IMPACT_SHARE"`, `"LOCALITY"`, `"OVERPAYMENT_TOTAL"`, `"OVERPAYMENT_NON_LOCAL"`, `"OVERPAYMENT_DELTA"`.
- **sort_dir** `string` — Направление сортировки: ASC — во возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filter": {
    "delivery_schema": "ALL",
    "description_categories": [
      {
        "category_id": 0,
        "children_category_id": 0,
        "type_id": 0
      }
    ],
    "macrolocal_cluster_from_ids": [
      "string"
    ],
    "macrolocal_cluster_to_ids": [
      "string"
    ],
    "overpayment_reasons": [
      "NO_SUPPLIES_TO_CLUSTER"
    ],
    "period": {
      "from": "string",
      "to": "string"
    },
    "skus": [
      "string"
    ],
    "supply_period": "ONE_WEEK"
  },
  "limit": 1,
  "offset": 0,
  "sort_by": "IMPACT_SHARE",
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о локальности продаж товара |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **items** `Array of objects` — Список товаров.
- **total** `integer <int64>` — Общее количество товаров.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "macrolocal_cluster_to_id": 0,
      "metrics": {
        "attention_level": "LOW",
        "impact_share": 0,
        "local_data": {
          "index": 0,
          "local_quantity": 0,
          "total_quantity": 0
        },
        "overpayment": {
          "delta": 0,
          "non_local_delivery": 0,
          "total": 0
        },
        "overpayment_reasons": [
          {
            "amount": 0,
            "quantity": 0,
            "reason": "NO_SUPPLIES"
          }
        ],
        "price": 0,
        "recommended_supply": 0
      },
      "sku": 0
    }
  ],
  "total": 0
}
```


---

## Получить список пунктов возврата для склада rFBS

`POST /v1/warehouse/rfbs/return-point/list`

Используйте метод при создании и обновлении складов rFBS и rFBS Express. Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **filters** `object` *обязательный* — Фильтры для поиска пунктов возврата.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.
- **limit** `integer <int32>` *обязательный* — Количество значений в ответе.

**Пример запроса:**

```json
{
  "filters": {
    "address": "Россия",
    "coordinates": {
      "latitude": 0,
      "longitude": 0
    },
    "country_code": "RU",
    "ids": [
      "1020001267468000"
    ],
    "types": [
      "PVZ"
    ],
    "warehouse_id": 920819
  },
  "last_id": 12,
  "limit": 10
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список пунктов возврата |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **points** `Array of objects` — Список пунктов возврата.
  - **address** `string` — Адрес пункта возврата.
  - **coordinates** `object` — Координаты пункта возврата.
  - **id** `integer <int64>` — Идентификатор пункта возврата.
  - **name** `string` — Название пункта возврата.
  - **type** `string` — Тип пункта возврата: PVZ — пункт выдачи заказов; PPZ — пункт приёма заказов.. Enum: `"PVZ"`, `"PPZ"`.
  - **utc_offset** `integer <int32>` — Смещение часового пояса от UTC-0 в минутах.
  - **working_days** `Array of objects` — Рабочие дни пункта возврата.

**Пример ответа (`200`):**

```json
{
  "points": [
    {
      "address": "Россия",
      "coordinates": {
        "latitude": 0,
        "longitude": 0
      },
      "id": 1020001267468000,
      "name": "МОСКВА_5259",
      "type": "PVZ",
      "utc_offset": 180,
      "working_days": [
        {
          "date": "2026-07-27",
          "day": "MONDAY",
          "from": "10:00",
          "to": "20:00"
        },
        {
          "date": "2026-07-28",
          "day": "TUESDAY",
          "from": "10:00",
          "to": "20:00"
        },
        {
          "date": "2026-07-29",
          "day": "WEDNESDAY",
          "from": "10:00",
          "to": "20:00"
        },
        {
          "date": "2026-07-30",
          "day": "THURSDAY",
          "from": "10:00",
          "to": "20:00"
        },
        {
          "date": "2026-07-31",
          "day": "FRIDAY",
          "from": "10:00",
          "to": "20:00"
        },
        {
          "date": "2026-08-01",
          "day": "SATURDAY",
          "from": "10:00",
          "to": "20:00"
        },
        {
          "date": "2026-08-02",
          "day": "SUNDAY",
          "from": "10:00",
          "to": "20:00"
        }
      ]
    }
  ]
}
```


---
