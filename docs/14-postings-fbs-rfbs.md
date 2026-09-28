# Обработка заказов FBS и rFBS

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 176. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Получить список необработанных отправлений

## Получить список необработанных отправлений

`POST /v4/posting/fbs/unfulfilled/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает список необработанных отправлений за указанный период времени — он должен быть не больше одного года. Возможные статусы отправлений: awaiting_approve — ожидает подтверждения; awaiting_deliver — ожидает отгрузки; client_arbitration — клиентский арбитраж доставки; delivering — доставляется; cancelled — отменено; not_accepted — не принято на сортировочном центре. Чтобы получать актуальную дату отгрузки, регулярно обновляйте информацию об отправлениях или подключите пуш-уведомления.

```
awaiting_registration  — ожидает регистрации;
acceptance_in_progress  — идёт приёмка;
awaiting_packaging  — ожидает упаковки;
arbitration  — арбитраж;
driver_pickup  — у водителя;
```

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр запроса. Используйте фильтр по времени сборки — cutoff или по дате передачи отправления в доставку — delivering_date . Если использовать их вместе, в ответе вернётся ошибка. Чтобы использовать фильтр по времени сборки, заполните поля cutoff_from и cutoff_to . Чтобы использовать фильтр по дате передачи отправления в доставку, заполните поля delivering_date_from и delivering_date_to .
- **limit** `integer <int64>` — Количество значений в ответе.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.
- **translit** `boolean` — true , чтобы включить транслитерацию адреса из кириллицы в латиницу.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "sort_dir": "asc",
  "limit": 100,
  "filter": {
    "cutoff_from": "2026-01-21T07:13:56. ",
    "cutoff_to": "2026-01-21T07:13:56.04 \"delivery_method_ids\": [ 123456 ]",
    "statuses": [
      "awaiting_packaging",
      "awaiting_deliver",
      "delivering"
    ],
    "warehouse_ids": [
      3092889984
    ],
    "provider_ids": [
      57
    ],
    "last_change_status_date": {
      "from": "2026-01-21T07:13:56.042 ",
      "to": "2026-01-21T07:13:56.042Z"
    }
  },
  "cursor": "",
  "with": {
    "barcodes": true,
    "analytics_data": true,
    "financial_data": true,
    "legal_info": true
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список необработанных отправлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **count** `integer <int64>` — Количество отправлений в ответе.
- **cursor** `string` — Указатель для выборки следующих данных.
- **has_next** `boolean` — true , если в ответе вернулись не все отправления.
- **postings** `Array of objects` — Список отправлений.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "cursor": "eyJmaWVsZHMiOlt7Im5hbWUiOiJvc \"postings\": [ { \"posting_number\": ",
  "order_id": 34953320005,
  "order_number": "41517061-0214",
  "pickup_code_verified_at": null,
  "status": "awaiting_deliver",
  "substatus": "posting_in_carriag \"delivery_method\": { \"id\": 20605650762000",
  "name": "Доставка Ozon самост \"warehouse_id\": 2060565076200 \"warehouse\": \"17023",
  "tpl_provider_id": 24,
  "tpl_provider": "Доставка Ozo",
  "delivery_schema": "fbs",
  "tracking_number": "",
  "tpl_integration_type": "ozon",
  "in_process_at": "2026-05-04T06: \"integration_type_flow\": \"ozon",
  "shipment_date": "2026-05-05T06: \"shipment_date_without_delay\": ",
  "sorting_center": null,
  "optional": {
    "products_with_possible_manda 4116250392 ] }, \"cancellation": {
      "cancel_reason_id": 0,
      "cancel_reason": "",
      "cancellation_type": "",
      "cancelled_after_ship": false,
      "affect_cancellation_rating": "cancellation_initiator\": \""
    },
    "customer": null,
    "products": [
      {
        "is_blr_traceable": false,
        "is_marketplace_buyout": "offer_id\": \"S5200657-28",
        "name": "Кроссовки для ма \"sku\": 4116250392",
        "quantity": 1,
        "imei": [],
        "weight": 0.549,
        "product_color": "темно-с \"price\": { \"amount\": \"300",
        "currency": "RUB"
      }
    ],
    "addressee": null,
    "barcodes": {
      "upper_barcode": "0",
      "lower_barcode": "0"
    },
    "analytics_data": {
      "region": "",
      "city": "",
      "delivery_type": "PVZ",
      "is_premium": false,
      "payment_type_group_name": "Б \"warehouse_id\": 2060565076200 \"warehouse\": \"17023",
      "tpl_provider_id": 24,
      "tpl_provider": "Доставка Ozo \"delivery_date_begin\": ",
      "delivery_date_end": "2026-05 \"is_legal\": true",
      "client_delivery_date_begin": "client_delivery_date_end"
    },
    "destination_place_id": 0,
    "destination_place_name": "",
    "financial_data": {
      "products": [
        {
          "payout": 0,
          "product_id": 41162503,
          "old_price": 300,
          "price": 300,
          "total_discount_value": "total_discount_percen",
          "quantity": 1,
          "customer_price": {
            "amount": "300",
            "currency": "RUB"
          },
          "actions": [],
          "commission": {
            "amount": 0,
            "percent": 0,
            "currency": "RUB"
          }
        }
      ],
      "cluster_from": "Москва",
      "cluster_to": "Москва"
    },
    "is_express": false,
    "legal_info": {
      "company_name": "",
      "inn": "",
      "kpp": ""
    },
    "quantum_id": 0,
    "require_blr_traceable_attrs": "f",
    "requirements": {
      "products_requiring_gtd": [
        4116250392
      ],
      "products_requiring_country": "products_requiring_mandatory \"products_requiring_rnpt\": [ \"products_requiring_jw_uin\": ",
      "products_requiring_imei": [
        {
          "products_requiring_weight": ""
        },
        {
          "scanit": "ii30525117479",
          "tariffication": {
            "current_tariff_rate": 3,
            "current_tariff_type": "commi \"current_tariff_charge\": { \"amount\": \"100",
            "currency": "RUB"
          },
          "current_tariff_min_charge": "amount\": \"100",
          "currency": "RUB"
        },
        {
          "next_tariff_rate": 0,
          "next_tariff_type": "",
          "next_tariff_charge": null,
          "next_tariff_min_charge": "nul",
          "next_tariff_starts_at": null
        },
        {
          "external_order": {
            "is_external": false,
            "platform_name": ""
          },
          "volume_weight": 0,
          "is_click_and_collect": false,
          "delivering_date": null,
          "is_multibox": false,
          "multi_box_qty": 1,
          "is_presortable": false,
          "prr_option": "",
          "parent_posting_number": "",
          "available_actions": [
            "add_additional_info",
            "cancel",
            "has_barcode_for_printing",
            "label_download",
            "label_download_small"
          ],
          "tariffication_steps": [
            {
              "min_charge": null,
              "tariff_charge": {
                "amount": "9",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 3",
              "tariff_type": "discount"
            },
            {
              "min_charge": null,
              "tariff_charge": {
                "amount": "6",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 2",
              "tariff_type": "discount"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 1",
              "tariff_type": "commissio"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 2",
              "tariff_type": "commissio"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "99 \"tariff_rate\": 3",
              "tariff_type": "commissio"
            }
          ],
          "container_sort_type": "sort",
          "container": null
        }
      ],
      "count": 2177
    }
  }
}
```


---

## Список необработанных отправлений

`POST /v3/posting/fbs/unfulfilled/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает список необработанных отправлений за указанный период времени — он должен быть не больше одного года. Возможные статусы отправлений: awaiting_approve — ожидает подтверждения, awaiting_deliver — ожидает отгрузки, client_arbitration — клиентский арбитраж доставки, delivering — доставляется, cancelled — отменено, not_accepted — не принят на сортировочном центре. Чтобы получать актуальную дату отгрузки, регулярно обновляйте информацию об отправлениях или подключите пуш-уведомления.

> **Примечание:** С 31 августа 2026 года метод будет отключён. Переключитесь на

```
awaiting_registration  — ожидает регистрации,
acceptance_in_progress  — идёт приёмка,
awaiting_packaging  — ожидает упаковки,
arbitration  — арбитраж,
driver_pickup  — у водителя,
```

**Тело запроса** (`application/json`):
- **dir** `string` — Направление сортировки: asc — по возрастанию, desc — по убыванию.
- **filter** `object` *обязательный* — Фильтр запроса. Используйте фильтр либо по времени сборки — cutoff , либо по дате передачи отправления в доставку — delivering_date . Если использовать их вместе, в ответе вернётся ошибка. Чтобы использовать фильтр по времени сборки, заполните поля cutoff_from и cutoff_to . Чтобы использовать фильтр по дате передачи отправления в доставку, заполните поля delivering_date_from и delivering_date_to .
- **limit** `integer <int64>` *обязательный* — Количество значений в ответе: максимум — 1000, минимум — 1.
- **offset** `integer <int64>` *обязательный* — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "dir": "ASC",
  "filter": {
    "cutoff_from": "2021-08-24T14:15:22Z ",
    "cutoff_to": "2021-08-31T14:15:22Z",
    "delivery_method_id": [],
    "is_quantum": false,
    "provider_id": [],
    "status": "awaiting_packaging",
    "warehouse_id": []
  },
  "limit": 100,
  "offset": 0,
  "with": {
    "analytics_data": true,
    "barcodes": true,
    "financial_data": true,
    "legal_info": false,
    "translit": true
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список необработанных отправлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат запроса.
  - **count** `integer <int64>` — Счётчик элементов в ответе.
  - **postings** `Array of objects` — Список отправлений и подробная информация по каждому.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "cursor": "eyJmaWVsZHMiOlt7Im5hbWUiOiJvc \"postings\": [ { \"posting_number\": ",
  "order_id": 35566808085,
  "order_number": "0132112277-0102 \"pickup_code_verified_at\": null",
  "status": "awaiting_packaging",
  "substatus": "posting_created",
  "delivery_method": {
    "id": 1020005003107121,
    "name": "Доставка Ozon самост \"warehouse_id\": 1020005003107 \"warehouse\": \"FBS LikeSK",
    "tpl_provider_id": 24,
    "tpl_provider": "Доставка Ozo"
  },
  "delivery_schema": "fbs",
  "tracking_number": "",
  "tpl_integration_type": "ozon",
  "in_process_at": "2026-03-30T11: \"integration_type_flow\": \"ozon",
  "shipment_date": "2026-03-31T09: \"shipment_date_without_delay\": ",
  "sorting_center": null,
  "optional": {
    "products_with_possible_manda }, \"cancellation": {
      "cancel_reason_id": 0,
      "cancel_reason": "",
      "cancellation_type": "",
      "cancelled_after_ship": false,
      "affect_cancellation_rating": "cancellation_initiator\": \""
    },
    "container": {
      "cargo_type": "BOX",
      "container_date": "string",
      "container_id": 0,
      "container_number": 0
    },
    "container_sort_type": "string",
    "customer": null,
    "products": [
      {
        "is_blr_traceable": false,
        "is_marketplace_buyout": "offer_id\": \"SK-58 (малин \"name\": ",
        "sku": 827098843,
        "quantity": 1,
        "imei": [],
        "weight": 0.55,
        "product_color": "малинов \"price\": { \"amount\": \"1530",
        "currency": "RUB"
      }
    ],
    "addressee": null,
    "barcodes": null,
    "analytics_data": null,
    "destination_place_id": 0,
    "destination_place_name": "",
    "financial_data": null,
    "is_express": false,
    "legal_info": null,
    "quantum_id": 0,
    "require_blr_traceable_attrs": "f",
    "requirements": {
      "products_requiring_gtd": [],
      "products_requiring_country": "products_requiring_mandatory \"products_requiring_rnpt\": [ \"products_requiring_jw_uin\": ",
      "products_requiring_imei": [
        {
          "products_requiring_weight": ""
        },
        {
          "tariffication": {
            "current_tariff_rate": 0,
            "current_tariff_type": "no_di \"current_tariff_charge\": { \"amount\": \"0",
            "currency": "RUB"
          },
          "current_tariff_min_charge": "next_tariff_rate",
          "next_tariff_type": "commissi \"next_tariff_charge\": { \"amount\": \"50",
          "currency": "RUB"
        },
        {
          "next_tariff_min_charge": {
            "amount": "50",
            "currency": "RUB"
          },
          "next_tariff_starts_at": "202"
        },
        {
          "external_order": {
            "is_external": false,
            "platform_name": ""
          },
          "volume_weight": 0,
          "is_click_and_collect": false,
          "delivering_date": null,
          "is_multibox": false,
          "multi_box_qty": 1,
          "is_presortable": false,
          "prr_option": "",
          "parent_posting_number": "",
          "available_actions": [
            "cancel",
            "has_barcode_for_printing",
            "product_cancel",
            "ship",
            "ship_async"
          ],
          "tariffication_steps": [
            {
              "min_charge": null,
              "tariff_charge": {
                "amount": "0",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 0",
              "tariff_type": "no_discou"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 1",
              "tariff_type": "commissio"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 1",
              "tariff_type": "commissio"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 2",
              "tariff_type": "commissio"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "20 \"tariff_rate\": 2",
              "tariff_type": "commissio"
            },
            {
              "min charge": {
                "min_charge": {
                  "amount": "150",
                  "currency": "RUB"
                },
                "tariff_charge": {
                  "amount": "150",
                  "currency": "RUB"
                },
                "tariff_deadline_at": "99 \"tariff_rate\": 3",
                "tariff_type": "commissio"
              },
              "count": 38
            }
          ]
        }
      ]
    }
  }
}
```


---

## Получить список отправлений

`POST /v4/posting/fbs/list`

Возвращает список отправлений за указанный период времени — он должен быть не больше одного года. Чтобы получать актуальную дату отгрузки, регулярно обновляйте информацию об отправлениях или подключите пуш-уведомления.

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений в ответе.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.
- **translit** `boolean` — true , чтобы включить транслитерацию адреса из кириллицы в латиницу.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "sort_dir": "asc",
  "filter": {
    "order_numbers": [
      "12345-1"
    ],
    "delivery_method_ids": [
      123456789
    ],
    "integration_type_flow": [
      "ozon"
    ],
    "is_blr_traceable": false,
    "last_changed_status_date": {
      "from": "2026-04-01T19:47:39.878 ",
      "to": "2026-04-02T11:47:39.878Z"
    },
    "order_id": 123456,
    "since": "2026-04-01T19:47:39.878Z",
    "to": "2026-04-02T11:47:39.878Z",
    "statuses": [
      "awaiting_packaging",
      "awaiting_deliver",
      "delivering",
      "delivered"
    ],
    "provider_ids": [
      123
    ],
    "warehouse_ids": [
      3092889984
    ]
  },
  "limit": 100,
  "cursor": "",
  "with": {
    "analytics_data": true,
    "barcodes": true,
    "financial_data": true,
    "legal_info": true,
    "translit": true
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
  "cursor": "eyJmaWVsZHMiOlt7Im5hbWUiOiJvc \"has_next\": false",
  "postings": [
    {
      "addressee": {
        "name": "Иван Петров"
      },
      "analytics_data": {
        "city": "Москва",
        "client_delivery_date_begin": "client_delivery_date_end\": \" \"delivery_date_begin\": ",
        "delivery_date_end": "2026-05 \"delivery_type\": \"PVZ",
        "is_legal": false,
        "is_premium": true,
        "payment_type_group_name": "Б \"region\": ",
        "tpl_provider": "Доставка Ozo \"tpl_provider_id\": 24",
        "warehouse": "Софьино",
        "warehouse_id": 17023
      },
      "available_actions": [
        "pack",
        "ship",
        "cancel"
      ],
      "barcodes": {
        "lower_barcode": "60130248180 \"upper_barcode\": "
      },
      "cancellation": {
        "affect_cancellation_rating": "cancel_reason\": \"",
        "cancel_reason_id": 0,
        "cancellation_initiator": "",
        "cancellation_type": "",
        "cancelled_after_ship": false
      },
      "container": {
        "cargo_type": "BOX",
        "container_date": "2026-05-14 \"container_id\": 100500",
        "container_number": 42
      },
      "container_sort_type": "standard \"customer\": { \"address\": { \"address_tail\": ",
      "city": "Москва",
      "comment": "Домофон не ра \"country\": \"Россия",
      "district": "ЦАО",
      "latitude": 55.7558,
      "longitude": 37.6176,
      "provider_pvz_code": "PVZ \"pvz_code\": 456",
      "region": "Москва",
      "zip_code": "101000"
    },
    {
      "customer_email": "ivan.petro \"customer_id\": 12345678",
      "name": "Иван Петров",
      "phone": "+79031234567"
    },
    {
      "delivering_date": "2026-05-19T1 \"delivery_method\": { \"id\": 20605650762000",
      "name": "Доставка Ozon самост \"tpl_provider\": ",
      "tpl_provider_id": 24,
      "warehouse": "17023",
      "warehouse_id": 2060565076200
    },
    {
      "delivery_schema": "fbs",
      "destination_place_id": 500,
      "destination_place_name": "ПВЗ № \"external_order\": { \"is_external\": false",
      "platform_name": ""
    },
    {
      "financial_data": {
        "cluster_from": "Москва",
        "cluster_to": "Казань",
        "products": [
          {
            "actions": [
              "Округление"
            ],
            "commission": {
              "amount": 120,
              "currency": "RUB",
              "percent": 10
            },
            "customer_price": {
              "amount": "2500.00 \"currency\": \"RUB\""
            },
            "old_price": 3000,
            "payout": 2100,
            "price": 2500,
            "product_id": 19046861,
            "quantity": 2
          }
        ]
      },
      "in_process_at": "2026-05-14T08: \"integration_type_flow\": \"ozon",
      "is_click_and_collect": false,
      "is_express": false,
      "is_multibox": false,
      "is_presortable": true,
      "legal_info": {
        "company_name": "ООО Ромашка",
        "inn": "7701234567",
        "kpp": "770101001"
      },
      "multi_box_qty": 1,
      "optional": {
        "products_with_possible_manda }, i \"order_id": 33301885134,
        "order_number": "0208245774-0029 \"parent_posting_number\": \"",
        "pickup_code_verified_at": null,
        "posting_number": "0208245774-00 \"products\": [ { \"imei\": [ ]",
        "is_blr_traceable": false,
        "is_marketplace_buyout": "name\": \"Смартфон Xiaomi \"offer_id\": \"b4408110",
        "price": {
          "amount": "12990.00",
          "currency": "RUB"
        },
        "product_color": "чёрный",
        "quantity": 1,
        "sku": 1904686181,
        "weight": 0.42
      },
      "imei": [
        "123456789012345",
        "987654321098765"
      ],
      "is_blr_traceable": false,
      "is_marketplace_buyout": "name\": \"Наушники Bluetoo \"offer_id\": \"h667722",
      "price": {
        "amount": "3490.00",
        "currency": "RUB"
      },
      "product_color": "белый",
      "quantity": 2,
      "sku": 1904686182,
      "weight": 0.15
    }
  ],
  "prr_option": "standard",
  "quantum_id": 98765,
  "require_blr_traceable_attrs": "f",
  "requirements": {
    "products_requiring_change_co \"products_requiring_country": "products_requiring_gtd\": [ \"1904686181",
    "products_requiring_imei": [
      {
        "products_requiring_jw_uin": "products_requiring_mandatory \"products_requiring_rnpt\": ["
      },
      {
        "scanit": "ii30525117479",
        "shipment_date": "2026-05-18T12: \"shipment_date_without_delay\": ",
        "sorting_center": null,
        "status": "awaiting_packaging",
        "substatus": "posting_created",
        "tariffication": {
          " t t iff h \" { \"current_tariff_charge": {
            "amount": "100.00",
            "currency": "RUB"
          },
          "current_tariff_min_charge": "amount\": \"50.00",
          "currency": "RUB"
        },
        "current_tariff_rate": 2,
        "current_tariff_type": "commi \"next_tariff_charge\": { \"amount\": \"150.00",
        "currency": "RUB"
      },
      {
        "next_tariff_min_charge": {
          "amount": "100.00",
          "currency": "RUB"
        },
        "next_tariff_rate": 2.5,
        "next_tariff_starts_at": "202 \"next_tariff_type\": "
      },
      {
        "tariffication_steps": [
          {
            "min_charge": {
              "amount": "24.00",
              "currency": "RUB"
            },
            "tariff_charge": {
              "amount": "24.00",
              "currency": "RUB"
            },
            "tariff_deadline_at": "20 \"tariff_rate\": 2",
            "tariff_type": "discount"
          }
        ],
        "tpl_integration_type": "ozon",
        "tracking_number": "TRK123456789 \"volume_weight\": 1.2 }"
      }
    ]
  }
}
```


---

## Список отправлений Deprecated

`POST /v3/posting/fbs/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает список отправлений за указанный период времени — он должен быть не больше одного года. has_next = true в ответе может значить, что вернули не весь массив отправлений. Чтобы получить информацию об остальных отправлениях, сделайте новый запрос с другим значением offset . Чтобы получать актуальную дату отгрузки, регулярно обновляйте информацию об отправлениях или подключите пуш-уведомления.

> **Примечание:** С 31 августа 2026 года метод будет отключён. Переключитесь на

**Тело запроса** (`application/json`):
- **dir** `string` — Направление сортировки: asc — по возрастанию, desc — по убыванию.
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений в ответе: максимум — 1000, минимум — 1.
- **offset** `integer <int64>` *обязательный* — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "dir": "ASC",
  "filter": {
    "delivery_method_id": [
      "21321684811000"
    ],
    "integration_type_flow": [
      "ozon"
    ],
    "is_blr_traceable": true,
    "is_quantum": false,
    "last_changed_status_date": {
      "from": "2023-11-03T11:47:39.878 ",
      "to": "2023-11-03T11:47:39.878Z"
    },
    "order_id": 0,
    "provider_id": [
      "24"
    ],
    "since": "2023-11-03T11:47:39.878Z",
    "status": "awaiting_packaging",
    "to": "2023-11-03T11:47:39.878Z",
    "warehouse_id": [
      "21321684811000"
    ]
  },
  "limit": 100,
  "offset": 0,
  "with": {
    "analytics_data": true,
    "barcodes": true,
    "financial_data": true,
    "translit": true
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
- **result** `object` — Массив отправлений.
  - **has_next** `boolean` — Признак, что в ответе вернули не весь массив отправлений: true — необходимо сделать новый запрос с другим значением offset , чтобы получить информацию об остальных отправлениях; false — в ответе вернули весь массив отправлений для фильтра, который был задан в запросе.
  - **postings** `Array of objects` — Информация об отправлении.

**Пример ответа (`200`):**

```json
{
  "result": {
    "postings": [
      {
        "posting_number": "0132112277 \"order_id\": 35566798085",
        "order_number": "0132112277-0 \"status\": ",
        "delivery_method": {
          "id": 1020005003107121,
          "name": "Доставка Ozon са \"warehouse_id\": 102000500 \"warehouse\": \"FBS LikeSK\" \"tpl_provider_id\": 24",
          "tpl_provider": "Доставка"
        },
        "tracking_number": "",
        "tpl_integration_type": "ozon \"in_process_at\": ",
        "integration_type_flow": "ozo \"shipment_date\": ",
        "delivering_date": null,
        "cancellation": {
          "cancel_reason_id": 0,
          "cancel_reason": "",
          "cancellation_type": "",
          "cancelled_after_ship": "f",
          "cancellation_initiator": ""
        },
        "container": {
          "cargo_type": "BOX",
          "container_date": "string \"container_id\": 0",
          "container_number": 0
        },
        "container_sort_type": "strin \"customer\": null",
        "products": [
          {
            "price": "1530.0000",
            "offer_id": "SK-58 (ма \"name\": ",
            "sku": 827098843,
            "quantity": 1,
            "currency_code": "RUB",
            "is_blr_traceable": "fa",
            "imei": []
          }
        ],
        "addressee": null,
        "barcodes": {
          "upper_barcode": "7110082 \"lower_barcode\": "
        },
        "analytics_data": {
          "region": "",
          "city": "",
          "delivery_type": "PVZ",
          "is_premium": false,
          "payment_type_group_name": "warehouse_id",
          "warehouse": "FBS LikeSK",
          "tpl_provider_id": 24,
          "tpl_provider": "Доставка \"delivery_date_begin\": ",
          "delivery_date_end": "202 \"is_legal\": false, \"client_delivery_date_beg \"client_delivery_date_end"
        },
        "financial_data": {
          "products": [
            {
              "commission_amount \"commission_percen \"payout": 0,
              "product_id": 8270,
              "old_price": 1530,
              "price": 1530,
              "total_discount_va \"total_discount_pe \"actions": [
                "Округление"
              ],
              "quantity": 1,
              "currency_code": " ",
              "customer_price": ""
            }
          ],
          "cluster_from": "Moskva",
          "cluster_to": "Rostov"
        },
        "is_express": false,
        "requirements": {
          "products_requiring_gtd": "products_requiring_count \"products_requiring_manda \"products_requiring_rnpt",
          "products_requiring_jw_ui \"products_requiring_chang \"products_requiring_imei": "products_requiring_weigh"
        },
        "parent_posting_number": "",
        "available_actions": [
          "cancel",
          "has_barcode_for_printing ",
          "product_cancel",
          "ship",
          "ship_async"
        ],
        "multi_box_qty": 1,
        "is_multibox": false,
        "substatus": "posting_created \"prr_option\": \"",
        "quantum_id": 0,
        "tariffication": {
          "current_tariff_rate": 0,
          "current_tariff_type": "n \"current_tariff_charge\": ",
          "next_tariff_rate": 0,
          "next_tariff_type": "comm \"next_tariff_charge\": ",
          "next_tariff_starts_at": "next_tariff_charge_curre"
        },
        "destination_place_id": 0,
        "destination_place_name": "",
        "is_presortable": false,
        "pickup_code_verified_at": "nu",
        "optional": {
          "products_with_possible_m }, \"legal_info": {
            "company_name": "",
            "inn": "",
            "kpp": ""
          },
          "shipment_date_without_delay": "sorting_center",
          "require_blr_traceable_attrs": "is_click_and_collect",
          "tariffication_steps": [
            {
              "min_charge": null,
              "tariff_charge": {
                "amount": "0",
                "currency": "RUB"
              },
              "tariff_deadline_at": "tariff_rate",
              "tariff_type": "no_dis"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "tariff_rate",
              "tariff_type": "commis"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "tariff_rate",
              "tariff_type": "commis"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "tariff_rate",
              "tariff_type": "commis"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "tariff_rate",
              "tariff_type": "commis"
            },
            {
              "min_charge": {
                "amount": "150",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "150",
                "currency": "RUB"
              },
              "tariff_deadline_at": "tariff_rate",
              "tariff_type": "commis"
            }
          ]
        },
        "has_next": false
      }
    ]
  }
}
```


---

## Получить информацию об отправлении по идентификатору

`POST /v3/posting/fbs/get`

Чтобы получать актуальную дату отгрузки, регулярно обновляйте информацию об отправлениях или подключите пуш-уведомления.

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Идентификатор отправления.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "posting_number": "57195475-0050-3",
  "with": {
    "analytics_data": false,
    "barcodes": false,
    "financial_data": false,
    "legal_info": false,
    "product_exemplars": false,
    "related_postings": true,
    "translit": false
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отправлении |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Информация об отправлении.
  - **additional_data** `Array of objects`
  - **addressee** `object` — Контактные данные получателя.
  - **analytics_data** `object` — Данные аналитики.
  - **available_actions** `Array of strings` — Доступные действия и информация об отправлении: arbitration — открыть спор; awaiting_delivery — перевести в статус «Ожидает отгрузки»; can_create_chat — начать чат с покупателем; cancel — отменить отправление; click_track_number — просмотреть по трек-номеру историю изменения статусов в личном кабинете; customer_phone_available — телефон покупателя; has_weight_products — весовые товары в отправлении; hide_region_and_city — скрыть регион и город покупателя в отчёте; invoice_get — получить информацию из счёта-фактуры; invoice_send — создать счёт- фактуру; invoice_update — отредактировать счёт-фактуру; label_download_big — скачать большую этикетку; label_download_small — скачать маленькую этикетку; label_download — скачать этикетку; non_int_delivered — перевести в статус «Условно доставлен»; non_int_delivering — перевести в статус «Доставляется»; non_int_last_mile — перевести в статус «Курьер в пути»; product_cancel — отменить часть товаров в отправлении; set_cutoff — необходимо указать дату отгрузки, воспользуйтесь методом /v1/posting/cutoff/set; set_timeslot — изменить время доставки покупателю; set_track_number — указать или изменить трек-номер; ship_async_in_process — отправление собирается; ship_async_retry — собрать отправление повторно после ошибки сборки; ship_async — собрать отправление; ship_with_additional_info — необходимо заполнить дополнительную информацию; ship — собрать отправление; update_cis — изменить дополнительную информацию.
  - **barcodes** `object` — Штрихкоды отправления.
  - **cancellation** `object` — Информация об отмене.
  - **courier** `object` — Данные о курьере.
  - **customer** `object` — Данные о покупателе.
  - **container** `object` — Информация о грузоместе.
  - **container_sort_type** `string` — Тип сортировки грузоместа: SORT — сортируемый; NON-SORT — несортируемый.
  - **delivering_date** `string <date-time>` — Дата передачи отправления в доставку.
  - **delivery_method** `object` — Метод доставки.
  - **delivery_price** `string` — Стоимость доставки.
  - **external_order** `object` — Информация о заказе с внешней платформы.
  - **fact_delivery_date** `string <date-time>` — Дата фактической передачи отправления в доставку.
  - **financial_data** `object` — Данные о стоимости товара, размере скидки, выплате и комиссии.
  - **in_process_at** `string <date-time>` — Дата и время начала обработки отправления.
  - **integration_type_flow** `string` — Процесс обработки отправления: ozon — доставка силами Ozon; aggregator — доставка внешней службой, Ozon регистрирует заказ; non_integrated — доставка силами продавца; 3pl_tracking — доставка внешней службой, продавец регистрирует заказ; hybrid — гибридная интеграция; hybrid_aggregator — гибридная интеграция с доставкой внешней службой, Ozon регистрирует заказ; hybrid_non_integrated — гибридная интеграция с доставкой силами продавца; hybrid_3pl_tracking — гибридная интеграция с доставкой внешней службой, продавец регистрирует заказ; click_and_collect — бронирование в магазине партнёра.
  - **is_express** `boolean` — Если использовалась быстрая доставка Ozon Express — true .
  - **is_multibox** `boolean` — Признак, что в отправлении есть многокоробочный товар и нужно передать количество коробок для него: true — до сборки передайте количество коробок через метод /v3/posting/multiboxqty/set. false — отправление собрано с указанием количества коробок в параметре multi_box_qty или в отправлении нет многокоробочного товара.
  - **legal_info** `object` — Юридическая информация о покупателе.
  - **multi_box_qty** `integer <int32>` — Количество коробок, в которые упакован товар.
  - **optional** `object` — Список товаров с дополнительными характеристиками.
  - **order_id** `integer <int64>` — Идентификатор заказа, к которому относится отправление.
  - **order_number** `string` — Номер заказа, к которому относится отправление.
  - **parent_posting_number** `string` — Номер родительского отправления, в результате разделения которого появилось текущее.
  - **pickup_code_verified_at** `string <date-time>` — Дата и время успешной валидации кода курьера. Чтобы проверить код курьера, воспользуйтесь методом /v1/posting/fbs/pick-up-code/verify.
  - **posting_number** `string` — Номер отправления.
  - **product_exemplars** `object` — Информация по продуктам и их экземплярам. Ответ содержит поле product_exemplars , если в запросе передан признак with.product_exemplars = true .
  - **products** `Array of objects` — Массив товаров в отправлении.
  - **provider_status** `string` — Статус службы доставки.
  - **prr_option** `object` — Информация об услуге погрузочно- разгрузочных работ. Актуально для КГТ-отправлений с доставкой силами продавца или интегрированной службой.
  - **related_postings** `object` — Связанные отправления.
  - **related_weight_postings** `Array of strings` — Список номеров связанных весовых отправлений.
  - **require_blr_traceable_attrs** `boolean` — true , если нужно заполнить атрибуты прослеживаемости.
  - **requirements** `object` — Cписок продуктов, для которых нужно передать страну-изготовителя, номер грузовой таможенной декларации (ГТД), регистрационный номер партии товара (РНПТ), маркировку «Честный ЗНАК», другие маркировки или вес, чтобы перевести отправление в следующий статус.
  - **scanit** `string` — Штрихкод ScanIt товара.
  - **shipment_date** `string <date-time>` — Дата и время, до которой необходимо собрать отправление. Показываем рекомендованное время отгрузки. По истечении этого времени начнёт применяться новый тариф, информацию о нём уточняйте в поле tariffication .
  - **shipment_date_without_delay** `string <date-time>` — Дата и время отгрузки без просрочки.
  - **sorting_center** `object` — Информация о сортировочном центре, в который нужно привезти отправление. Для integration_type_flow = hybrid_3pl_tracking . Если значение null , информацию получить не удалось.
  - **status** `string` — Статус отправления: acceptance_in_progress — идёт приёмка, arbitration — арбитраж, awaiting_approve — ожидает подтверждения, awaiting_deliver — ожидает отгрузки, awaiting_packaging — ожидает упаковки, awaiting_registration — ожидает регистрации, awaiting_verification — создано, cancelled — отменено, cancelled_from_split_pendin g — отменён из-за разделения отправления, client_arbitration — клиентский арбитраж доставки, delivered — доставлено, delivering — доставляется, driver_pickup — у водителя, not_accepted — не принят на сортировочном центре,
  - **substatus** `string` — Подстатус отправления: posting_acceptance_in_progre ss — идёт приёмка, posting_in_arbitration — арбитраж, posting_created — создано, posting_in_carriage — в перевозке, posting_not_in_carriage — не добавлено в перевозку, posting_registered — зарегистрировано, posting_transferring_to_deli very ( status=awaiting_deliver ) — передаётся в доставку, posting_awaiting_passport_da ta — ожидает паспортных данных, posting_created — создано, posting_awaiting_registratio n — ожидает регистрации, posting_registration_error — ошибка регистрации, posting_transferring_to_deli very ( status=awaiting_registratio n ) — передаётся курьеру, posting_split_pending — создано, posting_canceled — отменено, posting_in_client_arbitratio n — клиентский арбитраж доставки, posting_delivered — доставлено, posting_received — получено, posting_conditionally_delive red — условно доставлено, posting_in_courier_service — курьер в пути, posting_in_pickup_point — в пункте выдачи, posting_on_way_to_city — в пути в ваш город, posting_on_way_to_pickup_poi nt — в пути в пункт выдачи, posting_returned_to_warehous e — возвращено на склад, posting_transferred_to_couri er_service — передаётся в службу доставки, posting_driver_pick_up — у водителя, posting_not_in_sort_center — не принято на сортировочном центре, ship_failed — сборка не удалась.
  - **previous_substatus** `string` — Предыдущий подстатус отправления. Возможные значения: posting_acceptance_in_progre ss — идёт приёмка, posting_in_arbitration — арбитраж, posting_created — создано, posting_in_carriage — в перевозке, posting_not_in_carriage — не добавлено в перевозку, posting_registered — зарегистрировано, posting_transferring_to_deli very ( status=awaiting_deliver ) — передаётся в доставку, posting_awaiting_passport_da ta — ожидает паспортных данных, posting_created — создано, posting_awaiting_registratio n — ожидает регистрации, posting_registration_error — ошибка регистрации, posting_transferring_to_deli very ( status=awaiting_registratio n ) — передаётся курьеру, posting_split_pending — создано, posting_canceled — отменено, posting_in_client_arbitratio n — клиентский арбитраж доставки, posting_delivered — доставлено, posting_received — получено, posting_conditionally_delive red — условно доставлено, posting_in_courier_service — курьер в пути, posting_in_pickup_point — в пункте выдачи, posting_on_way_to_city — в пути в ваш город, posting_on_way_to_pickup_poi nt — в пути в пункт выдачи, posting_returned_to_warehous e — возвращено на склад, posting_transferred_to_couri er_service — передаётся в службу доставки, posting_driver_pick_up — у водителя, posting_not_in_sort_center — не принято на сортировочном центре.
  - **tpl_integration_type** `string` — Тип интеграции со службой доставки: ozon — доставка через Ozon логистику. aggregator — доставка внешней службой, Ozon регистрирует заказ. 3pl_tracking — доставка внешней службой, продавец регистрирует заказ. non_integrated — доставка силами продавца.
  - **tracking_number** `string` — Трек-номер отправления.
  - **tariffication** `object` — Информация по тарификации отгрузки.
  - **tariffication_steps** `Array of objects` — Этапы тарификации.

**Пример ответа (`200`):**

```json
{
  "result": {
    "posting_number": "0132112277-0101-1 \"order_id\": 35566798085",
    "order_number": "0132112277-0101",
    "status": "awaiting_packaging",
    "external_order": {
      "is_external": false,
      "platform_name": ""
    },
    "delivery_method": {
      "id": 1020005003107121,
      "name": "Доставка Ozon самостоят \"warehouse_id\": 1020005003107121 \"warehouse\": \"FBS LikeSK",
      "tpl_provider_id": 24,
      "tpl_provider": "Доставка Ozon"
    },
    "tracking_number": "",
    "tpl_integration_type": "ozon",
    "in_process_at": "2026-03-30T11:26:0 \"integration_type_flow\": \"ozon",
    "shipment_date": "2026-03-31T09:00:0 \"delivering_date\": null",
    "provider_status": "",
    "delivery_price": "",
    "cancellation": {
      "cancel_reason_id": 0,
      "cancel_reason": "",
      "cancellation_type": "",
      "cancelled_after_ship": false,
      "affect_cancellation_rating": "fa",
      "cancellation_initiator": ""
    },
    "container": {
      "cargo_type": "BOX",
      "container_date": "string",
      "container_id": 0,
      "container_number": 0
    },
    "container_sort_type": "string",
    "customer": null,
    "addressee": null,
    "products": [
      {
        "price": "1530.0000",
        "offer_id": "SK-58 (малиновый \"name\": ",
        "sku": 827098843,
        "quantity": 1,
        "dimensions": {
          "height": "150.00",
          "length": "500.00",
          "weight": "550",
          "width": "300.00"
        },
        "currency_code": "RUB",
        "is_blr_traceable": false,
        "is_marketplace_buyout": "fals",
        "has_imei": false,
        "weight_max": 0.55,
        "weight_min": 0,
        "is_weight_needed": false
      }
    ],
    "barcodes": null,
    "analytics_data": null,
    "financial_data": null,
    "additional_data": [],
    "is_express": false,
    "requirements": {
      "products_requiring_gtd": [],
      "products_requiring_country": [
        "products_requiring_mandatory_ma ",
        "products_requiring_rnpt",
        [],
        {
          "products_requiring_jw_uin": [],
          "products_requiring_change_count \"products_requiring_imei": [],
          "products_requiring_weight": []
        },
        {
          "product_exemplars": null,
          "courier": null,
          "parent_posting_number": "",
          "related_postings": null,
          "available_actions": [
            "cancel",
            "has_barcode_for_printing",
            "product_cancel",
            "ship",
            "ship_async"
          ],
          "multi_box_qty": 1,
          "is_multibox": false,
          "scanit": "ii30525117479",
          "substatus": "posting_created",
          "previous_substatus": "posting_split \"prr_option\": { \"code\": \"",
          "price": "",
          "currency_code": "RUB",
          "floor": ""
        },
        {
          "tariffication": {
            "current_tariff_rate": 1,
            "current_tariff_type": "no_disco \"current_tariff_charge\": ",
            "current_tariff_charge_currency_ \"next_tariff_rate": 1,
            "next_tariff_type": "commission",
            "next_tariff_charge": "50",
            "next_tariff_starts_at": "2026-0 "
          },
          "destination_place_id": 0,
          "destination_place_name": "",
          "is_presortable": false,
          "pickup_code_verified_at": null,
          "optional": {
            "products_with_possible_mandator }, \"fact_delivery_date": null,
            "legal_info": {
              "company_name": "",
              "inn": ""
            },
            "kpp": ""
          },
          "related_weight_postings": [],
          "shipment_date_without_delay": "2026 \"sorting_center\": null",
          "require_blr_traceable_attrs": false,
          "is_click_and_collect": false,
          "tariffication_steps": [
            {
              "min_charge": null,
              "tariff_charge": {
                "amount": "0",
                "currency": "RUB"
              },
              "tariff_deadline_at": "2026-0 \"tariff_rate\": 0",
              "tariff_type": "no_discount"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "2026-0 \"tariff_rate\": 1",
              "tariff_type": "commission"
            },
            {
              "min_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "50",
                "currency": "RUB"
              },
              "tariff_deadline_at": "2026-0 \"tariff_rate\": 1",
              "tariff_type": "commission"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "2026-0 \"tariff_rate\": 2",
              "tariff_type": "commission"
            },
            {
              "min_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "100",
                "currency": "RUB"
              },
              "tariff_deadline_at": "2026-0 \"tariff_rate\": 2",
              "tariff_type": "commission"
            },
            {
              "min_charge": {
                "amount": "150",
                "currency": "RUB"
              },
              "tariff_charge": {
                "amount": "150",
                "currency": "RUB"
              },
              "tariff_deadline_at": "9999-1 \"tariff_rate\": 3",
              "tariff_type": "commission"
            }
          ]
        }
      ]
    }
  }
}
```


---

## Получить информацию об отправлении по штрихкоду

`POST /v2/posting/fbs/get-by-barcode`

**Тело запроса** (`application/json`):
- **barcode** `string` *обязательный* — Штрихкод отправления. Можно получить с помощью методов /v3/posting/fbs/get, /v4/posting/fbs/list и /v4/posting/fbs/unfulfilled/list в массиве barcodes или параметре scanit .

**Пример запроса:**

```json
{
  "barcode": "20325804886000"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отправлении |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результаты запроса.
  - **barcodes** `object` — Штрихкоды отправления.
  - **cancel_reason_id** `integer <int64>` — Идентификатор причины отмены отправления.
  - **created_at** `string <date-time>` — Дата и время создания отправления.
  - **in_process_at** `string <date-time>` — Дата и время начала обработки отправления.
  - **order_id** `integer <int64>` — Идентификатор заказа, к которому относится отправление.
  - **order_number** `string` — Номер заказа, к которому относится отправление.
  - **posting_number** `string` — Номер отправления.
  - **products** `Array of objects` — Список товаров в отправлении.
  - **shipment_date** `string <date-time>` — Дата и время, до которой необходимо собрать отправление. Если отправление не собрать к этой дате — оно автоматически отменится.
  - **status** `string` — Статус отправления.

**Пример ответа (`200`):**

```json
{
  "result": {
    "order_id": 47558522075,
    "order_number": "2130415463-0013",
    "posting_number": "2130415463-0013-1 \"status\": \"delivered",
    "cancel_reason_id": 0,
    "created_at": "2025-01-29T08:58:07Z",
    "in_process_at": "2025-01-29T08:59:4 ",
    "shipment_date": "2025-01-29T18:00:0 \"products\": [ { \"sku\": 498274975",
    "name": "Стульчик для кормлен \"quantity\": 1",
    "offer_id": "6460551001",
    "price": "2300.0000"
  },
  "barcodes": {
    "upper_barcode": "%101%102931450 \"lower_barcode\": "
  }
}
```


---

## Указать количество коробок для многокоробочных отправлений

`POST /v3/posting/multiboxqty/set`

Метод для передачи количества коробок для отправлений, в которых есть многокоробочные товары. Используйте метод при работе по схеме rFBS Агрегатор — c доставкой партнёрами Ozon.

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Идентификатор многокоробочного отправления.
- **multi_box_qty** `integer <int64>` *обязательный* — Количество коробок, в которые упакован товар.

**Пример запроса:**

```json
{
  "multi_box_qty": 321231,
  "posting_number": "228245774-2229-1"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Количество коробок указано |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат передачи количества коробок.
  - **result** `boolean` — Возможные значения: true — значение передано успешно. false — при передаче произошла ошибка. Попробуйте снова.

**Пример ответа (`200`):**

```json
{
  "result": {
    "result": true
  }
}
```


---

## Список доступных стран- изготовителей

`POST /v2/posting/fbs/product/country/list`

Метод для получения списка доступных стран-изготовителей и их ISO кодов.

**Тело запроса** (`application/json`):
- **name_search** `string` — Фильтрация по строке.

**Пример запроса:**

```json
{
  "name_search": "Алжир"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список доступных стран-изготовителей |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список стран-изготовителей и ISO коды.
  - **name** `string` — Название страны на русском языке.
  - **country_iso_code** `string` — ISO код страны.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "name": "Алжир",
      "country_iso_code": "DZ"
    }
  ]
}
```


---

## Добавить информацию о стране- изготовителе товара

`POST /v2/posting/fbs/product/country/set`

Метод для добавления на продукт атрибута «Страна-изготовитель», если он не был указан.

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Номер отправления.
- **product_id** `integer <int64>` *обязательный* — Идентификатор товара в системе Ozon — product_id .
- **country_iso_code** `string` *обязательный* — Двухбуквенный код добавляемой страны по стандарту ISO_3166-1. Список доступных стран-изготовителей и их ISO коды можно получить с помощью метода /v2/posting/fbs/product/country/list.

**Пример запроса:**

```json
{
  "country_iso_code": "NO",
  "posting_number": "57195475-0050-3",
  "product_id": 180550365
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Страна-изготовитель добавлена |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **product_id** `integer <int64>` — Идентификатор товара в системе Ozon — product_id .
- **is_gtd_needed** `boolean` — Признак того, что необходимо передать номер грузовой таможенной декларации (ГТД) для продукта и отправления.

**Пример ответа (`200`):**

```json
{
  "product_id": 180550365,
  "is_gtd_needed": true
}
```


---

## Получить ограничения пункта приёма

`POST /v1/posting/fbs/restrictions`

Метод для получения габаритных, весовых и прочих ограничений пункта приёма по номеру отправления. Метод применим только для работы по схеме FBS.

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Номер отправления, для которого нужно определить ограничения.

**Пример запроса:**

```json
{
  "posting_number": "76673629-0020-1"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Ограничения пункта приёма |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object`
  - **posting_number** `string` — Номер отправления.
  - **max_posting_weight** `number <double>` — Ограничение по максимальному весу в граммах.
  - **min_posting_weight** `number <double>` — Ограничение по минимальному весу в граммах.
  - **width** `number <double>` — Ограничение по ширине в сантиметрах.
  - **length** `number <double>` — Ограничение по длине в сантиметрах.
  - **height** `number <double>` — Ограничение по высоте в сантиметрах.
  - **max_posting_price** `number <double>` — Ограничение по максимальной стоимости отправления в рублях.
  - **min_posting_price** `number <double>` — Ограничение по минимальной стоимости отправления в рублях.

**Пример ответа (`200`):**

```json
{
  "result": {
    "posting_number": "76673629-0020-1",
    "max_posting_weight": 40000,
    "min_posting_weight": 0,
    "width": 500,
    "height": 500,
    "length": 500,
    "max_posting_price": 500000,
    "min_posting_price": 0
  }
}
```


---

## Напечатать этикетку

`POST /v2/posting/fbs/package-label`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Генерирует PDF-файл с этикетками для указанных отправлений в статусе «Ожидает отгрузки» — awaiting_deliver . В одном запросе можно передать не больше 20 идентификаторов. Если хотя бы для одного отправления возникнет ошибка, этикетки не будут подготовлены для всех отправлений в запросе. Рекомендуем запрашивать этикетки через 45–60 секунд после сборки заказа. не готовы, повторите запрос позднее.

> **Примечание:** C 5 октября 2026 года метод будет возвращать новые этикетки

> **Примечание:** для отправлений FBS.

> **Примечание:** Подробнее о новых этикетках в Базе знаний продавца

> **Примечание:** С 2 ноября 2026 года метод будет отключён. Переключитесь на

> **Примечание:** label/get.

> **Примечание:** Если вы работаете по схеме rFBS или rFBS Express, изучите

> **Примечание:** процесс печати этикетки в Базе знаний продавца.

```
Ошибка The next postings aren't ready  означает, что этикетки ещё
```

**Тело запроса** (`application/json`):
- **posting_number** `Array of strings` *обязательный* — Идентификатор отправления.

**Пример запроса:**

```json
{
  "posting_number": [
    "48173252-0034-4"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Маркировка напечатана |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **file_content** `string <byte>` — Содержание файла в бинарном виде.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "application/pdf",
  "file_name": "ticket-170660-2023-07-13T13 :",
  "file_content": "PDF-1.7\n%âãÏÓ\n53 0 ob :"
}
```


---

## Создать задание на формирование этикеток

`POST /v3/posting/fbs/package-label/create`

Создаёт задания на асинхронное формирование этикеток для отправлений в статусе «Ожидает отгрузки» — awaiting_deliver . Рекомендуем запрашивать этикетки через 45–60 секунд после сборки заказа. Чтобы получить созданные этикетки, используйте

> **Примечание:** Если вы работаете по схеме rFBS или rFBS Express, изучите

> **Примечание:** процесс печати этикетки в Базе знаний продавца.

**Тело запроса** (`application/json`):
- **posting_numbers** `Array of strings` *обязательный* — Номера отправлений, для которых нужны этикетки.

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
| `200` | Задания на формирование этикеток |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **tasks** `Array of objects` — Список заданий.
  - **task_id** `integer <int64>` — Идентификатор задания. Получите файл с этикетками методом /v2/posting/fbs/package- label/get.
  - **task_type** `string` — Тип задания: big_label — для обычной этикетки; small_label — для маленькой этикетки.

**Пример ответа (`200`):**

```json
{
  "tasks": [
    {
      "task_id": 0,
      "task_type": "string"
    }
  ]
}
```


---

## Создать задание на формирование этикеток

`POST /v2/posting/fbs/package-label/create`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Метод для создания задания на асинхронное формирование этикеток для отправлений в статусе «Ожидает отгрузки» — awaiting_deliver . Метод может вернуть несколько заданий: на формирование маленькой и большой этикетки. Рекомендуем запрашивать этикетки через 45–60 секунд после сборки заказа. Чтобы получить созданные этикетки, используйте

> **Примечание:** C 5 октября 2026 года метод будет возвращать новые этикетки

> **Примечание:** для отправлений FBS.

> **Примечание:** Подробнее о новых этикетках в Базе знаний продавца

> **Примечание:** С 2 ноября 2026 года метод будет отключён. Переключитесь на

> **Примечание:** Если вы работаете по схеме rFBS или rFBS Express, изучите

> **Примечание:** процесс печати этикетки в Базе знаний продавца.

**Тело запроса** (`application/json`):
- **posting_number** `Array of strings` *обязательный* — Номера отправлений, для которых нужны этикетки.

**Пример запроса:**

```json
{
  "posting_number": [
    "4708216109137",
    "3697105098026"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задания на формирование этикеток |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **tasks** `Array of objects` — Список заданий.

**Пример ответа (`200`):**

```json
{
  "result": {
    "tasks": [
      {
        "task_id": 5819327210248,
        "task_type": "big_label"
      },
      {
        "task_id": 5819327210249,
        "task_type": "small_label"
      }
    ]
  }
}
```


---

## Создать задание на выгрузку этикеток

`POST /v1/posting/fbs/package-label/create`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Метод для создания задания на асинхронное формирование этикеток. Для получения этикеток, созданных в результате вызова метода, используйте /v1/posting/fbs/package-label/get.

> **Примечание:** C 5 октября 2026 года метод будет возвращать новые этикетки

> **Примечание:** для отправлений FBS.

> **Примечание:** Подробнее о новых этикетках в Базе знаний продавца

> **Примечание:** С 2 ноября 2026 года метод будет отключён. Переключитесь на

**Тело запроса** (`application/json`):
- **posting_number** `Array of strings` *обязательный* — Номера отправлений, для которых нужны этикетки.

**Пример запроса:**

```json
{
  "posting_number": [
    "228245774-2229-1"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Идентификатор задания на формирование этикеток |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **task_id** `integer <int64>` — Идентификатор задания на формирование этикеток.

**Пример ответа (`200`):**

```json
{
  "result": {
    "task_id": 5819327210249
  }
}
```


---

## Получить файл с этикетками

`POST /v2/posting/fbs/package-label/get`

**Тело запроса** (`application/json`):
- **task_id** `integer <int64>` *обязательный* — Идентификатор задания из ответа метода /v3/posting/fbs/package-label/create.

**Пример запроса:**

```json
{
  "task_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус формирования этикеток или файл с ними |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **error** `object` — Ошибка, которая возникла при формировании этикеток.
- **file_url** `string` — Ссылка на файл с этикетками.
- **status** `object` — Статус задания.

**Пример ответа (`200`):**

```json
{
  "error": {
    "code": "string",
    "message": "string"
  },
  "file_url": "string",
  "status": {
    "code": "string",
    "postings_count": 0,
    "printed_postings_count": 0,
    "unprinted_postings": [
      {
        "message": "string",
        "posting_number": "string"
      }
    ]
  }
}
```


---

## Получить файл с этикетками

`POST /v1/posting/fbs/package-label/get`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Метод для получения этикеток после вызова /v1/posting/fbs/package- label/create.

> **Примечание:** C 5 октября 2026 года метод будет возвращать новые этикетки

> **Примечание:** для отправлений FBS.

> **Примечание:** Подробнее о новых этикетках в Базе знаний продавца

> **Примечание:** С 2 ноября 2026 года метод будет отключён. Переключитесь на

**Тело запроса** (`application/json`):
- **task_id** `integer <int64>` *обязательный* — Номер задания на формирование этикеток из ответа метода /v1/posting/fbs/package-label/create.

**Пример запроса:**

```json
{
  "task_id": "323231234-1234"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус формирования этикеток или файл с ними |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **error** `string` — Код ошибки.
  - **file_url** `string` — Ссылка на файл с этикетками.
  - **printed_postings_count** `integer <int32>` — Количество напечатанных этикеток.
  - **status** `string` — Статус формирования этикеток: pending — задание в очереди. in_progress — формируются. completed — файл с этикетками готов. error — ошибка при создании файла.
  - **unprinted_postings** `Array of objects` — Информация об ошибках, из-за которых не получилось напечатать этикетки.
  - **unprinted_postings_count** `integer <int32>` — Количество этикеток, которые не получилось напечатать.

**Пример ответа (`200`):**

```json
{
  "result": {
    "error": "",
    "status": "completed",
    "file_url": "https://ir.ozone.ru/s3/ \"printed_postings_count\": 1",
    "unprinted_postings_count": 0,
    "unprinted_postings": []
  }
}
```


---

## Причины отмены отправления

`POST /v1/posting/fbs/cancel-reason`

Возвращает список причин отмены для конкретных отправлений.

**Тело запроса** (`application/json`):
- **related_posting_numbers** `Array of strings` *обязательный* — Номера отправлений.

**Пример запроса:**

```json
{
  "related_posting_numbers": [
    "73837363-0010-3"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Причины отмены отправлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат запроса.
  - **posting_number** `string` — Номер отправления.
  - **reasons** `Array of objects` — Информация о причинах отмены.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "posting_number": "73837363-0010 \"reasons\": [ { \"id\": 352",
      "title": "Товар закончилс \"type_id\": \"seller\""
    },
    {
      "id": 400,
      "title": "Остался только \"type_id\": \"seller\""
    },
    {
      "id": 402,
      "title": "Другое (вина пр \"type_id\": \"seller\" }"
    }
  ]
}
```


---

## Причины отмены отправлений

`POST /v2/posting/fbs/cancel-reason/list`

Возвращает список причин отмены для всех отправлений.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Причины отмены отправлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат работы метода.
  - **id** `integer <int64>` — Идентификатор причины отмены.
  - **is_available_for_cancellation** `boolean` — Результат отмены отправления. true , если запрос доступен для отмены.
  - **title** `string` — Название категории.
  - **type_id** `string` — Инициатор отмены отправления: buyer — покупатель, seller — продавец.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "id": 352,
      "title": "Товар закончился на ск \"type_id\": \"seller",
      "is_available_for_cancellation": ""
    },
    {
      "id": 401,
      "title": "Продавец отклонил арби \"type_id\": \"seller",
      "is_available_for_cancellation": ""
    },
    {
      "id": 402,
      "title": "Другое (вина продавца) \"type_id\": \"seller",
      "is_available_for_cancellation": ""
    },
    {
      "id": 666,
      "title": "Возврат из службы дост \"type_id\": \"seller",
      "is_available_for_cancellation": ""
    }
  ]
}
```


---

## Отменить отправку некоторых товаров в отправлении

`POST /v2/posting/fbs/product/cancel`

Используйте метод, если вы не можете отправить часть продуктов из отправления. Чтобы получить идентификаторы причин отмены cancel_reason_id при работе по схемам FBS или rFBS, используйте метод Условно-доставленные отправления отменить нельзя.

**Тело запроса** (`application/json`):
- **cancel_reason_id** `integer <int64>` *обязательный* — Идентификатор причины отмены отправления товара.
- **cancel_reason_message** `string` *обязательный* — Обязательное поле. Дополнительная информация по отмене.
- **items** `Array of objects` *обязательный* — Информация о товарах.
- **posting_number** `string` *обязательный* — Идентификатор отправления.

**Пример запроса:**

```json
{
  "cancel_reason_id": 352,
  "cancel_reason_message": "Product is out \"items\": [ { \"quantity\": 5",
  "sku": 150587396
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отправка отменена |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `string` — Номер отправления.

**Пример ответа (`200`):**

```json
{
  "result": ""
}
```


---

## Отменить отправление

`POST /v2/posting/fbs/cancel`

Меняет статус отправления на cancelled . Перед началом работы проверьте причины отмены для конкретного отправления методом /v1/posting/fbs/cancel-reason. Условно-доставленные отправления отменить нельзя. Если значение параметра cancel_reason_id — 402, заполните поле

```
cancel_reason_message .
```

**Тело запроса** (`application/json`):
- **cancel_reason_id** `integer <int64>` *обязательный* — Идентификатор причины отмены отправления.
- **cancel_reason_message** `string` — Дополнительная информация по отмене. Если cancel_reason_id = 402 , параметр обязательный.
- **posting_number** `string` *обязательный* — Идентификатор отправления.

**Пример запроса:**

```json
{
  "cancel_reason_id": 352,
  "cancel_reason_message": "Product is out \"posting_number\": \"33920113-1231-1\""
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отправление отменено |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `boolean` — Результат обработки запроса. true , если запрос выполнился без ошибок.

**Пример ответа (`200`):**

```json
{
  "result": true
}
```


---

## Открыть спор по отправлению

`POST /v2/posting/fbs/arbitration`

Если отправление передано в доставку, но не просканировано в сортировочном центре, можно открыть спор. Открытый спор переведёт отправление в статус arbitration .

**Тело запроса** (`application/json`):
- **posting_number** `Array of strings` *обязательный* — Идентификатор отправления.

**Пример запроса:**

```json
{
  "posting_number": [
    "33920143-1195-1"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Открыт спор по отправлению |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `boolean` — Результат обработки запроса. true , если запрос выполнился без ошибок.

**Пример ответа (`200`):**

```json
{
  "result": true
}
```


---

## Передать отправление к отгрузке

`POST /v2/posting/fbs/awaiting-delivery`

Передает спорные заказы к отгрузке. Статус отправления изменится

```
на awaiting_deliver .
```

**Тело запроса** (`application/json`):
- **posting_number** `Array of strings` *обязательный* — Идентификатор отправления. Максимальное количество в одном запросе — 100.

**Пример запроса:**

```json
{
  "posting_number": [
    "33920143-1195-1"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отправление передано к отгрузке |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `boolean` — Результат обработки запроса. true , если запрос выполнился без ошибок.

**Пример ответа (`200`):**

```json
{
  "result": true
}
```


---

## Проверить код курьера

`POST /v1/posting/fbs/pick-up-code/verify`

Метод позволяет проверить код курьера при передаче отправлений realFBS Express. Подробнее о передаче отправлений в Базе знаний продавца.

**Тело запроса** (`application/json`):
- **pickup_code** `string` *обязательный* — Код курьера.
- **posting_number** `string` *обязательный* — Номер отправления.

**Пример запроса:**

```json
{
  "pickup_code": "342341212312",
  "posting_number": "228245774-2229-1"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат проверки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **valid** `boolean` — true , если код корректный.

**Пример ответа (`200`):**

```json
{
  "valid": true
}
```


---

## Таможенные декларации ETGB

`POST /v1/posting/global/etgb`

Метод для получения таможенных деклараций Elektronik Ticaret Gümrük Beyannamesi (ETGB) для продавцов из Турции.

**Тело запроса** (`application/json`):
- **date** `object` *обязательный* — Фильтр по периоду создания деклараций.

**Пример запроса:**

```json
{
  "date": {
    "from": "2023-02-13T12:13:16.818Z",
    "to": "2023-02-13T12:13:16.818Z"
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о декларациях |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат запроса.
  - **posting_number** `string` — Номер отправления.
  - **etgb** `object` — Информация о декларации.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "posting_number": "228245774-222 \"etgb\": { \"number\": \"1",
      "date": "12-12-2026",
      "url": "htttp://testurl/posti"
    }
  ]
}
```


---

## Список неоплаченных товаров, заказанных юридическими лицами

`POST /v1/posting/unpaid-legal/product/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **limit** `integer <int32>` *обязательный* — Количество значений в ответе.

**Пример запроса:**

```json
{
  "cursor": "",
  "limit": 1000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список неоплаченных товаров |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **products** `Array of objects` — Список неоплаченных товаров.
- **cursor** `string` — Указатель для выборки следующих данных.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "product_id": 145123054,
      "offer_id": "10032",
      "quantity": 1,
      "name": "Телевизор LG",
      "image_url": "https://url"
    }
  ],
  "cursor": "hCGiPPopcBFMgMErdzaCEpzQfinuP"
}
```


---
