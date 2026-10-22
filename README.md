# ozon-api — Документация Ozon Seller API для ИИ

[![Онлайн-документация](https://img.shields.io/badge/%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD-005bff)](https://teliy.github.io/ozon-api/)
[![CI](https://img.shields.io/github/actions/workflow/status/teliy/ozon-api/ci.yml?label=CI)](https://github.com/teliy/ozon-api/actions)
[![Ozon Seller API](https://img.shields.io/badge/Ozon_Seller_API-2.1-005bff)](https://docs.ozon.ru/api/seller/)
[![Методов](https://img.shields.io/badge/%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%B2-482-brightgreen)](index.md)
[![Размер репо](https://img.shields.io/github/repo-size/teliy/ozon-api)](https://github.com/teliy/ozon-api)
[![Лицензия](https://img.shields.io/github/license/teliy/ozon-api)](LICENSE)

Полный справочник **Ozon Seller API (2.1)**, конвертированный из PDF (docs.ozon.ru, выгрузка от 2026-09-28) в структурированный Markdown, оптимизированный для больших языковых моделей и RAG-систем.

## Оглавление

- [Ключевые факты](#ключевые-факты)
- [Синхронизация с живой документацией (2026-10-22)](#синхронизация-с-живой-документацией-2026-10-22)
- [Сверка бейджей и примечаний (2026-10-23)](#сверка-бейджей-и-примечаний-2026-10-23)
- [Сверка схем тел запросов и ответов (2026-10-23)](#сверка-схем-тел-запросов-и-ответов-2026-10-23)
- [Структура](#структура)
- [Онлайн-просмотр](#онлайн-просмотр)
- [Как использовать с ИИ](#как-использовать-с-ии)
- [Формат описания метода](#формат-описания-метода)
- [Известные ограничения конверсии](#известные-ограничения-конверсии)
- [Генерация](#генерация)

### Разделы справочника (`docs/`)

| Раздел | Раздел | Раздел |
|---|---|---|
| [00 · Руководство по Ozon Seller API](docs/00-guides.md) | [21 · Доставка rFBS](docs/21-rfbs-delivery.md) | [42 · Работа с пуш-уведомлениями](docs/42-push-notifications.md) |
| [01 · Информация по API-ключу](docs/01-api-key.md) | [22 · Пропуски](docs/22-passes.md) | [43 · Работа с транспортными грузоместами FBO](docs/43-fbo-cargoplaces.md) |
| [02 · Информация по кабинету продавца](docs/02-seller-info.md) | [23 · Возвраты товаров FBO и FBS](docs/23-returns-fbo-fbs.md) | [44 · Работа с FBP-черновиками](docs/44-fbp-drafts.md) |
| [03 · Атрибуты и характеристики Ozon](docs/03-attributes.md) | [24 · Возвраты товаров rFBS](docs/24-returns-rfbs.md) | [45 · Работа с FBP-черновиками с доставкой direct](docs/45-fbp-drafts-direct.md) |
| [04 · Загрузка и обновление товаров](docs/04-products.md) | [25 · Возвратные отгрузки](docs/25-return-shipments.md) | [46 · Работа с FBP-черновиками c доставкой drop-off](docs/46-fbp-drafts-dropoff.md) |
| [05 · Штрихкоды товаров](docs/05-barcodes.md) | [26 · Отмены заказов](docs/26-order-cancellations.md) | [47 · Работа с FBP-черновиками с доставкой pick-up](docs/47-fbp-drafts-pickup.md) |
| [06 · Цены и остатки товаров](docs/06-prices-stocks.md) | [27 · Чаты с покупателями](docs/27-chats.md) | [48 · Работа с FBP-поставками с доставкой direct](docs/48-fbp-supplies-direct.md) |
| [07 · Акции Ozon](docs/07-actions-ozon.md) | [28 · Накладные](docs/28-invoices.md) | [49 · Работа с FBP-поставками с доставкой drop-off](docs/49-fbp-supplies-dropoff.md) |
| [08 · Стратегии ценообразования](docs/08-pricing-strategies.md) | [29 · Отчёты](docs/29-reports.md) | [50 · Работа с FBP-поставками с доставкой pick-up](docs/50-fbp-supplies-pickup.md) |
| [09 · Сертификаты брендов](docs/09-certificates-brands.md) | [30 · Аналитические отчёты](docs/30-analytics.md) | [51 · Работа с созданной поставкой FBP](docs/51-fbp-supply.md) |
| [10 · Сертификаты качества](docs/10-quality-certificates.md) | [31 · Финансовые отчёты](docs/31-finance-reports.md) | [52 · Работа с грузоместами FBS](docs/52-fbs-cargoplaces.md) |
| [11 · Работа со складами FBS и rFBS](docs/11-warehouses-fbs-rfbs.md) | [32 · Чеки](docs/32-receipts.md) | [53 · Работа с актами FBO](docs/53-fbo-acts.md) |
| [12 · Создание FBS-складов и управление ими](docs/12-warehouses-fbs.md) | [33 · Рейтинг продавца](docs/33-seller-rating.md) | [54 · Premium-методы](docs/54-premium.md) |
| [13 · Создание складов rFBS Express и управление ими](docs/13-warehouses-rfbs-express.md) | [34 · Работа с цифровыми товарами](docs/34-digital-goods.md) | [55 · Ozon Доставка](docs/55-ozon-delivery.md) |
| [14 · Обработка заказов FBS и rFBS](docs/14-postings-fbs-rfbs.md) | [35 · Работа с отзывами](docs/35-reviews.md) | [56 · Причины отмены](docs/56-cancel-reasons.md) |
| [15 · Полигоны](docs/15-polygons.md) | [36 · Работа с вопросами и ответами](docs/36-questions-answers.md) | [57 · Доставка](docs/57-delivery-info.md) |
| [16 · Доставка FBO](docs/16-fbo-delivery.md) | [37 · Бета-методы](docs/37-beta-methods.md) | [58 · Заказы](docs/58-orders.md) |
| [17 · Создание и управление заявками на поставку FBO](docs/17-fbo-supplies.md) | [38 · Прочие методы](docs/38-misc-methods.md) | [59 · Отправления](docs/59-postings-info.md) |
| [18 · Склады FBO](docs/18-fbo-warehouses.md) | [39 · Работа с квантами](docs/39-rabota-s-kvantami.md) | [60 · Частые ошибки](docs/60-common-errors.md) |
| [19 · Управление кодами маркировки и сборкой заказов для FBS/rFBS](docs/19-marking-codes.md) | [40 · Акции продавца](docs/40-seller-promotions.md) | [99 · Уведомления (Notifications)](docs/99-notifications.md) |
| [20 · Доставка FBS](docs/20-fbs-delivery.md) | [41 · Акции Ozon](docs/41-actions-ozon-2.md) |  |

## Ключевые факты

- **Базовый URL:** `https://api-seller.ozon.ru`
- **Авторизация:** заголовки `Client-Id` и `Api-Key` в каждом запросе
- **Формат данных:** JSON
- **Методов в справочнике:** 482
- **Ограничение запросов:** только back-to-back (сервер-сервер); браузерные запросы блокируются CORS
- **Рабочая среда:** api-seller.ozon.ru

## Синхронизация с живой документацией (2026-10-22)

Справочник сверен с актуальной документацией docs.ozon.ru (снапшот от 22 октября 2026 года). Внесены изменения:

- **Добавлен метод** `POST /v1/barcode/delete` — Отвязать штрихкод от товара (`docs/05-barcodes.md`)
- **Добавлен метод** `POST /v1/supply-order/shipment-plan-compliance/get` — Получить информацию о выполнении плана отгрузок (`docs/17-fbo-supplies.md`)
- **Отключённый метод помечен:** `GET /v1/cargoes-label/file/{file_guid}` удалён из актуальной документации (отключён 10 апреля 2026) и исключён из `index.md`
- **Исправлены артефакты PDF-конверсии** в разделах «Собрать заказ (версия 4)» и «Частичная сборка отправления (версия 4)» (`docs/19-marking-codes.md`): восстановлены разорванные примечания, исправлены сломанные JSON-примеры ответов и описания
- Обновлены `index.md`, `llms.txt`, `llms-full.txt`

## Сверка бейджей и примечаний (2026-10-23)

Полная сверка всех 482 методов с живой документацией: заголовки, бейджи «Deprecated», примечания и описания.

- **Добавлен бейдж `Deprecated`** всем 25 методам, помеченным бейджем в живой документации: после строки метода добавлено `> **Deprecated:** метод устарел или устаревает и будет отключён. Используйте актуальную версию.`
- **Исправлены заголовки**: у 16 методов бейдж из PDF был приклеен к названию («## Добавить товар в акцию Deprecated») — названия очищены, бейдж вынесен отдельной строкой
- **Восстановлены оборванные примечания** (~70): PDF обрезал тексты предупреждений на переносах строк — потерянные фрагменты (даты отключения, методы для переключения) восстановлены по живой документации
- **Восстановлены описания** 8 методов с оборванным текстом и посторонними код-блоками (артефакты PDF-конверсии), включая `/v1/product/pictures/import`, `/v2/posting/fbs/package-label`, `/v2/posting/fbs/digital/act/get-pdf`, `/v1/carriage/create`
- **Удалены устаревшие предупреждения** с `POST /v4/posting/fbs/unfulfilled/list` и `POST /v2/posting/fbs/act/list` — в актуальной документации они не помечены
- **Синхронизированы маркеры `(deprecated)` в `index.md`**: добавлены 9 методам с бейджем, сняты с 4 методов, которые в актуальной документации не помечены (`/v2/actions/candidates`, `/v2/actions/products`, `/v4/posting/fbs/unfulfilled/list`, `/v2/posting/fbs/act/list`)

Известное ограничение: таблица «Изменения в методах» в `docs/99-notifications.md` содержит усечённые строки из PDF — она не входит в Redoc-снапшот docs.ozon.ru и не может быть сверена автоматически.

## Сверка схем тел запросов и ответов (2026-10-23)

Полная сверка схем (поля и типы) всех методов с живой документацией: 482/482 операций сопоставлены, 2987 полей схем проверено. После правок — **0 расхождений типов, 0 недостающих и 0 лишних полей** относительно Redoc-снапшота docs.ozon.ru от 22.10.2026.

- **Восстановлены ограничения массивов** (35 полей): к типам добавлены лимиты `<= N items` (30 полей, например `prices <= 1000 items` в `/v1/product/import/prices`, `working_days <= 7 items` при создании FBS-склада) и `[ min .. max ] items` (13 полей, например `discount_levels [ 2 .. 4 ] items` в многоуровневой скидке, `review_ids [ 1 .. 100 ] items`)
- **Очищены типы от приклеенных форматов** (10 полей): PDF склеивал подсказки формата с типом — `string+7(XXX)XXX-XX-XX`, `string YYYY-MM-DD`, `string 7XXXXXXXXXX`, `string +86(XXX)XXXX-XXXX` заменены на `string` / `string <date-time>`, а подсказки формата перенесены в описания полей
- **Добавлены пропущенные типы** (9 полей): `id` и `delivery_method_id` → `int <int64>`, `containers_count` → `int <int32>`, `doc_type` → `any <string>`, `filter` → `posting_number (object) or date (object)`, `delivery` → `courier (object) or pick_up (object)`, `published_at` → `timestamp`, `status` → `enum` (типы взяты из живой документации дословно)
- **Добавлены пропущенные поля схем** (11 полей): `required` и `variants` в ответах `/v2/product/certification/{options,params}`, `courier_return_warehouse_info` в запросах `/v1/warehouse/fbs/create` и `/v1/warehouse/fbs/first-mile/update`, `is_courier_return_mile_available` и `is_dropoff_return_mile_available` в ответе `/v1/warehouse/fbs/return-mile/check`, `is_blr_traceable` и `scanit` в ответе `/v2/posting/fbs/act/get-postings`
- **Исправлены маркеры обязательности** (3 поля): `products` в `/v1/seller-actions/products/add` теперь *обязательный* с лимитом `<= 100 items` (и удалён фантомный вложенный `items` — артефакт PDF); снята ошибочная пометка `*обязательный*` с `name` в ответах методов сертификации
- **Замена 14 JSON-примеров** на чистые версии из живой документации (запросы и ответы метода, где менялись поля): устранены обрывы PDF и добавлены новые поля (`courier_return_warehouse_info`, `is_blr_traceable`, `variants` и др.)
- **Удалён дубликат метода** `POST /v1/product/info/stocks-by-warehouse/fbo`: секция была и в `docs/04-products.md`, и в `docs/38-misc-methods.md` — оставлена только версия в `docs/04-products.md` (также убраны дубль из `index.md` и лишний сегмент `llms-full.txt`; в `38-misc` теперь 26 методов)
- Обновлены `index.md`, `llms.txt`, `llms-full.txt`

Особенности, сверенные и признанные корректными (не являются ошибками): 9 методов с «свободным» телом запроса (`object` без фиксированных свойств) передаются в документации пустым примером `{}`; поле `last_id` в `/v1/question/answer/list` не имеет типа в живой документации.

## Структура

```
├── README.md            — этот файл
├── index.md             — шпаргалка: все endpoints в таблицах
├── llms.txt             — индекс файлов для ИИ (llms.txt standard)
├── llms-full.txt        — вся документация одним файлом
├── LICENSE              — лицензия (MIT)
├── scripts/validate_markdown.py — валидатор Markdown (ссылки, якоря, таблицы)
├── scripts/deploy_pages.py — публикация GitHub Pages (docsify)
└── docs/
    ├── 00-guides.md     — руководства: начало работы, авторизация, лимиты
    ├── 01…NN-*.md       — справочник методов по разделам API
    └── 99-notifications.md — push-уведомления
```

## Онлайн-просмотр

Сайт на GitHub Pages: **<https://teliy.github.io/ozon-api/>** — справочник открывается прямо в браузере, без клонирования репозитория. Реализовано на docsify: Markdown рендерится на лету, без сборки статики. В сайдбаре — все 62 раздела, сгруппированные по тематикам (товары, склады, FBO/FBP, возвраты и т.д.), плюс вложенные заголовки методов текущего раздела.

Есть полнотекстовый поиск по всем методам, схемам и примерам, подсветка синтаксиса JSON-примеров (935 код-блоков) и кнопки копирования кода. После правок в `docs/` сайт обновляется командой `python3 scripts/deploy_pages.py sync` (ветка `gh-pages` синхронизируется с `main` и пересобирается GitHub Pages автоматически).

## Как использовать с ИИ

- **RAG / выборка:** индексируйте файлы из `docs/` по разделам — каждый файл самодостаточен и содержит полные схемы.
- **Claude/ChatGPT с одним файлом:** дайте модели `llms-full.txt` (или части, если контекст мал).
- **Агенты с file-search:** подключите `llms.txt` как карту репозитория, затем подгружайте нужный раздел.

## Формат описания метода

Каждый метод описан по схеме: заголовок-название, `VERB /path`, предупреждения о deprecated, описание, схема тела запроса (вложенный список с типами, required, default, enum), пример запроса, таблица кодов ответов, схема и примеры ответов.

## Известные ограничения конверсии

- Исходный PDF содержит усечённые длинные строки в JSON-примерах (обрезка при печати) — такие значения восстановлены частично.
- Диаграммы схем работы (FBO/FBS/rFBS) в исходнике были картинками и не перенесены; их смысл описан текстом в руководствах.
- Инлайн-примеры внутри описаний сохранены как код-блоки.

## Генерация

Конвертация выполнена автоматически: PDF → PyMuPDF → структурный парсер (шрифты/колонки) → Markdown. Дата генерации: 2026-09-29. Сверка с живой документацией docs.ozon.ru: 2026-10-22, сверка бейджей и примечаний: 2026-10-23.

Для включения CI-проверок (битые ссылки, якоря, таблицы — `scripts/validate_markdown.py`) добавьте в репозиторий файл `.github/workflows/ci.yml` (например, через веб-интерфейс GitHub: *Add file → Create new file*). После первого запуска бейдж CI в шапке обновится автоматически.
