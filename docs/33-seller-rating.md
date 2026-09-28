# Рейтинг продавца

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 415. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

Работая с Ozon, продавцы должны соблюдать требования по качеству обслуживания, срокам доставки и общению с

клиентами. Система рейтингов отражает качество сервиса продавца, а некоторые показатели видны покупателям — это

рейтинг товаров и индекс цен.

Подробнее о системе рейтингов в Базе знаний продавца

### Получить информацию о текущих рейтингах продавца

## Получить информацию о текущих рейтингах продавца

`POST /v1/rating/summary`

Рейтинг продавца по следующим показателям: индекс цен, доставки вовремя, процент отмен, жалобы и другие. Соответствует разделу

**Пример запроса:**

```json
{}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о рейтингах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **groups** `Array of objects` — Список с группами рейтингов.
- **localization_index** `Array of objects` — Данные по индексу локализации. Если за последние 14 дней у вас не было продаж, поля параметра будут пустыми.
- **penalty_score_exceeded** `boolean` — Признак, что баланс штрафных баллов превышен.
- **premium** `boolean` — Признак наличия подписки Premium.
- **premium_plus** `boolean` — Признак наличия подписки Premium Plus.

**Пример ответа (`200`):**

```json
{
  "groups": [
    {
      "group_name": "string",
      "items": [
        {
          "change": {
            "direction": "string",
            "meaning": "string"
          },
          "current_value": 0,
          "name": "string",
          "past_value": 0,
          "rating": "string",
          "rating_direction": "stri \"status\": \"string",
          "value_type": "string"
        }
      ]
    }
  ],
  "localization_index": [
    {
      "calculation_date": "2019-08-24T \"localization_percentage\": 0"
    }
  ],
  "penalty_score_exceeded": true,
  "premium": true,
  "premium_plus": true
}
```


---

## Получить информацию о рейтингах продавца за период

`POST /v1/rating/history`

Информация о рейтингах за заданный период и с фильтром по нужному рейтингу. Соответствует разделу Рейтинги → Рейтинги продавца в личном кабинете.

**Тело запроса** (`application/json`):
- **date_from** `string <date-time>` *обязательный* — Начало периода.
- **date_to** `string <date-time>` *обязательный* — Конец периода.
- **ratings** `Array of strings` *обязательный* — Фильтр по рейтингу. Рейтинги, по которым нужно получить значение за период: rating_on_time — процент заказов, выполненных вовремя за последние 30 дней. rating_review_avg_score_total — средняя оценка всех товаров. rating_ssl — оценка работы по FBO. Учитывает rating_on_time_supply_delivery , rating_on_time_supply_cancellation и rating_order_accuracy . rating_on_time_supply_delivery — процент поставок, которые вы привезли на склад в выбранный временной интервал за последние 60 дней. rating_order_accuracy — процент поставок без излишков, недостач, пересорта и брака за последние 60 дней. rating_on_time_supply_cancellation — процент заявок на поставку, которые завершились или были отменены без опоздания за последние 60 дней. rating_reaction_time — время в секундах, в течение которого покупатели в среднем ждали ответа на своё первое сообщение в чате за последние 30 дней. rating_average_response_time — время в секундах, в течение которого покупатели в среднем ждали вашего ответа за последние 30 дней. rating_replied_dialogs_ratio — доля диалогов хотя бы с одним вашим ответом в течение 24 часов за последние 30 дней. rating_general_indicator_fbs_rfbs — индекс ошибок FBS и rFBS. rating_price_green — выгодный индекс цен. rating_price_yellow — умеренный индекс цен. rating_price_red — невыгодный индекс цен. rating_price_super — супер-выгодный индекс цен. Если вы хотите получить информацию по начисленным штрафным баллам для рейтингов rating_on_time и rating_review_avg_score_total , передайте значения нужных рейтингов в этом параметре и with_premium_scores=true .
- **with_premium_scores** `boolean` — Признак, что в ответе нужно вернуть информацию о штрафных баллах в Premium-программе.

**Пример запроса:**

```json
{
  "date_from": "2019-08-24T14:15:22Z",
  "date_to": "2019-08-24T14:15:22Z",
  "ratings": [
    "string"
  ],
  "with_premium_scores": true
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о рейтингах |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **premium_scores** `Array of objects` — Информация о штрафных баллах в Premium-программе.
- **ratings** `Array of objects` — Информация о рейтингах продавца.

**Пример ответа (`200`):**

```json
{
  "premium_scores": [
    {
      "rating": "string",
      "scores": [
        {
          "date": "2019-08-24T14:15 \"rating_value\": 0",
          "value": 0
        }
      ]
    }
  ],
  "ratings": [
    {
      "danger_threshold": 0,
      "premium_threshold": 0,
      "rating": "string",
      "values": [
        {
          "date_from": "2019-08-24T \"date_to\": ",
          "status": {
            "danger": true,
            "premium": true,
            "warning": true
          },
          "value": 0
        }
      ],
      "warning_threshold": 0
    }
  ]
}
```


---

## Получить индекс ошибок FBS и rFBS

`POST /v1/rating/index/fbs/info`

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Индекс ошибок |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **currency_code** `string` — Код валюты стоимости обработки ошибок.
- **defects** `Array of objects` — Индекс ошибок по дням.
- **index** `number <double>` — Значение индекса ошибок за период.
- **period_from** `string` — Дата начала расчётного периода в формате YYYY- MM-DD .
- **period_to** `string` — Дата окончания расчётного периода в формате YYYY-MM-DD .
- **processing_costs_sum** `number <double>` — Расходы на обработку ошибок за период.

**Пример ответа (`200`):**

```json
{
  "currency_code": "string",
  "defects": [
    {
      "date": "string",
      "index_by_date": 0,
      "processing_costs_sum_by_date": ""
    }
  ],
  "index": 0,
  "period_from": "string",
  "period_to": "string",
  "processing_costs_sum": 0
}
```


---

## Список отправлений, которые повлияли на индекс ошибок FBS и rFBS

`POST /v1/rating/index/fbs/posting/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений в ответе.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "date_from": "2019-08-24T14:15:22Z",
    "date_to": "2019-08-24T14:15:22Z",
    "posting_numbers": [
      "string"
    ]
  },
  "limit": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список отправлений |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **errors** `Array of objects` — Отправления, которые повлияли на индекс.
- **has_next** `boolean` — true , если в ответе вернулись не все отправления.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "errors": [
    {
      "charge_percent": 0,
      "charge_price": 0,
      "charge_price_currency_code": "s \"delivery_schema\": \"string",
      "error_at": "2019-08-24T14:15:22 \"has_grace_status\": true",
      "index": 0,
      "posting_error_type": "UNSPECIFI \"posting_number\": \"string",
      "product_price": 0,
      "product_price_currency_code": ""
    }
  ],
  "has_next": true
}
```


---
