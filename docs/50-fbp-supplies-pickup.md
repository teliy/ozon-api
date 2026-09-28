# Работа с FBP-поставками с доставкой pick-up

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 563. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Отменить pick-up поставку

`POST /v1/fbp/order/pick-up/cancel`

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
| `200` | Статус отмены |
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

## Изменить данные о точке забора

`POST /v1/fbp/order/pick-up/dlv/edit`

Вы можете оставить обратную связь по этому методу в комментариях к обсуждению в сообществе разработчиков Ozon for dev.

**Тело запроса** (`application/json`):
- **pickup_details** `object` *обязательный* — Детали отправителя.
- **row_version** `integer <int64>` *обязательный* — Идентификатор актуальной версии черновика.
- **supply_id** `string` *обязательный* — Идентификатор поставки.

**Пример запроса:**

```json
{
  "pickup_details": {
    "sender_name": "string",
    "sender_phone": "string"
  },
  "row_version": 0,
  "supply_id": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус изменения |
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
