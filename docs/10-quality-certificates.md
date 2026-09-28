# Сертификаты качества

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 124. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Список типов соответствия требованиям (версия 1)

## Список типов соответствия требованиям (версия 1)

`GET /v1/product/certificate/accordance-types`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Cправочник типов соответствия требованиям |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список типов и названий сертификатов.
  - **name** `string` — Название документа.
  - **value** `string` — Значение справочника.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "name": "ГОСТ",
      "value": "gost"
    },
    {
      "name": "Технический регламент Р \"value\": "
    },
    {
      "name": "Технический регламент Т \"value\": "
    }
  ]
}
```


---

## Список типов соответствия требованиям (версия 2)

`GET /v2/product/certificate/accordance-types/list`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список типов соответствия требованиям |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Список типов соответствия требованиям.
  - **base** `Array of objects` — Основные типы соответствия требованиям.
  - **hazard** `Array of objects` — Типов соответствия требованиям, относящиеся к опасным товарам.

**Пример ответа (`200`):**

```json
{
  "result": {
    "base": [
      {
        "title": "ГОСТ",
        "code": "gost"
      },
      {
        "title": "Технический регламе \"code\": "
      },
      {
        "title": "Технический регламе \"code\": "
      }
    ],
    "hazard": [
      {
        "title": "ПБ химической проду \"code\": \"chemical_products\""
      },
      {
        "title": "Safety Data Sheet ( \"code\": \"safety_data_sheet\""
      },
      {
        "title": "Отказное письмо",
        "code": "rejection_letter"
      }
    ]
  }
}
```


---

## Справочник типов документов

`GET /v1/product/certificate/types`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Справочник типов документов |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список типов и названий сертификатов.
  - **name** `string` — Название документа.
  - **value** `string` — Значение справочника.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "name": "Сертификат соответствия \"value\": "
    },
    {
      "name": "Декларация о соответств \"value\": \"declaration\""
    },
    {
      "name": "Свидетельство о регистр \"value\": "
    },
    {
      "name": "Регистрационное удостов \"value\": "
    },
    {
      "name": "Отказное письмо",
      "value": "refused_letter"
    },
    {
      "name": "Ветеринарное свидетельс \"value\": "
    },
    {
      "name": "Паспорт безопасности",
      "value": "safety_data_sheet"
    }
  ]
}
```


---

## Список сертифицируемых категорий

`POST /v2/product/certification/list`

**Тело запроса** (`application/json`):
- **page** `integer <int64>` *обязательный* — Номер страницы.
- **page_size** `integer <int64>` *обязательный* — Количество элементов на странице.

**Пример запроса:**

```json
{
  "page": 1,
  "page_size": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список сертифицируемых категорий |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **certification** `Array of objects` — Информация о сертифицируемых категориях.
- **total** `integer <int64>` — Всего категорий.

**Пример ответа (`200`):**

```json
{
  "certification": [
    {
      "category_id": 582676,
      "category_name": "Витаминно-мине \"is_required\": true",
      "type_id": 113,
      "type_name": "products"
    }
  ],
  "total": 1
}
```


---

## Список сертифицируемых категорий

`POST /v1/product/certification/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

> **Примечание:** 14 апреля 2025 года метод будет отключён. Переключитесь на

**Тело запроса** (`application/json`):
- **page** `integer <int32>` — Номер страницы, возвращаемой в запросе.
- **page_size** `integer <int32>` — Количество элементов на странице.

**Пример запроса:**

```json
{
  "page": 1,
  "page_size": 100
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список сертифицируемых категорий |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат запроса.
  - **certification** `Array of objects` — Информация о сертифицируемых категориях.
  - **total** `integer <int64>` — Всего категорий.

**Пример ответа (`200`):**

```json
{
  "result": {
    "certification": [
      {
        "is_required": true,
        "category_name": "Витаминно-м"
      }
    ],
    "total": 1
  }
}
```


---

## Добавить сертификаты для товаров

`POST /v1/product/certificate/create`

> **Примечание:** 31 августа 2026 года отключим метод. Переключитесь на методы

**Тело запроса** (`application/json`):
- **files** `Array of file` *обязательный* — Массив сертификатов для товара. Допустимые расширения jpg, jpeg, png, pdf.
- **name** `string` *обязательный* — Название сертификата. Максимум 100 символов.
- **number** `string` *обязательный* — Номер сертификата. Максимум 100 символов.
- **type_code** `string` *обязательный* — Тип сертификата. Чтобы получить доступные типы, используйте метод GET /v1/product/certificate/types.. Enum: `"certificate_of_conformity"`, `"declaration"`, `"certificate_of_registration"`, `"registration_certificate"`, `"refused_letter"`, `"veterinary_cover_document"`, `"safety_data_sheet"`.
- **accordance_type_code** `string` — Тип соответствия требованиям. Чтобы получить доступные типы, используйте метод GET /v1/product/certificate/accordance-types. Параметр обязательный, если type_code = declaration , certificate_of_conformity или safety_data_sheet .. Enum: `"technical_regulations_rf"`, `"technical_regulations_cu"`, `"gost"`.
- **issue_date** `string <date-time>` *обязательный* — Дата начала действия сертификата.
- **expire_date** `string <date-time>` — Дата окончания действия сертификата. Может быть пустым для бессрочных сертификатов. Формат: 2021-04-30T11:31:26Z .

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Идентификатор загруженного сертификата |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`200`):**

```json
{
  "id": 50058
}
```


---

## Привязать сертификат к товару

`POST /v1/product/certificate/bind`

**Тело запроса** (`application/json`):
- **certificate_id** `integer <int64>` *обязательный* — Идентификатор сертификата, который был присвоен при его загрузке.
- **product_id** `Array of integers <int64>` *обязательный* — Массив идентификаторов товаров в системе Ozon — product_id , к которым относится этот сертификат.
- **skus** `Array of strings <int64>` — Список идентификаторов товаров в системе Ozon — SKU, к которым относится этот сертификат.

**Пример запроса:**

```json
{
  "certificate_id": 50058,
  "skus": [
    "2901231"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Сертификат привязан к товару |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `boolean` — Результат обработки запроса. true , если запрос выполнен без ошибок.

**Пример ответа (`200`):**

```json
{
  "result": true
}
```


---

## Удалить сертификат

`POST /v1/product/certificate/delete`

**Тело запроса** (`application/json`):
- **certificate_id** `integer <int32>` *обязательный* — Идентификатор сертификата.

**Пример запроса:**

```json
{
  "certificate_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат удаления сертификата |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Результат удаления сертификата.
  - **is_delete** `boolean` — Удалён ли сертификат: true — удалён, false — не удалён.
  - **error_message** `string` — Описание ошибок при удалении сертификата.

**Пример ответа (`200`):**

```json
{
  "result": {
    "is_delete": true,
    "error_message": "string"
  }
}
```


---

## Информация о сертификате

`POST /v1/product/certificate/info`

**Тело запроса** (`application/json`):
- **certificate_number** `string` *обязательный* — Идентификатор сертификата.

**Пример запроса:**

```json
{
  "certificate_number": "2312342134123"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о сертификате |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Информация о сертификате.
  - **certificate_id** `integer <int32>` — Идентификатор.
  - **certificate_number** `string` — Номер.
  - **certificate_name** `string` — Название.
  - **type_code** `string` — Тип.
  - **status_code** `string` — Статус.
  - **accordance_type_code** `string` — Тип соответствия требованиям.
  - **rejection_reason_code** `string` — Причина отклонения сертификата.
  - **verification_comment** `string` — Комментарий модератора.
  - **issue_date** `string <date-time>` — Дата создания.
  - **expire_date** `string <date-time>` — Дата окончания действия.
  - **products_count** `integer <int32>` — Количество товаров, привязанных к сертификату.

**Пример ответа (`200`):**

```json
{
  "result": {
    "certificate_id": 54321,
    "certificate_number": "CERT-2026-MSK \"certificate_name\": ",
    "type_code": "SAFETY_2026",
    "status_code": "PENDING",
    "accordance_type_code": "PARTIAL",
    "rejection_reason_code": "DOCS_MISSI \"verification_comment\": ",
    "issue_date": "2025-11-01T08:00:00Z",
    "expire_date": "2027-11-01T08:00:00Z \"products_count\": 15"
  }
}
```


---

## Список сертификатов

`POST /v1/product/certificate/list`

**Тело запроса** (`application/json`):
- **offer_id** `string` — Идентификатор товара в системе продавца — артикул, привязанный к сертификату. Передайте параметр, если нужны сертификаты, к которым привязаны определённые товары.
- **status** `string` — Статус сертификата. Передайте параметр, если нужны сертификаты с определённым статусом.
- **type** `string` — Тип сертификата. Передайте параметр, если нужны сертификаты с определённым типом.
- **page** `integer <int32>` *обязательный* — Страница, с которой следует выводить список. Минимальное значение — 1.
- **page_size** `integer <int32>` *обязательный* — Количество объектов на странице. Значение — от 1 до 1000.

**Пример запроса:**

```json
{
  "offer_id": "OFFER-2026-001",
  "status": "approved",
  "type": "certificate_of_conformity",
  "page": 1,
  "page_size": 50
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список сертификатов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Список сертификатов.
  - **certificates** `Array of objects` — Информация о сертификате.
  - **page_count** `integer <int32>` — Количество страниц.

**Пример ответа (`200`):**

```json
{
  "result": {
    "certificates": [
      {
        "certificate_id": 1120593,
        "certificate_name": "Test com \"certificate_number\": ",
        "type_code": "certificate_of_ \"status_code\": \"approved",
        "accordance_type_code": "tech \"rejection_reason_code\": \"",
        "issue_date": "2021-08-12T03: \"expire_date\": ",
        "products_count": 0,
        "verification_comment": ""
      },
      {
        "certificate_id": 624047,
        "certificate_name": "Test com \"certificate_number\": ",
        "type_code": "declaration",
        "status_code": "approved",
        "accordance_type_code": "tech \"rejection_reason_code\": \"",
        "issue_date": "2020-07-03T03: \"expire_date\": ",
        "products_count": 1,
        "verification_comment": ""
      }
    ],
    "page_count": 7
  }
}
```


---

## Список возможных статусов товаров

`POST /v1/product/certificate/product_status/list`

Метод для получения списка возможных статусов товаров при их привязке к сертификату.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список статусов товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список статусов товаров.
  - **code** `string` — Код статуса товара при привязке к сертификату.
  - **name** `string` — Описание статуса.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "code": "approved",
      "name": "Одобрен"
    },
    {
      "code": "declined",
      "name": "Отклонён"
    },
    {
      "code": "awaiting_verification",
      "name": "На проверке"
    }
  ]
}
```


---

## Список товаров, привязанных к сертификату

`POST /v1/product/certificate/products/list`

> **Примечание:** 28 сентября 2026 года отключим параметры page  и page_size  в

> **Примечание:** запросе метода. Используйте параметры last_id  и limit .

**Тело запроса** (`application/json`):
- **certificate_id** `integer <int32>` *обязательный* — Идентификатор сертификата.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. При первом запросе оставьте это поле пустым. Чтобы получить следующие значения, укажите последнее значение result.items.product_id из ответа предыдущего запроса.
- **limit** `integer <int64>` — Количество значений на странице.
- **product_status_code** `string` — Статус проверки товара при привязке к сертификату.
- **page** `integer <int32>` *обязательный* — Номер страницы, с которой выводить список. Минимальное значение — 1.
- **page_size** `integer <int32>` *обязательный* — Количество объектов на странице.

**Пример запроса:**

```json
{
  "certificate_id": 624047,
  "product_status_code": "approved",
  "limit": 1000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Товары, привязанные к сертификату.
  - **items** `Array of objects` — Список товаров.
  - **count** `integer <int64>` — Количество найденных товаров.

**Пример ответа (`200`):**

```json
{
  "result": {
    "items": [
      {
        "product_id": 53110101,
        "sku": 0,
        "product_status_code": "appro"
      }
    ],
    "count": 1
  }
}
```


---

## Отвязать товар от сертификата

`POST /v1/product/certificate/unbind`

**Тело запроса** (`application/json`):
- **certificate_id** `integer <int32>` *обязательный* — Идентификатор сертификата.
- **product_id** `Array of strings <int64>` *обязательный* — Список идентификаторов товара в системе Ozon — product_id , которые нужно отвязать от сертификата.
- **skus** `Array of strings <int64>` — Список идентификаторов товаров в системе Ozon — SKU, которые нужно отвязать от сертификата.

**Пример запроса:**

```json
{
  "certificate_id": 624047,
  "skus": [
    "2901231"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товар отвязан от сертификата |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат работы метода.
  - **error** `string` — Сообщение об ошибке при отвязывании товара.
  - **product_id** `integer <int64>` — Идентификатор товара в системе Ozon — product_id .
  - **updated** `boolean` — Был ли отвязан товар от сертификата: true — отвязан, false — не отвязан.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "product_id": 53110101,
      "updated": true,
      "error": ""
    }
  ]
}
```


---

## Возможные причины отклонения сертификата

`POST /v1/product/certificate/rejection_reasons/list`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Причины отклонения сертификата |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Причины отклонения сертификата.
  - **code** `string` — Код причины отклонения сертификата.
  - **name** `string` — Описание причины отклонения сертификата.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "code": "incorrect_type",
      "name": "Необходим другой тип до"
    },
    {
      "code": "not_all_pages",
      "name": "Предоставлены не все ст"
    },
    {
      "code": "not_in_registry",
      "name": "Документа нет в едином"
    },
    {
      "code": "not_match_information",
      "name": "Копия документа не соот"
    },
    {
      "code": "not_signed",
      "name": "Документ не подписан ил"
    },
    {
      "code": "not_true",
      "name": "Информация в документе"
    },
    {
      "code": "not_valid_in_rf",
      "name": "Документ не действует н"
    },
    {
      "code": "bad_quality",
      "name": "Качество копии не позво"
    },
    {
      "code": "annulled",
      "name": "Документ аннулирован в"
    },
    {
      "code": "archive",
      "name": "Документ перенесен в ар"
    },
    {
      "code": "expired_document",
      "name": "Срок действия документа }"
    }
  ]
}
```


---

## Возможные статусы сертификатов

`POST /v1/product/certificate/status/list`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Возможные статусы сертификатов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список возможных статусов сертификатов.
  - **code** `string` — Код статуса сертификата.
  - **name** `string` — Описание статуса.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "code": "approved",
      "name": "Одобрены"
    },
    {
      "code": "awaiting_verification",
      "name": "Ожидают проверки"
    },
    {
      "code": "declined",
      "name": "Отклонены"
    },
    {
      "code": "verification",
      "name": "На проверке"
    }
  ]
}
```


---
