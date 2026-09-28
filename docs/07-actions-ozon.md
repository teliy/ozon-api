# Акции Ozon

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 90. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

Для продвижения товаров участвуйте в акциях, которые Ozon проводит для покупателей. Подробнее об акциях в Базе

знаний продавца.

## Список акций

`GET /v1/actions`

Метод для получения списка акций Ozon, в которых можно участвовать. Подробнее об акциях Ozon

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список акций |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результаты запроса.
  - **id** `number <double>` — Идентификатор акции.
  - **title** `string` — Название акции.
  - **action_type** `string` — Тип акции.
  - **description** `string` — Описание акции.
  - **date_start** `string` — Дата начала акции.
  - **date_end** `string` — Дата окончания акции.
  - **auto_add_dates** `Array of strings <date-time>` — Дата и время автодобавления товаров в акцию.
  - **freeze_date** `string` — Дата приостановки акции. Если поле заполнено, продавец не может повышать цены, изменять список товаров и уменьшать количество единиц товаров в акции. Продавец может понижать цены и увеличивать количество единиц товара в акции.
  - **potential_products_count** `number <double>` — Количество товаров, доступных для акции.
  - **participating_products_count** `number <double>` — Количество товаров, которые участвуют в акции.
  - **is_participating** `boolean` — Участвуете вы в этой акции или нет.
  - **is_voucher_action** `boolean` — Признак, что для участия в акции покупателям нужен промокод.
  - **banned_products_count** `number <double>` — Количество заблокированных товаров.
  - **with_targeting** `boolean` — Признак, что акция с целевой аудиторией.
  - **order_amount** `number <double>` — Сумма заказа.
  - **discount_type** `string` — Тип скидки.
  - **discount_value** `number <double>` — Размер скидки.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "id": 71342,
      "title": "test voucher #2",
      "date_start": "2021-11-22T09:46: ",
      "date_end": "2021-11-30T20:59:59 ",
      "auto_add_dates": [
        "2025-12-30T20:59:59Z"
      ],
      "potential_products_count": 0,
      "is_participating": true,
      "participating_products_count": "description\": \"",
      "action_type": "DISCOUNT",
      "banned_products_count": 0,
      "with_targeting": false,
      "discount_type": "UNKNOWN",
      "discount_value": 0,
      "order_amount": 0,
      "freeze_date": "",
      "is_voucher_action": true
    }
  ]
}
```


---

## Получить список товаров, которые могут участвовать в акции

`POST /v2/actions/candidates`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

> **Примечание:** До 13 октября 2026 года метод работает аналогично

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` — Идентификатор акции. Получите методом /v1/actions.
- **last_id** `string` — Идентификатор последнего значения на странице. При первом запросе оставьте пустым.
- **limit** `integer <uint64>` — Количество значений на странице.

**Пример запроса:**

```json
{
  "action_id": 258568,
  "last_id": "80698",
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров, которые могут участвовать в акции |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **last_id** `string` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, передайте полученное значение в следующем запросе в параметре last_id .
- **products** `Array of objects` — Список товаров.
- **total** `integer <uint64>` — Общее количество товаров, которое доступно для акции.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "id": 8888888,
      "price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "action_price": {
        "amount": "1800",
        "currency": "RUB"
      },
      "max_action_price": {
        "amount": "62",
        "currency": "RUB"
      },
      "min_stock": 1,
      "recommended_stock": 2,
      "marketplace_seller_price": {
        "amount": "70",
        "currency": "RUB"
      },
      "alert_max_action_price_failed": "alert_max_action_price",
      "amount": "30",
      "currency": "RUB"
    },
    {
      "current_boost": 15,
      "price_min_elastic": {
        "amount": "62",
        "currency": "RUB"
      },
      "price_max_elastic": {
        "amount": "53",
        "currency": "RUB"
      },
      "min_boost": 15,
      "max_boost": 55,
      "website_prices": {
        "price": {
          "amount": "54",
          "currency": "RUB"
        },
        "prices_by_schema": {
          "min_seller_price": {
            "amount": "1",
            "currency": "RUB"
          },
          "is_quarantined": false
        },
        "total": 219176,
        "last_id": "81881"
      }
    }
  ]
}
```


---

## Список доступных для акции товаров

`POST /v1/actions/candidates`

Метод для получения списка товаров, которые могут участвовать в акции, по её идентификатору.

> **Примечание:** 13 октября 2026 года отключим метод. Переключитесь на

**Тело запроса** (`application/json`):
- **action_id** `number <double>` *обязательный* — Идентификатор акции. Можно получить с помощью метода /v1/actions.
- **limit** `number <double>` — Количество ответов на странице. По умолчанию — 100.
- **last_id** `number <double>` — Идентификатор последнего значения на странице. При первом запросе оставьте это поле пустым.

**Пример запроса:**

```json
{
  "action_id": 63337,
  "limit": 10,
  "last_id": "bnVсbA==123123das"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **products** `Array of objects` — Список товаров.
  - **total** `number <double>` — Общее количество товаров, которое доступно для акции.
  - **last_id** `number <double>` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, передайте полученное значение в следующем запросе в параметре last_id .

**Пример ответа (`200`):**

```json
{
  "result": {
    "products": [
      {
        "id": 226,
        "price": 250,
        "action_price": 10,
        "alert_max_action_price_faile \"alert_max_action_price": 31,
        "max_action_price": 175,
        "add_mode": "NOT_SET",
        "stock": 2,
        "min_stock": 1,
        "current_boost": 3,
        "price_min_elastic": 150,
        "price_max_elastic": 300,
        "min_boost": 12,
        "max_boost": 15
      }
    ],
    "total": 2,
    "last_id": "bnVсbA=="
  }
}
```


---

## Получить список товаров, которые участвуют в акции

`POST /v2/actions/products`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

> **Примечание:** До 13 октября 2026 года метод работает аналогично

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите методом /v1/actions.
- **last_id** `string` — Идентификатор последнего значения на странице. При первом запросе оставьте пустым.
- **limit** `integer <uint64>` *обязательный* — Количество значений на странице.

**Пример запроса:**

```json
{
  "action_id": 213139,
  "last_id": "3262247282",
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров, которые участвуют в акции |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **last_id** `string` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, передайте полученное значение в следующем запросе в параметре last_id .
- **products** `Array of objects` — Список товаров.
- **total** `integer <uint64>` — Количество товаров в акции.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "id": 99999,
      "price": {
        "amount": "4000",
        "currency": "RUB"
      },
      "action_price": {
        "amount": "4000",
        "currency": "RUB"
      },
      "max_action_price": {
        "amount": "3560",
        "currency": "RUB"
      },
      "add_mode": "SELLER",
      "stock": 2,
      "min_stock": 1,
      "recommended_stock": 10,
      "marketplace_seller_price": {
        "amount": "500",
        "currency": "RUB"
      },
      "alert_max_action_price_failed": "alert_max_action_price",
      "amount": "4000",
      "currency": "RUB"
    },
    {
      "current_boost": 12,
      "price_min_elastic": {
        "amount": "3560",
        "currency": "RUB"
      },
      "price_max_elastic": {
        "amount": "3560",
        "currency": "RUB"
      },
      "min_boost": 1,
      "max_boost": 12,
      "website_prices": {
        "price": {
          "amount": "382",
          "currency": "RUB"
        },
        "prices_by_schema": {
          "min_seller_price": {
            "amount": "4000",
            "currency": "RUB"
          },
          "is_quarantined": true
        },
        "total": 44,
        "last_id": "28743"
      }
    }
  ]
}
```


---

## Список участвующих в акции товаров

`POST /v1/actions/products`

Метод для получения списка товаров, участвующих в акции, по её идентификатору.

> **Примечание:** 13 октября 2026 года отключим метод. Переключитесь на

**Тело запроса** (`application/json`):
- **action_id** `number <double>` *обязательный* — Идентификатор акции. Можно получить с помощью метода /v1/actions.
- **limit** `number <double>` — Количество ответов на странице. По умолчанию — 100.
- **last_id** `number <double>` — Идентификатор последнего значения на странице. При первом запросе оставьте это поле пустым.

**Пример запроса:**

```json
{
  "action_id": 66011,
  "limit": 10,
  "last_id": "bnVсbA=="
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **products** `Array of objects` — Список товаров.
  - **total** `number <double>` — Общее количество товаров, которое доступно для акции.
  - **last_id** `number <double>` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, передайте полученное значение в следующем запросе в параметре last_id .

**Пример ответа (`200`):**

```json
{
  "result": {
    "products": [
      {
        "id": 28745,
        "price": 99,
        "action_price": 50,
        "alert_max_action_price_faile \"alert_max_action_price": 31,
        "max_action_price": 32,
        "add_mode": "MANUAL",
        "stock": 20,
        "min_stock": 3,
        "current_boost": 1,
        "price_min_elastic": 2,
        "price_max_elastic": 5,
        "min_boost": 10,
        "max_boost": 15
      }
    ],
    "total": 263,
    "last_id": "bnVсbA=="
  }
}
```


---

## Добавить товар в акцию Deprecated

`POST /v1/actions/products/activate`

Метод для добавления товаров в доступную акцию.

> **Примечание:** 13 октября 2026 года отключим метод. Переключитесь на

**Тело запроса** (`application/json`):
- **action_id** `number <double>` *обязательный* — Идентификатор акции. Можно получить с помощью метода /v1/actions.
- **products** `Array of objects` *обязательный* — Список товаров.

**Пример запроса:**

```json
{
  "action_id": 60564,
  "products": [
    {
      "action_price": 356,
      "product_id": 1389,
      "stock": 10
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товар добавлен в акцию |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **product_ids** `Array of numbers <double>` — Список идентификаторов товаров, которые добавлены в акцию.
  - **rejected** `Array of objects` — Список товаров, которые не удалось добавить в акцию.

**Пример ответа (`200`):**

```json
{
  "result": {
    "product_ids": [
      1389
    ],
    "rejected": []
  }
}
```


---

## Добавить или обновить товар в акции

`POST /v1/actions/products/update`

> **Примечание:** До 13 октября 2026 года метод работает аналогично

> **Примечание:** помощью метода не получится.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите методом /v1/actions.
- **products** `Array of objects` *обязательный* — Список товаров.

**Пример запроса:**

```json
{
  "action_id": 258568,
  "products": [
    {
      "action_price": {
        "amount": "88",
        "currency": "RUB"
      },
      "product_id": 88888,
      "stock": "8"
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товары добавлены или обновлены |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **active_product_ids** `Array of strings <uint64>` — Список идентификаторов товаров, которые добавлены в акцию.
- **deactivated_product_ids** `Array of strings <uint64>` — Список идентификаторов товаров, которые удалены из акции.
- **rejected** `Array of objects` — Список товаров, которые не удалось добавить в акцию.
- **warnings** `Array of objects` — Информация о причинах, из-за которых товары удалены из акции.

**Пример ответа (`200`):**

```json
{
  "active_product_ids": [
    88888
  ],
  "deactivated_product_ids": [],
  "rejected": [],
  "warnings": []
}
```


---

## Удалить товары из акции «Промокоды»

`POST /v2/actions/products/deactivate`

Чтобы удалить товары из акций «Эластичный бустинг» или «Максимальный бустинг», используйте метод значение меньше или равное лимиту акции.

> **Примечание:** До 13 октября 2026 года метод работает аналогично

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции. Получите методом /v1/actions.
- **product_ids** `Array of strings <uint64>` *обязательный* — Список идентификаторов товаров в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "action_id": 213139,
  "product_ids": [
    999999
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товары удалены из акции |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **product_ids** `Array of strings <uint64>` — Список идентификаторов товаров, которые удалены из акции.

**Пример ответа (`200`):**

```json
{
  "product_ids": [
    999999
  ]
}
```


---

## Удалить товары из акции Deprecated

`POST /v1/actions/products/deactivate`

Метод для удаления товаров из акции.

> **Примечание:** 13 октября 2026 года отключим метод. Переключитесь на

**Тело запроса** (`application/json`):
- **action_id** `number <double>` *обязательный* — Идентификатор акции. Можно получить с помощью метода /v1/actions.
- **product_ids** `Array of numbers <double>` *обязательный* — Список идентификаторов товаров в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "action_id": 66011,
  "product_ids": [
    14975
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товары удалены из акции |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **product_ids** `Array of numbers <double>` — Список идентификаторов товаров, которые удалены из акции.
  - **rejected** `Array of objects` — Список товаров, которые не удалось удалить из акции.

**Пример ответа (`200`):**

```json
{
  "result": {
    "product_ids": [
      14975
    ],
    "rejected": []
  }
}
```


---

## Список заявок на скидку

`POST /v1/actions/discounts-task/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Метод для получения списка товаров, которые покупатели хотят купить со скидкой.

> **Примечание:** Метод устаревает и будет отключён в будущем. Переключитесь

> **Примечание:** на /v2/actions/discounts-task/list.

**Тело запроса** (`application/json`):
- **status** `string` *обязательный* — Статус заявки на скидку: NEW — новая, SEEN — просмотренная, APPROVED — одобренная, PARTLY_APPROVED — одобренная частично, DECLINED — отклонённая, AUTO_DECLINED — отклонена автоматически, DECLINED_BY_USER — отклонена покупателем, COUPON — скидка по купону, PURCHASED — купленная.. Enum: `"NEW"`, `"SEEN"`, `"APPROVED"`, `"PARTLY_APPROVED"`, `"DECLINED"`, `"AUTO_DECLINED"`, `"DECLINED_BY_USER"`, `"COUPON"`, `"PURCHASED"`.
- **page** `integer <uint64>` *обязательный* — Страница, с которой нужно выгрузить список заявок на скидку.
- **limit** `integer <uint64>` *обязательный* — Максимальное количество заявок на странице.

**Пример запроса:**

```json
{
  "status": "UNKNOWN",
  "page": 1,
  "limit": 50
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список заявок |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список заявок.
  - **id** `integer <uint64>` — Идентификатор заявки.
  - **created_at** `string <date-time>` — Дата создания заявки.
  - **end_at** `string <date-time>` — Время окончания действия заявки.
  - **edited_till** `string <date-time>` — Время для изменения решения.
  - **status** `string` — Статус заявки.
  - **customer_name** `string` — Имя покупателя.
  - **sku** `integer <uint64>` — Идентификатор товара в системе Ozon — SKU.
  - **user_comment** `string` — Комментарий покупателя к заявке.
  - **seller_comment** `string` — Комментарий продавца к заявке.
  - **requested_price** `number <double>` — Цена по заявке.
  - **approved_price** `number <double>` — Одобренная цена.
  - **original_price** `number <double>` — Цена товара до всех скидок.
  - **discount** `number <double>` — Скидка в рублях.
  - **discount_percent** `number <double>` — Скидка в процентах.
  - **base_price** `number <double>` — Базовая цена, по которой товар продаётся на Ozon, если не участвует в акции.
  - **min_auto_price** `number <double>` — Минимальное значение цены после автоприменения скидок и акций.
  - **prev_task_id** `integer <uint64>` — Идентификатор предыдущей заявки от покупателя по этому товару.
  - **is_damaged** `boolean` — Является ли товар уценённым. true , если уценённый.
  - **moderated_at** `string <date-time>` — Дата модерации: просмотра, одобрения или отклонения заявки.
  - **approved_discount** `number <double>` — Скидка в рублях, которую одобрил продавец. Передайте значение 0 , если продавец не одобрял заявку.
  - **approved_discount_percent** `number <double>` — Скидка в процентах, которую одобрил продавец. Передайте значение 0 , если продавец не одобрял заявку.
  - **is_purchased** `boolean` — Покупал ли пользователь товар. true , если покупал.
  - **is_auto_moderated** `boolean` — Была ли заявка промодерирована автоматически. true , если модерация была автоматической.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **email** `string` — Электронный адрес сотрудника продавца, который обработал заявку.
  - **last_name** `string` — Фамилия сотрудника продавца, который обработал заявку.
  - **first_name** `string` — Имя сотрудника продавца, который обработал заявку.
  - **patronymic** `string` — Отчество сотрудника продавца, который обработал заявку.
  - **approved_quantity_min** `integer <uint64>` — Минимальное одобренное количество товаров.
  - **approved_quantity_max** `integer <uint64>` — Максимальное одобренное количество товаров.
  - **requested_quantity_min** `integer <uint64>` — Запрошенное минимальное количество товаров.
  - **requested_quantity_max** `integer <uint64>` — Запрошенное максимальное количество товаров.
  - **requested_price_with_fee** `number <double>` — Цена по заявке c региональной наценкой.
  - **approved_price_with_fee** `number <double>` — Одобренная цена с региональной наценкой.
  - **approved_price_fee_percent** `number <double>` — Региональная наценка в процентах.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "id": 12345,
      "created_at": "2023-10-15T09:30: ",
      "end_at": "2023-10-20T18:45:00Z",
      "edited_till": "2023-10-18T12:00 \"status\": \"approved",
      "customer_name": "Иван Иванов",
      "sku": 100500,
      "user_comment": "Товар необходим \"seller_comment\": ",
      "requested_price": 15000,
      "approved_price": 14500,
      "original_price": 16000,
      "discount": 1000,
      "discount_percent": 6.25,
      "base_price": 15500,
      "min_auto_price": 14000,
      "prev_task_id": 12344,
      "is_damaged": false,
      "moderated_at": "2023-10-16T10:1 \"approved_discount\": 500",
      "approved_discount_percent": 3.1,
      "is_purchased": true,
      "is_auto_moderated": false,
      "offer_id": "OFFER-2023-1001",
      "email": "ivan.ivanov@example.co \"last_name\": \"Иванов",
      "first_name": "Иван",
      "patronymic": "Петрович",
      "approved_quantity_min": 1,
      "approved_quantity_max": 5,
      "requested_quantity_min": 2,
      "requested_quantity_max": 10,
      "requested_price_with_fee": 1550,
      "approved_price_with_fee": 15000,
      "approved_price_fee_percent": 3.0
    }
  ]
}
```


---

## Согласовать заявку на скидку

`POST /v1/actions/discounts-task/approve`

Вы можете согласовывать заявки в статусах: NEW — новые, SEEN — просмотренные.

**Тело запроса** (`application/json`):
- **tasks** `Array of objects` *обязательный* — Список заявок.

**Пример запроса:**

```json
{
  "tasks": [
    {
      "id": 78901,
      "approved_price": 12500,
      "seller_comment": "ok",
      "approved_quantity_min": 3,
      "approved_quantity_max": 7
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заявки согласованы |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **fail_details** `Array of objects` — Ошибки при создании заявки.
  - **success_count** `integer <int32>` — Количество заявок с успешной сменой статуса.
  - **fail_count** `integer <int32>` — Количество заявок, у которых не удалось сменить статус.

**Пример ответа (`200`):**

```json
{
  "result": {
    "fail_details": [
      {
        "task_id": 78901,
        "error_for_user": "Скидка отк"
      }
    ],
    "success_count": 5,
    "fail_count": 1
  }
}
```


---

## Отклонить заявку на скидку

`POST /v1/actions/discounts-task/decline`

Вы можете отклонить заявки в статусах: NEW — новые, SEEN — просмотренные.

**Тело запроса** (`application/json`):
- **tasks** `Array of objects` *обязательный* — Список заявок.

**Пример запроса:**

```json
{
  "tasks": [
    {
      "id": 78901,
      "seller_comment": "Ok"
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заявки отклонены |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **fail_details** `Array of objects` — Ошибки при создании заявки.
  - **success_count** `integer <int32>` — Количество заявок с успешной сменой статуса.
  - **fail_count** `integer <int32>` — Количество заявок, у которых не удалось сменить статус.

**Пример ответа (`200`):**

```json
{
  "result": {
    "fail_details": [
      {
        "task_id": 78901,
        "error_for_user": "Скидка отк"
      }
    ],
    "success_count": 5,
    "fail_count": 1
  }
}
```


---

## Получить список товаров из автодобавления в акцию

`POST /v2/actions/auto-add/products/list`

> **Примечание:** До 13 октября 2026 года метод работает аналогично

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции.
- **auto_add_date** `string <date-time>` *обязательный* — Дата и время автодобавления товаров в акцию из параметра result.auto_add_dates в ответе метода /v1/actions.
- **limit** `integer <uint64>` *обязательный* — Количество значений в ответе.
- **offset** `integer <uint64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , ответ начнётся с 11-го найденного элемента.

**Пример запроса:**

```json
{
  "action_id": 0,
  "auto_add_date": "2025-01-01T00:00:00Z",
  "offset": 0,
  "limit": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров с автодобавлением |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **products** `Array of objects` — Список товаров с автодобавлением.
- **total** `integer <uint64>` — Количество товаров.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "action_price_to_auto_add": {
        "amount": "1800",
        "currency": "RUB"
      },
      "add_mode": true,
      "base_price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "currency": "RUB",
      "has_expired_min_seller_price": "marketplace_seller_price",
      "amount": "70"
    },
    {
      "max_discount_price": {
        "amount": "62",
        "currency": "RUB"
      },
      "min_action_quantity": 1,
      "min_seller_price": {
        "amount": "1",
        "currency": "RUB"
      },
      "name": "Ароматизатор / Масло дл \"offer_id\": \"SR0000",
      "price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "product_id": 8888888,
      "quantity_to_auto_add": 2,
      "sku": 8888888,
      "website_prices": {
        "price": {
          "amount": "54",
          "currency": "RUB"
        },
        "prices_by_schema": {
          "additionalProp1": {
            "black_price": {
              "amount": "111",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "222",
              "currency": "RUB"
            }
          },
          "additionalProp2": {
            "black_price": {
              "amount": "333",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "444",
              "currency": "RUB"
            }
          },
          "additionalProp3": {
            "additionalProp3": {
              "black_price": {
                "amount": "555",
                "currency": "RUB"
              },
              "green_price": {
                "amount": "666",
                "currency": "RUB"
              }
            }
          }
        },
        "will_be_quarantined": false
      },
      "total": 219176
    }
  ]
}
```


---

## Получить список доступных товаров для автодобавления в акцию

`POST /v2/actions/auto-add/products/candidates`

> **Примечание:** До 13 октября 2026 года метод работает аналогично

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции.
- **auto_add_date** `string <date-time>` *обязательный* — Дата и время автодобавления товаров в акцию из параметра result.auto_add_dates в ответе метода /v1/actions.
- **limit** `integer <uint64>` *обязательный* — Количество значений в ответе.
- **offset** `integer <uint64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , ответ начнётся с 11-го найденного элемента.

**Пример запроса:**

```json
{
  "action_id": 250204,
  "auto_add_date": "2025-01-01T00:00:00Z",
  "offset": 5,
  "limit": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список доступных товаров для автодобавления в акцию |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **products** `Array of objects` — Список доступных товаров для автодобавления.
- **total** `integer <uint64>` — Количество товаров.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "action_price_to_auto_add": {
        "amount": "1800",
        "currency": "RUB"
      },
      "base_price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "currency": "RUB",
      "has_expired_min_seller_price": "id",
      "is_manually_added": true,
      "marketplace_seller_price": {
        "amount": "70",
        "currency": "RUB"
      },
      "max_discount_price": {
        "amount": "62",
        "currency": "RUB"
      },
      "min_action_quantity": 1,
      "min_seller_price": {
        "amount": "1",
        "currency": "RUB"
      },
      "name": "Ароматизатор / Масло дл \"offer_id\": \"PS0000",
      "price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "quantity_to_auto_add": 2,
      "sku": 8888888,
      "website_prices": {
        "price": {
          "amount": "54",
          "currency": "RUB"
        },
        "prices_by_schema": {
          "additionalProp1": {
            "black_price": {
              "amount": "1400",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "18888",
              "currency": "RUB"
            }
          },
          "additionalProp2": {
            "black_price": {
              "amount": "1500",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "1600",
              "currency": "RUB"
            }
          },
          "additionalProp3": {
            "additionalProp3": {
              "black_price": {
                "amount": "1700",
                "currency": "RUB"
              },
              "green_price": {
                "amount": "1800",
                "currency": "RUB"
              }
            }
          }
        },
        "will_be_quarantined": false
      },
      "total": 219176
    }
  ]
}
```


---

## Удалить товары из автодобавления в акцию

`POST /v2/actions/auto-add/products/delete`

> **Примечание:** До 13 октября 2026 года метод работает аналогично

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции.
- **auto_add_date** `string <date-time>` *обязательный* — Дата и время автодобавления товаров в акцию из параметра result.auto_add_dates в ответе метода /v1/actions.
- **product_ids** `Array of strings <uint64>` *обязательный* — Идентификаторы товаров в системе Ozon — product_id .

**Пример запроса:**

```json
{
  "action_id": 250204,
  "product_ids": [
    88888
  ],
  "auto_add_date": "2025-01-01T00:00:00Z"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товары удалены из автодобавления |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **product_ids** `Array of strings <uint64>` — Идентификаторы товаров, которые удалены из автодобавления.

**Пример ответа (`200`):**

```json
{
  "product_ids": [
    88888
  ]
}
```


---

## Добавить или обновить товары в автодобавлении в акцию

`POST /v2/actions/auto-add/products/update`

> **Примечание:** До 13 октября 2026 года метод работает аналогично

> **Примечание:** товара с помощью метода не получится.

**Тело запроса** (`application/json`):
- **action_id** `integer <uint64>` *обязательный* — Идентификатор акции.
- **auto_add_date** `string <date-time>` *обязательный* — Дата и время автодобавления товаров в акцию из параметра result.auto_add_dates в ответе метода /v1/actions.
- **products** `Array of objects` *обязательный* — Список товаров, которые нужно добавить или обновить в автодобавлении.

**Пример запроса:**

```json
{
  "action_id": 250204,
  "auto_add_date": "2026-09-22T11:37:38.94 \"products\": [ { \"action_price\": { \"amount\": \"1000",
  "currency": "RUB",
  "id": 88888,
  "stock": 10
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товары добавлены или обновлены в автодобавлении |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **below_min_price** `Array of objects` — Список товаров с ценой ниже минимальной.
- **deactivated_ids** `Array of strings <uint64>` — Идентификаторы товаров, которые удалены из акции.
- **extremely_low_price** `Array of objects` — Список товаров со скидкой больше 70%.
- **failed_price** `Array of objects` — Список товаров, которые не прошли валидацию по цене.
- **product_ids** `Array of strings <uint64>` — Идентификаторы товаров, которые получилось добавить или обновить.
- **rejected** `Array of objects` — Идентификаторы товаров, которые не получилось добавить или обновить.
- **warnings** `Array of objects` — Список предупреждений по товарам.

**Пример ответа (`200`):**

```json
{
  "product_ids": [
    "    88888  "
  ],
  "deactivated_ids": [
    0
  ],
  "rejected": [
    {
      "product_id": 0,
      "reason": ""
    }
  ],
  "warnings": [
    {
      "product_id": 0,
      "reason": ""
    }
  ],
  "below_min_price": {
    "key": 0,
    "value": ""
  },
  "extremely_low_price": {
    "key": 0,
    "value": ""
  },
  "failed_price": {
    "key": 0,
    "value": ""
  }
}
```


---
