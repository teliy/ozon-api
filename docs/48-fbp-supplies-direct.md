# Работа с FBP-поставками с доставкой direct

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 557. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Отменить поставку

`POST /v1/fbp/order/direct/cancel`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.

**Пример запроса:**

```json
{
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат отмены |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error** `object` — Информация об ошибке.
- **is_error** `boolean` — true , если есть ошибка.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "error": {
    "order_errors": [
      "ERROR_TYPE_UNSPECIFIED"
    ]
  },
  "is_error": true,
  "row_version": 0
}
```


---

## Обновить информацию о доставке силами продавца

`POST /v1/fbp/order/direct/seller-dlv/edit`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **driver_name** `string` *обязательный* — ФИО водителя.
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.
- **vehicle_number** `string` *обязательный* — Номер автомобиля.
- **vehicle_type** `string` *обязательный* — Тип автомобиля.

**Пример запроса:**

```json
{
  "driver_name": "string",
  "row_version": 0,
  "supply_id": "string",
  "vehicle_number": "string",
  "vehicle_type": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация обновлена |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error** `object` — Информация об ошибке.
- **is_error** `boolean` — true , если есть ошибка.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "error": {
    "order_errors": "ERROR_TYPE_UNSPECIF"
  },
  "is_error": true,
  "row_version": 0
}
```


---

## Обновить информацию о доставке сторонней транспортной компанией

`POST /v1/fbp/order/direct/tpl-dlv/edit`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.
- **tracking_number** `string` *обязательный* — Трек-номер отправления.
- **transport_company_name** `string` *обязательный* — Название транспортной компании.

**Пример запроса:**

```json
{
  "row_version": 0,
  "supply_id": "string",
  "tracking_number": "string",
  "transport_company_name": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация обновлена |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error** `object` — Информация об ошибке.
- **is_error** `boolean` — true , если есть ошибка.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "error": {
    "order_errors": [
      "DELIVERY_DRIVER_NAME_LENGTH_MAX ] }, ",
      "is_error",
      true,
      {
        "row_version": 0
      }
    ]
  }
}
```


---

## Отредактировать таймслот в заявке на поставку

`POST /v1/fbp/order/direct/timeslot/edit`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.
- **timeslot_start** `string <date-time>` *обязательный* — Начало таймслота.

**Пример запроса:**

```json
{
  "row_version": 0,
  "supply_id": "string",
  "timeslot_start": "2019-08-24T14:15:22Z"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Таймслот отредактирован |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_reasons** `Array of strings` — Причина ошибки: RESERVE_FAILURE_TYPE_UNSPECIFIED — не определена; REQUEST_VALIDATION — в запросе указана дата резервирования в прошлом; INVALID_RESERVE — исходный резерв не найден, неактивен или уже содержит заявки, а его пытаются перезаписать; LOGISTICS_REASON — ошибка на стороне логистики; SCHEDULE_REASON — ошибка на стороне расписаний.. Enum: `"RESERVE_FAILURE_TYPE_UNSPECIFIED"`, `"REQUEST_VALIDATION"`, `"INVALID_RESERVE"`, `"LOGISTICS_REASON"`, `"SCHEDULE_REASON"`.
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "error_reasons": [
    "RESERVE_FAILURE_TYPE_UNSPECIFIED"
  ],
  "row_version": 0
}
```


---

## Получить список таймслотов для поставки

`POST /v1/fbp/order/direct/timeslot/list`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **interval_end** `string <date-time>` *обязательный* — Дата окончания нужного периода доступных таймслотов.
- **interval_start** `string <date-time>` *обязательный* — Дата начала нужного периода доступных таймслотов.
- **supply_id** `string` *обязательный* — Идентификатор заявки на поставку.

**Пример запроса:**

```json
{
  "interval_end": "2019-08-24T14:15:22Z",
  "interval_start": "2019-08-24T14:15:22Z \"supply_id\": \"string\""
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список таймслотов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **reasons** `Array of strings` — Причины отсутствия таймслотов: EMPTY_TIMESLOTS_REASON_UNSPECIFIED — не определено; LOGISTICS_UNKNOWN — неизвестная ошибка на стороне логистики; NO_ROUTE — нет маршрута; NO_ROUTE_SCHEDULES — нет расписания на маршруте; NO_LOGISTICS_CAPACITY — недостаточно доступных слотов на маршруте; SCHEDULE_UNKNOWN — неизвестная ошибка на стороне расписаний; NOT_ENOUGH_CAPACITY — недостаточно доступных слотов на складе; NOT_ENOUGH_TRUCKS — недостаточно машиномест; LIMITS_NOT_AVAILABLE — не настроены лимиты на складе; CROSS_DOCK_RESERVE_MISSING — не забронирован кросс-докинговый резерв на складе; SCHEDULE_RESERVE_MISSING — отсутствует необходимый резерв по расписанию.. Enum: `"EMPTY_TIMESLOTS_REASON_UNSPECIFIED"`, `"LOGISTICS_UNKNOWN"`, `"NO_ROUTE"`, `"NO_ROUTE_SCHEDULES"`, `"NO_LOGISTICS_CAPACITY"`, `"SCHEDULE_UNKNOWN"`, `"NOT_ENOUGH_CAPACITY"`, `"NOT_ENOUGH_TRUCKS"`, `"LIMITS_NOT_AVAILABLE"`, `"CROSS_DOCK_RESERVE_MISSING"`, `"SCHEDULE_RESERVE_MISSING"`.
- **timeslots** `Array of objects` — Список доступных таймслотов.
- **warehouse_timezone_name** `string` — Часовой пояс склада продавца.

**Пример ответа (`200`):**

```json
{
  "reasons": [
    "EMPTY_TIMESLOTS_REASON_UNSPECIFIED"
  ],
  "timeslots": [
    {
      "timeslot_end": "2019-08-24T14:1 \"timeslot_start\": "
    }
  ],
  "warehouse_timezone_name": "string"
}
```


---
