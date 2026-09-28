# Информация по кабинету продавца

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 28. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Информация о кабинете продавца

`POST /v1/seller/info`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о кабинете продавца |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **company** `object` — Компания.
- **ratings** `Array of objects` — Список рейтингов.
- **subscription** `object` — Подписка.

**Пример ответа (`200`):**

```json
{
  "company": {
    "country": "Россия",
    "currency": "RUB",
    "inn": "7707083893",
    "legal_name": "Общество с ограниченн \"name\": \"ООО 'Ромашка'",
    "ogrn": "1027700132195",
    "ownership_form": "Частная собственн \"tax_system\": \"ОСНО\""
  },
  "ratings": [
    {
      "current_value": {
        "date_from": "2023-01-15T09:0 ",
        "date_to": "2023-12-31T23:59: \"formatted\": \"AA+",
        "status": {
          "danger": false,
          "premium": true,
          "warning": false
        },
        "value": 85
      },
      "name": "Финансовая устойчивость \"past_value\": { ",
      "date_from": "2022-01-01T00:0 ",
      "date_to": "2022-12-31T23:59: \"formatted\": \"A",
      "status": {
        "danger": false,
        "premium": false,
        "warning": true
      },
      "value": 78
    },
    {
      "rating": "Высокий уровень",
      "status": "Активно",
      "value_type": "Количественный"
    }
  ],
  "subscription": {
    "is_premium": true,
    "type": "Профессиональный"
  }
}
```


---

## Информация о подключении Ozon Доставки

`POST /v1/seller/ozon-logistics/info`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о подключении Ozon Доставки |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **available_schemas** `Array of strings` — Тип доступной схемы: UNKNOWN — не определён, FBO , FBS .. Enum: `"UNKNOWN"`, `"FBO"`, `"FBS"`.
- **ozon_logistics_enabled** `boolean` — true , если Ozon Доставка подключена.

**Пример ответа (`200`):**

```json
{
  "available_schemas": [
    "UNKNOWN"
  ],
  "ozon_logistics_enabled": true
}
```


---
