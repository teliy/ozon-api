# Создание и управление заявками на поставку FBO

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 256. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Получить информацию о макролокальных кластерах

## Получить информацию о макролокальных кластерах

`POST /v2/cluster/list`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Макролокальные кластеры |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список кластеров.
  - **data** `object` — Кластер.
  - **macrolocal_cluster_id** `integer <int64>` — Идентификатор кластера.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "data": {
        "fulfillments": [
          {
            "name": "string",
            "warehouse_id": 0
          }
        ],
        "macrolocal_cluster": {
          "country": {
            "name": "string",
            "uid": "string"
          },
          "name": "string"
        }
      },
      "macrolocal_cluster_id": 0
    }
  ]
}
```


---

## Информация о кластерах и их складах

`POST /v1/cluster/list`

**Тело запроса** (`application/json`):
- **cluster_ids** `Array of strings <int64>` — Идентификаторы кластеров.
- **cluster_type** `string` *обязательный* — Тип кластера: CLUSTER_TYPE_OZON — кластер в России, CLUSTER_TYPE_CIS — кластер в СНГ.. Enum: `"CLUSTER_TYPE_OZON"`, `"CLUSTER_TYPE_CIS"`.

**Пример запроса:**

```json
{
  "cluster_type": "CLUSTER_TYPE_OZON"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о кластерах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **clusters** `Array of objects` — Кластеры.
  - **id** `integer <int64>` — Идентификатор кластера.
  - **logistic_clusters** `Array of objects` — Информация о складах кластера.
  - **macrolocal_cluster_id** `integer <int64>` — Идентификатор кластера размещения.
  - **name** `string` — Название кластера.
  - **type** `string` — Тип кластера: CLUSTER_TYPE_OZON — кластер в России, CLUSTER_TYPE_CIS — кластер в СНГ.. Enum: `"CLUSTER_TYPE_OZON"`, `"CLUSTER_TYPE_CIS"`.

**Пример ответа (`200`):**

```json
{
  "clusters": [
    {
      "id": 0,
      "logistic_clusters": [
        {
          "warehouses": [
            {
              "name": "string",
              "type": "FULL_FILL \"warehouse_id\": 0"
            }
          ]
        }
      ],
      "macrolocal_cluster_id": 0,
      "name": "string",
      "type": "CLUSTER_TYPE_OZON"
    }
  ]
}
```


---

## Поиск точек для отгрузки поставки

`POST /v1/warehouse/fbo/list`

Используйте метод, чтобы найти точки отгрузки для кросс-докинга и прямых поставок. Вы можете посмотреть адреса всех точек на карте и в виде таблицы в Базе знаний.

**Тело запроса** (`application/json`):
- **filter_by_supply_type** `Array of strings` *обязательный* — Тип поставки: CREATE_TYPE_CROSSDOCK — кросс-докинг, CREATE_TYPE_DIRECT — прямая.. Enum: `"CREATE_TYPE_CROSSDOCK"`, `"CREATE_TYPE_DIRECT"`.
- **search** `string` *обязательный* — Поиск по названию склада. Для поиска пунктов выдачи заказов укажите полное название.

**Пример запроса:**

```json
{
  "filter_by_supply_type": [
    "CREATE_TYPE_CROSSDOCK"
  ],
  "search": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о складах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **search** `Array of objects` — Результат поиска складов.
  - **address** `string` — Адрес склада.
  - **coordinates** `object` — Координаты склада.
  - **name** `string` — Название склада.
  - **warehouse_id** `integer <int64>` — Идентификатор склада, пункта выдачи заказов или сортировочного центра.
  - **warehouse_type** `string` — Тип склада, пункта выдачи заказов или сортировочного центра: WAREHOUSE_TYPE_DELIVERY_POINT — пункт выдачи заказов, WAREHOUSE_TYPE_ORDERS_RECEIVING_POINT — пункт приёма заказов, WAREHOUSE_TYPE_SORTING_CENTER — сортировочный центр, WAREHOUSE_TYPE_FULL_FILLMENT — фулфилмент, WAREHOUSE_TYPE_CROSS_DOCK — кросс- докинг.. Enum: `"WAREHOUSE_TYPE_DELIVERY_POINT"`, `"WAREHOUSE_TYPE_ORDERS_RECEIVING_POINT"`, `"WAREHOUSE_TYPE_SORTING_CENTER"`, `"WAREHOUSE_TYPE_FULL_FILLMENT"`, `"WAREHOUSE_TYPE_CROSS_DOCK"`.

**Пример ответа (`200`):**

```json
{
  "search": [
    {
      "address": "string",
      "coordinates": {
        "latitude": 0,
        "longitude": 0
      },
      "name": "string",
      "warehouse_id": 0,
      "warehouse_type": "WAREHOUSE_TYP }"
    }
  ]
}
```


---

## Создать черновик заявки на поставку кросс-докингом

`POST /v1/draft/crossdock/create`

Вы можете создавать черновики заявки на поставку: 2 раза в минуту; 50 раз в час; 500 раз в день. Если превысите лимит, вернётся ошибка 429.

> **Примечание:** Черновик заявки на поставку не отображается в личном кабинете

> **Примечание:** продавца и доступен 30 минут.

**Тело запроса** (`application/json`):
- **cluster_info** `object` *обязательный* — Информация о кластере.
- **deletion_sku_mode** `string` *обязательный* — Режим удаления SKU, которые не попали в поставку. Возможные значения: PARTIAL — система удалит только те единицы SKU, которые не прошли проверку; FULL — система удалит все единицы SKU, если хотя бы одна единица этого SKU не прошла проверку.. Enum: `"FULL"`, `"PARTIAL"`.
- **delivery_info** `object` *обязательный* — Информация о доставке.

**Пример запроса:**

```json
{
  "cluster_info": {
    "items": [
      {
        "quantity": 0,
        "sku": 0
      }
    ],
    "macrolocal_cluster_id": 0
  },
  "deletion_sku_mode": "FULL",
  "delivery_info": {
    "drop_off_warehouse": {
      "warehouse_id": 0,
      "warehouse_type": "DELIVERY_POIN"
    },
    "seller_warehouse_id": 0,
    "type": "DROPOFF"
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Черновик создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **draft_id** `integer <int64>` — Идентификатор черновика. Используйте в методе /v2/draft/create/info.
- **errors** `Array of objects` — Ошибки.

**Пример ответа (`200`):**

```json
{
  "draft_id": 0,
  "errors": [
    {
      "error_message": "UNSPECIFIED",
      "error_reasons": [
        "UNSPECIFIED"
      ],
      "items_validation": [
        {
          "macrolocal_cluster_id": "rejected_items",
          "reasons": [
            "UNSPECIFIED"
          ],
          "sku": 0
        }
      ]
    }
  ],
  "macrolocal_cluster_ids": [
    "string"
  ],
  "message": "string",
  "skus": [
    "string"
  ]
}
```


---

## Создать черновик заявки на прямую поставку

`POST /v1/draft/direct/create`

Вы можете создавать черновики заявки на поставку: 2 раза в минуту; 50 раз в час; 500 раз в день. Если превысите лимит, вернётся ошибка 429.

> **Примечание:** Черновик заявки на поставку не отображается в личном кабинете

> **Примечание:** продавца и доступен 30 минут.

**Тело запроса** (`application/json`):
- **cluster_info** `object` *обязательный* — Информация о кластере.
- **deletion_sku_mode** `string` *обязательный* — Режим удаления SKU, которые не попали в поставку. Возможные значения: PARTIAL — система удалит только те единицы SKU, которые не прошли проверку; FULL — система удалит все единицы SKU, если хотя бы одна единица этого SKU не прошла проверку.. Enum: `"FULL"`, `"PARTIAL"`.

**Пример запроса:**

```json
{
  "cluster_info": {
    "items": [
      {
        "quantity": 0,
        "sku": 0
      }
    ],
    "macrolocal_cluster_id": 0
  },
  "deletion_sku_mode": "FULL"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Черновик создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **draft_id** `integer <int64>` — Идентификатор черновика. Используйте в методе /v2/draft/create/info.
- **errors** `Array of objects` — Ошибки.

**Пример ответа (`200`):**

```json
{
  "draft_id": 0,
  "errors": [
    {
      "error_message": "UNSPECIFIED",
      "error_reasons": [
        "UNSPECIFIED"
      ],
      "items_validation": [
        {
          "macrolocal_cluster_id": "rejected_items",
          "reasons": [
            "UNSPECIFIED"
          ],
          "sku": 0
        }
      ]
    }
  ],
  "macrolocal_cluster_ids": [
    "string"
  ],
  "message": "string",
  "skus": [
    "string"
  ]
}
```


---

## Создать черновик заявки на поставку для нескольких кластеров

`POST /v1/draft/multi-cluster/create`

Вы можете создавать черновики заявки на поставку: 2 раза в минуту; 50 раз в час; 500 раз в день. Если превысите лимит, вернётся ошибка 429.

> **Примечание:** Черновик заявки на поставку не отображается в личном кабинете

> **Примечание:** продавца и доступен 30 минут.

**Тело запроса** (`application/json`):
- **clusters_info** `Array of objects` *обязательный* — Информация о кластерах.
- **deletion_sku_mode** `string` *обязательный* — Режим удаления SKU, которые не попали в поставку. Возможные значения: PARTIAL — система удалит только те единицы SKU, которые не прошли проверку; FULL — система удалит все единицы SKU, если хотя бы одна единица этого SKU не прошла проверку.. Enum: `"FULL"`, `"PARTIAL"`.
- **delivery_info** `object` *обязательный* — Информация о доставке.

**Пример запроса:**

```json
{
  "clusters_info": [
    {
      "items": [
        {
          "quantity": 0,
          "sku": 0
        }
      ],
      "macrolocal_cluster_id": 0
    }
  ],
  "deletion_sku_mode": "FULL",
  "delivery_info": {
    "drop_off_warehouse": {
      "warehouse_id": 0,
      "warehouse_type": "DELIVERY_POIN"
    },
    "seller_warehouse_id": 0,
    "type": "DROPOFF"
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Черновик создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **draft_id** `integer <int64>` — Идентификатор черновика. Используйте в методе /v2/draft/create/info.
- **errors** `Array of objects` — Ошибки.

**Пример ответа (`200`):**

```json
{
  "draft_id": 0,
  "errors": [
    {
      "error_message": "UNSPECIFIED",
      "error_reasons": [
        "UNSPECIFIED"
      ],
      "items_validation": [
        {
          "macrolocal_cluster_id": "rejected_items",
          "reasons": [
            "UNSPECIFIED"
          ],
          "sku": 0
        }
      ]
    }
  ],
  "macrolocal_cluster_ids": [
    "string"
  ],
  "message": "string",
  "skus": [
    "string"
  ]
}
```


---

## Получить информацию о черновике заявки на поставку

`POST /v2/draft/create/info`

Вы можете создавать черновики заявки на поставку 2 раза в минуту и 50 раз в час. Если превысите лимит, вернётся ошибка 429.

**Тело запроса** (`application/json`):
- **draft_id** `integer <int64>` *обязательный* — Идентификатор черновика из методов /v1/draft/crossdock/create, /v1/draft/direct/create или /v1/draft/multi-cluster/create.

**Пример запроса:**

```json
{
  "draft_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о черновике |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **clusters** `Array of objects` — Кластеры.
- **errors** `Array of objects` — Ошибки.
- **status** `string` — Статус создания черновика заявки на поставку: UNSPECIFIED — не определён, SUCCESS — создан, IN_PROGRESS — создаётся, FAILED — не удалось создать.. Enum: `"UNSPECIFIED"`, `"SUCCESS"`, `"IN_PROGRESS"`, `"FAILED"`.

**Пример ответа (`200`):**

```json
{
  "clusters": [
    {
      "cluster_name": "string",
      "macrolocal_cluster_id": 0,
      "supply_type": "CROSSDOCK",
      "warehouses": [
        {
          "availability_status": {
            "invalid_reason": "UNS \"state\": \"UNSPECIFIED\""
          },
          "bundle_id": "string",
          "restricted_bundle_id": " \"storage_warehouse\": { \"address\": \"string",
          "name": "string",
          "warehouse_id": 0
        },
        {
          "supply_tags": [
            "UNSPECIFIED"
          ],
          "total_rank": 0,
          "total_score": 0
        }
      ]
    }
  ],
  "errors": [
    {
      "error_message": "UNSPECIFIED",
      "error_reasons": [
        "UNSPECIFIED"
      ],
      "items_validation": [
        {
          "limit": 0,
          "macrolocal_cluster_id": "supply_id",
          "rejected_items": [
            {
              "reasons": [
                "UNSPECIFIED"
              ],
              "sku": 0
            }
          ]
        }
      ],
      "macrolocal_cluster_ids": [
        "string"
      ],
      "message": "string",
      "skus": [
        "string"
      ]
    }
  ],
  "status": "UNSPECIFIED"
}
```


---

## Получить список доступных таймслотов

`POST /v2/draft/timeslot/info`

**Тело запроса** (`application/json`):
- **date_from** `string YYYY-MM-DD` *обязательный* — Дата начала периода доступных таймслотов.
- **date_to** `string YYYY-MM-DD` *обязательный* — Дата окончания периода доступных таймслотов. Максимальный период — 28 дней с текущей даты.
- **draft_id** `integer <int64>` *обязательный* — Идентификатор черновика из метода /v2/draft/create/info.
- **supply_type** `string` *обязательный* — Тип поставки: CROSSDOCK — кросс-докинг; DIRECT — прямая; MULTI_CLUSTER — для нескольких кластеров.. Enum: `"CROSSDOCK"`, `"DIRECT"`, `"MULTI_CLUSTER"`.
- **selected_cluster_warehouses** `Array of objects` *обязательный* — Информация о кластере и складах в нём. Можно передать один кластер для кросс- докинговой и прямой поставки или список всех кластеров для поставки в несколько кластеров.

**Пример запроса:**

```json
{
  "date_from": "string",
  "date_to": "string",
  "draft_id": 0,
  "supply_type": "CROSSDOCK",
  "selected_cluster_warehouses": [
    {
      "macrolocal_cluster_id": 0,
      "storage_warehouse_id": 0
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список таймслотов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_reason** `string` — Причина ошибки: UNSPECIFIED — не определена; INVALID_CLUSTERS_COUNT — переданы не все кластеры из расчёта; REQUESTED_PERIOD_MORE_THAN_MAX — превышен период; INVALID_REQUESTED_CLUSTER_IDS — переданы кластеры, которых нет в расчёте. UNDEFINED — неизвестная ошибка.. Enum: `"UNSPECIFIED"`, `"INVALID_CLUSTERS_COUNT"`, `"REQUESTED_PERIOD_MORE_THAN_MAX"`, `"UNDEFINED"`.
- **result** `object` — Информация о таймслотах.
  - **drop_off_warehouse_timeslots** `object` — Таймслоты складов.
  - **requested_date_from** `string` — Дата начала периода.
  - **requested_date_to** `string` — Дата окончания периода.

**Пример ответа (`200`):**

```json
{
  "error_reason": "UNSPECIFIED",
  "result": {
    "drop_off_warehouse_timeslots": {
      "current_time_in_timezone": "str \"days\": [ { \"date_in_timezone\": ",
      "timeslots": [
        {
          "from_in_timezone": "to_in_timezone",
          "warehouse_timezone": "string"
        },
        {
          "requested_date_from": "string",
          "requested_date_to": "string"
        }
      ]
    }
  }
}
```


---

## Установка грузомест

`POST /v1/cargoes/create`

Используйте метод, чтобы передать грузоместа и товарный состав в заявку на поставку.

**Тело запроса** (`application/json`):
- **cargoes** `Array of objects` *обязательный* — Информация о грузоместах. Вы можете передать не больше 40 палет или 30 коробок.
- **delete_current_version** `boolean` — true , если нужно удалить предыдущие грузоместа.
- **supply_id** `integer <int64>` *обязательный* — Идентификатор поставки. Можно получить с помощью метода /v3/supply-order/get. Нужное значение — в параметре ответа orders.supplies.supply_id .

**Пример запроса:**

```json
{
  "cargoes": [
    {
      "key": "box-001",
      "value": {
        "items": [
          {
            "barcode": "4601234567 \"expires_at\": ",
            "offer_id": "12345678",
            "quant": 1,
            "quantity": 5
          },
          {
            "barcode": "4609876543 \"expires_at\": ",
            "offer_id": "87654321",
            "quant": 2,
            "quantity": 3
          }
        ],
        "type": "BOX"
      }
    }
  ],
  "delete_current_version": true,
  "supply_id": 123456
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Грузоместа установлены |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции.
- **errors** `object` — Ошибки.

**Пример ответа (`200`):**

```json
{
  "operation_id": "op-1689012345",
  "errors": {
    "error_reasons": [
      "INVALID_STATE"
    ],
    "items_validation": [
      {
        "barcode": "4601234567890",
        "cargo_key": "box-001",
        "quant": 2,
        "type": "SUPPLY_ITEM_NOT_FOUN }"
      }
    ]
  }
}
```


---

## Получить информацию по установке грузомест

`POST /v2/cargoes/create/info`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции.

**Пример запроса:**

```json
{
  "operation_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат запроса |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **errors** `object` — Ошибки.
- **result** `object` — Результат запроса.
  - **cargoes** `Array of objects` — Информация о грузоместах.
- **status** `string` — Статус формирования грузоместа: SUCCESS — успешно; IN_PROGRESS — формируются; FAILED — при формировании грузомест произошла ошибка.. Enum: `"STATUS_UNSPECIFIED"`, `"SUCCESS"`, `"IN_PROGRESS"`, `"FAILED"`.

**Пример ответа (`200`):**

```json
{
  "errors": {
    "error_reasons": [
      "ERROR_REASON_UNSPECIFIED"
    ],
    "items_validation": [
      {
        "cargo_key": "string",
        "item": "string",
        "quant": 0,
        "type": "SUPPLY_ITEM_NOT_FOUN"
      }
    ]
  },
  "result": {
    "cargoes": [
      {
        "key": "string",
        "value": {
          "cargo_id": 0
        }
      }
    ]
  },
  "status": "STATUS_UNSPECIFIED"
}
```


---

## Получить информацию о грузоместах

`POST /v1/cargoes/get`

**Тело запроса** (`application/json`):
- **supply_ids** `Array of strings <int64>` *обязательный* — Список идентификаторов поставок в заявке.

**Пример запроса:**

```json
{
  "supply_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о грузоместах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **supply** `Array of objects` — Информация о грузоместах.
  - **bundle_id** `string` — Идентификатор товарного состава.
  - **cargoes** `Array of objects` — Грузоместа.
  - **supply_id** `integer <int64>` — Идентификатор поставки.

**Пример ответа (`200`):**

```json
{
  "supply": [
    {
      "bundle_id": "string",
      "cargoes": [
        {
          "bundle_id": "string",
          "cargo_id": 0,
          "content_type": "UNSPECIF \"placement_zone_type\": ",
          "tracking_info": {
            "date": "string",
            "status": "UNSPECIFIED \"type\": \"UNSPECIFIED\""
          },
          "type": "UNSPECIFIED"
        }
      ],
      "supply_id": 0
    }
  ]
}
```


---

## Удалить грузоместо в заявке на поставку

`POST /v1/cargoes/delete`

Метод для удаления грузомест в заявке на поставку. Чтобы проверить статус удаления, используйте метод

**Тело запроса** (`application/json`):
- **cargo_ids** `Array of strings <int64>` *обязательный* — Список идентификаторов грузомест, которые нужно удалить. Максимум 70 значений.
- **supply_id** `integer <int64>` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "cargo_ids": [
    "box-001"
  ],
  "supply_id": 123456
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Грузоместо удалено |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **errors** `object` — Список ошибок, которые возникли при удалении грузомест.
- **operation_id** `string` — Идентификатор операции.

**Пример ответа (`200`):**

```json
{
  "errors": {
    "cargo_error_reasons": [
      {
        "cargo_id": 0,
        "error_reasons": [
          "CARGO_NOT_FOUND"
        ]
      }
    ],
    "supply_error_reasons": [
      "SUPPLY_NOT_FOUND"
    ]
  },
  "operation_id": "string"
}
```


---

## Информация о статусе удаления грузоместа

`POST /v1/cargoes/delete/status`

Метод для получения статуса удаления грузомест в заявке на поставку.

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции.

**Пример запроса:**

```json
{
  "operation_id": "test-operation-delete-1"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус удаления грузоместа |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **errors** `object` — Список ошибок, которые возникли при удалении грузомест.
- **status** `string` — Статус удаления грузоместа. Возможные статусы: SUCCESS — грузоместо удалено, IN_PROGRESS — грузоместо в процессе удаления, ERROR — возникла ошибка при удалении грузоместа.. Enum: `"SUCCESS"`, `"IN_PROGRESS"`, `"ERROR"`.

**Пример ответа (`200`):**

```json
{
  "status": "SUCCESS",
  "errors": {
    "supply_error_reasons": [],
    "cargo_error_reasons": []
  }
}
```


---

## Чек-лист по установке грузомест FBO

`POST /v1/cargoes/rules/get`

Метод для получения чек-листа с правилами по установке грузомест.

**Тело запроса** (`application/json`):
- **supply_ids** `Array of strings <int64>` *обязательный* — Список идентификаторов поставок в заявке. Максимум 100 идентификаторов.

**Пример запроса:**

```json
{
  "supply_ids": [
    2000007863,
    2000007864,
    2000007865
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Чек-лист по установке грузомест |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **supply_check_lists** `Array of objects` — Список чек-листов с правилами заполнения грузомест по поставкам.
  - **cargoes_presents_rule** `object` — Правило указания грузомест.
  - **edit_deadline_expire_rule** `object` — Правило крайнего срока редактирования грузомест.
  - **expire_dates_presented_rule** `object` — Правило указания сроков годности для товаров.
  - **is_valid_distribution_rule** `object` — Правило совпадения составов грузомест с составом поставки.
  - **package_units_with_distribution_rule** `object` — Правило заполнения состава грузомест.
  - **placement_zones_rule** `object` — Правило распределения товаров в грузоместах по зонам размещения.
  - **supply_id** `integer <int64>` — Идентификатор поставки.

**Пример ответа (`200`):**

```json
{
  "supply_check_lists": [
    {
      "supply_id": 2000007863,
      "cargoes_presents_rule": {
        "count": 4,
        "satisfied": true,
        "cargo_count_per_type": [
          {
            "type": "BOX",
            "count": 3
          },
          {
            "type": "PALLET",
            "count": 1
          }
        ]
      },
      "edit_deadline_expire_rule": {
        "is_applicable": true,
        "is_required": true,
        "satisfied": true
      },
      "expire_dates_presented_rule": {
        "is_applicable": true,
        "is_required": true,
        "satisfied": true,
        "count_sku_with_expiration": "count_sku_with_expiration_fi"
      },
      "is_valid_distribution_rule": {
        "is_applicable": true,
        "satisfied": true,
        "count_distributed_sku": 24,
        "count_sku_total": 24,
        "percents_int": 100
      },
      "package_units_with_distribution \"is_applicable": true,
      "is_required": true,
      "satisfied": true,
      "count_all": 4,
      "count_with_distribution": 4
    },
    {
      "placement_zones_rule": {
        "is_applicable": true,
        "satisfied": true,
        "count_cargoes_all": 4,
        "count_cargoes_with_mono_plac } } , { \"supply_id": 2000007864,
        "cargoes_presents_rule": {
          "count": 2,
          "satisfied": true,
          "cargo_count_per_type": [
            {
              "type": "BOX",
              "count": 2
            }
          ]
        }
      },
      "edit_deadline_expire_rule": {
        "is_applicable": true,
        "is_required": true,
        "satisfied": true
      },
      "expire_dates_presented_rule": {
        "is_applicable": false,
        "is_required": false,
        "satisfied": true,
        "count_sku_with_expiration": "count_sku_with_expiration_fi"
      },
      "is_valid_distribution_rule": {
        "is_applicable": true,
        "satisfied": true,
        "count_distributed_sku": 8,
        "count_sku_total": 8,
        "percents_int": 100
      },
      "package_units_with_distribution \"is_applicable": true,
      "is_required": true,
      "satisfied": true,
      "count_all": 2,
      "count_with_distribution": 2
    },
    {
      "placement_zones_rule": {
        "is_applicable": false,
        "satisfied": false,
        "count_cargoes_all": 0,
        "count_cargoes_with_mono_plac } }": ""
      }
    }
  ]
}
```


---

## Сгенерировать этикетки для грузомест

`POST /v1/cargoes-label/create`

Используйте метод, чтобы сгенерировать этикетки для грузомест из заявки на поставку.

**Тело запроса** (`application/json`):
- **cargoes** `Array of objects` — Информация о грузоместах.
- **supply_id** `integer <int64>` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "supply_id": 2000007863,
  "cargoes": [
    {
      "cargo_id": 50001234
    },
    {
      "cargo_id": 50001235
    },
    {
      "cargo_id": 50001236
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат запроса |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции.
- **errors** `object` — Ошибки.

**Пример ответа (`200`):**

```json
{
  "operation_id": "test-cargo-label-create \"errors\": { \"error_reasons\": [ ] }"
}
```


---

## Получить идентификатор этикетки для грузомест

`POST /v1/cargoes-label/get`

Возвращает статус формирования этикеток и ссылку на PDF-файл с ними.

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции.

**Пример запроса:**

```json
{
  "operation_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Этикетка для грузомест |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Информация об этикетках.
  - **file_guid** `string` — Идентификатор для получения файла с этикетками.
  - **file_url** `string` — Ссылка на PDF-файл с этикетками.
- **status** `string` — Статус формирования этикеток: SUCCESS — готовы. IN_PROGRESS — формируются. FAILED — ошибка при формировании.. Enum: `"SUCCESS"`, `"IN_PROGRESS"`, `"FAILED"`.
- **errors** `object` — Ошибки.

**Пример ответа (`200`):**

```json
{
  "result": {
    "file_guid": "string",
    "file_url": "string"
  },
  "status": "SUCCESS",
  "errors": {
    "error_reasons": [
      "INVALID_STATE"
    ]
  }
}
```


---

## Получить PDF с этикетками грузовых мест

`GET /v1/cargoes-label/file/{file_guid}`

> **Примечание:** 10 апреля 2026 года отключим метод. Переключитесь на

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

## Отменить заявку на поставку

`POST /v1/supply-order/cancel`

**Тело запроса** (`application/json`):
- **order_id** `integer <int64>` *обязательный* — Идентификатор заявки на поставку.

**Пример запроса:**

```json
{
  "order_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отмена заявки на поставку в процессе |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции на отмену заявки.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---

## Получить статус отмены заявки на поставку

`POST /v1/supply-order/cancel/status`

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции на отмену заявки на поставку.

**Пример запроса:**

```json
{
  "operation_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус отмены заявки на поставку |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_reasons** `Array of strings` — Причина, по которой не удалось отменить заявку на поставку: INVALID_ORDER_STATE — неверный статус заявки на поставку. ORDER_IS_VIRTUAL — заявка виртуальная. ORDER_DOES_NOT_BELONG_TO_CONTRACTOR — заявка на поставку не принадлежит вашему юридическому лицу. ORDER_DOES_NOT_BELONG_TO_COMPANY — заявка на поставку не принадлежит продавцу. OTHER_ASYNCHRONOUS_OPERATION_IN_PROGRESS — заявка на поставку в процессе отмены.. Enum: `"INVALID_ORDER_STATE"`, `"ORDER_IS_VIRTUAL"`, `"ORDER_DOES_NOT_BELONG_TO_CONTRACTOR"`, `"ORDER_DOES_NOT_BELONG_TO_COMPANY"`, `"OTHER_ASYNCHRONOUS_OPERATION_IN_PROGRESS"`.
- **result** `object` — Информация об отмене заявки на поставку.
  - **is_order_cancelled** `boolean` — true , если заявка на поставку отменена.
  - **supplies** `Array of objects` — Список отменённых поставок.
- **status** `string` — Статус отмены заявки на поставку. Возможные значения: SUCCESS — заявка отменена. IN_PROGRESS — заявки в процессе отмены. ERROR — ошибка.. Enum: `"SUCCESS"`, `"IN_PROGRESS"`, `"ERROR"`.

**Пример ответа (`200`):**

```json
{
  "error_reasons": [
    "INVALID_ORDER_STATE"
  ],
  "result": {
    "is_order_cancelled": true,
    "supplies": [
      {
        "error_reasons": [
          "INVALID_SUPPLY_STATE"
        ],
        "is_supply_cancelled": true,
        "supply_id": 0
      }
    ]
  },
  "status": "SUCCESS"
}
```


---

## Редактирование товарного состава

`POST /v1/supply-order/content/update`

Метод для редактирования товарного состава в заявке на поставку. Чтобы проверить статус редактирования, используйте метод

**Тело запроса** (`application/json`):
- **items** `Array of objects` *обязательный* — Новый товарный состав заявки на поставку. Максимум 5000 товаров.
- **order_id** `integer <int64>` *обязательный* — Идентификатор заявки на поставку.
- **supply_id** `integer <int64>` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "items": [
    {
      "quant": 0,
      "quantity": 0,
      "sku": 0
    }
  ],
  "order_id": 0,
  "supply_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Товарный состав обновлён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **errors** `Array of strings` — Ошибки при редактировании товарного состава: INVALID_DRAFT_BUNDLE_ID , SOME_SERVICE_ERROR , ORDER_IS_NOT_FOUND , SUPPLY_IS_NOT_FOUND , SUPPLY_DOES_NOT_BELONGS_TO_ORDER — ошибка при редактировании поставки. HAS_UTD , UTD_IS_UPLOADED — документы в системе ЭДО не удалены. Аннулируйте документы в системе ЭДО. Когда отредактируете состав, сформируйте и подпишите новые документы. ORDER_SKU_LIMIT — количество товаров в поставке должно быть меньше или равно 5000. SAME_SKU — товарный состав поставки остался прежним. SUPPLY_LOCKED — обновление товарного состава в процессе, попробуйте позже. INBOUND_NO_CAPACITY — на складе недостаточно места для поставки. INBOUND_LOCK , ORDER_LOCKED , STORAGE_WAREHOUSE_IS_NOT_WMS — нельзя редактировать товарный состав. SUPPLY_CONTENT_NOT_VALID — в составе поставки есть товары, которые склад не может принять. SUPPLY_BELONG_TO_ANOTHER_CONTRACTOR , COMPANY_DOES_NOT_BELONGS_TO_CONTRACTOR , ORDER_DOES_NOT_BELONG_TO_CONTRACTOR — заявка на поставку не принадлежит вашему юридическому лицу. SUPPLY_BELONG_TO_ANOTHER_COMPANY , ORDER_DOES_NOT_BELONGS_TO_COMPANY — заявка на поставку не принадлежит вашему кабинету. INCORRECT_SUPPLY_STATE — нельзя изменить поставку в этом статусе. INCORRECT_SUPPLY_SOURCE — нельзя изменить поставку с этим источником данных. INCORRECT_STORAGE_WAREHOUSE — нельзя изменить поставку с этим складом хранения. NO_SUPPLY_PRODUCT_BUNDLE_ID — отсутствует идентификатор товарного состава поставки. INVALID_VOLUME — некорректный объём поставки. SUPPLY_IS_VIRTUAL — нельзя редактировать виртуальную поставку. DEADLINE — нельзя изменить поставку за час до таймслота. INACTIVE_CONTRACT — нельзя редактировать состав поставки с истекшим договором. QUANTITY_OUT_OF_RANGE_BOTTOM — количество экземпляров каждого товара должно быть больше 0. QUANTITY_OUT_OF_RANGE_UPPER — количество экземпляров каждого товара должно быть меньше или равно 1 000 000. EMPTY_CONTENT — не сможем принять пустую поставку, добавьте товары. CONTRACT_IS_NOT_FOUND , CONTRACT_IS_NOT_VALID_FOR_HANDLING_ORDERS — в этом личном кабинете нельзя изменить поставку. MINIMUM_VOLUME_IN_LITRES_INVALID — объём товаров в поставке ниже минимального.. Enum: `"INVALID_DRAFT_BUNDLE_ID"`, `"SOME_SERVICE_ERROR"`, `"HAS_UTD"`, `"ORDER_SKU_LIMIT"`, `"SAME_SKU"`, `"SUPPLY_LOCKED"`, `"INBOUND_NO_CAPACITY"`, `"INBOUND_LOCK"`, `"SUPPLY_CONTENT_NOT_VALID"`, `"SUPPLY_BELONG_TO_ANOTHER_CONTRACTOR"`, `"SUPPLY_BELONG_TO_ANOTHER_COMPANY"`, `"INCORRECT_SUPPLY_STATE"`, `"INCORRECT_SUPPLY_SOURCE"`, `"INCORRECT_STORAGE_WAREHOUSE"`, `"DEADLINE"`, `"INACTIVE_CONTRACT"`, `"QUANTITY_OUT_OF_RANGE_BOTTOM"`, `"QUANTITY_OUT_OF_RANGE_UPPER"`, `"EMPTY_CONTENT"`, `"NO_SUPPLY_PRODUCT_BUNDLE_ID"`, `"INVALID_VOLUME"`, `"SUPPLY_IS_VIRTUAL"`, `"ORDER_LOCKED"`, `"CONTRACT_IS_NOT_FOUND"`.
- **operation_id** `string` — Идентификатор операции.

**Пример ответа (`200`):**

```json
{
  "errors": [
    "INVALID_DRAFT_BUNDLE_ID"
  ],
  "operation_id": "string"
}
```


---

## Информация о статусе редактирования товарного состава

`POST /v1/supply-order/content/update/status`

Метод для получения статуса редактирования товарного состава.

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции.

**Пример запроса:**

```json
{
  "operation_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус редактирования |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_details** `object` — Информация об ошибках при попытке редактирования товарного состава.
- **errors** `Array of strings` — Список ошибок при редактировании товарного состава: INVALID_DRAFT_BUNDLE_ID , SOME_SERVICE_ERROR — ошибка при редактировании поставки. HAS_UTD — документы в системе ЭДО не удалены. Аннулируйте документы в системе ЭДО. Когда отредактируете состав, сформируйте и подпишите новые документы. ORDER_SKU_LIMIT — количество товаров в поставке должно быть меньше или равно 5000. SAME_SKU — товарный состав поставки остался прежним. SUPPLY_LOCKED — обновление товарного состава в процессе, попробуйте позже. INBOUND_NO_CAPACITY — на складе недостаточно места для поставки. INBOUND_LOCK , ORDER_LOCKED — нельзя редактировать товарный состав. SUPPLY_CONTENT_NOT_VALID — в составе поставки есть товары, которые склад не может принять. Провалидируйте товарный состав методом /v1/supply- order/content/update/validation. SUPPLY_BELONG_TO_ANOTHER_CONTRACTOR — заявка на поставку не принадлежит вашему юридическому лицу. SUPPLY_BELONG_TO_ANOTHER_COMPANY — заявка на поставку не принадлежит вашему кабинету. INCORRECT_SUPPLY_STATE — нельзя изменить поставку в этом статусе. INCORRECT_SUPPLY_SOURCE — нельзя изменить поставку с этим источником данных. INCORRECT_STORAGE_WAREHOUSE — нельзя изменить поставку с этим складом хранения. NO_SUPPLY_PRODUCT_BUNDLE_ID — отсутствует идентификатор товарного состава поставки. INVALID_VOLUME — некорректный объём поставки. SUPPLY_IS_VIRTUAL — нельзя редактировать виртуальную поставку. DEADLINE — нельзя изменить поставку за час до таймслота. INACTIVE_CONTRACT — нельзя редактировать состав поставки с истекшим договором. QUANTITY_OUT_OF_RANGE_BOTTOM — количество экземпляров каждого товара должно быть больше 0. QUANTITY_OUT_OF_RANGE_UPPER — количество экземпляров каждого товара должно быть меньше или равно 1 000 000. EMPTY_CONTENT — не сможем принять пустую поставку, добавьте товары. MINIMUM_VOLUME_IN_LITRES_INVALID — объём товаров в поставке ниже минимального.. Enum: `"INVALID_DRAFT_BUNDLE_ID"`, `"SOME_SERVICE_ERROR"`, `"HAS_UTD"`, `"ORDER_SKU_LIMIT"`, `"SAME_SKU"`, `"SUPPLY_LOCKED"`, `"INBOUND_NO_CAPACITY"`, `"INBOUND_LOCK"`, `"SUPPLY_CONTENT_NOT_VALID"`, `"SUPPLY_BELONG_TO_ANOTHER_CONTRACTOR"`, `"SUPPLY_BELONG_TO_ANOTHER_COMPANY"`, `"INCORRECT_SUPPLY_STATE"`, `"INCORRECT_SUPPLY_SOURCE"`, `"INCORRECT_STORAGE_WAREHOUSE"`, `"DEADLINE"`, `"INACTIVE_CONTRACT"`, `"QUANTITY_OUT_OF_RANGE_BOTTOM"`, `"QUANTITY_OUT_OF_RANGE_UPPER"`, `"EMPTY_CONTENT"`, `"NO_SUPPLY_PRODUCT_BUNDLE_ID"`, `"INVALID_VOLUME"`, `"SUPPLY_IS_VIRTUAL"`, `"ORDER_LOCKED"`, `"MINIMUM_VOLUME_IN_LITRES_INVALID"`.
- **new_bundle_id** `string` — Идентификатор нового товарного состава поставки.
- **status** `string` — Статус редактирования товарного состава поставки. Возможные статусы: SUCCESS — товарный состав изменён, IN_PROGRESS — товарный состав в процессе изменения, ERROR — возникла ошибка при изменении товарного состава.. Enum: `"SUCCESS"`, `"IN_PROGRESS"`, `"ERROR"`.

**Пример ответа (`200`):**

```json
{
  "error_details": {
    "backup_supply_id": 0,
    "code": [
      "SHIPMENT_PLANNING_DISCIPLINE_CL ], ",
      "items_quantity_limit",
      0
    ],
    "errors": [
      "INVALID_DRAFT_BUNDLE_ID"
    ],
    "new_bundle_id": "string",
    "status": "SUCCESS"
  }
}
```


---

## Проверить новый товарный состав

`POST /v1/supply-order/content/update/validation`

Используйте этот метод, если в /v1/supply-order/content/update/status

```
вы получили ошибку SUPPLY_CONTENT_NOT_VALID .
```

**Тело запроса** (`application/json`):
- **new_bundle_id** `string` *обязательный* — Идентификатор нового товарного состава поставки.
- **supply_id** `integer <int64>` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "new_bundle_id": "string",
  "supply_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **editing_errors** `Array of strings` — Ошибки: UNSPECIFIED — не определено. UNKNOWN — неизвестный тип. INCORRECT_SUPPLY_STATE — нельзя изменить поставку в этом статусе. DEADLINE — нельзя изменить поставку за час до таймслота. UTD_IS_UPLOADED — документы в системе ЭДО не удалены. Аннулируйте документы в системе ЭДО. Когда отредактируете состав, сформируйте и подпишите новые документы. STORAGE_WAREHOUSE_IS_NOT_WMS — нельзя редактировать товарный состав. CONTRACT_IS_NOT_VALID_FOR_HANDLING_ORDERS — в этом личном кабинете нельзя изменить поставку. SUPPLY_IS_VIRTUAL — нельзя редактировать виртуальную поставку. SUPPLY_DOES_NOT_BELONG_TO_COMPANY — заявка на поставку не принадлежит вашему кабинету. ASSORTMENT_REJECTION_REASON_CORRUPTED_ASSORTMENT — не получилось добавить товар в заявку. Попробуйте ещё раз. ASSORTMENT_REJECTION_REASON_STORAGE_BELARUS_SKU_HAS_NO_ANY_FEA CN , ASSORTMENT_REJECTION_REASON_STORAGE_BELARUS_SKU_HAS_NO_SELLER_ FEACN — у товара нет кода ТН ВЭД ЕАЭС. ASSORTMENT_REJECTION_REASON_TRACEABLE_SKU_HAS_NO_GTIN_BARCODE — у товара нет штрихкода GTIN. ASSORTMENT_REJECTION_REASON_TRACEABLE_SKU_HAS_NO_MEASUREMENT_U NIT_QUANTITY — не указано количество товара в унифицированных единицах измерения.. Enum: `"UNSPECIFIED"`, `"UNKNOWN"`, `"INCORRECT_SUPPLY_STATE"`, `"UTD_IS_UPLOADED"`, `"STORAGE_WAREHOUSE_IS_NOT_WMS"`, `"CONTRACT_IS_NOT_VALID_FOR_HANDLING_ORDERS"`, `"SUPPLY_IS_VIRTUAL"`, `"SUPPLY_DOES_NOT_BELONG_TO_COMPANY"`, `"ASSORTMENT_REJECTION_REASON_CORRUPTED_ASSORTMENT"`, `"ASSORTMENT_REJECTION_REASON_STORAGE_BELARUS_SKU_HAS_NO_ANY_FEACN"`, `"ASSORTMENT_REJECTION_REASON_STORAGE_BELARUS_SKU_HAS_NO_SELLER_FEACN"`, `"ASSORTMENT_REJECTION_REASON_TRACEABLE_SKU_HAS_NO_GTIN_BARCODE"`, `"ASSORTMENT_REJECTION_REASON_TRACEABLE_SKU_HAS_NO_MEASUREMENT_UNIT_QUANTITY"`.
- **validated_assortment** `object` — Информация о товарном составе.

**Пример ответа (`200`):**

```json
{
  "editing_errors": [
    "UNSPECIFIED"
  ],
  "validated_assortment": {
    "approved_items": [
      {
        "barcode": "string",
        "item_link": "string",
        "name": "string",
        "offer_id": "string",
        "origin_quantity": 0,
        "origin_total_volume_in_litre \"quant": 0,
        "quantity": 0,
        "sku": 0,
        "sku_quantity_limit": 0,
        "total_volume_in_litres": 0
      }
    ],
    "rejected_items": [
      {
        "barcode": "string",
        "name": "string",
        "offer_id": "string",
        "origin_quantity": 0,
        "origin_total_volume_in_litre \"quantity": 0,
        "rejection_reason": [
          "UNSPECIFIED"
        ],
        "restrictions": {
          "reasons_restrictions": [
            "UNKNOWN"
          ],
          "sku_has_no_sales_in_days \"sku_quantity_limit": 0
        },
        "sku": 0,
        "total_volume_in_litres": 0
      }
    ],
    "total_approved_item_count": 0,
    "total_approved_quantity": 0,
    "total_approved_volume_in_litres": 0,
    "total_rejected_item_count": 0,
    "total_restricted_item_count": 0
  }
}
```


---

## Создать заявку на поставку по черновику

`POST /v2/draft/supply/create`

Вы можете создавать заявку на поставку по черновику: 2 раза в минуту; 50 раз в час; 500 раз в день. Если превысите лимит, вернётся ошибка 429.

**Тело запроса** (`application/json`):
- **draft_id** `integer <int64>` *обязательный* — Идентификатор черновика из метода /v2/draft/create/info.
- **selected_cluster_warehouses** `Array of objects` *обязательный* — Информация о кластере и складах в нём. Можно передать один кластер для кросс- докинговой и прямой поставки или список всех кластеров для поставки в несколько кластеров.
- **timeslot** `object` — Таймслот поставки.
- **supply_type** `string` *обязательный* — Тип поставки: CROSSDOCK — кросс-докинг; DIRECT — прямая; MULTI_CLUSTER — для нескольких кластеров.. Enum: `"CROSSDOCK"`, `"DIRECT"`, `"MULTI_CLUSTER"`.

**Пример запроса:**

```json
{
  "draft_id": 0,
  "selected_cluster_warehouses": [
    {
      "macrolocal_cluster_id": 0,
      "storage_warehouse_id": 0
    }
  ],
  "timeslot": {
    "from_in_timezone": "string",
    "to_in_timezone": "string"
  },
  "supply_type": "CROSSDOCK"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заявка создана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **draft_id** `integer <int64>` — Идентификатор черновика.
- **error_reasons** `Array of strings` — Причина ошибки: UNSPECIFIED — не определена; SOME_SERVICE_ERROR — ошибка при редактировании поставки; ORDER_SKU_LIMIT — количество товаров в поставке больше 5000; INVALID_QUANTITY_OR_QUANT — некорректное количество товара или грузомест; ORDER_ALREADY_CREATED — заказ уже создан; ORDER_CREATION_IN_PROGRESS — создание заказа в процессе; DRAFT_DOES_NOT_EXIST — черновик не существует; CONTRACTOR_CAN_NOT_CREATE_ORDER — контрагент не может создать заказ; INACTIVE_CONTRACT — нельзя редактировать состав поставки с неактивным договором; DRAFT_INCORRECT_STATE — некорректный статус черновика; INVALID_VOLUME — некорректный объём поставки; INVALID_ROUTE — некорректный маршрут; INVALID_STORAGE_WAREHOUSE — некорректный склад хранения; INVALID_STORAGE_REGION — некорректный регион хранения; INVALID_SPLITTING — некорректное разделение; INVALID_SUPPLY_CONTENT — некорректное содержимое поставки; TIMESLOT_NOT_AVAILABLE — нет доступных таймслотов; SKU_DISTRIBUTION_REQUIRED_BUT_NOT_POSSIBLE — требуется распределение SKU, но оно невозможно; XDOCK_IN_DELIVERY_POINT_DISABLED_FOR_SELLER — поставка кросс-докингом через пункт выдачи заказов недоступна для продавца; DRAFT_IS_LOCKED — черновик заблокирован; INVALID_PACKAGE_UNITS_COUNTS — некорректное количество грузомест; SELLER_CONVERSATION_DOES_NOT_EXIST — точка отгрузки с таким id не существует; USER_CAN_NOT_CREATE_SELLER_CONVERSATION — пользователь не может создать диалог с продавцом; SKU_WITH_ETTN_REQUIRED_TAG_NOT_ALLOWED_FOR_DROP _OFF_POINT — товар с меткой is_ettn_required не разрешён для точки отгрузки; INVALID_SELLER_WAREHOUSE — склад продавца недоступен; PICKUP_ORDER_LIMIT_EXCEEDED — превышен лимит заказов на самовывоз; MINIMUM_VOLUME_IN_LITRES_INVALID — некорректный минимальный объём в литрах; INVALID_CLUSTERS_COUNT — переданы не все кластеры из расчёта; CAN_NOT_CREATE_ORDER — не удалось создать заказ; UNDEFINED — неизвестная ошибка.. Enum: `"UNSPECIFIED"`, `"SOME_SERVICE_ERROR"`, `"ORDER_SKU_LIMIT"`, `"INVALID_QUANTITY_OR_QUANT"`, `"ORDER_ALREADY_CREATED"`, `"ORDER_CREATION_IN_PROGRESS"`, `"DRAFT_DOES_NOT_EXIST"`, `"CONTRACTOR_CAN_NOT_CREATE_ORDER"`, `"INACTIVE_CONTRACT"`, `"DRAFT_INCORRECT_STATE"`, `"INVALID_VOLUME"`, `"INVALID_ROUTE"`, `"INVALID_STORAGE_WAREHOUSE"`, `"INVALID_STORAGE_REGION"`, `"INVALID_SPLITTING"`, `"INVALID_SUPPLY_CONTENT"`, `"TIMESLOT_NOT_AVAILABLE"`, `"SKU_DISTRIBUTION_REQUIRED_BUT_NOT_POSSIBLE"`, `"XDOCK_IN_DELIVERY_POINT_DISABLED_FOR_SELLER"`, `"DRAFT_IS_LOCKED"`, `"INVALID_PACKAGE_UNITS_COUNTS"`, `"SELLER_CONVERSATION_DOES_NOT_EXIST"`, `"USER_CAN_NOT_CREATE_SELLER_CONVERSATION"`, `"SKU_WITH_ETTN_REQUIRED_TAG_NOT_ALLOWED_FOR_DROP_OFF_POINT"`.

**Пример ответа (`200`):**

```json
{
  "draft_id": 0,
  "error_reasons": [
    "UNSPECIFIED"
  ]
}
```


---

## Получить информацию о создании заявки на поставку

`POST /v2/draft/supply/create/status`

**Тело запроса** (`application/json`):
- **draft_id** `integer <int64>` *обязательный* — Идентификатор черновика. Получите значение параметра методом /v2/draft/supply/create.

**Пример запроса:**

```json
{
  "draft_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о создании заявки на поставку |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_reasons** `Array of strings` — Причина ошибки: UNSPECIFIED — не определена; SOME_SERVICE_ERROR — ошибка при редактировании поставки; ORDER_SKU_LIMIT — количество товаров в поставке больше 5000; INVALID_QUANTITY_OR_QUANT — некорректное количество товара или грузомест; ORDER_ALREADY_CREATED — заказ уже создан; ORDER_CREATION_IN_PROGRESS — создание заказа в процессе; DRAFT_DOES_NOT_EXIST — черновик не существует; CONTRACTOR_CAN_NOT_CREATE_ORDER — контрагент не может создать заказ; INACTIVE_CONTRACT — нельзя редактировать состав поставки с неактивным договором; DRAFT_INCORRECT_STATE — некорректный статус черновика; INVALID_VOLUME — некорректный объём поставки; INVALID_ROUTE — некорректный маршрут; INVALID_STORAGE_WAREHOUSE — некорректный склад хранения; INVALID_STORAGE_REGION — некорректный регион хранения; INVALID_SPLITTING — некорректное разделение; INVALID_SUPPLY_CONTENT — некорректное содержимое поставки; TIMESLOT_NOT_AVAILABLE — нет доступных таймслотов; SKU_DISTRIBUTION_REQUIRED_BUT_NOT_POSSIBLE — требуется распределение SKU, но оно невозможно; XDOCK_IN_DELIVERY_POINT_DISABLED_FOR_SELLER — поставка кросс-докингом через пункт выдачи заказов недоступна для продавца; DRAFT_IS_LOCKED — черновик заблокирован; INVALID_PACKAGE_UNITS_COUNTS — некорректное количество грузомест; SELLER_CONVERSATION_DOES_NOT_EXIST — точка отгрузки с таким id не существует; USER_CAN_NOT_CREATE_SELLER_CONVERSATION — пользователь не может написать продавцу; SKU_WITH_ETTN_REQUIRED_TAG_NOT_ALLOWED_FOR_DROP _OFF_POINT — товар с меткой is_ettn_required не разрешён для точки отгрузки; INVALID_SELLER_WAREHOUSE — склад продавца недоступен; PICKUP_ORDER_LIMIT_EXCEEDED — превышен лимит заказов на самовывоз; MINIMUM_VOLUME_IN_LITRES_INVALID — некорректный минимальный объём в литрах; INVALID_CLUSTERS_COUNT — переданы не все кластеры из расчёта; UNDEFINED — неизвестная ошибка.. Enum: `"UNSPECIFIED"`, `"SOME_SERVICE_ERROR"`, `"ORDER_SKU_LIMIT"`, `"INVALID_QUANTITY_OR_QUANT"`, `"ORDER_ALREADY_CREATED"`, `"ORDER_CREATION_IN_PROGRESS"`, `"DRAFT_DOES_NOT_EXIST"`, `"CONTRACTOR_CAN_NOT_CREATE_ORDER"`, `"INACTIVE_CONTRACT"`, `"DRAFT_INCORRECT_STATE"`, `"INVALID_VOLUME"`, `"INVALID_ROUTE"`, `"INVALID_STORAGE_WAREHOUSE"`, `"INVALID_STORAGE_REGION"`, `"INVALID_SPLITTING"`, `"INVALID_SUPPLY_CONTENT"`, `"TIMESLOT_NOT_AVAILABLE"`, `"SKU_DISTRIBUTION_REQUIRED_BUT_NOT_POSSIBLE"`, `"XDOCK_IN_DELIVERY_POINT_DISABLED_FOR_SELLER"`, `"DRAFT_IS_LOCKED"`, `"INVALID_PACKAGE_UNITS_COUNTS"`, `"SELLER_CONVERSATION_DOES_NOT_EXIST"`, `"USER_CAN_NOT_CREATE_SELLER_CONVERSATION"`, `"SKU_WITH_ETTN_REQUIRED_TAG_NOT_ALLOWED_FOR_DROP_OFF_POINT"`.
- **order_id** `integer <int64>` — Идентификатор заявки на поставку.
- **status** `string` — Статус создания заявки на поставку: UNSPECIFIED — не определён, SUCCESS — создана, IN_PROGRESS — создаётся, FAILED — не удалось создать.. Enum: `"UNSPECIFIED"`, `"SUCCESS"`, `"IN_PROGRESS"`, `"FAILED"`.

**Пример ответа (`200`):**

```json
{
  "error_reasons": [
    "UNSPECIFIED"
  ],
  "order_id": 0,
  "status": "UNSPECIFIED"
}
```


---

## Получить список складов продавца

`POST /v1/warehouse/fbo/seller/list`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список складов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **warehouses** `Array of objects` — Список складов продавца.
  - **address** `object` — Информация об адресе склада продавца.
  - **contacts** `object` — Контакты.
  - **courier_comment** `string` — Комментарий для курьера.
  - **is_active** `boolean` — true , если склад активный.
  - **is_pickup** `boolean` — true , если доступна отгрузка курьером.
  - **seller_warehouse_id** `integer <int64>` — Идентификатор склада продавца.
  - **seller_warehouse_name** `string` — Название склада продавца.
  - **working_days** `Array of objects` — Рабочие дни склада продавца.

**Пример ответа (`200`):**

```json
{
  "warehouses": [
    {
      "address": {
        "address": "string",
        "city": "string",
        "coordinates": {
          "latitude": 0,
          "longitude": 0
        },
        "country_code": "string",
        "macrolocal_cluster_id": 0,
        "region": "string",
        "timezone": "string"
      },
      "contacts": {
        "phone_numbers": [
          "string"
        ]
      },
      "courier_comment": "string",
      "is_active": true,
      "is_pickup": true,
      "seller_warehouse_id": 0,
      "seller_warehouse_name": "string \"working_days\": [ { \"day\": \"UNSPECIFIED",
      "time_from_local": "strin \"time_to_local\": \"string\" }"
    }
  ]
}
```


---
