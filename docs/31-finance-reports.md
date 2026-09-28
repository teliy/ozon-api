# Финансовые отчёты

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 400. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

Больше методов в разделе Premium-методы.

## Отчёт о реализации товаров (версия 2)

`POST /v2/finance/realization`

Отчёт о реализации доставленных и возвращённых товаров за месяц. Отмены и невыкупы не включаются. Соответствует разделу Финансы в личном кабинете. Отчёт придёт не позднее 5-го числа следующего месяца. Подробнее об отчёте в Базе знаний продавца

> **Примечание:** Метод недоступен для продавцов, которые заключили договор с

> **Примечание:** ТОО «ОЗОН Маркетплейс Казахстан».

> **Примечание:** Метод позволяет получить отчёт за период не раньше августа

> **Примечание:** 2023 года. Отчёты за более ранние периоды доступны в личном

> **Примечание:** кабинете.

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
| `200` | Отчёт о реализации |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат запроса.
  - **header** `object` — Титульный лист отчёта.
  - **rows** `Array of objects` — Таблица отчёта.

**Пример ответа (`200`):**

```json
{
  "result": {
    "header": {
      "contract_date": "string",
      "contract_number": "string",
      "currency_sys_name": "string",
      "doc_date": "string",
      "number": "string",
      "payer_inn": "string",
      "payer_kpp": "string",
      "payer_name": "string",
      "receiver_inn": "string",
      "receiver_kpp": "string",
      "receiver_name": "string",
      "start_date": "string",
      "stop_date": "string"
    },
    "rows": [
      {
        "commission_ratio": 0,
        "delivery_commission": {
          "amount": 0,
          "bonus": 0,
          "commission": 0,
          "compensation": 0,
          "price_per_instance": 0,
          "quantity": 0,
          "standard_fee": 0,
          "bank_coinvestment": 0,
          "stars": 0,
          "pick_up_point_coinvestme \"total": 0
        },
        "item": {
          "barcode": "string",
          "name": "string",
          "offer_id": "string",
          "sku": 0
        },
        "return_commission": {
          "amount": 0,
          "bonus": 0,
          "commission": 0,
          "compensation": 0,
          "price_per_instance": 0,
          "quantity": 0,
          "standard_fee": 0,
          "bank_coinvestment": 0,
          "stars": 0,
          "pick_up_point_coinvestme \"total": 0
        },
        "rowNumber": 0,
        "seller_price_per_instance": ""
      }
    ]
  }
}
```


---

## Позаказный отчёт о реализации товаров

`POST /v1/finance/realization/posting`

Отчёт о реализации доставленных и возвращённых товаров с детализацией по каждому заказу. Отмены и невыкупы не включаются. Отчёт доступен с настоящего времени по август 2023 года включительно.

> **Примечание:** Метод недоступен для продавцов, которые заключили договор с

> **Примечание:** ТОО «ОЗОН Маркетплейс Казахстан».

**Тело запроса** (`application/json`):
- **month** `integer <int32>` *обязательный* — Месяц.
- **year** `integer <int32>` *обязательный* — Год.

**Пример запроса:**

```json
{
  "month": 2,
  "year": 2025
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
- **header** `object` — Титульный лист отчёта.
- **rows** `Array of objects` — Таблица отчёта.

**Пример ответа (`200`):**

```json
{
  "header": {
    "contract_date": "string",
    "contract_number": "string",
    "currency_sys_name": "string",
    "doc_date": "string",
    "number": "string",
    "payer_inn": "string",
    "payer_kpp": "string",
    "payer_name": "string",
    "receiver_inn": "string",
    "receiver_kpp": "string",
    "receiver_name": "string",
    "start_date": "string",
    "stop_date": "string"
  },
  "rows": [
    {
      "commission_ratio": 0,
      "delivery_commission": {
        "amount": 0,
        "bonus": 0,
        "commission": 0,
        "compensation": 0,
        "price_per_instance": 0,
        "quantity": 0,
        "standard_fee": 0,
        "bank_coinvestment": 0,
        "stars": 0,
        "pick_up_point_coinvestment": "total"
      },
      "item": {
        "barcode": "string",
        "name": "string",
        "offer_id": "string",
        "sku": 0
      },
      "return_commission": {
        "amount": 0,
        "bonus": 0,
        "commission": 0,
        "compensation": 0,
        "price_per_instance": 0,
        "quantity": 0,
        "standard_fee": 0,
        "bank_coinvestment": 0,
        "stars": 0,
        "pick_up_point_coinvestment": "total"
      },
      "row_number": 0,
      "seller_price_per_instance": 0,
      "order": {
        "posting_number": "string",
        "created_date": "string"
      },
      "legal_entity_document": {
        "number": "string",
        "sale_date": "string"
      }
    }
  ]
}
```


---

## Список транзакций

`POST /v3/finance/transaction/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает подробную информацию по всем начислениям. Максимальный период, за который можно получить информацию в одном запросе — 1 месяц. Если в запросе не указывать posting_number , то в ответе будут все отправления за указанный период или отправления определённого типа.

> **Примечание:** Метод устаревает и будет отключён 8 сентября 2026 года.

> **Примечание:** Переключитесь на /v1/finance/accrual/postings,

> **Примечание:** Используйте метод с последовательной отправкой запросов.

> **Примечание:** Данные могут не соответствовать информации в личном

> **Примечание:** кабинете.

**Тело запроса** (`application/json`):
- **filter** — Фильтр.
- **page** `integer <int64>` *обязательный* — Номер страницы, возвращаемой в запросе.
- **page_size** `integer <int64>` *обязательный* — Количество элементов на странице.

**Пример запроса:**

```json
{
  "filter": {
    "date": {
      "from": "2021-11-01T00:00:00.000 ",
      "to": "2021-11-02T00:00:00.000Z"
    },
    "operation_type": [],
    "posting_number": "",
    "transaction_type": "all"
  },
  "page": 1,
  "page_size": 1000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список транзакций |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **operations** `Array of objects` — Информация об операциях.
  - **page_count** `integer <int64>` — Количество страниц. Если 0, страниц больше нет.
  - **row_count** `integer <int64>` — Количество транзакций на всех страницах. Если 0, транзакций больше нет.

**Пример ответа (`200`):**

```json
{
  "result": {
    "operations": [
      {
        "operation_id": 1140118218784,
        "operation_type": "Marketplac \"operation_date\": ",
        "operation_type_name": "Услуг \"delivery_charge\": 0",
        "return_delivery_charge": 0,
        "accruals_for_sale": 0,
        "sale_commission": 0,
        "amount": -6.46,
        "type": "services",
        "posting": {
          "delivery_schema": "",
          "order_date": "",
          "posting_number": "",
          "warehouse_id": 0
        },
        "items": [],
        "services": []
      }
    ],
    "page_count": 1,
    "row_count": 355
  }
}
```


---

## Суммы транзакций

`POST /v3/finance/transaction/totals`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает итоговые суммы по транзакциям за указанный период. Если вы неправильно заполните номера отправлений, в ответе вернутся нулевые значения.

> **Примечание:** Метод устаревает и будет отключён 8 сентября 2026 года.

> **Примечание:** Переключитесь на /v1/finance/accrual/postings,

> **Примечание:** Данные могут не соответствовать информации в личном

> **Примечание:** кабинете.

**Тело запроса** (`application/json`):
- **date** `object` — Фильтр по дате.
- **posting_number** `string` *обязательный* — Номер отправления.
- **transaction_type** `string` — Тип операции: all — все, orders — заказы, returns — возвраты и отмены, services — сервисные сборы, compensation — компенсация, transferDelivery — стоимость доставки, other — прочее.

**Пример запроса:**

```json
{
  "date": {
    "from": "2021-11-01T00:00:00.000Z",
    "to": "2021-11-02T00:00:00.000Z"
  },
  "posting_number": "",
  "transaction_type": "all"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Суммы транзакций |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **accruals_for_sale** `number <double>` — Общая стоимость товаров и возвратов в заданный период.
  - **compensation_amount** `number <double>` — Компенсации.
  - **money_transfer** `number <double>` — Начисления за доставку и возвраты при работе по схеме «Доставка по выбору продавца».
  - **others_amount** `number <double>` — Прочие начисления.
  - **processing_and_delivery** `number <double>` — Стоимость услуг обработки отправлений, сборки заказов, магистрали и последней мили, а также доставки до введения новых комиссий и тарифов с 1 февраля 2021 года. Магистраль — доставка товаров между кластерами. Последняя миля — доставка товаров покупателю в пункт выдачи заказов, постамат или курьером.
  - **refunds_and_cancellations** `number <double>` — Стоимость обратной магистрали, обработки возвратов, отмен и невыкупа товара, а также возвратов до введения новых комиссий и тарифов с 1 февраля 2021 года. Магистраль — доставка товаров между кластерами. Последняя миля — доставка товаров покупателю в пункт выдачи заказов, постамат или курьером.
  - **sale_commission** `number <double>` — Сумма комиссии, которая была удержана при продаже товара и возвращена при его возврате.
  - **services_amount** `number <double>` — Стоимость дополнительных услуг, не связанных напрямую с доставками и возвратами товаров. Например, продвижения или размещения товаров.

**Пример ответа (`200`):**

```json
{
  "result": {
    "accruals_for_sale": 96647.58,
    "sale_commission": -11456.65,
    "processing_and_delivery": -24405.68,
    "refunds_and_cancellations": -330,
    "services_amount": -1307.57,
    "compensation_amount": 0,
    "money_transfer": 0,
    "others_amount": 113.05
  }
}
```


---

## Реестр продаж юридическим лицам

`POST /v1/finance/document-b2b-sales`

Используйте метод, чтобы получить отчёт по продажам юридическим

**Тело запроса** (`application/json`):
- **date** `string` *обязательный* — Отчётный период в формате YYYY-MM .
- **language** `string` — Язык ответа: RU — русский, EN — английский.

**Пример запроса:**

```json
{
  "date": "string",
  "language": "DEFAULT"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат запроса |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **code** `string` — Уникальный идентификатор отчёта. По нему вы можете получить отчёт в течение 3 дней после запроса. Чтобы получить отчёт, передайте это значение в метод /v1/report/info.

**Пример ответа (`200`):**

```json
{
  "result": {
    "code": "string"
  }
}
```


---

## Реестр продаж юридическим лицам в JSON-формате

`POST /v1/finance/document-b2b-sales/json`

Используйте метод, чтобы получить отчёт по продажам юридическим лицам в JSON-формате. Соответствует разделу Финансы →

**Тело запроса** (`application/json`):
- **date** `string` *обязательный* — Отчётный период в формате YYYY-MM . Отчёт доступен до января 2019 включительно.

**Пример запроса:**

```json
{
  "date": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт в JSON-формате |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **date_from** `string` — Дата начала отчётного периода в формате YYYY-MM-DD .
- **date_to** `string` — Дата окончания отчётного периода в формате YYYY-MM- DD .
- **invoices** `Array of objects` — Список счетов-фактур.
- **seller_info** `object` — Информация о продавце.

**Пример ответа (`200`):**

```json
{
  "date_from": "string",
  "date_to": "string",
  "invoices": [
    {
      "buyer_info": {
        "name": "string",
        "address": "string",
        "inn": "string",
        "kpp": "string"
      },
      "currency": "string",
      "currency_code": 0,
      "info": {
        "date": "string",
        "number": "string",
        "status": "string",
        "type": "UPD"
      },
      "offer_id": "string",
      "operations": [
        {
          "amount": 0,
          "cost_without_vat": 0,
          "date": "string",
          "gtd_number": "string",
          "origin_country": "string \"posting_number\": ",
          "price": 0,
          "quantity": 0,
          "rnpt_number": "string",
          "type": "DELIVERY",
          "vat_amount": 0,
          "vat_rate": 0
        }
      ],
      "product_name": "string",
      "sku": 0,
      "unit_code": 0,
      "unit_name": "string"
    }
  ],
  "seller_info": {
    "company_name": "string",
    "inn": "string",
    "kpp": "string"
  }
}
```


---

## Отчёт о взаиморасчётах

`POST /v1/finance/mutual-settlement`

Используйте метод, чтобы получить отчёт о взаиморасчетах.

**Тело запроса** (`application/json`):
- **date** `string` *обязательный* — Отчётный период в формате YYYY-MM .
- **language** `string` — Язык ответа: RU — русский, EN — английский.

**Пример запроса:**

```json
{
  "date": "string",
  "language": "DEFAULT"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат запроса |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **code** `string` — Уникальный идентификатор отчёта. По нему вы можете получить отчёт в течение 3 дней после запроса. Чтобы получить отчёт, передайте это значение в метод /v1/report/info.

**Пример ответа (`200`):**

```json
{
  "result": {
    "code": "string"
  }
}
```


---

## Отчёт о выкупленных товарах

`POST /v1/finance/products/buyout`

Возвращает отчёт о товарах, которые выкупил Ozon. Соответствует Подробнее о выкупе товаров в Базе знаний

**Тело запроса** (`application/json`):
- **date_from** `string` *обязательный* — Дата, с которой будут данные в отчёте.
- **date_to** `string` *обязательный* — Дата, по которую будут данные в отчёте. Максимальный период — 31 день.

**Пример запроса:**

```json
{
  "date_from": "YYYY-MM-DD",
  "date_to": "YYYY-MM-DD"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт по выкупленным товарам |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **products** `Array of objects` — Список выкупленных товаров
  - **amount** `number <float>` — Сумма к начислению.
  - **buyout_price** `number <float>` — Цена выкупа товара с НДС.
  - **deduction_by_category_percent** `number <float>` — Скидка по категории в процентах.
  - **name** `string` — Название товара.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **posting_number** `string` — Номер отправления.
  - **quantity** `integer <int32>` — Количество товара.
  - **seller_price_per_instance** `number <float>` — Цена продавца с учётом скидки.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
  - **vat_percent** `integer <int32>` — Ставка НДС для товара в процентах.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "name": "Футболка Daniele Patric \"offer_id\": \"y9604060-S",
      "sku": "985111329",
      "posting_number": "0208194185-00 \"seller_price_per_instance\": 95",
      "deduction_by_category_percent": "buyout_price",
      "vat_percent": 20,
      "quantity": 1,
      "amount": 92.3
    },
    {
      "name": "Сабо T.TACCARDI",
      "offer_id": "W1496390-41",
      "sku": "1505091950",
      "posting_number": "84189625-0009 \"seller_price_per_instance\": 208 \"deduction_by_category_percent\": \"buyout_price\": 2023.3",
      "vat_percent": 20,
      "quantity": 1,
      "amount": 2023.3
    }
  ]
}
```


---

## Отчёт о компенсациях

`POST /v1/finance/compensation`

Метод для получения отчёта о компенсациях. Соответствует отчёту из в личном кабинете.

**Тело запроса** (`application/json`):
- **date** `string` *обязательный* — Отчётный период в формате YYYY-MM .
- **language** `string` — Язык отчёта: RU — русский, EN — английский.

**Пример запроса:**

```json
{
  "date": "2023-09",
  "language": "RU"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт о компенсациях |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат запроса.
  - **code** `string` — Уникальный идентификатор отчёта. Чтобы получить отчёт, передайте это значение в метод /v1/report/info.

**Пример ответа (`200`):**

```json
{
  "result": {
    "code": "string"
  }
}
```


---

## Отчёт о декомпенсациях

`POST /v1/finance/decompensation`

Метод для получения отчёта о декомпенсациях. Соответствует отчёту начисления в личном кабинете.

**Тело запроса** (`application/json`):
- **date** `string` *обязательный* — Отчётный период в формате YYYY-MM .
- **language** `string` — Язык отчёта: RU — русский, EN — английский.

**Пример запроса:**

```json
{
  "date": "2023-09",
  "language": "RU"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт о декомпенсациях |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат запроса.
  - **code** `string` — Уникальный идентификатор отчёта. Чтобы получить отчёт, передайте это значение в метод /v1/report/info.

**Пример ответа (`200`):**

```json
{
  "result": {
    "code": "string"
  }
}
```


---
