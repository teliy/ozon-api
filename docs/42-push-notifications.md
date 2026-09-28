# Работа с пуш-уведомлениями

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 505. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

### Подключить URL-адрес для уведомлений

## Подключить URL-адрес для уведомлений

`POST /v1/notification/set`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **types** `Array of strings` *обязательный* — Типы уведомлений: TYPE_NEW_MESSAGE — новое сообщение в чате; TYPE_UPDATE_MESSAGE — изменение сообщения в чате; TYPE_MESSAGE_READ — ваше сообщение прочитано покупателем или поддержкой; TYPE_CHAT_CLOSED — чат закрыт; TYPE_NEW_POSTING — новое отправление; TYPE_POSTING_CANCELLED — отмена отправления; TYPE_STATE_CHANGED — изменение статуса отправления; TYPE_DELIVERY_DATE_CHANGED — изменение даты доставки отправления; TYPE_CUTOFF_DATE_CHANGED — изменение даты отгрузки отправления; TYPE_CREATE_ITEM — создание товара или ошибка при его создании; TYPE_UPDATE_ITEM — обновление товара или ошибка при обновлении; TYPE_CREATE_OR_UPDATE_ITEM — создание и обновление товара или ошибка в процессе; TYPE_STOCKS_CHANGED — изменение остатков на складах продавца; TYPE_FBO_POSTING_NEW — новое отправление FBO; TYPE_FBO_POSTING_CANCELLED — отмена отправления FBO; TYPE_FBO_POSTING_STATE_CHANGED — изменение статуса отправления FBO; TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED — изменение даты доставки отправления FBO; TYPE_FBO_STOCKS_CHANGED — изменение остатков на складах Ozon; TYPE_ORDER_NEW — новый заказ; TYPE_ORDER_CANCELLED — отмена заказа; TYPE_ORDER_STATE_CHANGED — изменение статуса заказа.. Enum: `"TYPE_NEW_MESSAGE"`, `"TYPE_UPDATE_MESSAGE"`, `"TYPE_MESSAGE_READ"`, `"TYPE_CHAT_CLOSED"`, `"TYPE_NEW_POSTING"`, `"TYPE_POSTING_CANCELLED"`, `"TYPE_STATE_CHANGED"`, `"TYPE_DELIVERY_DATE_CHANGED"`, `"TYPE_CUTOFF_DATE_CHANGED"`, `"TYPE_CREATE_ITEM"`, `"TYPE_UPDATE_ITEM"`, `"TYPE_CREATE_OR_UPDATE_ITEM"`, `"TYPE_STOCKS_CHANGED"`, `"TYPE_FBO_POSTING_NEW"`, `"TYPE_FBO_POSTING_CANCELLED"`, `"TYPE_FBO_POSTING_STATE_CHANGED"`, `"TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED"`, `"TYPE_FBO_STOCKS_CHANGED"`, `"TYPE_ORDER_NEW"`, `"TYPE_ORDER_CANCELLED"`, `"TYPE_ORDER_STATE_CHANGED"`.
- **url** `string` *обязательный* — URL-адрес.

**Пример запроса:**

```json
{
  "types": [
    "TYPE_NEW_MESSAGE"
  ],
  "url": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`400`):**

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

## Изменить URL-адрес для уведомлений

`POST /v1/notification/update`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Идентификатор URL-адреса.
- **types** `Array of strings` — Типы уведомлений: TYPE_NEW_MESSAGE — новое сообщение в чате; TYPE_UPDATE_MESSAGE — изменение сообщения в чате; TYPE_MESSAGE_READ — ваше сообщение прочитано покупателем или поддержкой; TYPE_CHAT_CLOSED — чат закрыт; TYPE_NEW_POSTING — новое отправление; TYPE_POSTING_CANCELLED — отмена отправления; TYPE_STATE_CHANGED — изменение статуса отправления; TYPE_DELIVERY_DATE_CHANGED — изменение даты доставки отправления; TYPE_CUTOFF_DATE_CHANGED — изменение даты отгрузки отправления; TYPE_CREATE_ITEM — создание товара или ошибка при его создании; TYPE_UPDATE_ITEM — обновление товара или ошибка при обновлении; TYPE_CREATE_OR_UPDATE_ITEM — создание и обновление товара или ошибка в процессе; TYPE_STOCKS_CHANGED — изменение остатков на складах продавца; TYPE_FBO_POSTING_NEW — новое отправление FBO; TYPE_FBO_POSTING_CANCELLED — отмена отправления FBO; TYPE_FBO_POSTING_STATE_CHANGED — изменение статуса отправления FBO; TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED — изменение даты доставки отправления FBO; TYPE_FBO_STOCKS_CHANGED — изменение остатков на складах Ozon; TYPE_ORDER_NEW — новый заказ; TYPE_ORDER_CANCELLED — отмена заказа; TYPE_ORDER_STATE_CHANGED — изменение статуса заказа.. Enum: `"TYPE_NEW_MESSAGE"`, `"TYPE_UPDATE_MESSAGE"`, `"TYPE_MESSAGE_READ"`, `"TYPE_CHAT_CLOSED"`, `"TYPE_NEW_POSTING"`, `"TYPE_POSTING_CANCELLED"`, `"TYPE_STATE_CHANGED"`, `"TYPE_DELIVERY_DATE_CHANGED"`, `"TYPE_CUTOFF_DATE_CHANGED"`, `"TYPE_CREATE_ITEM"`, `"TYPE_UPDATE_ITEM"`, `"TYPE_CREATE_OR_UPDATE_ITEM"`, `"TYPE_STOCKS_CHANGED"`, `"TYPE_FBO_POSTING_NEW"`, `"TYPE_FBO_POSTING_CANCELLED"`, `"TYPE_FBO_POSTING_STATE_CHANGED"`, `"TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED"`, `"TYPE_FBO_STOCKS_CHANGED"`, `"TYPE_ORDER_NEW"`, `"TYPE_ORDER_CANCELLED"`, `"TYPE_ORDER_STATE_CHANGED"`.
- **url** `string` — Новый URL-адрес.

**Пример запроса:**

```json
{
  "id": 0,
  "types": [
    "TYPE_NEW_MESSAGE"
  ],
  "url": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`400`):**

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

## Удалить URL-адрес для уведомлений

`POST /v1/notification/delete`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Идентификатор URL-адреса.

**Пример запроса:**

```json
{
  "id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`400`):**

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

## Проверить URL-адрес для уведомлений

`POST /v1/notification/check`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **url** `string` *обязательный* — URL-адрес.

**Пример запроса:**

```json
{
  "url": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Результат проверки |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **errors** `Array of objects` — Ошибки, возникшие при проверке.
- **is_active** `boolean` *обязательный* — true , если URL-адрес активен.

**Пример ответа (`200`):**

```json
{
  "errors": [
    {
      "description": "string",
      "type": "REQUEST_ERROR"
    }
  ],
  "is_active": true
}
```


---

## Включить или выключить уведомления на URL-адрес

`POST /v1/notification/enable`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **enabled** `boolean` *обязательный* — Передайте: true — чтобы включить уведомления; false — чтобы выключить уведомления.
- **id** `integer <int64>` *обязательный* — Идентификатор URL-адреса.

**Пример запроса:**

```json
{
  "enabled": true,
  "id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`400`):**

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

## Получить информацию по подключённым URL-адресам

`POST /v1/notification/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **availability_statuses** `Array of strings` — Информация о доступности URL-адресов: GREEN — активен; YELLOW — нестабилен; RED — недоступен.. Enum: `"GREEN"`, `"YELLOW"`, `"RED"`.
- **limit** `integer <uint64>` — Количество элементов в ответе.
- **offset** `integer <uint64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию; DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "availability_statuses": [
    "GREEN"
  ],
  "limit": 100,
  "offset": 0,
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Подключённые URL-адреса |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **availability_status_thresholds** `Array of objects` *обязательный* — Информация о пороговых значениях статусов доступности URL-адресов.
- **total_count** `integer <int64>` *обязательный* — Общее количество подключённых URL- адресов.
- **urls** `Array of objects` *обязательный* — Подключённые URL-адреса.

**Пример ответа (`200`):**

```json
{
  "availability_status_thresholds": [
    {
      "status": "string",
      "threshold": 0
    }
  ],
  "total_count": 0,
  "urls": [
    {
      "availability_status": "string",
      "availability_status_date": "201 ",
      "created_at": "2019-08-24T14:15: \"disable_reason\": \"string",
      "enable": true,
      "id": 0,
      "problematic_type": "string",
      "reason_details": "string",
      "types": [
        {
          "description": "string",
          "type": "TYPE_NEW_MESSAGE"
        }
      ],
      "url": "string"
    }
  ]
}
```


---

## Получить типы пуш-уведомлений

`POST /v1/notification/push-type/list`

Вы можете оставить обратную связь о работе метода в комментариях в сообществе разработчиков Ozon for dev.

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Типы пуш-уведомлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **types** `Array of objects` *обязательный* — Типы пуш-уведомлений.
  - **description** `string` *обязательный* — Описание.
  - **seller_endpoint** `object` — URL-адрес, на который приходит тип уведомлений.
  - **type** `string` *обязательный* — Тип уведомления: TYPE_NEW_MESSAGE — новое сообщение в чате; TYPE_UPDATE_MESSAGE — изменение сообщения в чате; TYPE_MESSAGE_READ — ваше сообщение прочитано покупателем или поддержкой; TYPE_CHAT_CLOSED — чат закрыт; TYPE_NEW_POSTING — новое отправление; TYPE_POSTING_CANCELLED — отмена отправления; TYPE_STATE_CHANGED — изменение статуса отправления; TYPE_DELIVERY_DATE_CHANGED — изменение даты доставки отправления; TYPE_CUTOFF_DATE_CHANGED — изменение даты отгрузки отправления; TYPE_CREATE_ITEM — создание товара или ошибка при его создании; TYPE_UPDATE_ITEM — обновление товара или ошибка при обновлении; TYPE_CREATE_OR_UPDATE_ITEM — создание и обновление товара или ошибка в процессе; TYPE_STOCKS_CHANGED — изменение остатков на складах продавца; TYPE_FBO_POSTING_NEW — новое отправление FBO; TYPE_FBO_POSTING_CANCELLED — отмена отправления FBO; TYPE_FBO_POSTING_STATE_CHANGED — изменение статуса отправления FBO; TYPE_FBO_POSTING_DELIVERY_DATE_CHAN GED — изменение даты доставки отправления FBO; TYPE_FBO_STOCKS_CHANGED — изменение остатков на складах Ozon; TYPE_ORDER_NEW — новый заказ; TYPE_ORDER_CANCELLED — отмена заказа; TYPE_ORDER_STATE_CHANGED — изменение статуса заказа.. Enum: `"TYPE_NEW_MESSAGE"`, `"TYPE_UPDATE_MESSAGE"`, `"TYPE_MESSAGE_READ"`, `"TYPE_CHAT_CLOSED"`, `"TYPE_NEW_POSTING"`, `"TYPE_POSTING_CANCELLED"`, `"TYPE_STATE_CHANGED"`, `"TYPE_DELIVERY_DATE_CHANGED"`, `"TYPE_CUTOFF_DATE_CHANGED"`, `"TYPE_CREATE_ITEM"`, `"TYPE_UPDATE_ITEM"`, `"TYPE_CREATE_OR_UPDATE_ITEM"`, `"TYPE_STOCKS_CHANGED"`, `"TYPE_FBO_POSTING_NEW"`, `"TYPE_FBO_POSTING_CANCELLED"`, `"TYPE_FBO_POSTING_STATE_CHANGED"`, `"TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED"`, `"TYPE_FBO_STOCKS_CHANGED"`, `"TYPE_ORDER_NEW"`, `"TYPE_ORDER_CANCELLED"`, `"TYPE_ORDER_STATE_CHANGED"`.

**Пример ответа (`200`):**

```json
{
  "types": [
    {
      "description": "string",
      "seller_endpoint": {
        "id": 0,
        "url": "string"
      },
      "type": "TYPE_NEW_MESSAGE"
    }
  ]
}
```


---
