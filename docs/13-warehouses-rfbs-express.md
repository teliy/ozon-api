# Создание складов rFBS Express и управление ими

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 167. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Создать склад с методом доставки «Партнёры Ozon»

## Создать склад с методом доставки «Партнёры Ozon»

`POST /v1/warehouse/erfbs/aggregator/create`

Подробнее о схеме realFBS Express

**Тело запроса** (`application/json`):
- **address_coordinates** `object` *обязательный* — Координаты адреса склада.
- **is_auto_assembly** `boolean` — true , если на складе доступна автосборка.
- **delivery_method** `object` *обязательный* — Информация о методе доставки «Партнёры Ozon».
- **min_order_value** `integer <int64>` — Минимальная стоимость заказа.
- **name** `string` *обязательный* — Название склада.
- **phone** `string+7(XXX)XXX-XX-XX` *обязательный* — Номер телефона склада.
- **timetable_warehouse** `object` *обязательный* — Расписание работы склада.

**Пример запроса:**

```json
{
  "address_coordinates": {
    "latitude": 0,
    "longitude": 0
  },
  "is_auto_assembly": false,
  "delivery_method": {
    "courier_comment": "string",
    "is_courier_phone_same_as_warehouse": "courier_phones",
    "string\" ], \"cut_in": 15,
    "deliver_to_pvz": true,
    "delivery_costs": {
      "min_weight": 0,
      "max_weight": 0,
      "min_order_price": 0,
      "max_order_price": 0,
      "seller_payment": 0
    },
    "name": "string",
    "return_settings": {
      "contact_days": 0,
      "post_office_zipcode": "string",
      "return_method": "UNSPECIFIED",
      "return_point_id": 0,
      "transport_company_name": "strin"
    }
  },
  "min_order_value": 0,
  "name": "string",
  "phone": "string",
  "timetable_warehouse": {
    "holidays": [
      {
        "day": "string",
        "from": "string",
        "to": "string"
      }
    ],
    "working_days": [
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      }
    ]
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад создан |
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

## Обновить склад

`POST /v1/warehouse/erfbs/update`

Подробнее о схеме realFBS Express

**Тело запроса** (`application/json`):
- **is_auto_assembly** `boolean` — true , если на складе доступна автосборка.
- **min_order_value** `integer <int64>` — Минимальная стоимость заказа.
- **name** `string` — Название склада.
- **phone** `string+7(XXX)XXX-XX-XX` — Номер телефона склада.
- **timetable_warehouse** `object` — Расписание работы склада.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "is_auto_assembly": false,
  "min_order_value": 0,
  "name": "string",
  "phone": "string",
  "timetable_warehouse": {
    "holidays": [
      {
        "day": "string",
        "from": "string",
        "to": "string"
      }
    ],
    "working_days": [
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      },
      {
        "day": "UNSPECIFIED",
        "from": "string",
        "to": "string"
      }
    ]
  },
  "warehouse_id": 0
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

## Обновить метод доставки «Партнёры Ozon»

`POST /v1/warehouse/erfbs/aggregator/delivery-method/update`

Подробнее о схеме rFBS Express

**Тело запроса** (`application/json`):
- **courier_comment** `string` — Комментарий для курьера.
- **is_courier_phone_same_as_warehouse** `boolean` — true , если номер телефона курьера совпадает с номером телефона склада. Если is_courier_phone_same_as_warehous e = true , текущий номер телефона будет указан в courier_phones .
- **courier_phones** `Array of strings` — Номера телефонов для связи с курьером.
- **cut_in** `integer <int64>` — Время сборки.
- **deliver_to_pvz** `boolean` — true , если доставка Ozon Express в пункт выдачи Ozon.
- **delivery_costs** `object` — Расходы на доставку, которые вы готовы оплатить.
- **delivery_method_id** `integer <int64>` *обязательный* — Идентификатор метода доставки.
- **name** `string` — Название метода доставки.
- **return_settings** `object` — Настройки возвратов от покупателей.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "courier_comment": "string",
  "is_courier_phone_same_as_warehouse": "t",
  "courier_phones": [
    "string"
  ],
  "cut_in": 15,
  "deliver_to_pvz": true,
  "delivery_costs": {
    "min_weight": 0,
    "max_weight": 0,
    "min_order_price": 0,
    "max_order_price": 0,
    "seller_payment": 0
  },
  "delivery_method_id": 0,
  "name": "string",
  "return_settings": {
    "contact_days": 0,
    "post_office_zipcode": "string",
    "return_method": "COURIER",
    "return_point_id": 0,
    "transport_company_name": "string"
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
- **operation_id** `string` — Идентификатор операции. Получите статус операции методом /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---

## Создать склад с методом доставки «Вы или сторонняя служба»

`POST /v1/warehouse/erfbs/non-integrated/create`

Подробнее о схеме realFBS Express

**Тело запроса** (`application/json`):
- **address_coordinates** `object` *обязательный* — Координаты адреса склада.
- **is_auto_assembly** `boolean` — true , если на складе доступна автосборка.
- **delivery_method** `object` *обязательный* — Информация о методе доставки «Вы или сторонняя служба».
- **min_order_value** `integer <int64>` — Минимальная стоимость заказа в рублях.
- **name** `string` *обязательный* — Название склада.
- **phone** `string+7(XXX)XXX-XX-XX` *обязательный* — Номер телефона склада.
- **timetable_warehouse** `object` *обязательный* — Расписание работы склада.

**Пример запроса:**

```json
{
  "address_coordinates": {
    "latitude": 0,
    "longitude": 0
  },
  "is_auto_assembly": false,
  "delivery_method": {
    "courier_cutoff": 5,
    "cut_in": 15,
    "delivery_polygons": [
      {
        "id": 0,
        "time": 15
      }
    ],
    "name": "string",
    "return_settings": {
      "contact_days": 0,
      "post_office_zipcode": "string",
      "return_method": "COURIER",
      "transport_company_name": "strin"
    }
  },
  "min_order_value": 0,
  "name": "string",
  "phone": "string",
  "timetable_warehouse": {
    "holidays": [
      {
        "day": "string",
        "from": "string",
        "to": "string"
      }
    ],
    "working_days": [
      {
        "day": "MONDAY",
        "from": "string",
        "to": "string"
      },
      {
        "day": "MONDAY",
        "from": "string",
        "to": "string"
      },
      {
        "day": "MONDAY",
        "from": "string",
        "to": "string"
      },
      {
        "day": "MONDAY",
        "from": "string",
        "to": "string"
      },
      {
        "day": "MONDAY",
        "from": "string",
        "to": "string"
      }
    ]
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад создан |
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

## Обновить метод доставки «Вы или сторонняя служба»

`POST /v1/warehouse/erfbs/non-integrated/delivery-method/update`

Подробнее о схеме rFBS Express

**Тело запроса** (`application/json`):
- **courier_cutoff** `integer <int64>` *обязательный* — Скорость отгрузки.
- **cut_in** `integer <int64>` *обязательный* — Время сборки.
- **delivery_method_id** `integer <int64>` *обязательный* — Идентификатор метода доставки.
- **name** `string` *обязательный* — Название метода доставки.
- **return_settings** `object` *обязательный* — Настройки возвратов от покупателей.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "courier_cutoff": 5,
  "cut_in": 15,
  "delivery_method_id": 0,
  "name": "string",
  "return_settings": {
    "contact_days": 0,
    "post_office_zipcode": "string",
    "return_method": "COURIER",
    "transport_company_name": "string"
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
- **operation_id** `string` — Идентификатор операции. Получите статус операции методом /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---

## Поставить rFBS-склад на паузу

`POST /v1/warehouse/rfbs/pause`

Скрывает товары склада с витрины. Изменять сток не нужно.

**Тело запроса** (`application/json`):
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример запроса:**

```json
{
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад на паузе |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции. Получите статус операции методом /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---

## Снять rFBS-склад с паузы

`POST /v1/warehouse/rfbs/unpause`

Возвращает товары склада на витрину.

**Тело запроса** (`application/json`):
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример запроса:**

```json
{
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Склад снят с паузы |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **operation_id** `string` — Идентификатор операции. Получите статус операции методом /v1/warehouse/operation/status.

**Пример ответа (`200`):**

```json
{
  "operation_id": "string"
}
```


---
