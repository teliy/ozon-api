# Аналитические отчёты

> Раздел документации Ozon Seller API (2.1), источник: PDF docs.ozon.ru, стр. 390. Базовый URL: `https://api-seller.ozon.ru`.

Все методы требуют заголовки `Client-Id` (идентификатор клиента) и `Api-Key` (API-ключ), если явно не указано иное.

Больше методов в разделе Premium-методы.

## Отчёт по остаткам и товарам

`POST /v2/analytics/stock_on_warehouses`

> **ВНИМАНИЕ:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.

Метод для получения отчёта по остаткам и товарам в перемещении по складам Ozon.

> **Примечание:** В будущем метод будет отключён. Переключитесь на

**Тело запроса** (`application/json`):
- **limit** `integer <int64>` *обязательный* — Количество ответов на странице. По умолчанию — 100.
- **offset** `integer <int64>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , то ответ начнётся с 11-го найденного элемента.
- **warehouse_type** `string` — Фильтр по типу склада: EXPRESS_DARK_STORE — склады Ozon с доставкой Fresh. NOT_EXPRESS_DARK_STORE — склады Ozon без доставки Fresh. ALL — все склады Ozon.. Enum: `"ALL"`, `"EXPRESS_DARK_STORE"`, `"NOT_EXPRESS_DARK_STORE"`.

**Пример запроса:**

```json
{
  "limit": 1000,
  "offset": 0,
  "warehouse_type": "ALL"
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Отчёт по остаткам и товарам |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **result** `object` — Результат запроса.
  - **rows** `Array of objects` — Информация о товарах и остатках.

**Пример ответа (`200`):**

```json
{
  "result": {
    "rows": [
      {
        "free_to_sell_amount": 0,
        "item_code": "string",
        "item_name": "string",
        "promised_amount": 0,
        "reserved_amount": 0,
        "sku": 0,
        "warehouse_name": "string"
      }
    ]
  }
}
```


---

## Оборачиваемость товара

`POST /v1/analytics/turnover/stocks`

Используйте метод, чтобы узнать оборачиваемость товара и количество дней, на которое хватит текущего остатка. Метод соответствует разделу FBO -> Управление остатками в личном кабинете. Вы можете делать не больше 1 запроса в минуту по одному кабинету Client-Id . Если вы запрашиваете список товаров по sku , параметры limit и offset необязательны.

**Тело запроса** (`application/json`):
- **limit** `integer <int32>` — Количество значений в ответе.
- **offset** `integer <int32>` — Количество элементов, которое будет пропущено в ответе. Например, если offset = 10 , ответ начнётся с 11-го найденного элемента.
- **sku** `Array of strings <int64>` — Идентификаторы товаров в системе Ozon — SKU.

**Пример запроса:**

```json
{
  "limit": 1,
  "offset": 0,
  "sku": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Информация об оборачиваемости |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **items** `Array of objects` — Товары.
  - **ads** `number <double>` — Среднесуточное количество проданных единиц товара за последние 60 дней.
  - **current_stock** `integer <int64>` — Остаток товара, шт.
  - **idc** `number <double>` — На сколько дней хватит остатка товара с учётом среднесуточных продаж.
  - **idc_grade** `string` — Уровень остатка товара: GRADES_NONE — ожидаются поставки; GRADES_NOSALES — нет продаж; GRADES_GREEN — зелёный, «хороший»; GRADES_YELLOW — жёлтый, «средний»; GRADES_RED — красный, «плохой»; GRADES_CRITICAL — критический.. Enum: `"GRADES_NONE"`, `"GRADES_NOSALES"`, `"GRADES_GREEN"`, `"GRADES_YELLOW"`, `"GRADES_RED"`, `"GRADES_CRITICAL"`.
  - **name** `string` — Название товара.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
  - **turnover** `number <double>` — Фактическая оборачиваемость в днях.
  - **turnover_grade** `string` — Уровень оборачиваемости: GRADES_NONE — ожидаются поставки; GRADES_NOSALES — нет продаж; GRADES_GREEN — зелёный, «хороший»; GRADES_YELLOW — жёлтый, «средний»; GRADES_RED — красный, «плохой»; GRADES_CRITICAL — критический.. Enum: `"GRADES_NONE"`, `"GRADES_NOSALES"`, `"GRADES_GREEN"`, `"GRADES_YELLOW"`, `"GRADES_RED"`, `"GRADES_CRITICAL"`.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "ads": 0,
      "current_stock": 0,
      "idc": 0,
      "idc_grade": "GRADES_NONE",
      "name": "string",
      "offer_id": "string",
      "sku": 0,
      "turnover": 0,
      "turnover_grade": "GRADES_NONE"
    }
  ]
}
```


---

## Получить аналитику по остаткам

`POST /v1/analytics/stocks`

Используйте метод, чтобы получить аналитику по остаткам товаров на складах в реальном времени. Метод соответствует разделу FBO → В запросе используйте только одно из полей: cluster_ids или

```
macrolocal_cluster_ids , иначе вернётся ошибка.
```

**Тело запроса** (`application/json`):
- **cluster_ids** `Array of strings <int64>` — Фильтр по идентификаторам кластеров. Получить идентификаторы можно через метод /v1/cluster/list.
- **item_tags** `Array of strings` — Фильтр по тегам товара: ITEM_ATTRIBUTE_NONE — без тега; ECONOM — эконом-товар; NOVEL — новинка; DISCOUNT — уценённый товар; FBS_RETURN — товар из возврата FBS; SUPER — Super-товар; MARKABLE — товар, подлежащий маркировке.. Enum: `"ITEM_ATTRIBUTE_NONE"`, `"ECONOM"`, `"NOVEL"`, `"DISCOUNT"`, `"FBS_RETURN"`, `"SUPER"`, `"MARKABLE"`.
- **macrolocal_cluster_ids** `Array of strings <int64>` — Фильтр по идентификаторам макролокальных кластеров. Получить идентификаторы можно в параметре macrolocal_cluster_ids метода /v1/cluster/list или через метод /v2/cluster/list.
- **placement_zone** `Array of strings` — Зона размещения товара: PLACEMENT_ZONE_NONE — не указана; CLOSED_ZONE — закрытая; DANGEROUS_GOOD — опасные товары; PRODUCTS_PLUS_17 — продукты; SORT — сортируемый товар; NON_SORT_MEZ — несортируемый товар; OVERSIZE — крупногабаритный товар; JEWELRY — ювелирные изделия; UNRESOLVED — ещё не определена.. Enum: `"PLACEMENT_ZONE_NONE"`, `"CLOSED_ZONE"`, `"DANGEROUS_GOOD"`, `"PRODUCTS_PLUS_17"`, `"SORT"`, `"NON_SORT_MEZ"`, `"OVERSIZE"`, `"JEWELRY"`, `"UNRESOLVED"`.
- **skus** `Array of strings <int64>` *обязательный* — Фильтр по идентификаторам товаров в системе Ozon — SKU.
- **turnover_grades** `Array of strings` — Фильтр по статусу ликвидности товаров: TURNOVER_GRADE_NONE — нет статуса ликвидности. DEFICIT — дефицитный. Остатков товара хватит до 28 дней. POPULAR — очень популярный. Остатков товара хватит на 28–56 дней. ACTUAL — популярный. Остатков товара хватит на 56–120 дней. SURPLUS — избыточный. Товар продаётся медленно, остатков хватит более чем на 120 дней. NO_SALES — без продаж. У товара нет продаж последние 28 дней. WAS_NO_SALES — был без продаж. У товара не было продаж и остатков последние 28 дней. RESTRICTED_NO_SALES — без продаж, ограничен. У товара не было продаж более 120 дней. Такой товар нельзя добавить в поставку. COLLECTING_DATA — сбор данных. Для расчёта ликвидности нового товара собираем данные в течение 60 дней после поставки. WAITING_FOR_SUPPLY — ожидаем поставки. На складе нет остатков, доступных к продаже. Сделайте поставку для начала сбора данных. WAS_DEFICIT — был дефицитным. Товар был дефицитным последние 56 дней. Сейчас у него нет остатков. WAS_POPULAR — был очень популярным. Товар был очень популярным последние 56 дней. Сейчас у него нет остатков. WAS_ACTUAL — был популярным. Товар был популярным последние 56 дней. Сейчас у него нет остатков. WAS_SURPLUS — был избыточным. Товар был избыточным последние 56 дней. Сейчас у него нет остатков.. Enum: `"TURNOVER_GRADE_NONE"`, `"DEFICIT"`, `"POPULAR"`, `"ACTUAL"`, `"SURPLUS"`, `"NO_SALES"`, `"WAS_NO_SALES"`, `"RESTRICTED_NO_SALES"`, `"COLLECTING_DATA"`, `"WAITING_FOR_SUPPLY"`, `"WAS_DEFICIT"`, `"WAS_POPULAR"`, `"WAS_ACTUAL"`, `"WAS_SURPLUS"`.
- **unmarked_stocks_only** `boolean` — true , чтобы получить только товары, которые нужно промаркировать.
- **warehouse_ids** `Array of strings <int64>` — Фильтр по идентификаторам складов. Получить идентификаторы можно через метод /v1/warehouse/list.

**Пример запроса:**

```json
{
  "cluster_ids": [
    "string"
  ],
  "item_tags": [
    "ITEM_ATTRIBUTE_NONE"
  ],
  "macrolocal_cluster_ids": [
    "string"
  ],
  "placement_zone": [
    "PLACEMENT_ZONE_NONE"
  ],
  "skus": [
    "string"
  ],
  "turnover_grades": [
    "TURNOVER_GRADE_NONE"
  ],
  "unmarked_stocks_only": true,
  "warehouse_ids": [
    "string"
  ]
}
```

**Ответы:**

| Код | Описание |
|---|---|
| `200` | Аналитика по остаткам на складах |
| `400` | Неверный параметр |
| `403` | Доступ запрещён |
| `404` | Ответ не найден |
| `409` | Конфликт запроса |
| `500` | Внутренняя ошибка сервера |

**Схема ответа (`200`):**
- **items** `Array of objects` — Информация о товарах.
  - **ads** `number <double>` — Среднесуточное количество проданных единиц товара за последние 28 дней по всем кластерам.
  - **ads_cluster** `number <double>` — Среднесуточное количество проданных единиц товара за последние 28 дней в кластере.
  - **available_stock_count** `integer <int32>` — Количество товаров, которые доступны к продаже. Соответствует столбцу «Доступно к продаже».
  - **cluster_id** `integer <int64>` — Идентификатор кластера. Получить подробную информацию о кластере можно через метод /v1/cluster/list.
  - **cluster_name** `string` — Название кластера.
  - **days_without_sales** `integer <int32>` — Количество дней без продаж по всем кластерам.
  - **days_without_sales_cluster** `integer <int32>` — Количество дней без продаж в кластере.
  - **excess_stock_count** `integer <int32>` — Количество излишков с поставки, которые доступны к вывозу.
  - **expiring_stock_count** `integer <int32>` — Количество единиц товара с истекающим сроком годности.
  - **idc** `number <double>` — Количество дней, на которое хватит остатка товара с учётом среднесуточных продаж за 28 дней по всем кластерам.
  - **idc_cluster** `number <double>` — Количество дней, на которое хватит остатка товара с учётом среднесуточных продаж за 28 дней в кластере.
  - **inbound_replenishment** `integer <int32>` — Количество товаров в перемещении.
  - **item_tags** `Array of strings` — Теги товара: UNSPECIFIED — не определено; ITEM_ATTRIBUTE_NONE — без тега; ECONOM — эконом- товар; NOVEL — новинка; DISCOUNT — уценённый товар; FBS_RETURN — товар из возврата FBS; SUPER — Super-товар; MARKABLE — товар, подлежащий маркировке.. Enum: `"UNSPECIFIED"`, `"ITEM_ATTRIBUTE_NONE"`, `"ECONOM"`, `"NOVEL"`, `"DISCOUNT"`, `"FBS_RETURN"`, `"SUPER"`, `"MARKABLE"`.
  - **macrolocal_cluster_id** `integer <int64>` — Идентификатор макролокального кластера. Получите информацию о кластере методом /v1/cluster/list или /v2/cluster/list.
  - **name** `string` — Название товара.
  - **offer_id** `string` — Идентификатор товара в системе продавца — артикул.
  - **other_stock_count** `integer <int32>` — Количество единиц товара, проходящих проверку.
  - **outbound_pending_delivery** `integer <int32>` — Количество товаров, которые доставляются покупателям.
  - **outbound_returns_picking** `integer <int32>` — Количество товаров, которые готовятся к вывозу.
  - **outbound_returns_ready_to_ship** `integer <int32>` — Количество товаров, которые готовы к вывозу.
  - **outbound_returns_return_to_seller** `integer <int32>` — Количество товаров, которые возвращаются продавцу.
  - **placement_zone** `Array of strings` — Зона размещения товара: UNSPECIFIED — не указана; CLOSED_ZONE — закрытая; DANGEROUS_GOOD — опасные товары; PRODUCTS — продукты; SORT — сортируемый товар; NON_SORT — несортируемый товар; OVERSIZE — крупногабаритный товар; JEWELRY — ювелирные изделия; UNRESOLVED — ещё не определена.. Enum: `"UNSPECIFIED"`, `"CLOSED_ZONE"`, `"DANGEROUS_GOOD"`, `"PRODUCTS"`, `"SORT"`, `"NON_SORT"`, `"OVERSIZE"`, `"JEWELRY"`, `"UNRESOLVED"`.
  - **requested_stock_count** `integer <int32>` — Количество единиц товара в заявках на поставку.
  - **return_from_customer_stock_count** `integer <int32>` — Количество единиц товара в процессе возврата от покупателей.
  - **return_to_seller_stock_count** `integer <int32>` — Количество единиц товара, готовящихся к вывозу по вашей заявке.
  - **sku** `integer <int64>` — Идентификатор товара в системе Ozon — SKU.
  - **stock_defect_stock_count** `integer <int32>` — Количество брака, доступное к вывозу со стока.
  - **stock_not_being_sold** `integer <int32>` — Количество товаров, которые сняты с продажи.
  - **transit_defect_stock_count** `integer <int32>` — Количество брака, доступное к вывозу с поставки.
  - **transit_stock_count** `integer <int32>` — Количество единиц товара в поставках в пути.
  - **turnover_grade** `string` — Статус ликвидности товара по всем кластерам: UNSPECIFIED — значение не определено. TURNOVER_GRADE_NONE — нет статуса ликвидности. DEFICIT — дефицитный. Остатков товара хватит до 28 дней. POPULAR — очень популярный. Остатков товара хватит на 28–56 дней. ACTUAL — популярный. Остатков товара хватит на 56–120 дней. SURPLUS — избыточный. Товар продаётся медленно, остатков хватит более чем на 120 дней. NO_SALES — без продаж. У товара нет продаж последние 28 дней. WAS_NO_SALES — был без продаж. У товара не было продаж и остатков последние 28 дней. RESTRICTED_NO_SALES — без продаж, ограничен. У товара не было продаж более 120 дней. Такой товар нельзя добавить в поставку. COLLECTING_DATA — сбор данных. Для расчёта ликвидности нового товара собираем данные в течение 60 дней после поставки. WAITING_FOR_SUPPLY — ожидаем поставки. На складе нет остатков, доступных к продаже. Сделайте поставку для начала сбора данных. WAS_DEFICIT — был дефицитным. Товар был дефицитным последние 56 дней. Сейчас у него нет остатков. WAS_POPULAR — был очень популярным. Товар был очень популярным последние 56 дней. Сейчас у него нет остатков. WAS_ACTUAL — был популярным. Товар был популярным последние 56 дней. Сейчас у него нет остатков. WAS_SURPLUS — был избыточным. Товар был избыточным последние 56 дней. Сейчас у него нет остатков.. Enum: `"UNSPECIFIED"`, `"TURNOVER_GRADE_NONE"`, `"DEFICIT"`, `"POPULAR"`, `"ACTUAL"`, `"SURPLUS"`, `"NO_SALES"`, `"WAS_NO_SALES"`, `"RESTRICTED_NO_SALES"`, `"COLLECTING_DATA"`, `"WAITING_FOR_SUPPLY"`, `"WAS_DEFICIT"`, `"WAS_POPULAR"`, `"WAS_ACTUAL"`, `"WAS_SURPLUS"`.
  - **turnover_grade_cluster** `string` — Статус ликвидности товара в кластере: UNSPECIFIED — значение не определено. TURNOVER_GRADE_NONE — нет статуса ликвидности. DEFICIT — дефицитный. Остатков товара хватит до 28 дней. POPULAR — очень популярный. Остатков товара хватит на 28–56 дней. ACTUAL — популярный. Остатков товара хватит на 56–120 дней. SURPLUS — избыточный. Товар продаётся медленно, остатков хватит более чем на 120 дней. NO_SALES — без продаж. У товара нет продаж последние 28 дней. WAS_NO_SALES — был без продаж. У товара не было продаж и остатков последние 28 дней. RESTRICTED_NO_SALES — без продаж, ограничен. У товара не было продаж более 120 дней. Такой товар нельзя добавить в поставку. COLLECTING_DATA — сбор данных. Для расчёта ликвидности нового товара собираем данные в течение 60 дней после поставки. WAITING_FOR_SUPPLY — ожидаем поставки. На складе нет остатков, доступных к продаже. Сделайте поставку для начала сбора данных. WAS_DEFICIT — был дефицитным. Товар был дефицитным последние 56 дней. Сейчас у него нет остатков. WAS_POPULAR — был очень популярным. Товар был очень популярным последние 56 дней. Сейчас у него нет остатков. WAS_ACTUAL — был популярным. Товар был популярным последние 56 дней. Сейчас у него нет остатков. WAS_SURPLUS — был избыточным. Товар был избыточным последние 56 дней. Сейчас у него нет остатков.. Enum: `"UNSPECIFIED"`, `"TURNOVER_GRADE_NONE"`, `"DEFICIT"`, `"POPULAR"`, `"ACTUAL"`, `"SURPLUS"`, `"NO_SALES"`, `"WAS_NO_SALES"`, `"RESTRICTED_NO_SALES"`, `"COLLECTING_DATA"`, `"WAITING_FOR_SUPPLY"`, `"WAS_DEFICIT"`, `"WAS_POPULAR"`, `"WAS_ACTUAL"`, `"WAS_SURPLUS"`.
  - **valid_stock_count** `integer <int32>` — Количество товаров, которые готовятся к продаже. Соответствует столбцу «Готовим к продаже».
  - **waiting_docs_stock_count** `integer <int32>` — Количество маркируемых товаров, которые ожидают ваших действий.
  - **waiting_docs_to_export_stock_count** `integer <int32>` — Количество маркируемых товаров, которые ожидают вывоз.
  - **warehouse_id** `integer <int64>` — Идентификатор склада.
  - **warehouse_name** `string` — Название склада.

**Пример ответа (`200`):**

```json
{
  "items": [
    {
      "ads": 0,
      "ads_cluster": 0,
      "available_stock_count": 0,
      "cluster_id": 0,
      "cluster_name": "string",
      "days_without_sales": 0,
      "days_without_sales_cluster": 0,
      "excess_stock_count": 0,
      "expiring_stock_count": 0,
      "idc": 0,
      "idc_cluster": 0,
      "inbound_replenishment": 0,
      "item_tags": [
        "UNSPECIFIED"
      ],
      "macrolocal_cluster_id": 0,
      "name": "string",
      "offer_id": "string",
      "other_stock_count": 0,
      "outbound_pending_delivery": 0,
      "outbound_returns_picking": 0,
      "outbound_returns_ready_to_ship": "outbound_returns_return_to_sell",
      "placement_zone": [
        "UNSPECIFIED"
      ],
      "requested_stock_count": 0,
      "return_from_customer_stock_coun \"return_to_seller_stock_count": "sku",
      "stock_defect_stock_count": 0,
      "stock_not_being_sold": 0,
      "transit_defect_stock_count": 0,
      "transit_stock_count": 0,
      "turnover_grade": "UNSPECIFIED",
      "turnover_grade_cluster": "UNSPE \"valid_stock_count\": 0",
      "waiting_docs_stock_count": 0,
      "waiting_docs_to_export_stock_co \"warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```


---
