# Работа со складами FBS и rFBS

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 138. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Список складов

`POST /v2/warehouse/list`

Метод возвращает список складов FBS и rFBS. Чтобы получить список складов FBO, используйте метод /v1/warehouse/fbo/list.

**Тело запроса** (`application/json`):
- **limit** `integer` *обязательный* — Количество значений в ответе.
- **cursor** `string` — Указатель для выборки следующих данных.
- **warehouse_ids** `Array of strings <int64>` — Идентификаторы складов.

**Пример запроса:**

```json
{
  "cursor": "string",
  "limit": 0,
  "warehouse_ids": [
    20605650762000
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список складов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **warehouses** `Array of objects` — Список складов.
- **has_next** `boolean` — true , если в ответе вернулись не все значения.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "warehouses": [
    {
      "address_info": {
        "address": "Россия",
        "latitude": 55.495093,
        "longitude": 38.172731,
        "utc": "UTC+03:00"
      },
      "carriage_label_type": "BIG",
      "courier_comment": "",
      "courier_phones": [
        "+7(999)999-99-99"
      ],
      "created_at": "2025-03-11T11:57: \"first_mile\": { \"type\": \"PICK_UP",
      "dropoff_point_id": "10200020 ",
      "timeslot_from": "20:59",
      "timeslot_id": 287231,
      "timeslot_to": "21:00",
      "first_mile_is_changing": "fal"
    },
    {
      "has_entrusted_acceptance": true,
      "has_postings_limit": false,
      "is_auto_assembly": true,
      "is_kgt": true,
      "is_rfbs": true,
      "is_waybill_enabled": true,
      "min_postings_limit": 2,
      "is_comfort": true,
      "is_express": true,
      "warehouse_type": "string",
      "cut_in_time": 0,
      "name": "17023",
      "phone": "+7(999)999-99-99",
      "postings_limit": -1,
      "sla_cut_in": 2939,
      "status": "created",
      "timetable": {
        "timetable_from": "2025-03-11 \"timetable_to\": ",
        "working_hours": [
          {
            "time_from": "2025-03- \"time_to\": "
          }
        ]
      },
      "updated_at": "2025-03-11T11:57: \"warehouse_id\": 20605650762000",
      "with_item_list": true,
      "working_days": [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY"
      ]
    }
  ],
  "has_next": "string"
}
```


---

## Список складов

`POST /v1/warehouse/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает список складов FBS и rFBS. Чтобы получить список складов FBO, используйте метод /v1/cluster/list. Метод можно использовать 1 раз в минуту.

> **Примечание:** Метод устаревает и будет отключён 7 апреля 2026 года.

> **Примечание:** Переключитесь на /v2/warehouse/list.

**Тело запроса** (`application/json`):
- **limit** `integer <int64>` *обязательный* — Количество значений в ответе.
- **offset** `integer <int64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **with** `object` — Дополнительные поля, которые нужно добавить в ответ.

**Пример запроса:**

```json
{
  "limit": 1,
  "offset": 1,
  "with": {
    "able_to_set_price": true
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список складов |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Список складов.
  - **has_entrusted_acceptance** `boolean` — Признак доверительной приёмки. true , если доверительная приёмка включена на складе.
  - **is_rfbs** `boolean` — Признак работы склада по схеме rFBS: true — склад работает по схеме rFBS; false — не работает по схеме rFBS.
  - **name** `string` — Название склада.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.
  - **can_print_act_in_advance** `boolean` — Возможность печати акта приёма- передачи заранее. true , если печатать заранее возможно.
  - **first_mile_type** `object` — Первая миля FBS.
  - **has_postings_limit** `boolean` — Признак наличия лимита минимального количества заказов. true , если лимит есть.
  - **is_karantin** `boolean` — Признак, что склад не работает из-за карантина.
  - **is_kgt** `boolean` — Признак, что склад принимает крупногабаритные товары.
  - **is_economy** `boolean` — true , если склад работает с эконом- товарами.
  - **is_able_to_set_price** `boolean` — true , если можно установить цену.
  - **is_presorted** `boolean` — true , если отгрузка с предсортировкой.
  - **is_timetable_editable** `boolean` — Признак, что можно менять расписание работы складов.
  - **min_postings_limit** `integer <int32>` — Минимальное значение лимита — количество заказов, которые можно привезти в одной поставке.
  - **postings_limit** `integer <int32>` — Значение лимита. -1 , если лимита нет.
  - **min_working_days** `integer <int64>` — Количество рабочих дней склада.
  - **status** `string` — Статус склада. Соответствие статусов склада со статусами с личном кабинете: Активируется new Активный created В архиве disabled Заблокирован blocked disabled_du На паузе e_to_limit Ошибка error
  - **working_days** `Array of strings` — Рабочие дни склада.. Enum: `"1"`, `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"`.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "warehouse_id": 17777777788000,
      "name": "BlueMarketplace",
      "is_rfbs": false,
      "is_able_to_set_price": false,
      "has_entrusted_acceptance": true,
      "first_mile_type": {
        "dropoff_point_id": "11211119 \"dropoff_timeslot_id\": 294144 \"first_mile_is_changing\": fal \"first_mile_type\": \"DropOff\""
      },
      "is_kgt": false,
      "can_print_act_in_advance": "fals",
      "min_working_days": 5,
      "is_karantin": false,
      "has_postings_limit": false,
      "postings_limit": -1,
      "working_days": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "min_postings_limit": 2,
      "is_timetable_editable": false,
      "status": "created",
      "is_economy": false,
      "is_presorted": false
    }
  ]
}
```


---

## Список методов доставки realFBS- склада

`POST /v2/delivery-method/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр для поиска методов доставки.
- **limit** `integer <int64>` *обязательный* — Количество значений в ответе.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "delivery_method_ids": [
      "string"
    ],
    "provider_ids": [
      "string"
    ],
    "status": [
      "NEW"
    ],
    "warehouse_ids": [
      "string"
    ]
  },
  "limit": 1,
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список методов склада |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **has_next** `boolean` — true , если в ответе вернули не все методы доставки.
- **delivery_methods** `Array of objects` — Методы доставки.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "has_next": true,
  "delivery_methods": [
    {
      "created_at": "2019-08-24T14:15: \"cutoff\": \"string",
      "id": 0,
      "is_express": true,
      "name": "string",
      "provider_id": 0,
      "sla_cut_in": 0,
      "status": "NEW",
      "template_id": 0,
      "tpl_dropoff_point": {
        "address": "string",
        "address_coordinates": {
          "latitude": 0,
          "longitude": 0
        },
        "code": "string",
        "name": "string"
      },
      "tpl_integration_type": "string",
      "updated_at": "2019-08-24T14:15: \"warehouse_id\": 0 }"
    }
  ]
}
```


---

## Список методов доставки склада

`POST /v1/delivery-method/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

> **Примечание:** Метод устаревает и будет отключён 7 апреля 2026 года.

> **Примечание:** Переключитесь на /v2/delivery-method/list.

**Тело запроса** (`application/json`):
- **filter** `object` — Фильтр для поиска методов доставки.
- **limit** `integer <int64>` *обязательный* — Количество элементов в ответе. Максимум — 50, минимум — 1.
- **offset** `integer <int64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.

**Пример запроса:**

```json
{
  "filter": {
    "provider_id": 424,
    "status": "ACTIVE",
    "warehouse_id": 15588127982000
  },
  "limit": 100,
  "offset": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список методов склада |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **has_next** `boolean` — Признак, что в запросе вернулась только часть методов доставки: true — сделайте повторный запрос с новым параметром offset для получения остальных методов; false — ответ содержит все методы доставки по запросу.
- **result** `Array of objects` — Результат запроса.
  - **company_id** `integer <int64>` — Идентификатор продавца.
  - **created_at** `string <date-time>` — Дата и время создания метода доставки.
  - **cutoff** `string` — Время, до которого продавцу нужно собрать заказ.
  - **id** `integer <int64>` — Идентификатор метода доставки.
  - **name** `string` — Название метода доставки.
  - **provider_id** `integer <int64>` — Идентификатор службы доставки.
  - **sla_cut_in** `integer <int64>` — Минимальное время на сборку заказа в минутах в соответствии с настройками склада.
  - **status** `string` — Статус метода доставки: NEW — создан, EDITED — редактируется, ACTIVE — активный, DISABLED — неактивный.
  - **template_id** `integer <int64>` — Идентификатор услуги по доставке заказа.
  - **updated_at** `string <date-time>` — Дата и время последнего обновления метода метода доставки.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "id": 15588127982000,
      "company_id": 1,
      "name": "Ozon Логистика курьеру",
      "status": "ACTIVE",
      "cutoff": "13:00",
      "provider_id": 24,
      "template_id": 0,
      "warehouse_id": 15588127982000,
      "created_at": "2019-04-04T15:22: ",
      "updated_at": "2021-08-15T10:21: \"sla_cut_in\": 1440"
    }
  ],
  "has_next": false
}
```


---

## Получить информацию по возвратным настройкам rFBS и rFBS Express

`POST /v1/delivery-method/return/settings/get`

**Тело запроса** (`application/json`):
- **delivery_method_id** `integer <int64>` *обязательный* — Идентификатор способа доставки. Получите значение параметра методом /v2/delivery-method/list.

**Пример запроса:**

```json
{
  "delivery_method_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация получена |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **settings** `object` — Информация о возвратных настройках.
  - **courier_details** `object` — Настройки курьера.
  - **post_office_zipcode** `string` — Индекс отделения Почты России для «лёгкого возврата».
  - **return_point** `object` — Информация о пункте возврата.
  - **transport_company_details** `object` — Настройки транспортной компании.

**Пример ответа (`200`):**

```json
{
  "settings": {
    "courier_details": {
      "contact_days": 0
    },
    "post_office_zipcode": "string",
    "return_point": {
      "address": "string",
      "address_coordinates": {
        "latitude": "string",
        "longitude": "string"
      },
      "id": 0,
      "type": "UNSPECIFIED",
      "working_days": [
        {
          "day": "UNSPECIFIED",
          "from": "string",
          "to": "string"
        }
      ]
    },
    "transport_company_details": {
      "transport_company_names": [
        "string"
      ],
      "zipcode": "string"
    }
  }
}
```


---

## Получить статус операции

`POST /v1/warehouse/operation/status`

**Тело запроса** (`application/json`):
- **operation_id** `string` *обязательный* — Идентификатор операции.

**Пример запроса:**

```json
{
  "operation_id": "a0cfefee-9a5a-4580-bc32"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус операции |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error** `object` — Ошибка при обработке операции.
- **result** `object` — Результат операции.
  - **entity_id** `integer <int64>` — Идентификатор обрабатываемой сущности. Если операция CREATE_FBS_WAREHOUSE , вернётся идентификатор склада.
- **status** `string` — Статус операции: UNSPECIFIED — не определено; IN_PROGRESS — в процессе; SUCCESS — выполнена; ERROR — завершилась с ошибкой.. Enum: `"UNSPECIFIED"`, `"IN_PROGRESS"`, `"SUCCESS"`, `"ERROR"`.
- **type** `string` — Тип операции: UNSPECIFIED — не определено; CREATE_FBS_WAREHOUSE — создание FBS-склада; UPDATE_FBS_WAREHOUSE — обновление FBS-склада; SET_FIRST_MILE — установка первой мили; WAREHOUSE_ENABLE_DISABLE — архивация или разархивация FBS-склада; WAREHOUSE_PAUSE_UNPAUSE — включение или выключение паузы rFBS-склада.. Enum: `"UNSPECIFIED"`, `"CREATE_FBS_WAREHOUSE"`, `"UPDATE_FBS_WAREHOUSE"`, `"SET_FIRST_MILE"`, `"WAREHOUSE_ENABLE_DISABLE"`, `"WAREHOUSE_PAUSE_UNPAUSE"`.

**Пример ответа (`200`):**

```json
{
  "error": {
    "code": "string",
    "message": "string"
  },
  "result": {
    "warehouse_id": 1020005000219156
  },
  "status": "SUCCESS",
  "type": "CREATE_FBS_WAREHOUSE"
}
```


---

## Перенести склад в архив

`POST /v1/warehouse/archive`

**Тело запроса** (`application/json`):
- **reason** `string` *обязательный* — Причина переноса склада в архив.
- **return_point_id** `integer <int64>` — Идентификатор пункта возврата. Получите значение параметра методом /v1/warehouse/fbs/update/return- point/list.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "reason": "Тестовая причина",
  "warehouse_id": 1020002929332000,
  "return_point_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад перенесён в архив |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции. Получите статус операции методом /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---

## Перенести склад из архива

`POST /v1/warehouse/unarchive`

**Тело запроса** (`application/json`):
- **return_point_id** `integer <int64>` — Идентификатор пункта возврата. Получите значение параметра методом /v1/warehouse/fbs/update/return- point/list.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "warehouse_id": 1020002929332000,
  "return_point_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад перенесён из архива |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции. Получите статус операции методом /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---

## Получить список товаров с ограничениями по доставке

`POST /v1/warehouse/invalid-products/get`

**Тело запроса** (`application/json`):
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. При первом запросе оставьте это поле пустым. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада. Получите значение параметра методом /v1/warehouse/warehouses-with-invalid-products.

**Пример запроса:**

```json
{
  "last_id": 0,
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров с ограничениями |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — true , если в ответе вернулись не все товары.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, передайте полученное значение в следующем запросе в параметре last_id .
- **validation_results** `Array of objects` — Результат проверки.
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "last_id": 0,
  "validation_results": [
    {
      "item": {
        "size": {
          "height_mm": 0,
          "length_mm": 0,
          "width_mm": 0
        },
        "sku": 0,
        "weight_g": 0
      },
      "state": "UNSPECIFIED",
      "validation_errors": [
        {
          "characteristic": "UNSPEC \"restriction_price\": { \"currency\": \"string",
          "value": 0
        },
        {
          "restriction_vwc": 0,
          "template_id": 0,
          "type": "UNSPECIFIED"
        }
      ]
    }
  ],
  "warehouse_id": 0
}
```


---

## Получить список складов с ограниченными для доставки товарами

`POST /v1/warehouse/warehouses-with-invalid-products`

Возвращает идентификаторы складов, на которых находятся товары с ограничениями. Такие товары недоступны для доставки со склада.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список складов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **warehouse_ids** `Array of strings <int64>` — Список идентификаторов складов, у которых есть хотя бы 1 товар, который недоступен для доставки со склада. Чтобы получить список товаров с ограничениями, используйте метод /v1/warehouse/invalid-products/get.

**Пример ответа (`200`):**

```json
{
  "warehouse_ids": [
    "string"
  ]
}
```


---
