# Пропуски

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 343. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Список пропусков

`POST /v1/pass/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтры.
- **limit** `integer <int32>` *обязательный* — Ограничение по количеству записей в ответе.

**Пример запроса:**

```json
{
  "cursor": "",
  "filter": {
    "arrival_pass_ids": [
      "5000123456",
      "5000123457"
    ],
    "arrival_reason": "FBS_DELIVERY",
    "dropoff_point_ids": [
      "7000123456",
      "7000123457"
    ],
    "only_active_passes": true,
    "warehouse_ids": [
      "3000007863",
      "3000007864"
    ]
  },
  "limit": 1000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список пропусков |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **arrival_passes** `Array of objects` — Список пропусков для перевозки.
- **cursor** `string` — Указатель для выборки следующих данных. Если параметр пустой, данных больше нет.

**Пример ответа (`200`):**

```json
{
  "arrival_passes": [
    {
      "arrival_pass_id": 5000123456,
      "arrival_reasons": [
        "FBS_DELIVERY",
        "FBS_RETURN"
      ],
      "arrival_time": "2026-03-16T10:0 \"driver_name\": ",
      "driver_phone": "+79991234567",
      "dropoff_point_id": 7000123456,
      "is_active": true,
      "vehicle_license_plate": "А123БВ \"vehicle_model\": \"ГАЗель NEXT",
      "warehouse_id": 3000007863
    },
    {
      "arrival_pass_id": 5000123457,
      "arrival_reasons": [
        "FBS_RETURN"
      ],
      "arrival_time": "2026-03-16T14:3 \"driver_name\": ",
      "driver_phone": "+79997654321",
      "dropoff_point_id": 7000123457,
      "is_active": true,
      "vehicle_license_plate": "В456ГД \"vehicle_model\": \"Ford Transit",
      "warehouse_id": 3000007864
    }
  ],
  "cursor": "next-page-cursor-12345"
}
```


---

## Создать пропуск

`POST /v1/carriage/pass/create`

Идентификатор созданного пропуска добавится к перевозке.

**Тело запроса** (`application/json`):
- **arrival_passes** `Array of objects` *обязательный* — Список пропусков.
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "carriage_id": 5000123456,
  "arrival_passes": [
    {
      "driver_name": "Иванов Иван Иван \"driver_phone\": \"+79991234567",
      "vehicle_license_plate": "А123БВ \"vehicle_model\": \"ГАЗель NEXT",
      "with_returns": true
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Пропуск создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **arrival_pass_ids** `Array of strings <int64>` — Идентификаторы пропусков.

**Пример ответа (`200`):**

```json
{
  "arrival_pass_ids": [
    6000123456
  ]
}
```


---

## Обновить пропуск

`POST /v1/carriage/pass/update`

**Тело запроса** (`application/json`):
- **arrival_passes** `Array of objects` *обязательный* — Список пропусков.
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "carriage_id": 5000123456,
  "arrival_passes": [
    {
      "id": 6000123456,
      "driver_name": "Иванов Иван Иван \"driver_phone\": \"+79991234567",
      "vehicle_license_plate": "А123БВ \"vehicle_model\": \"ГАЗель NEXT",
      "with_returns": true
    }
  ]
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

## Удалить пропуск

`POST /v1/carriage/pass/delete`

**Тело запроса** (`application/json`):
- **arrival_pass_ids** `Array of strings <int64>` *обязательный* — Идентификаторы пропусков.
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "carriage_id": 5000123456,
  "arrival_pass_ids": [
    6000123456,
    6000123457
  ]
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

## Создать пропуск для возврата

`POST /v1/return/pass/create`

**Тело запроса** (`application/json`):
- **arrival_passes** `Array of objects` *обязательный* — Список пропусков.

**Пример запроса:**

```json
{
  "arrival_passes": [
    {
      "arrival_time": "2026-03-17T10:0 \"driver_name\": ",
      "driver_phone": "+79991234567",
      "dropoff_point_id": 7000123456,
      "vehicle_license_plate": "А123БВ \"vehicle_model\": \"ГАЗель NEXT",
      "warehouse_id": 3000007863
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Пропуск создан |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **arrival_pass_ids** `Array of strings <int64>` — Идентификаторы пропусков.

**Пример ответа (`200`):**

```json
{
  "arrival_pass_ids": [
    6000123456
  ]
}
```


---

## Обновить пропуск для возврата

`POST /v1/return/pass/update`

**Тело запроса** (`application/json`):
- **arrival_passes** `Array of objects` *обязательный* — Список пропусков.

**Пример запроса:**

```json
{
  "arrival_passes": [
    {
      "arrival_pass_id": 6000123456,
      "arrival_time": "2026-03-17T14:3 \"driver_name\": ",
      "driver_phone": "+79991234567",
      "vehicle_license_plate": "А123БВ \"vehicle_model\": \"ГАЗель NEXT\" }"
    }
  ]
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

## Удалить пропуск для возврата

`POST /v1/return/pass/delete`

**Тело запроса** (`application/json`):
- **arrival_pass_ids** `Array of strings <int64>` *обязательный* — Идентификаторы пропусков.

**Пример запроса:**

```json
{
  "arrival_pass_ids": [
    6000123456,
    6000123457
  ]
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
