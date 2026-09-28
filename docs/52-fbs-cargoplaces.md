# Работа с грузоместами FBS

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 579. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

Методы в этом разделе работают только для доверительной приёмки грузовых мест.

Подробнее о доверительной приёмке грузового места в Базе знаний продавца

## Создать грузоместо

`POST /v1/carriage/container/create`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **cargo_type** `string` *обязательный* — Тип грузоместа: box — коробка; pallet — палета.
- **containers_count** `integer <int32>` *обязательный* — Количество грузомест.
- **sort_type** `string` *обязательный* — Тип сортировки: sort — сортируемый; non-sort — несортируемый.
- **warehouse_id** `integer <int64>` *обязательный* — Идентификатор склада.

**Пример запроса:**

```json
{
  "cargo_type": "string",
  "containers_count": 1,
  "sort_type": "string",
  "warehouse_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Грузоместо создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **container_ids** `Array of strings <int64>` — Идентификаторы грузомест.

**Пример ответа (`200`):**

```json
{
  "container_ids": [
    "string"
  ]
}
```


---

## Наполнить грузоместо отправлениями

`POST /v1/carriage/container/fill`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_id** `integer <int64>` *обязательный* — Идентификатор грузоместа.
- **posting_numbers** `Array of strings` *обязательный* — Номера отправлений.

**Пример запроса:**

```json
{
  "container_id": 0,
  "posting_numbers": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_postings** `Array of objects` — Ошибки по отправлениям.
- **task_id** `integer <int64>` — Идентификатор задания.

**Пример ответа (`200`):**

```json
{
  "error_postings": [
    {
      "error_message": "string",
      "posting_number": "string"
    }
  ],
  "task_id": 0
}
```


---

## Подтвердить состав грузоместа

`POST /v1/carriage/container/approve`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_ids** `Array of strings <int64>` *обязательный* — Идентификаторы грузомест.

**Пример запроса:**

```json
{
  "container_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Состав подтверждён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_containers** `Array of objects` — Ошибки по грузоместам.
- **task_id** `integer <int64>` — Идентификатор задания.

**Пример ответа (`200`):**

```json
{
  "error_containers": [
    {
      "container_id": 0,
      "error_message": "string"
    }
  ],
  "task_id": 0
}
```


---

## Разместить коробки на палете

`POST /v1/carriage/container/place-into`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **child_container_ids** `Array of strings <int64>` *обязательный* — Идентификаторы грузомест.
- **parent_container_id** `integer <int64>` *обязательный* — Идентификатор родительского грузоместа — палеты.

**Пример запроса:**

```json
{
  "child_container_ids": [
    "string"
  ],
  "parent_container_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_containers** `Array of objects` — Ошибки по грузоместам.
- **task_id** `integer <int64>` — Идентификатор задания.

**Пример ответа (`200`):**

```json
{
  "error_containers": [
    {
      "container_id": 0,
      "error_message": "string"
    }
  ],
  "task_id": 0
}
```


---

## Убрать отправления из грузоместа

`POST /v1/carriage/container/remove-postings`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_id** `integer <int64>` *обязательный* — Идентификатор грузоместа.
- **posting_numbers** `Array of strings` *обязательный* — Номера отправлений.

**Пример запроса:**

```json
{
  "container_id": 0,
  "posting_numbers": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_postings** `Array of objects` — Ошибки по отправлениям.
- **task_id** `integer <int64>` — Идентификатор задания.

**Пример ответа (`200`):**

```json
{
  "error_postings": [
    {
      "error_message": "string",
      "posting_number": "string"
    }
  ],
  "task_id": 0
}
```


---

## Убрать коробки с палеты

`POST /v1/carriage/container/remove-from`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **child_container_ids** `Array of strings <int64>` *обязательный* — Идентификаторы грузомест.
- **parent_container_id** `integer <int64>` *обязательный* — Идентификатор родительского грузоместа — палеты.

**Пример запроса:**

```json
{
  "child_container_ids": [
    "string"
  ],
  "parent_container_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_containers** `Array of objects` — Ошибки по грузоместам.
- **task_id** `integer <int64>` — Идентификатор задания.

**Пример ответа (`200`):**

```json
{
  "error_containers": [
    {
      "container_id": 0,
      "error_message": "string"
    }
  ],
  "task_id": 0
}
```


---

## Отменить грузоместо

`POST /v1/carriage/container/cancel`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_ids** `Array of strings <int64>` *обязательный* — Идентификаторы грузомест.

**Пример запроса:**

```json
{
  "container_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Задание создано |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_containers** `Array of objects` — Ошибки по грузоместам.
- **task_id** `integer <int64>` — Идентификатор задания.

**Пример ответа (`200`):**

```json
{
  "error_containers": [
    {
      "container_id": 0,
      "error_message": "string"
    }
  ],
  "task_id": 0
}
```


---

## Получить список грузомест

`POST /v1/carriage/container/list`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр.
- **limit** `integer <int64>` — Количество значений в ответе. Значение по умолчанию — 100.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "cargo_type": "string",
    "created_from": "2019-08-24T14:15:22 ",
    "created_to": "2019-08-24T14:15:22Z",
    "sort_type": "string",
    "statuses": [
      "string"
    ],
    "warehouse_id": 0
  },
  "limit": 1,
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список грузомест |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **containers** `Array of objects` — Информация о грузоместах.
- **cursor** `string` — Указатель для выборки следующих данных. Если параметр пустой, данных больше нет.

**Пример ответа (`200`):**

```json
{
  "containers": [
    {
      "available_actions": [
        "string"
      ],
      "cargo_type": "string",
      "container_id": 0,
      "container_number": 0,
      "count_of_postings": 0,
      "created_at": "2019-08-24T14:15: \"related_containers\": [ ]",
      "sort_type": "string",
      "status": "string",
      "warehouse_date": "string",
      "warehouse_id": 0,
      "warehouse_name": "string",
      "weight": 0
    }
  ],
  "cursor": "string"
}
```


---

## Получить информацию о грузоместах

`POST /v1/carriage/container/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_id** `integer <int64>` *обязательный* — Идентификатор грузоместа.

**Пример запроса:**

```json
{
  "container_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о грузоместах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **available_actions** `Array of strings` — Действия с грузоместом: approve — подтвердить состав; get_label_container — получить этикетку; delete — удалить; place_box_into_pallet — добавить коробку на палету; remove_box_from_pallet — убрать коробку с палеты; place_posting_into_container — перенести отправление в другое грузоместо; remove_posting_from_container — убрать отправление из грузоместа; get_documents — получить транспортную накладную.
- **cargo_type** `string` — Тип грузоместа.
- **container_id** `integer <int64>` — Идентификатор грузоместа.
- **container_number** `integer <int32>` — Порядковый номер грузоместа.
- **count_of_postings** `integer <int32>` — Количество отправлений в грузоместе.
- **created_at** `string <date-time>` — Дата создания грузоместа в UTC.
- **parent_container_id** `integer <int64>` — Идентификатор родительского грузоместа.
- **postings** `Array of objects` — Список отправлений.
- **related_container_ids** `Array of strings <int64>` — Идентификаторы дочерних грузомест.
- **sort_type** `string` — Тип сортировки грузоместа: sort — сортируемый; non-sort — несортируемый.
- **status** `string` — Статус грузоместа.
- **warehouse_date** `string` — Дата создания грузоместа в часовом поясе склада.
- **warehouse_id** `integer <int64>` — Идентификатор склада продавца.
- **warehouse_name** `string` — Название склада.
- **weight** `number <float>` — Суммарный вес отправлений в грузоместе, кг.

**Пример ответа (`200`):**

```json
{
  "available_actions": [
    "string"
  ],
  "cargo_type": "string",
  "container_id": 0,
  "container_number": 0,
  "count_of_postings": 0,
  "created_at": "2019-08-24T14:15:22Z",
  "parent_container_id": 0,
  "postings": [
    {
      "available_actions": [
        "string"
      ],
      "in_process_at": "2019-08-24T14: \"posting_number\": \"string",
      "products": [
        {
          "sku": 0,
          "name": "string",
          "offer_id": "string",
          "quantity": 0,
          "picture_url": "string",
          "product_color": "string",
          "product_size_manufacture \"product_size_russian": ""
        }
      ],
      "sort_type": "string",
      "weight": 0
    }
  ],
  "related_container_ids": [
    "string"
  ],
  "sort_type": "string",
  "status": "string",
  "warehouse_date": "string",
  "warehouse_id": 0,
  "warehouse_name": "string",
  "weight": 0
}
```


---

## Получить статус грузомест FBS

`POST /v1/carriage/container/status/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_ids** `Array of strings <int64>` *обязательный* — Идентификаторы грузомест.

**Пример запроса:**

```json
{
  "container_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус грузомест |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **containers** `Array of objects` — Список грузомест.
  - **container_id** `integer <int64>` — Идентификатор грузоместа.
  - **status** `string` — Статус грузоместа.

**Пример ответа (`200`):**

```json
{
  "containers": [
    {
      "container_id": 0,
      "status": "string"
    }
  ]
}
```


---

## Получить статус задачи грузового места

`POST /v1/carriage/container/task/info`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **task_id** `integer <int64>` — Идентификатор задачи. Получите его в ответе метода /v1/carriage/container/fill или /v1/carriage/container/approve.

**Пример запроса:**

```json
{
  "task_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус задачи |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **error_message** `string` — Текст ошибки.
- **status** `string` — Статус выполнения задачи: pending — в ожидании; in_progress — в процессе; completed — выполнено; failed — ошибка при выполнении;

**Пример ответа (`200`):**

```json
{
  "error_message": "string",
  "status": "string"
}
```


---

## Получить документы по грузоместам — ТрН и лист отгрузки

`POST /v1/carriage/container/document/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_ids** `Array of strings <int64>` *обязательный* — Идентификаторы грузомест.

**Пример запроса:**

```json
{
  "container_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список документов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **content_type** `string` — Тип файла: application или pdf.
- **file_content** `string <byte>` — Содержание файла в бинарном виде.
- **file_name** `string` — Название файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "string",
  "file_content": "string",
  "file_name": "string"
}
```


---

## Получить этикетку по грузоместам

`POST /v1/carriage/container/label/get`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **container_ids** `Array of strings <int64>` — Идентификаторы грузомест.

**Пример запроса:**

```json
{
  "container_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список этикеток |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **content** `object` — Информация о сформированной этикетке.
- **error_containers** `Array of objects` — Ошибки грузомест, по которым не удалось сформировать этикетку.

**Пример ответа (`200`):**

```json
{
  "content": {
    "content_type": "string",
    "file_content": "string",
    "file_name": "string"
  },
  "error_containers": [
    {
      "container_id": 0,
      "error_message": "string"
    }
  ]
}
```


---
