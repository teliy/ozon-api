# Доставка FBS

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 299. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.


## Создание отгрузки

`POST /v1/carriage/create`

Используйте метод для создания первой FBS отгрузки. В неё попадут все отправления со статусом «Готов к отгрузке». Созданная отгрузка получит статус new . Для отгрузки в статусе new можно перезаписать состав отправлений методом /v1/carriage/set-postings. Если из отгрузки исключить часть отправлений, они могут попасть в следующую отгрузку. Чтобы получить список отправлений в отгрузке, используйте метод

> **Примечание:** Если вы продавец не из России, обратите внимание на

> **Примечание:** доступность рекомендованного времени в личном кабинете.

**Тело запроса** (`application/json`):
- **all_blr_traceable** `boolean` — true , если нужно создать отгрузку с прослеживаемыми товарами.
- **delivery_method_id** `integer <int64>` — Идентификатор метода доставки.
- **departure_date** `string <date-time>` — Дата отгрузки. По умолчанию — текущая дата.

**Пример запроса:**

```json
{
  "all_blr_traceable": true,
  "delivery_method_id": 0,
  "departure_date": "2019-08-24T14:15:22Z"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отгрузке |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **carriage_id** `integer <int64>` — Идентификатор перевозки.

**Пример ответа (`200`):**

```json
{
  "carriage_id": 0
}
```


---

## Подтверждение отгрузки

`POST /v1/carriage/approve`

Используйте метод, чтобы подтвердить отгрузку после её создания. После подтверждения отгрузка перейдёт в статус «Сформирована». После подтверждения отгрузки вы можете получить лист отгрузки методом /v2/posting/fbs/act/get-pdf и штрихкод отгрузки методом

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор отгрузки.
- **containers_count** `integer <int32>` — Количество грузовых мест. Используйте параметр, если вы подключены к доверительной приёмке и отгружаете заказы грузовыми местами. Если вы не подключены к доверительной приёмке, пропустите его.

**Пример запроса:**

```json
{
  "carriage_id": 0,
  "containers_count": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отгрузка подтверждена |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Пример ответа (`200`):**

```json
{}
```


---

## Изменение состава отгрузки

`POST /v1/carriage/set-postings`

> **Примечание:** Метод недоступен для продавцов из СНГ.

> **Примечание:** Полностью перезаписывает список заказов в отгрузке.

> **Примечание:** Передавайте только те заказы, которые находятся в статусе

> **Примечание:** Ожидает отгрузки , и вы готовы их отгрузить.

> **Примечание:** Менять состав можно только у отгрузок со статусом new .

> **Примечание:** Чтобы вернуться к списку заказов, удалите отгрузку с помощью

> **Примечание:** метода /v1/carriage/cancel, и создайте новую.

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор отгрузки.
- **posting_numbers** `Array of strings` *обязательный* — Актуальный список отправлений.

**Пример запроса:**

```json
{
  "carriage_id": 0,
  "posting_numbers": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отправлении |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects`
  - **error** `string` — Описание ошибки.
  - **posting_number** `string` — Номер отправления.
  - **result** `boolean` — Результат обработки запроса. true , если запрос был обработан успешно.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "error": "string",
      "posting_number": "string",
      "result": true
    }
  ]
}
```


---

## Удаление отгрузки

`POST /v1/carriage/cancel`

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор отгрузки.

**Пример запроса:**

```json
{
  "carriage_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об отправлении |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **error** `string` — Описание ошибки.
- **carriage_status** `string` — Статус отгрузки.

**Пример ответа (`200`):**

```json
{
  "error": "string",
  "carriage_status": "string"
}
```


---

## Список методов доставки и отгрузок

`POST /v2/carriage/delivery/list`

> **Примечание:** Метод не возвращает информацию по методам доставки, у

> **Примечание:** которых нет отправлений.

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` — Фильтр для поиска методов доставки и отгрузок.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "delivery_method_id": 0,
    "departure_date": "string"
  },
  "limit": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список методов и отгрузок |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных.
- **has_next** `boolean` — true , если в ответе вернулись не все методы доставки.
- **methods** `Array of objects` — Список методов доставки.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "has_next": true,
  "methods": [
    {
      "carriage_postings_count": 0,
      "carriages": [
        {
          "all_blr_traceable": true,
          "available_actions": [
            "string"
          ],
          "carriage_volume": 0,
          "id": 0,
          "pickup_fee": {
            "currency_code": "stri \"value\": 0"
          },
          "postings_count": 0,
          "quantum_count": 0,
          "status": "string"
        }
      ],
      "cut_in": "string",
      "cutoff_at": "string",
      "delivery_method_id": 0,
      "delivery_method_name": "string",
      "delivery_method_status": "strin \"departure_date\": \"string",
      "dropoff_address": "string",
      "dropoff_change_availability": " \"dropoff_point_id\": 0",
      "dropoff_point_type": "string",
      "errors": [
        {
          "code": "string",
          "description": "string",
          "status": "string"
        }
      ],
      "first_mile_changing": true,
      "first_mile_type": "string",
      "has_entrusted_acceptance": true,
      "integration_type": "string",
      "is_optional_carriage": true,
      "is_presort": true,
      "is_rfbs": true,
      "mandatory_packaged_count": 0,
      "mandatory_postings_count": 0,
      "optional_packaged_count": 0,
      "recommended_time_local": "strin ",
      "timeslot_from": "string",
      "timeslot_to": "string",
      "tpl_provider_icon_url": "string \"tpl_provider_name\": \"string",
      "warehouse_city": "string",
      "warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---

## Список методов доставки и отгрузок

`POST /v1/carriage/delivery/list`

Используйте метод, чтобы получить список созданных отгрузок для метода доставки и их статусы.

> **Примечание:** Метод не возвращает информацию по методам доставки, у

> **Примечание:** которых нет отправлений.

> **Примечание:** 20 марта 2026 года отключим метод. Переключитесь на

**Тело запроса** (`application/json`):
- **delivery_method_id** `integer <int64>` — Идентификатор метода доставки.
- **departure_date** `string <date-time>` — Дата отгрузки. По умолчанию — текущая дата.

**Пример запроса:**

```json
{
  "delivery_method_id": 0,
  "departure_date": "2019-08-24T14:15:22Z"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список методов и отгрузок |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects`
  - **assembly_list_availability** `boolean` — true , если доступен лист подбора.
  - **can_create_another_carriage** `boolean` — true , если можно создать ещё одну перевозку.
  - **carriage_postings_count** `integer <int32>` — Количество отправлений в перевозке.
  - **carriage_quantum_count** `integer <int32>` — Количество квантов в перевозке.
  - **carriages** `Array of objects` — Список перевозок.
  - **cut_in** `string <date-time>` — Время начала сборки и часовой пояс времени склада.
  - **delivery_method_id** `integer` — Идентификатор метода доставки.
  - **delivery_method_name** `string` — Название метода доставки.
  - **delivery_method_status** `string` — Статус метода доставки.
  - **departure_date** `string <date-time>` — Дата отгрузки.
  - **dropoff_address** `string` — Адрес точки отгрузки.
  - **dropoff_change_availability** `string` — Статус возможности смены точки отгрузки.
  - **dropoff_point_id** `integer <int64>` — Идентификатор точки отгрузки.
  - **dropoff_point_type** `string` — Способ отгрузки.
  - **errors** `Array of objects` — Массив ошибок, которые возникли при обработке запроса.
  - **first_mile_changing** `boolean` — true , если точка отгрузки изменилась.
  - **first_mile_type** `string` — Тип первой мили.
  - **has_entrusted_acceptance** `boolean` — Признак доверительной приёмки. true , если доверительная приёмка включена на складе.
  - **integration_type** `string` — Тип интеграции со службой доставки.
  - **is_presort** `boolean` — true , если отгрузка с предсортировкой.
  - **is_rfbs** `boolean` — true , если склад работает по схеме rFBS.
  - **recommended_time_local** `string` — Рекомендуемое местное время отгрузки в пункт приёма заказов.
  - **recommended_time_utc_offset_in_minutes** `number <int32>` — Смещение часового пояса рекомендуемого времени отгрузки от UTC-0 в минутах.
  - **cutoff_at** `string <date-time>` — Дата и время, до которых нужно собрать отправление.
  - **mandatory_packaged_count** `integer <int32>` — Количество «обязательных» собранных отправлений.
  - **mandatory_packaged_quantum_count** `integer <int32>` — Количество «обязательных» собранных квантов.
  - **mandatory_postings_count** `integer <int32>` — Количество отправлений, которые нужно собрать.
  - **mandatory_quantum_count** `integer <int32>` — Количество квантов, которые нужно собрать.
  - **optional_packaged_count** `integer <int32>` — Количество собранных «необязательных» отправлений.
  - **postings_for_another_carriage_count** `integer <int32>` — Количество отправлений, которые могут попасть в следующую перевозку.
  - **quantum_for_another_carriage_count** `integer <int32>` — Количество квантов, которые могут попасть в следующую перевозку.
  - **timeslot_from** `string <date-time>` — Начало таймслота в точке отгрузки.
  - **timeslot_to** `string <date-time>` — Окончание таймслота в точке отгрузки.
  - **tpl_provider_icon_url** `string` — Ссылка на иконку службы доставки.
  - **tpl_provider_name** `string` — Название службы доставки.
  - **warehouse_city** `string` — Город склада.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.
  - **warehouse_name** `string` — Название склада.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "assembly_list_availability": "tr",
      "can_create_another_carriage": "t",
      "carriage_postings_count": 0,
      "carriage_quantum_count": 0,
      "carriages": [
        {
          "id": "string",
          "postings_count": 0,
          "quantum_count": 0,
          "status": "string"
        }
      ],
      "cut_in": "2019-08-24T14:15:22Z",
      "delivery_method_id": 0,
      "delivery_method_name": "string",
      "delivery_method_status": "strin \"departure_date\": ",
      "dropoff_address": "string",
      "dropoff_change_availability": " \"dropoff_point_id\": 0",
      "dropoff_point_type": "string",
      "errors": [
        {
          "code": "string",
          "description": "string",
          "status": "string"
        }
      ],
      "first_mile_changing": true,
      "first_mile_type": "string",
      "has_entrusted_acceptance": true,
      "integration_type": "string",
      "is_presort": true,
      "is_rfbs": true,
      "recommended_time_local": "strin ",
      "cutoff_at": "2019-08-24T14:15:2 \"mandatory_packaged_count\": 0, ",
      "mandatory_postings_count": 0,
      "mandatory_quantum_count": 0,
      "optional_packaged_count": 0,
      "postings_for_another_carriage_c \"quantum_for_another_carriage_co \"timeslot_from": "2019-08-24T14: ",
      "timeslot_to": "2019-08-24T14:15 \"tpl_provider_icon_url\": ",
      "tpl_provider_name": "string",
      "warehouse_city": "string",
      "warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---

## Подтвердить отгрузку и создать документы

`POST /v2/posting/fbs/act/create`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Подтверждает отгрузку и запускает формирование транспортной накладной и штрихкода для отгрузки. Для продавцов из России также запускается формирование листа отгрузки, а для продавцов из СНГ — акта приёма-передачи. Чтобы сформировать и получить документы, переведите отправление

> **Примечание:** Метод устаревает и будет отключён 7 сентября 2026.

> **Примечание:** Переключитесь на /v1/carriage/create и /v1/carriage/approve.

```
в статус awaiting_deliver .
```

**Тело запроса** (`application/json`):
- **containers_count** `integer <int32>` — Количество грузовых мест. Используйте параметр, если вы подключены к доверительной приёмке и отгружаете заказы грузовыми местами. Если вы не подключены к доверительной приёмке, пропустите его. Подробнее в Базе знаний продавца
- **delivery_method_id** `integer <int64>` *обязательный* — Идентификатор метода доставки. Для realFBS-складов получите его с помощью метода /v2/delivery-method/list. Для FBS-складов используйте значение параметра warehouse_id . Его можно получить с помощью метода /v2/warehouse/list.
- **departure_date** `string <date-time>` — Дата отгрузки.

**Пример запроса:**

```json
{
  "containers_count": 1,
  "delivery_method_id": 230039077005,
  "departure_date": "2022-06-10T11:42:06.4"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отгрузка подтверждена |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **id** `integer <int64>` — Номер задания на формирование штрихкода и документов.

**Пример ответа (`200`):**

```json
{
  "result": {
    "id": 5819327210249
  }
}
```


---

## Список доступных перевозок

`POST /v1/posting/carriage-available/list`

Метод для получения перевозок, по которым нужно распечатать штрихкод для отгрузки и документы: для продацов из России — лист отгрузки и транспортную накладную; для продавцов из СНГ — акт и транспортную накладную.

> **Примечание:** 20 марта 2026 года отключим метод. Переключитесь на

**Тело запроса** (`application/json`):
- **delivery_method_id** `integer <int64>` *обязательный* — Фильтр по методу доставки. Можно получить с помощью метода /v2/delivery-method/list.
- **departure_date** `string <date-time>` — Дата отгрузки. По умолчанию — текущая дата.

**Пример запроса:**

```json
{
  "delivery_method_id": 0,
  "departure_date": "2019-08-24T14:15:22Z"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список перевозок |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат работы метода.
  - **carriage_id** `integer <int64>` — Идентификатор перевозки (также номер задания на формирование документов).
  - **carriage_postings_count** `integer <int32>` — Количество отправлений в перевозке.
  - **carriage_status** `string` — Статус перевозки для запрашиваемого метода доставки и даты отгрузки.
  - **cutoff_at** `string <date-time>` — Дата и время, до которых нужно собрать отправление.
  - **delivery_method_id** `integer <int64>` — Идентификатор метода доставки.
  - **delivery_method_name** `string` — Название метода доставки.
  - **errors** `Array of objects` — Список ошибок.
  - **first_mile_type** `string` — Тип первой мили.
  - **has_entrusted_acceptance** `boolean` — Признак доверительной приёмки. true , если доверительная приёмка включена на складе.
  - **mandatory_postings_count** `integer <int32>` — Количество отправлений, которые нужно собрать.
  - **mandatory_packaged_count** `integer <int32>` — Количество собранных отправлений.
  - **recommended_time_local** `string` — Рекомендуемое местное время отгрузки на пункт приёма заказов.
  - **recommended_time_utc_offset_in_minutes** `number <int32>` — Смещение часового пояса рекомендуемого времени отгрузки от UTC-0 в минутах.
  - **tpl_provider_icon_url** `string` — Ссылка на иконку службы доставки.
  - **tpl_provider_name** `string` — Название службы доставки.
  - **warehouse_city** `string` — Город склада.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.
  - **warehouse_name** `string` — Название склада.
  - **warehouse_timezone** `string` — Часовой пояс, в котором находится склад.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "carriage_id": 0,
      "carriage_postings_count": 0,
      "carriage_status": "string",
      "cutoff_at": "2019-08-24T14:15:2 \"delivery_method_id\": 0",
      "delivery_method_name": "string",
      "errors": [
        {
          "code": "string",
          "status": "string"
        }
      ],
      "first_mile_type": "string",
      "has_entrusted_acceptance": true,
      "mandatory_postings_count": 0,
      "mandatory_packaged_count": 0,
      "recommended_time_local": "strin ",
      "tpl_provider_icon_url": "string \"tpl_provider_name\": \"string",
      "warehouse_city": "string",
      "warehouse_id": 0,
      "warehouse_name": "string",
      "warehouse_timezone": "string"
    }
  ]
}
```


---

## Информация о перевозке

`POST /v1/carriage/get`

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "carriage_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация о перевозке |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **act_type** `string` — Тип акта приёма-передачи. Актуально для продавцов FBS.
- **all_blr_traceable** `boolean` — true , если отгрузка с прослеживаемыми товарами.
- **is_waybill_enabled** `boolean` — true , если доступна печать транспортной накладной.
- **is_econom** `boolean` — true , если отгрузка относится к товарам «Суперэконом».
- **arrival_pass_ids** `Array of strings <int64>` — Список идентификаторов пропусков, оформленных на перевозку.
- **available_actions** `Array of strings` — Доступные действия с перевозкой: get_shipping_list — получить лист отгрузки; get_act_of_acceptance — получить акт приёма-передачи; get_waybill — получить товарную накладную в формате PDF; set_arrival_passes — оформить пропуск.
- **cancel_availability** `object` — Возможность отмены.
- **carriage_id** `integer <int64>` — Идентификатор перевозки.
- **company_id** `integer <int64>` — Идентификатор продавца.
- **containers_count** `integer <int32>` — Количество грузовых мест.
- **created_at** `string <date-time>` — Дата создания перевозки.
- **delivery_method_id** `integer <int64>` — Идентификатор метода доставки.
- **departure_date** `string` — Дата выполнения перевозки.
- **first_mile_type** `string` — Тип первой мили.
- **has_postings_for_next_carriage** `boolean` — true , если есть отправления, которые не попали в перевозку, но нужно отгрузить.
- **integration_type** `string` — Тип перевозки.
- **is_container_label_printed** `boolean` — true , если вы уже напечатали этикетки на грузовые места.
- **is_partial** `boolean` — true , если перевозка частичная.
- **partial_num** `integer <int64>` — Порядковый номер частичной перевозки.
- **retry_count** `integer <int32>` — Количество повторных попыток создания перевозки.
- **status** `string` — Статус перевозки: received — идёт приёмка, closed — завершена после приёмки, sended — отправлена, cancelled — отменена.
- **tpl_provider_id** `integer <int64>` — Идентификатор провайдера доставки.
- **updated_at** `string <date-time>` — Дата последнего обновления информации о перевозке.
- **warehouse_id** `integer <int64>` — Идентификатор склада.

**Пример ответа (`200`):**

```json
{
  "act_type": "string",
  "all_blr_traceable": true,
  "is_waybill_enabled": true,
  "is_econom": true,
  "arrival_pass_ids": [
    "string"
  ],
  "available_actions": [
    "string"
  ],
  "cancel_availability": {
    "is_cancel_available": true,
    "reason": "string"
  },
  "carriage_id": 0,
  "company_id": 0,
  "containers_count": 0,
  "created_at": "2019-08-24T14:15:22Z",
  "delivery_method_id": 0,
  "departure_date": "string",
  "first_mile_type": "string",
  "has_postings_for_next_carriage": true,
  "integration_type": "string",
  "is_container_label_printed": true,
  "is_partial": true,
  "partial_num": 0,
  "retry_count": 0,
  "status": "string",
  "tpl_provider_id": 0,
  "updated_at": "2019-08-24T14:15:22Z",
  "warehouse_id": 0
}
```


---

## Добавить или обновить контактные данные продавца для курьера

`POST /v1/carriage/courier-contact/set`

Используйте метод, чтобы добавить или обновить контактные данные продавца, которые передаются курьеру для перевозок с в ответе метода /v1/carriage/get.

```
first_mile_type = pickup  и integration_type = ozon_outsourced .
Получите значения параметров first_mile_type  и integration_type
```

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.
- **phone** `string +86(XXX)XXXX-XXXX` *обязательный* — Телефон продавца.
- **wechat_nickname** `string` — WeChat продавца.
- **comment** `string` — Комментарий для курьера.

**Пример запроса:**

```json
{
  "carriage_id": 543234,
  "phone": "+86(123)4567-8901",
  "wechat_nickname": "string",
  "comment": "string"
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

## Получить контактные данные продавца для курьера

`POST /v1/carriage/courier-contact/get`

Возвращает контактные данные продавца, которые добавили или обновили методом /v1/carriage/courier-contact/set.

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "carriage_id": 5435123
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Контактные данные продавца для курьера |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **contact** `Array of objects` — Информация о контактах продавца.
  - **carriage_id** `integer <int64>` — Идентификатор перевозки.
  - **phone** `string` — Телефон продавца.
  - **wechat_nickname** `string` — WeChat продавца.
  - **comment** `string` — Комментарий для курьера.
  - **updated_at** `string <date-time>` — Дата и время последнего обновления записи в UTC.

**Пример ответа (`200`):**

```json
{
  "contact": [
    {
      "carriage_id": 5435123,
      "phone": "+86(123)4567-8901",
      "wechat_nickname": "string",
      "comment": "string",
      "updated_at": "2026-07-29T10:38: }"
    }
  ]
}
```


---

## Разделить заказ на отправления без сборки

`POST /v1/posting/fbs/split`

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Номер отправления.
- **postings** `Array of objects` *обязательный* — Список отправлений, на которые поделится заказ. За один запрос можно разделить один заказ.

**Пример запроса:**

```json
{
  "posting_number": "string",
  "postings": [
    {
      "products": [
        {
          "product_id": 0,
          "quantity": 0
        }
      ]
    }
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заказ разделён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **parent_posting** `object` — Информация об изначальном отправлении.
- **postings** `Array of objects` — Список отправлений, на которые разделился заказ.

**Пример ответа (`200`):**

```json
{
  "parent_posting": {
    "posting_number": "string",
    "products": [
      {
        "product_id": 0,
        "quantity": 0
      }
    ]
  },
  "postings": [
    {
      "posting_number": "string",
      "products": [
        {
          "product_id": 0,
          "quantity": 0
        }
      ]
    }
  ]
}
```


---

## Список отправлений в акте

`POST /v2/posting/fbs/act/get-postings`

Возвращает список отправлений в акте по его идентификатору.

**Тело запроса** (`application/json`):
- **id** *обязательный* — Идентификатор акта. Получите значение параметра методом /v2/posting/fbs/act/list или /v1/carriage/create.

**Пример запроса:**

```json
{
  "id": 900000250859000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список отправлений |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Информация об отправлениях.
  - **id** `integer <int64>` — Идентификатор акта.
  - **multi_box_qty** `integer <int32>` — Количество коробок, в которые упакован товар.
  - **posting_number** `string` — Номер отправления.
  - **status** `string` — Статус отправления.
  - **seller_error** `string` — Расшифровка кода ошибки.
  - **updated_at** `string <date-time>` — Дата и время обновления записи об отправлении.
  - **created_at** `string <date-time>` — Дата и время создания записи об отправлении.
  - **products** `Array of objects` — Список товаров в отправлении.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "id": 0,
      "multi_box_qty": 0,
      "posting_number": "string",
      "status": "string",
      "seller_error": "string",
      "updated_at": "2019-08-24T14:15: ",
      "created_at": "2019-08-24T14:15: \"products\": [ { \"name\": \"string",
      "offer_id": "string",
      "price": "string",
      "quantity": 0,
      "sku": 0
    }
  ]
}
```


---

## Этикетки для грузового места

`POST /v2/posting/fbs/act/get-container-labels`

Метод создает этикетки для грузового места.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Идентификатор перевозки из метода /v1/carriage/create.

**Пример запроса:**

```json
{
  "id": 295662811
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Этикетки для грузового места |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **file_content** `string <byte>` — Содержание файла в бинарном виде.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "application/pdf",
  "file_name": "carriage-containers-2090359 :",
  "file_content": "PDF-1.4\n%âãÏÓ\n2 0 obj :"
}
```


---

## Штрихкод для отгрузки отправления

`POST /v2/posting/fbs/act/get-barcode`

Метод для получения штрихкода, который нужно показать в пункте выдачи или сортировочном центре при отгрузке отправления.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "id": "295662811"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Штрихкод для отправления |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **file_content** `string` — Изображение со штрихкодом в бинарном виде.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "image/png",
  "file_name": "0913984_barcode.png",
  "file_content": "PNG\r\n\u001a\n\u0000\\u :"
}
```


---

## Значение штрихкода для отгрузки отправления

`POST /v2/posting/fbs/act/get-barcode/text`

Используйте этот метод, чтобы получить штрихкод из ответа

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "id": "295662811"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Значение штрихкода |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **result** `string` — Штрихкод в текстовом виде.

**Пример ответа (`200`):**

```json
{
  "result": "%303%24276481394"
}
```


---

## Статус формирования накладной Deprecated

`POST /v2/posting/fbs/digital/act/check-status`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

> **Примечание:** Метод устаревает и будет отключён 22 марта 2026 года.

> **Примечание:** Переключитесь на /v2/posting/fbs/act/check-status.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Номер задания на формирование документов (также идентификатор перевозки) из метода POST /v2/posting/fbs/act/create.

**Пример запроса:**

```json
{
  "id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус формирования накладной |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **id** `integer <int64>` — Номер задания на формирование документов.
- **status** `string` — Cтатус формирования документов: FORMING — ещё не готовы, FORMED — сформированы успешно, CONFIRMED — подписаны Ozon, CONFIRMED_WITH_MISMATCH — подписаны Ozon с расхождениями, NOT_FOUND — документы не найдены, UNKNOWN_ERROR — произошла ошибка.

**Пример ответа (`200`):**

```json
{
  "id": 0,
  "status": "string"
}
```


---

## Получить PDF c документами

`POST /v2/posting/fbs/act/get-pdf`

С помощью метода можно получить: продацам из России — лист отгрузки и транспортную накладную; продавцам из СНГ — акт и транспортную накладную. Получите список доступных документов для отгрузки в параметре available_actions метода /v1/carriage/get.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Номер задания на формирование документов (также идентификатор перевозки) из методов /v2/posting/fbs/act/create или /v1/carriage/create.

**Пример запроса:**

```json
{
  "id": 22435521842000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Документы |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **file_content** `string <byte>` — Содержание файла в бинарном виде.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "application/pdf",
  "file_name": "20928233.pdf",
  "file_content": "PDF-1.4\n%âãÏÓ\n2 0 obj :"
}
```


---

## Получить акт о расхождениях по отгрузке FBS

`POST /v1/carriage/act-discrepancy/pdf`

Акт о расхождениях доступен только для отгрузок в статусе closed и только для продавцов из СНГ.

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор отгрузки.

**Пример запроса:**

```json
{
  "carriage_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Акт о расхождениях |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **content** `string <byte>` — Содержание файла в бинарном виде.
- **name** `string` — Название файла.
- **type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content": "string",
  "name": "string",
  "type": "string"
}
```


---

## Список актов по отгрузкам

`POST /v2/posting/fbs/act/list`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Возвращает список актов по отгрузкам с возможностью отфильтровать отгрузки по периоду, статусу и типу интеграции.

**Тело запроса** (`application/json`):
- **filter** `object` — Параметры фильтра.
- **limit** `integer <int64>` *обязательный* — Максимальное количество актов в ответе.

**Пример запроса:**

```json
{
  "filter": {
    "date_from": "2021-08-04",
    "date_to": "2022-08-04",
    "integration_type": "ozon",
    "status": [
      "delivered"
    ]
  },
  "limit": 50
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список актов |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `Array of objects` — Результат запроса.
  - **id** — Идентификатор отгрузки.
  - **delivery_method_id** — Идентификатор метода доставки.
  - **delivery_method_name** `string` — Название метода доставки.
  - **integration_type** `string` — Тип интеграции со службой доставки: ozon — доставка через Ozon логистику. 3pl — доставка внешней службой, продавец регистрирует заказ.
  - **containers_count** — Число грузовых мест.
  - **status** `string` — Статус отгрузки.
  - **departure_date** `string` — Дата отгрузки.
  - **created_at** `string <date-time>` — Дата создания записи об отгрузке.
  - **updated_at** `string <date-time>` — Дата обновления записи об отгрузке.
  - **act_type** `string` — Тип акта приёма-передачи для FBS продавцов.
  - **is_partial** `boolean` — Признак частичной перевозки. true , если перевозка частичная. Частичная перевозка значит, что отгрузка была разделена на несколько частей и по каждой из частей формируются отдельные акты.
  - **has_postings_for_next_carriage** `boolean` — Признак наличия подлежащих отгрузке отправлений, которые не попали в текущую перевозку. true , если такие отправления есть.
  - **partial_num** `integer <int64>` — Порядковый номер частичной перевозки.
  - **related_docs** `object` — Информация про акты перевозки.

**Пример ответа (`200`):**

```json
{
  "result": [
    {
      "id": null,
      "delivery_method_id": null,
      "delivery_method_name": "string",
      "integration_type": "string",
      "containers_count": null,
      "status": "string",
      "departure_date": "string",
      "created_at": "2019-08-24T14:15: ",
      "updated_at": "2019-08-24T14:15: \"act_type\": \"string",
      "is_partial": true,
      "has_postings_for_next_carriage": "partial_num",
      "related_docs": {
        "act_of_acceptance": {
          "created_at": "2019-08-24 \"document_status\": "
        },
        "act_of_mismatch": {
          "created_at": "2019-08-24 \"document_status\": "
        },
        "act_of_excess": {
          "created_at": "2019-08-24 \"document_status\": "
        }
      }
    }
  ]
}
```


---

## Получить лист отгрузки по перевозке

`POST /v2/posting/fbs/digital/act/get-pdf`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Вы можете получить документы, если в ответе метода FORMED — перевозка сформирована успешно, CONFIRMED — перевозка подтверждена Ozon, расхождениями.

> **Примечание:** Метод устаревает и будет отключён 22 марта 2026 года.

> **Примечание:** Переключитесь на /v2/posting/fbs/act/get-pdf.

```
CONFIRMED_WITH_MISMATCH  — перевозка принята Ozon с
```

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Номер задания на формирование документов (также идентификатор перевозки) из метода POST /v2/posting/fbs/act/create.
- **doc_type** — Тип электронного документа: act_of_acceptance — лист отгрузки, act_of_mismatch — акт о расхождениях, act_of_excess — акт об излишках, waybill — транспортная накладная.

**Пример запроса:**

```json
{
  "id": 900000250859000,
  "doc_type": "act_of_acceptance"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Файл с документом |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **file_content** `string <byte>` — Содержание файла в бинарном виде.
- **file_name** `string` — Название файла.
- **content_type** `string` — Тип файла.

**Пример ответа (`200`):**

```json
{
  "content_type": "application/pdf",
  "file_name": "0816409_act_of_mismatch.pd :",
  "file_content": "PDF-1.4\n%ÓôÌá\n1 0 obj :"
}
```


---

## Статус отгрузки и документов

`POST /v2/posting/fbs/act/check-status`

Возвращает статус формирования штрихкода для отгрузки и документов: для продавцов из России — транспортной накладной и листа отгрузки; для продавцов из СНГ — транспортной накладной и акта приёма- передачи.

**Тело запроса** (`application/json`):
- **id** `integer <int64>` *обязательный* — Номер задания на формирование документов (также идентификатор перевозки) из метода POST /v2/posting/fbs/act/create.

**Пример запроса:**

```json
{
  "id": 900000250859000
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус отгрузки и документов |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат работы метода.
  - **act_type** `string` — Тип документов.
  - **added_to_act** `Array of strings` — Массив c номерами отправлений, которые добавлены в перевозку. Эти отправления нужно передать сегодня.
  - **removed_from_act** `Array of strings` — Массив с номерами отправлений, которые не попали в перевозку. Такие отправления нужно передавать со следующей отгрузкой.
  - **status** `string` — Статус запроса: in_process — документы формируются, нужно подождать. ready — документы сформированы и готовы для скачивания. error — произошла ошибка при формировании документов, запросите документы повторно. cancelled — создание документов отменено, запросите их повторно. The next postings aren't ready — произошла ошибка, отправления не включены в отгрузку. Подождите некоторое время и проверьте результат запроса. Если ошибка повторяется, обратитесь в службу поддержки.
  - **is_partial** `boolean` — Признак частичной перевозки. true , если перевозка частичная. Частичная перевозка значит, что отгрузка была разделена на несколько частей.
  - **has_postings_for_next_carriage** `boolean` — true , если есть отправления, не попавшие в текущую перевозку, но которые нужно отгрузить. Если в ответе вернулось true , подтвердите отгрузку или создайте новый акт через метод /v2/posting/fbs/act/create и проверьте их статус. Повторяйте действия, пока в ответе не вернётся false .
  - **partial_num** `integer <int64>` — Порядковый номер частичной перевозки.

**Пример ответа (`200`):**

```json
{
  "result": {
    "status": "ready",
    "added_to_act": [
      "76673629-0020-1"
    ],
    "removed_from_act": [
      "87784739-0030-1"
    ],
    "act_type": "ozon_digital",
    "is_partial": false,
    "has_postings_for_next_carriage": "fa",
    "partial_num": 0
  }
}
```


---

## Разделить отправление с прослеживаемыми товарами

`POST /v1/posting/fbs/traceable/split`

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Номер отправления.

**Пример запроса:**

```json
{
  "posting_number": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Заказ разделён |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **postings** `Array of objects` — Информация об отправлениях.
  - **posting_number** `string` — Номер отправления.
  - **potential_blr_traceable** `boolean` — Признак, что товар потенциально прослеживаемый: true — отправление считается прослеживаемым на данный момент. При сборке статус может измениться. false — отправление не прослеживаемое на данный момент или его статус неизвестный.
  - **products** `Array of objects` — Список товаров в отправлении.

**Пример ответа (`200`):**

```json
{
  "postings": [
    {
      "posting_number": "string",
      "potential_blr_traceable": true,
      "products": [
        {
          "quantity": 0,
          "sku": 0
        }
      ]
    }
  ]
}
```


---

## Получить список незаполненных атрибутов для прослеживаемых товаров

`POST /v1/posting/fbs/product/traceable/attribute`

**Тело запроса** (`application/json`):
- **posting_number** `string` *обязательный* — Номер отправления.

**Пример запроса:**

```json
{
  "posting_number": "string"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список незаполненных атрибутов |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **products** `Array of objects` — Список товаров в отправлении.
  - **required_attributes** `Array of strings` — Обязательные атрибуты.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.

**Пример ответа (`200`):**

```json
{
  "products": [
    {
      "required_attributes": [
        "string"
      ],
      "sku": 0
    }
  ]
}
```


---

## Получить статус проверки электронной ТТН на прослеживаемой перевозке FBS

`POST /v1/carriage/ettn/status`

**Тело запроса** (`application/json`):
- **carriage_id** `integer <int64>` *обязательный* — Идентификатор перевозки.

**Пример запроса:**

```json
{
  "carriage_id": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Статус проверки электронной ТТН |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **errors** `Array of strings` — Ошибки проверки электронной ТТН на прослеживаемой отгрузке.
- **status** `string` — Статус проверки электронной ТТН на прослеживаемой отгрузке: NOT_UPLOADED — не загружена; PROCESSING — в процессе проверки; SUCCESS — проверена; FAILED — ошибка.. Enum: `"NOT_UPLOADED"`, `"PROCESSING"`, `"SUCCESS"`, `"FAILED"`.

**Пример ответа (`200`):**

```json
{
  "errors": [
    "string"
  ],
  "status": "NOT_UPLOADED"
}
```


---

## Получить список отправлений в отгрузке

`POST /v1/assembly/carriage/posting/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "carriage_id": 0,
    "cutoff_from": "2019-08-24T14:15:22Z ",
    "cutoff_to": "2019-08-24T14:15:22Z",
    "delivery_method_id": 0
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
- **can_print_mass_label** `boolean` — true , если можно распечатать этикетки массово.
- **cursor** `string` — Указатель для выборки следующих данных. Если параметр пустой, данных больше нет.
- **postings** `Array of objects` — Список отправлений.

**Пример ответа (`200`):**

```json
{
  "can_print_mass_label": true,
  "cursor": "string",
  "postings": [
    {
      "assembly_code": "string",
      "can_print_label": true,
      "posting_number": "string",
      "products": [
        {
          "offer_id": "string",
          "picture_url": "string",
          "product_name": "string",
          "quantity": 0,
          "sku": 0
        }
      ]
    }
  ]
}
```


---

## Получить список товаров в отгрузке

`POST /v1/assembly/carriage/product/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.

**Пример запроса:**

```json
{
  "cursor": "string",
  "filter": {
    "carriage_id": 0,
    "cutoff_from": "2019-08-24T14:15:22Z ",
    "cutoff_to": "2019-08-24T14:15:22Z",
    "delivery_method_id": 0
  },
  "limit": 0
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных. Если параметр пустой, данных больше нет.
- **products** `Array of objects` — Список товаров.

**Пример ответа (`200`):**

```json
{
  "cursor": "string",
  "products": [
    {
      "offer_id": "string",
      "picture_url": "string",
      "posting_numbers": [
        "string"
      ],
      "product_name": "string",
      "quantity": 0,
      "sku": 0
    }
  ]
}
```


---

## Получить список отправлений

`POST /v1/assembly/fbs/posting/list`

**Тело запроса** (`application/json`):
- **cursor** `string` — Указатель для выборки следующих данных.
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.
- **sort_dir** `string` *обязательный* — Направление сортировки: ASC — по возрастанию, DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filter": {
    "cutoff_from": "2026-03-01T00:00:00Z ",
    "cutoff_to": "2026-03-07T23:59:59Z",
    "delivery_method_id": 323123321
  },
  "limit": 50,
  "sort_dir": "ASC",
  "cursor": ""
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список отправлений |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **cursor** `string` — Указатель для выборки следующих данных. Если параметр пустой, данных больше нет.
- **cutoff** `string <date-time>` — Время, до которого продавцу нужно собрать заказ.
- **postings** `Array of objects` — Список отправлений.

**Пример ответа (`200`):**

```json
{
  "cutoff": "2026-03-07T10:00:00Z",
  "postings": [
    {
      "posting_number": "789456123-000 \"assembly_code\": ",
      "products": [
        {
          "sku": 1000123456,
          "offer_id": "test-offer-1 \"product_name\": ",
          "picture_url": "https://t \"quantity\": 2"
        },
        {
          "sku": 1000123457,
          "offer_id": "test-offer-1 \"product_name\": ",
          "picture_url": "https://t \"quantity\": 1"
        }
      ]
    },
    {
      "posting_number": "123456789-000 \"assembly_code\": ",
      "products": [
        {
          "sku": 1000123458,
          "offer_id": "test-offer-1 \"product_name\": ",
          "picture_url": "https://t \"quantity\": 3"
        }
      ]
    },
    {
      "posting_number": "456123789-000 \"assembly_code\": ",
      "products": [
        {
          "sku": 1000123459,
          "offer_id": "test-offer-1 \"product_name\": ",
          "picture_url": "https://t \"quantity\": 1"
        },
        {
          "sku": 1000123460,
          "offer_id": "test-offer-1 \"product_name\": ",
          "picture_url": "https://t \"quantity\": 2"
        },
        {
          "sku": 1000123461,
          "offer_id": "test-offer-1 \"product_name\": ",
          "picture_url": "https://t \"quantity\": 1"
        }
      ]
    }
  ],
  "cursor": "test-cursor-next-page-67890"
}
```


---

## Получить список товаров в отправлениях

`POST /v1/assembly/fbs/product/list`

**Тело запроса** (`application/json`):
- **filter** `object` *обязательный* — Фильтр.
- **limit** `integer <int64>` *обязательный* — Количество значений на странице.
- **offset** `integer <int64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , ответ начнётся с 11 найденного элемента.
- **sort_dir** `string` — Направление сортировки: ASC — по возрастанию, DESC — по убыванию.. Enum: `"ASC"`, `"DESC"`.

**Пример запроса:**

```json
{
  "filter": {
    "cutoff_from": "2019-08-24T14:15:22Z ",
    "cutoff_to": "2019-08-24T14:15:22Z",
    "delivery_method_id": 0
  },
  "limit": 0,
  "offset": 0,
  "sort_dir": "ASC"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Список товаров в отправлениях |
| `default` | Ошибка |

**Схема ответа (`200`):**
- **has_next** `boolean` — Признак, что в ответе вернули не все товары: true — сделайте повторный запрос с другим значением offset , чтобы получить остальные значения; false — ответ содержит все значения.
- **products** `Array of objects` — Список товаров.
- **products_count** `integer <int32>` — Количество товаров.

**Пример ответа (`200`):**

```json
[
  {
    "products": [
      {
        "sku": 1000123456,
        "offer_id": "test-offer-123456",
        "product_name": "Тестовый товар ",
        "picture_url": "https://test-exa \"quantity\": 15",
        "postings": [
          {
            "posting_number": "789456 \"quantity\": 2"
          },
          {
            "posting_number": "123456 \"quantity\": 3"
          },
          {
            "posting_number": "456123 \"quantity\": 1"
          }
        ]
      },
      {
        "sku": 1000123457,
        "offer_id": "test-offer-123457",
        "product_name": "Тестовый товар ",
        "picture_url": "https://test-exa \"quantity\": 8",
        "postings": [
          {
            "posting_number": "321654 \"quantity\": 2"
          },
          {
            "posting_number": "987321 \"quantity\": 1"
          },
          {
            "posting_number": "789456 \"quantity\": 3"
          },
          {
            "posting_number": "123456 \"quantity\": 2"
          }
        ]
      },
      {
        "sku": 1000123458,
        "offer_id": "test-offer-123458",
        "product_name": "Тестовый товар ",
        "picture_url": "https://test-exa \"quantity\": 23",
        "postings": [
          {
            "posting_number": "456123 \"quantity\": 5"
          },
          {
            "posting_number": "321654 \"quantity\": 4"
          }
        ],
        "posting_number": "987321 \"quantity\": 3"
      },
      {
        "posting_number": "789456 \"quantity\": 6"
      },
      {
        "posting_number": "123456 \"quantity\": 5"
      }
    ]
  },
  {
    "sku": 1000123459,
    "offer_id": "test-offer-123459",
    "product_name": "Тестовый товар ",
    "picture_url": "https://test-exa \"quantity\": 5",
    "postings": [
      {
        "posting_number": "456123 \"quantity\": 2"
      },
      {
        "posting_number": "321654 \"quantity\": 3"
      }
    ]
  },
  {
    "sku": 1000123460,
    "offer_id": "test-offer-123460",
    "product_name": "Тестовый товар ",
    "picture_url": "https://test-exa \"quantity\": 12",
    "postings": [
      {
        "posting_number": "987321 \"quantity\": 4"
      },
      {
        "posting_number": "789456 \"quantity\": 3"
      },
      {
        "posting_number": "123456 \"quantity\": 5"
      }
    ]
  }
]
```


---
