# Отправления

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 624. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Отменить отправление из заказа

`POST /v1/posting/cancel`

Отменяет отправление из заказа. Используйте идентификатор причины отмены reasons.id из метода /v1/cancel-reason/list-by- posting.

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Номер отправления.
- **reason_id** `integer <int32>` *обязательный* — Идентификатор причины отмены.
- **reason_message** `string` — Дополнительная информация по отмене.

**Пример запроса:**

```json
{
  "posting_number": "string",
  "reason_id": 0,
  "reason_message": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Сообщение со статусом отмены |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **message** `string` — Текст сообщения.

**Пример ответа (`200`):**

```json
{
  "message": "string"
}
```


---

## Проверить статус отмены отправления

`POST /v1/posting/cancel/status`

**Тело запроса** (`application/json`):
- **posting_number** `string` — Идентификатор отправления.

**Пример запроса:**

```json
{
  "posting_number": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус отмены отправления |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **order_number** `string` — Номер заказа.
- **posting_number** `Array of strings` — Идентификатор отправления.
- **state** `string` — Статус отмены отправления: Подтверждена , На подтверждении , Отклонена , Ожидает обработки .

**Пример ответа (`200`):**

```json
{
  "order_number": "string",
  "posting_number": [
    "string"
  ],
  "state": "string"
}
```


---

## Получить маркировки экземпляров из отправления

`POST /v1/posting/marks`

Возвращает статусы выдачи экземпляров и коды маркировки «Честный ЗНАК» для каждого отправления. Укажите в чеке и выведите из оборота маркировки экземпляров из параметра issued_exemplars в ответе.

**Тело запроса** (`application/json`):
- **posting_numbers** `Array of strings` — Идентификаторы отправлений.

**Пример запроса:**

```json
{
  "posting_numbers": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список экземпляров отправления с маркировками |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **invalid_postings** `Array of strings` — Список неверных идентификаторов отправлений.
- **issued_exemplars** `Array of objects` — Список выданных покупателям экземпляров товаров.
- **non_issued_exemplars** `Array of objects` — Список не выданных покупателям экземпляров товаров.

**Пример ответа (`200`):**

```json
{
  "invalid_postings": [
    "string"
  ],
  "issued_exemplars": [
    {
      "exemplar_id": 0,
      "mandatory_marks": [
        "string"
      ],
      "posting_number": "string",
      "sku": 0
    }
  ],
  "non_issued_exemplars": [
    {
      "exemplar_id": 0,
      "posting_number": "string",
      "sku": 0
    }
  ]
}
```


---
