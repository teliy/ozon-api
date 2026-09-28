# Работа с созданной поставкой FBP

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 565. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Сгенерировать акт приёмки

`POST /v1/fbp/act-from/create`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

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
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **errors** `Array of strings` — Причина ошибки: CREATE_ACT_ERROR_REASON_UNSPECIFIED — не определена; INVALID_ORDER_TYPE — нельзя создать акт для указанного идентификатора поставки.. Enum: `"CREATE_ACT_ERROR_REASON_UNSPECIFIED"`, `"INVALID_ORDER_TYPE"`.
- **file_uuid** `string` — Идентификатор акта приёмки.
- **is_success** `boolean` — true , если в запросе нет ошибок.

**Пример ответа (`200`):**

```json
{
  "errors": [
    "CREATE_ACT_ERROR_REASON_UNSPECIFIED ], ",
    "file_uuid\": \"string",
    {
      "is_success": true
    }
  ]
}
```


---

## Получить статус генерации акта приёмки

`POST /v1/fbp/act-from/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **file_uuid** `string` *обязательный* — Идентификатор акта приёмки.

**Пример запроса:**

```json
{
  "file_uuid": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус генерации акта приёмки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cdn_url** `string` — Ссылка на акт приёмки.
- **error** `string` — Ошибка генерации: ERROR_REASON_UNSPECIFIED — не определена; INVALID_COMPANY — неверная компания; FILE_NOT_FOUND — файл не найден; GENERATE_TIMEOUT_REACHED — превышено время генерации; GENERATION_ERROR — ошибка во время генерации.. Enum: `"ERROR_REASON_UNSPECIFIED"`, `"INVALID_COMPANY"`, `"FILE_NOT_FOUND"`, `"GENERATE_TIMEOUT_REACHED"`, `"GENERATION_ERROR"`.
- **status** `string` — Статус генерации: STATUS_UNSPECIFIED — не определён; NOT_EXIST — не существует; PROCESSING — в процессе; EXIST — завершена; ERROR — ошибка.. Enum: `"STATUS_UNSPECIFIED"`, `"NOT_EXIST"`, `"PROCESSING"`, `"EXIST"`, `"ERROR"`.

**Пример ответа (`200`):**

```json
{
  "cdn_url": "string",
  "error": "ERROR_REASON_UNSPECIFIED",
  "status": "STATUS_UNSPECIFIED"
}
```


---

## Сгенерировать транспортную накладную

`POST /v1/fbp/act-to/create`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

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
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **code** `string` — Идентификатор транспортной накладной.

**Пример ответа (`200`):**

```json
{
  "code": "string"
}
```


---

## Получить статус генерации транспортной накладной

`POST /v1/fbp/act-to/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **code** `string` *обязательный* — Идентификатор транспортной накладной.
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "code": "string",
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус генерации транспортной накладной |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_message** `string` — Описание ошибки.
- **label_url** `string` — Ссылка на этикетки для поставки.
- **state** `string` — Статус генерации: STATE_TYPE_UNSPECIFIED — не определён; IN_PROGRESS — в процессе; FINISHED — завершилась успешно; FAILED — ошибка.. Enum: `"STATE_TYPE_UNSPECIFIED"`, `"IN_PROGRESS"`, `"FINISHED"`, `"FAILED"`.

**Пример ответа (`200`):**

```json
{
  "error_message": "string",
  "label_url": "string",
  "state": "STATE_TYPE_UNSPECIFIED"
}
```


---

## Получить информацию о завершённой поставке

`POST /v1/fbp/archive/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

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
| `200` | Информация о завершённой поставке |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **act_file_uuid** `string` — Идентификатор акта приёмки.
- **bundle_id** `string` — Идентификатор провалидированного списка товаров.
- **bundle_sku_summary** `object` — Сводная информация по товарам в поставке.
- **business_flow_type_id** `integer <int64>` — Идентификатор типа поставки.
- **created_date** `string <date-time>` — Дата и время создания заявки на поставку.
- **decline_reason** `object` — Причина отклонения поставки.
- **delivery_details** `object` — Детали доставки.
- **has_act** `boolean` — true , если был сформирован акт приёмки.
- **has_label** `boolean` — true , если были сформированы этикетки.
- **id** `integer <int64>` — Номер записи в архиве.
- **order_draft_id** `integer <int64>` — Идентификатор черновика поставки.
- **order_number** `string` — Идентификатор завершённой поставки.
- **package_units_count** `integer <int32>` — Количество грузомест.
- **receive_date** `string <date-time>` — Дата и время принятия поставки.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.
- **status** `string` — Статус завершённой поставки: ARCHIVE_STATUS_UNSPECIFIED — не определён; COMPLETED — завершена; REJECTED_AT_SUPPLY_WAREHOUSE — отклонена складом; CANCELLED_BY_SELLER — отменена продавцом.. Enum: `"ARCHIVE_STATUS_UNSPECIFIED"`, `"COMPLETED"`, `"REJECTED_AT_SUPPLY_WAREHOUSE"`, `"CANCELLED_BY_SELLER"`.
- **supply_id** `string` — Идентификатор поставки.
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "act_file_uuid": "string",
  "bundle_id": "string",
  "bundle_sku_summary": {
    "rounded_total_volume_in_litres": 0,
    "total_items_count": 0,
    "total_quantity": 0
  },
  "business_flow_type_id": 0,
  "created_date": "2019-08-24T14:15:22Z",
  "decline_reason": {
    "code": "DECLINE_REASON_CODE_UNSPECI \"message\": \"string\""
  },
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
  "has_act": true,
  "has_label": true,
  "id": 0,
  "order_draft_id": 0,
  "order_number": "string",
  "package_units_count": 0,
  "receive_date": "2019-08-24T14:15:22Z",
  "row_version": 0,
  "status": "ARCHIVE_STATUS_UNSPECIFIED",
  "supply_id": "string",
  "warehouse_id": 0
}
```


---

## Получить список завершённых поставок

`POST /v1/fbp/archive/list`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **count** `string <int32>` *обязательный* — Количество элементов в ответе.
- **last_id** `string <int64>` — Идентификатор последнего значения на странице. Оставьте это поле пустым при выполнении первого запроса. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.

**Пример запроса:**

```json
{
  "count": "string",
  "last_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список завершённых поставок |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернулись не все значения.
- **items** `Array of objects` — Завершённые поставки.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "items": [
    {
      "act_file_uuid": "string",
      "bundle_id": "string",
      "bundle_sku_summary": {
        "rounded_total_volume_in_litr \"total_items_count": 0,
        "total_quantity": 0
      },
      "created_date": "2019-08-24T14:1 \"decline_reason\": { \"code\": ",
      "message": "string"
    },
    {
      "delivery_details": {
        "direct_details": {
          "by_seller_details": {
            "driver_name": "string ",
            "vehicle_type": "strin"
          },
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
        "external_order_id": "string",
        "has_act": true,
        "has_label": true,
        "order_draft_id": 0,
        "package_units_count": 0,
        "receive_date": "2019-08-24T14:1 \"row_version\": 0",
        "status": "ARCHIVE_STATUS_UNSPEC \"supply_id\": \"string",
        "warehouse_id": 0,
        "whc_order_id": 0
      }
    }
  ],
  "last_id": 0
}
```


---

## Cоздать задание на генерацию этикеток

`POST /v1/fbp/label/create`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

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
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **code** `string` — Идентификатор задания на генерацию этикеток.

**Пример ответа (`200`):**

```json
{
  "code": "string"
}
```


---

## Получить статус задания на генерацию этикеток

`POST /v1/fbp/label/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **code** `string` *обязательный* — Идентификатор задания на генерацию этикеток.
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "code": "string",
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **label_url** `string` — Ссылка на этикетки для поставки.
- **state** `string` — Статус задания на генерацию этикеток: UNSPECIFIED — не определён; IN_PROGRESS — в процессе генерации; FINISHED — генерация завершилась успешно; FAILED — генерация завершилась с ошибкой.. Enum: `"UNSPECIFIED"`, `"IN_PROGRESS"`, `"FINISHED"`, `"FAILED"`.

**Пример ответа (`200`):**

```json
{
  "label_url": "string",
  "state": "UNSPECIFIED"
}
```


---

## Получить информацию о конкретной поставке

`POST /v1/fbp/order/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

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
| `200` | Детали поставки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **attention_reasons** `Array of strings` — Причины предупреждения: ORDER_ATTENTION_TYPE_UNSPECIFIED — не определена; OLD — устаревшая заявка; TIME_SLOT_EXPIRED — таймслот просрочен.. Enum: `"ORDER_ATTENTION_TYPE_UNSPECIFIED"`, `"OLD"`, `"TIME_SLOT_EXPIRED"`.
- **bundle_uuid** `string` — Идентификатор товарного состава.
- **can_be_cancelled** `boolean` — true , если заявку можно отменить.
- **cancellation_state** `object` — Статус отмены.
- **created_date** `string <date-time>` — Дата создания поставки.
- **delivery_details** `object` — Детали доставки.
- **draft_id** `integer <int64>` — Идентификатор черновика.
- **has_consignment_note** `boolean` — true , если есть подписанные документы.
- **has_label** `boolean` — true , если есть этикетки.
- **id** `integer <int64>` — Идентификатор заявки на поставку.
- **locked** `boolean` — true , если нельзя редактировать поставку.
- **order_number** `string` — Номер поставки.
- **package_units_count** `integer <int32>` — Количество грузомест.
- **receive_date** `string <date-time>` — Дата и время принятия поставки.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.
- **status** `string` — Статус заказа: ORDER_STATUS_UNSPECIFIED — не определён; READY_TO_SUPPLY — готов к отгрузке; FILLING_DELIVERY_DETAILS — заполнение данных поставки; COURIER_ASSIGNED — курьер назначен; COURIER_PICKED_UP — курьер забрал поставку; ACCEPTANCE_AT_DROP_OFF_POINT — принято на drop-off пункте; IN_TRANSIT_TO_STORAGE_WAREHOUSE — в пути на склад размещения; ACCEPTANCE_AT_STORAGE_WAREHOUSE — приёмка на складе; CANCELLED — заявка отменена.. Enum: `"ORDER_STATUS_UNSPECIFIED"`, `"READY_TO_SUPPLY"`, `"FILLING_DELIVERY_DETAILS"`, `"COURIER_ASSIGNED"`, `"COURIER_PICKED_UP"`, `"ACCEPTANCE_AT_DROP_OFF_POINT"`, `"IN_TRANSIT_TO_STORAGE_WAREHOUSE"`, `"ACCEPTANCE_AT_STORAGE_WAREHOUSE"`, `"CANCELLED"`.
- **supply_id** `string` — Идентификатор поставки.
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "attention_reasons": "ORDER_ATTENTION_TY \"bundle_uuid\": \"string",
  "can_be_cancelled": true,
  "cancellation_state": {
    "cancellation_error": {
      "error_code": "CODE_UNSPECIFIED",
      "message": "string"
    },
    "cancellation_status": "STATUS_UNSPE"
  },
  "created_date": "2019-08-24T14:15:22Z",
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
  "draft_id": 0,
  "has_consignment_note": true,
  "has_label": true,
  "id": 0,
  "locked": true,
  "order_number": "string",
  "package_units_count": 0,
  "receive_date": "2019-08-24T14:15:22Z",
  "row_version": 0,
  "status": "ORDER_STATUS_UNSPECIFIED",
  "supply_id": "string",
  "warehouse_id": 0
}
```


---

## Получить список поставок

`POST /v1/fbp/order/list`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **count** `integer <int32>` *обязательный* — Количество поставок в ответе.
- **last_id** `integer <int64>` — Идентификатор последней поставки на странице. Для первого запроса оставьте это поле пустым. Чтобы получить следующие значения, укажите id последней поставки из ответа предыдущего запроса.

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
| `200` | Список поставок |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернули не все поставки.
- **items** `Array of objects` — Поставки.
- **last_id** `integer <int64>` — Идентификатор последней поставки на странице.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "items": [
    {
      "attention_reasons": "ORDER_ATTE \"bundle_summary\": { ",
      "total_item_count": 0,
      "total_quantity": 0
    },
    {
      "can_be_cancelled": true,
      "cancellation_state": {
        "cancellation_error": {
          "error_code": "CODE_UNSPE \"message\": \"string\""
        },
        "cancellation_status": "STATU"
      },
      "created_date": "2019-08-24T14:1 \"delivery_details\": { \"direct_details\": { \"by_seller_details\": { \"driver_name\": \"string \"vehicle_registration_ \"vehicle_type\": "
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
      "has_consignment_note": true,
      "has_label": true,
      "id": 0,
      "locked": true,
      "order_number": "string",
      "package_units_count": 0,
      "receive_date": "2019-08-24T14:1 \"status\": ",
      "supply id": "string",
      "supply_id": "string",
      "warehouse_id": 0
    }
  ],
  "last_id": 0
}
```


---

## Получить список отправлений

`POST /v1/posting/fbp/list`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр для поиска отправлений.
- **limit** `integer <int64>` — Количество значений в ответе.
- **sort_by** `string` — Параметр, по которому сортируются отправления: last_change_status_date — по дате последнего изменения статуса; in_process_at — по дате начала обработки.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "name": "string",
    "offer_id": "string",
    "posting_numbers": [
      "string"
    ],
    "since": "2019-08-24T14:15:22Z",
    "statuses": [
      "string"
    ],
    "to": "2019-08-24T14:15:22Z"
  },
  "limit": 1,
  "sort_by": "string",
  "sort_dir": "ASC"
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
- **postings** `Array of objects` — Список отправлений.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "postings": [
    {
      "financial_data": {
        "cluster_from": "string",
        "cluster_to": "string",
        "delivery_amount": 0,
        "products": [
          {
            "actions": [
              {
                "action_id": "s \"date_from\": ",
                "date_to": "201 \"discount_perce \"discount_value ",
                "description": ""
              }
            ],
            "commissions_currency_ \"old_price": 0,
            "price": 0,
            "product_id": 0,
            "quantity": 0,
            "total_discount_percen \"posting_commission": "amount",
            "payout": 0,
            "percent": 0
          },
          {
            "return_commission": {
              "amount": 0,
              "payout": 0,
              "percent": 0
            }
          }
        ]
      },
      "in_process_at": "2019-08-24T14: ",
      "order_date": "2019-08-24T14:15: \"order_id\": 0",
      "order_number": "string",
      "posting_number": "string",
      "products": [
        {
          "customer_price": {
            "amount": "string",
            "currency": "string"
          },
          "name": "string",
          "offer_id": "string",
          "price": {
            "amount": "string",
            "currency": "string"
          },
          "quantity": 0,
          "seller_price": {
            "amount": "string",
            "currency": "string"
          },
          " k \" 0 \"sku": 0
        }
      ],
      "provider_id": 0,
      "status": "string"
    }
  ]
}
```


---
