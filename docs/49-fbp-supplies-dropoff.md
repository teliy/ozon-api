# Работа с FBP-поставками с доставкой drop-off

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 561. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Отменить поставку drop-off

`POST /v1/fbp/order/drop-off/cancel`

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
| `200` | Поставка отменена |
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

## Отредактировать информацию о поставке на drop-off пункт

`POST /v1/fbp/order/drop-off/dlv/edit`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **drop_off_date** `string` *обязательный* — Дата прибытия поставки на drop-off пункт.
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "drop_off_date": "string",
  "row_version": 0,
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация передана |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **row_version** `integer <int64>` — Идентификатор актуальной версии черновика.

**Пример ответа (`200`):**

```json
{
  "row_version": 0
}
```


---

## Получить график работы drop-off пункта

`POST /v1/fbp/order/drop-off/timetable`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **drop_off_point_id** `integer <int64>` *обязательный* — Идентификатор drop-off пункта.
- **province_uuid** `string` *обязательный* — Уникальный идентификатор провинции.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "drop_off_point_id": 0,
  "province_uuid": "string",
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | График работы получен |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **calendar** `Array of objects` — Информация о графике работы drop-off пункта.
  - **calendar_item** `object` — Информация о дне.
  - **day_of_week** `string` — Дни недели: DAY_OF_WEEK_UNSPECIFIED — не определён, MONDAY — понедельник, TUESDAY — вторник, WEDNESDAY — среда, THURSDAY — четверг, FRIDAY — пятница, SATURDAY — суббота, SUNDAY — воскресенье.. Enum: `"DAY_OF_WEEK_UNSPECIFIED"`, `"MONDAY"`, `"TUESDAY"`, `"WEDNESDAY"`, `"THURSDAY"`, `"FRIDAY"`, `"SATURDAY"`, `"SUNDAY"`.

**Пример ответа (`200`):**

```json
{
  "calendar": [
    {
      "calendar_item": {
        "break_hours": {
          "timeslot_end": "string",
          "timeslot_start": "string"
        },
        "is_holiday": true,
        "opening_hours": {
          "timeslot_end": "string",
          "timeslot_start": "string"
        }
      },
      "day_of_week": "DAY_OF_WEEK_UNSP }"
    }
  ]
}
```


---
