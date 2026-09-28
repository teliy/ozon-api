# Работа с FBP-черновиками

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 531. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Получить список партнёрских складов

`POST /v1/fbp/warehouse/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список партнёрских складов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **warehouses** `Array of objects` — Список складов.
  - **address_detailing** `object` — Детали адреса.
  - **id** `integer <int64>` — Идентификатор склада.
  - **is_bonded** `boolean` — true , если склад бондовый.
  - **name** `string` — Название склада.
  - **partner_name** `string` — Название партнёра.
  - **supply_types** `Array of integers <int32>` — Тип поставки.
  - **timezone_name** `string` — Часовой пояс склада.

**Пример ответа (`200`):**

```json
{
  "warehouses": [
    {
      "address_detailing": {
        "city": "string",
        "country": "string",
        "house": "string",
        "region": "string",
        "street": "string",
        "zipcode": "string"
      },
      "id": 0,
      "is_bonded": true,
      "name": "string",
      "partner_name": "string",
      "supply_types": [
        0
      ],
      "timezone_name": "string"
    }
  ]
}
```


---

## Получить информацию о черновике поставки

`POST /v1/fbp/draft/get`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Детали черновика поставки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **bundle_id** `string` — Идентификатор списка провалидированных товаров.
- **cancellation_state** `object` — Статус отмены.
- **created_at** `string <date-time>` — Дата создания черновика.
- **decline_reason** `object` — Причина отказа.
- **deleted_at** `string <date-time>` — Дата удаления черновика.
- **delivery_details** `object` — Детали доставки.
- **editable** `boolean` — true , если черновик можно изменить.
- **id** `integer <int64>` — Идентификатор черновика.
- **is_cancelable** `boolean` — true , если черновик можно отменить.
- **is_deletable** `boolean` — true , если черновик можно удалить.
- **is_registration_available** `boolean` — true , если доступна регистрация.
- **locked** `boolean` — true , если черновик заблокирован.
- **package_units_count** `integer <int32>` — Количество грузомест.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.
- **status** `string` — Статус черновика: DRAFT_STATUS_UNSPECIFIED — не определён; NEW — новый; SUPPLY_VARIANT_CONFIRMATION — ожидает подтверждения; SUPPLY_NOT_CONFIRMED — отклонён складом.. Enum: `"DRAFT_STATUS_UNSPECIFIED"`, `"NEW"`, `"SUPPLY_VARIANT_CONFIRMATION"`, `"SUPPLY_NOT_CONFIRMED"`.
- **supply_id** `string` — Идентификатор поставки.
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "bundle_id": "string",
  "cancellation_state": {
    "cancellation_error": {
      "error_code": "CODE_UNSPECIFIED",
      "message": "string"
    },
    "cancellation_status": "STATUS_UNSPE"
  },
  "created_at": "2019-08-24T14:15:22Z",
  "decline_reason": {
    "failed_sku_ids": [
      "string"
    ],
    "message": "string"
  },
  "deleted_at": "2019-08-24T14:15:22Z",
  "delivery_details": {
    "direct_details": {
      "by_seller_details": {
        "driver_name": "string",
        "vehicle_registration_number": "vehicle_type"
      },
      "by_tpl_details": {
        "tracking_number": "string",
        "transport_company_name": "st"
      },
      "timeslot_details": {
        "timeslot": {
          "timeslot_end": "2019-08- \"timeslot_start\": "
        },
        "timeslot_reservation_id": "s"
      }
    },
    "drop_off_point": {
      "id": 0,
      "province_uuid": "string",
      "timeslot": {
        "timeslot_end": "2019-08-24T1 \"timeslot_start\": "
      }
    },
    "pickup_details": {
      "address": "string",
      "comment": "string",
      "date": "2019-08-24T14:15:22Z",
      "sender_name": "string",
      "sender_phone": "string"
    },
    "supply_type": "SUPPLY_TYPE_UNSPECIF"
  },
  "editable": true,
  "id": 0,
  "is_cancelable": true,
  "is_deletable": true,
  "is_registration_available": true,
  "locked": true,
  "package_units_count": 0,
  "row_version": 0,
  "status": "DRAFT_STATUS_UNSPECIFIED",
  "supply_id": "string",
  "warehouse_id": 0
}
```


---

## Список черновиков поставки

`POST /v1/fbp/draft/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **count** `integer <int32>` *обязательный* — Количество элементов в ответе.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. Оставьте это поле пустым при выполнении первого запроса. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.

**Пример запроса:**

```json
{
  "count": 0,
  "last_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список черновиков поставки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернулись не все значения.
- **items** `Array of objects` — Черновики.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "items": [
    {
      "bundle_id": "string",
      "cancellation_state": {
        "cancellation_error": {
          "error_code": "CODE_UNSPE \"message\": \"string\""
        },
        "cancellation_status": "STATU"
      },
      "created_at": "2019-08-24T14:15: ",
      "deleted_at": "2019-08-24T14:15: \"delivery_details\": { \"direct_details\": { \"by_seller_details\": { \"driver_name\": \"string \"vehicle_registration_ \"vehicle_type\": "
    },
    {
      "by_tpl_details": {
        "tracking_number": "st "
      },
      "timeslot_details": {
        "timeslot": {
          "timeslot_end": "2 \"timeslot_start\": }, "
        }
      },
      "drop_off_point": {
        "id": 0,
        "province_uuid": "string",
        "timeslot": {
          "timeslot_end": "2019- \"timeslot_start\": "
        }
      },
      "pickup_details": {
        "address": "string",
        "comment": "string",
        "date": "2019-08-24T14:15 \"sender_name\": \"string",
        "sender_phone": "string"
      },
      "supply_type": "SUPPLY_TYPE_U"
    },
    {
      "editable": true,
      "id": 0,
      "is_cancelable": true,
      "is_deletable": true,
      "locked": true,
      "package_units_count": 0,
      "status": "DRAFT_STATUS_UNSPECIF \"supply_id\": \"string",
      "warehouse_id": 0
    }
  ],
  "last_id": 0
}
```


---
