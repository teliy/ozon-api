# Создание FBS-складов и управление ими

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 151. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Получить список drop-off пунктов для создания склада

## Получить список drop-off пунктов для создания склада

`POST /v1/warehouse/fbs/create/drop-off/list`

**Тело запроса** (`application/json`):
- **coordinates** `object` — Координаты.
- **country_code** `string` *обязательный* — Код страны в формате ISO 2.
- **is_kgt** `boolean` *обязательный* — true , если товар крупногабаритный.
- **search** `object` — Параметры поиска.

**Пример запроса:**

```json
{
  "country_code": "RU",
  "is_kgt": false,
  "coordinates": {
    "latitude": 55,
    "longitude": 37
  },
  "search": {
    "address": "москва",
    "types": [
      "PPZ"
    ]
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список получен |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **points** `Array of objects` — Список пунктов.
  - **address** `string` — Адрес drop-off пункта.
  - **coordinates** `object` — Координаты drop-off пункта.
  - **discount_percent** `number <float>` — Процент скидки за передачу отправления.
  - **id** `string` — Идентификатор drop-off пункта.
  - **last_transit_time_local** `object` — Время, до которого нужно передать отправления, чтобы получить скидку за отгрузку.
  - **type** `string` — Тип drop-off пункта: PVZ — пункт выдачи заказов; PPZ — пункт приёма заказов; SC — сортировочный центр.. Enum: `"PVZ"`, `"PPZ"`, `"SC"`.

**Пример ответа (`200`):**

```json
{
  "points": [
    {
      "address": "Россия",
      "discount_percent": 1,
      "id": "1020002487458000",
      "last_transit_time_local": {
        "hours": 12,
        "minutes": 0,
        "nanos": 0,
        "seconds": 0
      },
      "coordinates": {
        "latitude": 55.756107,
        "longitude": 37.620426
      },
      "type": "PVZ"
    }
  ]
}
```


---

## Получить список drop-off пунктов для изменения информации склада

`POST /v1/warehouse/fbs/update/drop-off/list`

**Тело запроса** (`application/json`):
- **search** `object` — Параметры поиска.
- **warehouse_id** `integer <int64>` *обязательный* — Фильтр по существующему FBS-складу.

**Пример запроса:**

```json
{
  "search": {
    "address": "москва",
    "types": [
      "PPZ"
    ]
  },
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список получен |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **points** `Array of objects` — Список пунктов.
  - **address** `string` — Адрес drop-off пункта.
  - **coordinates** `object` — Координаты drop-off пункта.
  - **discount_percent** `number <float>` — Процент скидки за передачу отправления.
  - **id** `string` — Идентификатор drop-off пункта.
  - **last_transit_time_local** `object` — Время, до которого нужно передать отправления, чтобы получить скидку за отгрузку.
  - **type** `string` — Тип drop-off пункта: PVZ — пункт выдачи заказов; PPZ — пункт приёма заказов; SC — сортировочный центр.. Enum: `"PVZ"`, `"PPZ"`, `"SC"`.

**Пример ответа (`200`):**

```json
{
  "points": [
    {
      "address": "Россия",
      "discount_percent": 1,
      "id": "1020002487458000",
      "last_transit_time_local": {
        "hours": 12,
        "minutes": 0,
        "nanos": 0,
        "seconds": 0
      },
      "coordinates": {
        "latitude": 55.756107,
        "longitude": 37.620426
      },
      "type": "PVZ"
    }
  ]
}
```


---

## Получить список таймслотов для создания склада с отгрузкой drop-off

`POST /v1/warehouse/fbs/create/drop-off/timeslot/list`

**Тело запроса** (`application/json`):
- **drop_off_point_id** `integer <int64>` *обязательный* — Идентификатор drop-off пункта.

**Пример запроса:**

```json
{
  "drop_off_point_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список таймслотов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **timeslots** `Array of objects` — Список таймслотов.
  - **acceptance_end_time_local** `string` — Местное время окончания приёма заказа.
  - **acceptance_start_time_local** `string` — Местное время начала приёма заказа.
  - **from** `string` — Время начала таймслота.
  - **id** `integer <int64>` — Идентификатор таймслота.
  - **to** `string` — Время окончания таймслота.

**Пример ответа (`200`):**

```json
{
  "timeslots": [
    {
      "acceptance_end_time_local": "st \"acceptance_start_time_local\": ",
      "from": "string",
      "id": 0,
      "to": "string"
    }
  ]
}
```


---

## Получить список таймслотов для обновления склада с отгрузкой drop-off

`POST /v1/warehouse/fbs/update/drop-off/timeslot/list`

**Тело запроса** (`application/json`):
- **drop_off_point_id** `integer <int64>` *обязательный* — Идентификатор drop-off пункта.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "drop_off_point_id": 0,
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список таймслотов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **timeslots** `Array of objects` — Список таймслотов.
  - **acceptance_end_time_local** `string` — Местное время окончания приёма заказа.
  - **acceptance_start_time_local** `string` — Местное время начала приёма заказа.
  - **from** `string` — Время начала таймслота.
  - **id** `integer <int64>` — Идентификатор таймслота.
  - **to** `string` — Время окончания таймслота.

**Пример ответа (`200`):**

```json
{
  "timeslots": [
    {
      "acceptance_end_time_local": "st \"acceptance_start_time_local\": ",
      "from": "string",
      "id": 0,
      "to": "string"
    }
  ]
}
```


---

## Получить список таймслотов для создания склада с отгрузкой pick-up

`POST /v1/warehouse/fbs/create/pick-up/timeslot/list`

**Тело запроса** (`application/json`):
- **address_coordinates** `object` *обязательный* — Координаты склада.
- **is_kgt** `boolean` *обязательный* — Признак крупногабаритного товара.

**Пример запроса:**

```json
{
  "is_kgt": true,
  "address_coordinates": {
    "latitude": 55.7558,
    "longitude": 37.6173
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список таймслотов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **is_pickup_supported** `boolean` — Признак поддержки отгрузки pick-up.
- **timeslots** `Array of objects` — Список таймслотов.

**Пример ответа (`200`):**

```json
{
  "is_pickup_supported": true,
  "timeslots": [
    {
      "id": 123456789,
      "from": "00:00",
      "to": "00:00"
    },
    {
      "id": 987654321,
      "from": "00:00",
      "to": "00:00"
    }
  ]
}
```


---

## Получить список таймслотов для обновления склада с отгрузкой pick-up

`POST /v1/warehouse/fbs/update/pick-up/timeslot/list`

**Тело запроса** (`application/json`):
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "warehouse_id": 987654321
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список таймслотов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **timeslots** `Array of objects` — Список таймслотов.
  - **from** `string` — Время начала таймслота.
  - **id** `integer <int64>` — Идентификатор таймслота.
  - **to** `string` — Время окончания таймслота.

**Пример ответа (`200`):**

```json
{
  "timeslots": [
    {
      "id": 1001,
      "from": "00:00",
      "to": "00:00"
    },
    {
      "id": 1002,
      "from": "00:00",
      "to": "00:00"
    }
  ]
}
```


---

## Создать склад

`POST /v1/warehouse/fbs/create`

Если создаёте склад с доставкой в drop-off пункт, используйте метод

**Тело запроса** (`application/json`):
- **address_coordinates** `object` *обязательный* — Координаты адреса склада.
- **cut_in_time** `integer <int64>` *обязательный* — Время на приём заказов в минутах. Например, если вы передадите 3000 , приём заказов будет завершён через 50 часов с момента передачи.
- **drop_off_point_id** `integer <int64>` — Идентификатор drop-off пункта.
- **first_mile_type** `string` *обязательный* — Тип первой мили: PICK_UP — отгрузка заказов курьеру; DROP_OFF — отгрузка заказов в пункт приёма.. Enum: `"PICK_UP"`, `"DROP_OFF"`.
- **is_kgt** `boolean` *обязательный* — true , если товар крупногабаритный.
- **name** `string` *обязательный* — Название склада.
- **options** `object` — Параметры склада.
- **phone** `string` *обязательный* — Номер телефона склада. Укажите в формате +7(XXX)XXX-XX-XX.
- **timeslot_id** `integer <int64>` *обязательный* — Идентификатор таймслота.
- **return_point_id** `integer <int64>` — Идентификатор пункта возврата. Получите значение параметра методом /v1/warehouse/fbs/create/return- point/list.
- **working_days** `Array of strings` — Рабочие дни склада: MONDAY — понедельник, TUESDAY — вторник, WEDNESDAY — среда, THURSDAY — четверг, FRIDAY — пятница, SATURDAY — суббота, SUNDAY — воскресенье.. Enum: `"MONDAY"`, `"TUESDAY"`, `"WEDNESDAY"`, `"THURSDAY"`, `"FRIDAY"`, `"SATURDAY"`, `"SUNDAY"`.

**Пример запроса:**

```json
{
  "address_coordinates": {
    "latitude": 55.69626,
    "longitude": 37.42686
  },
  "first_mile_type": "DROP_OFF",
  "drop_off_point_id": 1020002487458000,
  "cut_in_time": 0,
  "timeslot_id": 0,
  "return_point_id": 0,
  "is_kgt": false,
  "name": "Склад",
  "options": {
    "comment": "Комментарий",
    "courier_phones": [
      "+7(999)999-99-99"
    ],
    "is_auto_assembly": true,
    "is_waybill_enabled": true
  },
  "phone": "+7(999)999-99-99",
  "working_days": [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции на создание FBS-склада. Чтобы получить статус операции, используйте метод /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "a0cfefee-9a5a-4580-bc32"
}
```


---

## Обновить склад

`POST /v1/warehouse/fbs/update`

**Тело запроса** (`application/json`):
- **address_coordinates** `object` *обязательный* — Координаты склада.
- **name** `string` — Название склада.
- **options** `object` — Параметры склада.
- **phone** `string+7(XXX)XXX-XX-XX` — Номер телефона склада.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.
- **working_days** `Array of strings` — Рабочие дни склада: MONDAY — понедельник; TUESDAY — вторник; WEDNESDAY — среда; THURSDAY — четверг; FRIDAY — пятница; SATURDAY — суббота; SUNDAY — воскресенье.. Enum: `"MONDAY"`, `"TUESDAY"`, `"WEDNESDAY"`, `"THURSDAY"`, `"FRIDAY"`, `"SATURDAY"`, `"SUNDAY"`.

**Пример запроса:**

```json
{
  "address_coordinates": {
    "latitude": 55.69626,
    "longitude": 37.42686
  },
  "name": "Склад Балашиха",
  "options": {
    "comment": "Заезд на склад через гла \"courier_phones\": [ \"+7(999)999-99-99\" ]",
    "is_auto_assembly": true,
    "is_waybill_enabled": true
  },
  "phone": "+7(XXX)XXX-XX-XX",
  "warehouse_id": 1020002929332000,
  "working_days": [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад обновлён |
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

## Обновить первую милю

`POST /v1/warehouse/fbs/first-mile/update`

**Тело запроса** (`application/json`):
- **cut_in_time** `integer <int64>` *обязательный* — Время на приём заказов в минутах. Например, если вы передадите 3000 , приём заказов будет завершён через 50 часов с момента передачи.
- **drop_off_point_id** `integer <int64>` — Идентификатор drop-off пункта. Если first_mile_type = DROP_OFF , параметр обязательный.
- **first_mile_type** `string` *обязательный* — Тип первой мили: PICK_UP — отгрузка заказов курьеру; DROP_OFF — отгрузка заказов в пункт приёма.. Enum: `"PICK_UP"`, `"DROP_OFF"`.
- **timeslot_id** `integer <int64>` *обязательный* — Идентификатор таймслота.
- **return_point_id** `integer <int64>` — Идентификатор пункта возврата. Получите значение параметра методом /v1/warehouse/fbs/update/return- point/list.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "first_mile_type": "DROP_OFF",
  "drop_off_point_id": 0,
  "cut_in_time": 0,
  "timeslot_id": 0,
  "return_point_id": 0,
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Первая миля обновлена |
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

## Получить список пунктов возврата для создания склада

`POST /v1/warehouse/fbs/create/return-point/list`

**Тело запроса** (`application/json`):
- **coordinates** `object` *обязательный* — Координаты пункта возврата.
- **country_code** `string` *обязательный* — Код страны в формате ISO 2.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.
- **limit** `integer <int32>` *обязательный* — Количество значений в ответе.
- **search** `object` — Параметры поиска.
- **selected_dropoff_point_id** `integer <int64>` — Идентификатор выбранной точки отгрузки на складе.

**Пример запроса:**

```json
{
  "coordinates": {
    "latitude": 0,
    "longitude": 0
  },
  "country_code": "string",
  "last_id": 0,
  "limit": 1,
  "search": {
    "address": "string",
    "types": [
      "PVZ"
    ]
  },
  "selected_dropoff_point_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — Признак, что в ответе вернули не все пункты возврата.
- **is_selected_point_available** `boolean` — Признак доступности пункта возврата.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.
- **points** `Array of objects` — Список пунктов возврата.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "is_selected_point_available": true,
  "last_id": 0,
  "points": [
    {
      "address": "string",
      "coordinates": {
        "latitude": 0,
        "longitude": 0
      },
      "id": 0,
      "name": "string",
      "type": "UNSPECIFIED",
      "utc_offset": 0,
      "working_days": [
        {
          "day": "UNSPECIFIED",
          "from": "string",
          "to": "string"
        }
      ]
    }
  ]
}
```


---

## Получить список пунктов возврата для обновления склада

`POST /v1/warehouse/fbs/update/return-point/list`

**Тело запроса** (`application/json`):
- **current_dropoff_point_id** `integer <int64>` — Идентификатор выбранной точки отгрузки на складе.
- **current_return_point_id** `integer <int64>` — Установленный пункт возврата. Получите значение параметра методом /v1/warehouse/fbs/return- mile/info.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.
- **limit** `integer <int32>` *обязательный* — Количество значений в ответе.
- **search** `object` — Параметры поиска.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "current_dropoff_point_id": 0,
  "current_return_point_id": 0,
  "last_id": 0,
  "limit": 1,
  "search": {
    "address": "string",
    "types": [
      "PVZ"
    ]
  },
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — Признак, что в ответе вернули не все пункты возврата.
- **is_selected_point_available** `boolean` — Признак доступности пункта возврата для выбора.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице.
- **points** `Array of objects` — Список пунктов возврата.

**Пример ответа (`200`):**

```json
{
  "has_next": true,
  "is_selected_point_available": true,
  "last_id": 0,
  "points": [
    {
      "address": "string",
      "coordinates": {
        "latitude": 0,
        "longitude": 0
      },
      "id": 0,
      "name": "string",
      "type": "UNSPECIFIED",
      "utc_offset": 0,
      "working_days": [
        {
          "day": "UNSPECIFIED",
          "from": "string",
          "to": "string"
        }
      ]
    }
  ]
}
```


---

## Получить информацию о возвратной миле

`POST /v1/warehouse/fbs/return-mile/info`

**Тело запроса** (`application/json`):
- **warehouse_ids** `Array of strings <int64>` *обязательный* — Идентификаторы складов.

**Пример запроса:**

```json
{
  "warehouse_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **return_mile_settings** `Array of objects` — Информация о возвратной миле на складе.
  - **is_return_mile_required** `boolean` — Признак, что необходимо установить пункт возврата.
  - **return_point** `object` — Информация о пункте возврата.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "return_mile_settings": [
    {
      "is_return_mile_required": true,
      "return_point": {
        "address": "string",
        "coordinates": {
          "latitude": 0,
          "longitude": 0
        },
        "id": 0,
        "name": "string",
        "type": "UNSPECIFIED",
        "utc_offset": 0,
        "working_days": [
          {
            "day": "UNSPECIFIED",
            "from": "string",
            "to": "string"
          }
        ]
      },
      "warehouse_id": 0
    }
  ]
}
```


---

## Проверить необходимость установки возвратной мили на склад

`POST /v1/warehouse/fbs/return-mile/check`

**Тело запроса** (`application/json`):
- **country_code** `string` *обязательный* — Код страны в формате ISO 2.
- **first_mile_type** `string` *обязательный* — Тип первой мили: PICK_UP — отгрузка заказов курьеру; DROP_OFF — отгрузка заказов в пункт приёма.. Enum: `"PICK_UP"`, `"DROP_OFF"`.
- **is_kgt** `boolean` *обязательный* — Признак крупногабаритного товара.
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример запроса:**

```json
{
  "country_code": "string",
  "first_mile_type": "PICK_UP",
  "is_kgt": true,
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Успешно |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **should_set_return_mile** `boolean` — Признак, что необходимо установить возвратную милю.
- **unavailability_reasons** `Array of strings` — Причины, по которым нельзя установить возвратную милю.

**Пример ответа (`200`):**

```json
{
  "should_set_return_mile": true,
  "unavailability_reasons": [
    "string"
  ]
}
```


---

## Создать вызов курьера на забор отгрузки pick-up

`POST /v1/warehouse/fbs/pickup/courier/create`

Метод позволяет запланировать приезд курьера для отгрузки ему отправлений. Подробнее об отгрузках курьеру на FBS в Базе знаний

**Тело запроса** (`application/json`):
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада. Чтобы получить список складов для планирования выездов, используйте /v1/warehouse/fbs/pickup/planning/list.

**Пример запроса:**

```json
{
  "warehouse_id": 0
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

## Отменить вызов курьера на забор отгрузки pick-up

`POST /v1/warehouse/fbs/pickup/courier/cancel`

Метод позволяет отменить запланированный приезд курьера. Подробнее об отгрузках курьеру на FBS в Базе знаний

**Тело запроса** (`application/json`):
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "warehouse_id": 0
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

## Получить историю отгрузок курьерам

`POST /v1/warehouse/fbs/pickup/history/list`

Подробнее об отгрузках курьеру в Базе знаний продавца

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "planned_date": "string",
    "warehouse_id": [
      "string"
    ],
    "was_planned": true
  },
  "limit": 1
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | История отгрузок |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат метода.
  - **cursor** `string` — Указатель для выборки следующих данных.
  - **history** `Array of objects` — История отгрузок.

**Пример ответа (`200`):**

```json
{
  "result": {
    "cursor": "string",
    "history": [
      {
        "planned_date": "string",
        "status": "string",
        "updated_at": "2019-08-24T14: \"warehouse_id\": 0",
        "warehouse_name": "string",
        "was_planned": true
      }
    ]
  }
}
```


---

## Получить список складов для планирования отгрузок курьеру

`POST /v1/warehouse/fbs/pickup/planning/list`

Чтобы создать отгрузку, используйте метод Подробнее об отгрузках курьеру на FBS в Базе знаний

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список складов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `object` — Список складов.
  - **warehouses** `Array of objects` — Информация о складах.

**Пример ответа (`200`):**

```json
{
  "result": {
    "warehouses": [
      {
        "can_modify_pickup_plan": "tru",
        "has_postings_to_be_planned": "is_pickup_planned",
        "last_pickup_plan_date_at": " \"warehouse_id\": 0",
        "warehouse_name": "string"
      }
    ]
  }
}
```


---
