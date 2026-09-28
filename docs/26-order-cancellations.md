# Отмены заказов

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 366. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Получить список заявок на отмену rFBS

`POST /v2/conditional-cancellation/list`

Метод для получения списка заявок на отмену rFBS-заказов.

**Тело запроса** (`application/json`):
- **filters** `object` — Фильтры.
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. Оставьте это поле пустым при выполнении первого запроса. Чтобы получить следующие значения, укажите last_id из ответа предыдущего запроса.
- **limit** `integer <int32>` *обязательный* — Количество заявок в ответе.
- **with** `object` — Дополнительная информация.

**Пример запроса:**

```json
{
  "filters": {
    "cancellation_initiator": [
      "CLIENT"
    ],
    "posting_number": [
      "34009011-0094-1"
    ],
    "state": "ALL"
  },
  "limit": 500,
  "last_id": 0,
  "with": {
    "counter": true
  }
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список заявок на отмену |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **counter** `integer <int64>` — Cчётчик заявок в статусе ON_APPROVAL .
- **last_id** `integer <int64>` — Идентификатор последнего значения на странице. Чтобы получить следующие значения, передайте полученное значение в следующем запросе в параметре last_id .
- **result** `Array of objects` — Информация о заявках на отмену.
  - **approve_comment** `string` — Комментарий, оставленный при подтверждении или отклонении заявки на отмену.
  - **approve_date** `string <date-time>` — Дата подтверждения или отклонения заявки на отмену.
  - **auto_approve_date** `string <date-time>` — Дата, после которой заявка будет автоматически подтверждена.
  - **cancellation_id** `integer <int64>` — Идентификатор заявки на отмену.
  - **cancellation_initiator** `string` — Инициатор отмены: SELLER — продавец, CLIENT — покупатель, OZON — Ozon, SYSTEM — система, DELIVERY — служба доставки.. Enum: `"OZON"`, `"SELLER"`, `"CLIENT"`, `"SYSTEM"`, `"DELIVERY"`.
  - **cancellation_reason** `object` — Причина отмены.
  - **cancellation_reason_message** `string` — Комментарий к заявке на отмену, введённый инициатором отмены вручную.
  - **cancelled_at** `string <date-time>` — Дата создания заявки на отмену.
  - **order_date** `string <date-time>` — Дата создания заказа.
  - **posting_number** `string` — Номер отправления.
  - **source_id** `integer <int64>` — Предыдущий идентификатор заявки на отмену. Используется для поддержания обратной совместимости.
  - **state** `object` — Статус заявки на отмену.
  - **tpl_integration_type** `string` — Тип интеграции со службой доставки.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "approve_comment": "string",
      "approve_date": "2024-11-27T12:3 \"auto_approve_date\": ",
      "cancellation_id": 0,
      "cancellation_initiator": "OZON",
      "cancellation_reason": {
        "id": 0,
        "name": "string"
      },
      "cancellation_reason_message": " ",
      "cancelled_at": "2024-11-27T12:3 ",
      "order_date": "2024-11-27T12:31: \"posting_number\": \"string",
      "state": {
        "id": 0,
        "name": "string",
        "state": "ALL"
      },
      "tpl_integration_type": "string"
    }
  ],
  "counter": "1",
  "last_id": 283784254
}
```


---

## Подтвердить заявку на отмену rFBS

`POST /v2/conditional-cancellation/approve`

Метод позволяет согласовать заявку на отмену в статусе ON_APPROVAL . Заказ будет отменён, а деньги вернутся покупателю.

**Тело запроса** (`application/json`):
- **cancellation_id** `integer <int64>` *обязательный* — Идентификатор заявки на отмену.
- **comment** `string` — Комментарий.

**Пример запроса:**

```json
{
  "cancellation_id": 0,
  "comment": "string"
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

## Отклонить заявку на отмену rFBS

`POST /v2/conditional-cancellation/reject`

Метод позволяет отклонить заявку на отмену в статусе ON_APPROVAL . В параметре comment опишите причину. Заказ останется в том же статусе, и его нужно будет доставить покупателю.

**Тело запроса** (`application/json`):
- **cancellation_id** `integer <int64>` *обязательный* — Идентификатор заявки на отмену.
- **comment** `string` — Комментарий.

**Пример запроса:**

```json
{
  "cancellation_id": 0,
  "comment": "string"
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
