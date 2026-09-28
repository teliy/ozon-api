# Уведомления (Notifications)

> Документация push-уведомлений Ozon Seller API. Базовый URL: `https://api-seller.ozon.ru`.

## Введение

В разделе описано, как подключить пуш-уведомления, чтобы получать от Ozon на свой сервис информацию о событиях:

создании нового отправления,

отмене отправления,

изменении статуса отправления,

изменении даты доставки или отгрузки отправления.

Также можно получать информацию о сообщениях и уведомлениях, которые не были доставлены из-за недоступности

вашего сервиса.

## Как подключить

Ваш сервис должен отправлять ответы по стандартам REST API и с кодами ошибок, указанными в документации.

Если ответы вашего сервиса отличаются от требуемой структуры, отправка уведомлений может быть

приостановлена.

IP-адреса, с которых приходят уведомления

195.34.21.0/24,

185.73.192.0/22,

91.223.93.0/24.

### Первичное подключение пуш-уведомлений

1. В личном кабинете продавца перейдите в раздел Настройки → Уведомления.

2. На вкладке Push уведомления включите получение уведомлений.

3. Нажмите Подключить.

4. Введите URL-адрес сервиса, на который будут отправляться уведомления. Например,

https://www.example.com/api/method.

5. Нажмите Проверить. Ozon отправит запрос для проверки соединения, на который должен ответить ваш сервис.

Если соединение установлено, появится сообщение «Данный url доступен для подключения».

6. Нажмите Сохранить.

7. В блоке Настройки подключения в выпадающем списке Типы уведомлений выберите нужные.

Описания уведомлений

Отключить уведомления можно в разделе Настройки → Уведомления на вкладке Push уведомления.

Коды ошибок при подключении пуш-уведомлений

Ошибка

Описание

Решение

Запрос не отправлен, нет

REQUEST_ERROR

подключения по указанному

Проверьте, что ваш сервис работает.

адресу.

Превышено время ожидания

REQUEST_TIMEOUT

Увеличьте время ожидания запроса.

запроса.

Изучите логи сервера, обновите серверное ПО,

Ваш сервис вернул внутреннюю

SERVER_FAULT

увеличьте выделенные ресурсы или обратитесь к

ошибку сервера.

администратору сервера.

HTTP-статус ответа сервиса не

STATUS_CODE_NOT_OK

Проверьте передаваемый код статуса.

равен 200.

Тело ответа пустое или

Проверьте, что ответ на сервере сформирован

EMPTY_BODY

отсутствует.

правильно, и, что данные корректно передаются.

Некорректный формат тела

Проверьте формат ответа и убедитесь, что

INVALID_BODY

ответа.

```
заголовок Content-Type  равен application/json .
```

Ошибка при разборе или

Проверьте правильность JSON-данных и

INVALID_JSON

валидации JSON-данных.

исправьте ошибки в синтаксисе.

Проверьте, что формат ответа соответствует

Ваш сервис вернул тело ответа

WRONG_RESULT_FIELD

шаблону.

не по шаблону.

Подробнее о шаблоне

Ошибка

Описание

Решение

Некорректное поле time в

WRONG_RESULT_TIME_FIELD

Проверьте формат времени в ответе.

теле ответа.

### Изменить адрес сервиса

1. В личном кабинете продавца перейдите в раздел Настройки → Интеграции.

2. На вкладке Push уведомления нажмите Редактировать.

3. Введите URL-адрес сервиса, на который будут отправляться уведомления.

4. Нажмите Проверить. Ozon отправит запрос для проверки соединения, на который должен ответить ваш сервис.

Если соединение установлено, появится сообщение «Данный url доступен для подключения».

5. Нажмите Сохранить.

### Запрос для проверки соединения

Что отправляет Ozon

```
{
"message_type"  "string"
:
,
"time"  "2019-08-24T14:15:22Z"
:
}
```

Параметр

Тип

Формат

Описание

Тип уведомления — TYPE_PING .

```
message_type
```

string

—

```
time
```

string

date-time

Дата и время отправки уведомления в формате UTC.

Что должен отвечать ваш сервис

Если уведомление получено успешно

При успешной обработке уведомления сервис должен вернуть ответ с кодом HTTP 200:

```
{
"version"  "string"
:
,
"name"  "string"
:
,
"time"  "2019-08-24T14:15:22Z"
:
}
```

Параметр

Тип

Формат

Описание

```
version
```

string

—

Версия приложения.

```
name
```

string

—

Название приложения.

```
time
```

string

date-time

Дата и время начала обработки уведомления в формате UTC.

Если произошла ошибка

При ошибке во время обработки уведомления сервис должен вернуть ответ с кодом HTTP из групп 4xx или 5xx:

```
{
"error"
: {
"code"  "ERROR_UNKNOWN"
:
,
"message"  "ошибка"
:
,
"details"  null
:
}
}
```

Параметр

Тип

Формат

Описание

```
error
```

object

—

Информация об ошибке.

Код ошибки:

- ERROR_UNKNOWN — неизвестная ошибка.

```
code
```

string

—

- ERROR_PARAMETER_VALUE_MISSED — не указано значение одного или

нескольких параметров.

```
• ERROR_REQUEST_DUPLICATED  — дублирующийся запрос.
message
```

string

—

Детальное описание ошибки.

```
details
```

string

—

Дополнительная информация.

### Посмотреть статус уведомлений

В личном кабинете перейдите в раздел Настройки → Интеграции → Push уведомления.

В таблице покажем:

Адрес — ваш URL-адрес для приёма пуш-уведомлений.

Статус доступности — статус уведомлений. Наведите курсор на статус, чтобы узнать подробности и рекомендации.

Причина отключения — причина, по которой отключили отправку.

Дата проверки — дата последней проверки доступности.

### Повторное подключение

Проверьте доступность и скорость ответа вашего URL-адреса. Затем включите отправку пуш-уведомлений в личном

кабинете или через метод /v1/notification/enable. Система проверит URL-адрес в ближайший плановый запуск. Если

проверка пройдёт успешно, статус изменится на «Доступен».

Если ваш URL-адрес принудительно отключила служба поддержки и указала причину, включить адрес самостоятельно

не получится. Исправьте проблемы, удалите старый адрес и подключите новый.

## Повторная отправка уведомлений

Интервалы повторной отправки

Если уведомление не доставлено, через несколько секунд система попытается отправить запрос ещё несколько раз.

Интервал между попытками будет постепенно увеличиваться. Когда он достигнет максимального значения в 10 минут,

будет ещё 5 попыток каждые 10 минут.

Автоматическая приостановка отправки уведомлений

Если сообщение по-прежнему не получится доставить, попытки отправки запроса прекратятся.

Отправка всех уведомлений будет приостановлена, если соблюдено хотя бы одно из условий:

сервис недоступен;

сервис возвращает ошибки в течение 24 часов;

ответов 200 меньше половины от всех уведомлений;

время обработки уведомлений больше 5 секунд.

Чтобы снова получать уведомления, в личном кабинете продавца повторно подтвердите URL-адрес сервиса.

## Уведомления, которые отправляет Ozon

Уведомление о новом заказе может приходить с задержкой. Чтобы иметь актуальную информацию, периодически

получайте список необработанных отправлений через метод POST /v3/posting/fbs/unfulfilled/list.

Для каждого из типов уведомлений Ozon отправляет REST-запросы на адрес вашего сервиса. Ваш сервис должен

отвечать по стандартам REST API.

Тип

Назначение

Проверка статуса готовности сервиса при первичном

TYPE_PING

подключении и периодически после подключения

TYPE_NEW_POSTING

Новое отправление

TYPE_POSTING_CANCELLED

Отмена отправления

TYPE_STATE_CHANGED

Изменение статуса отправления

TYPE_CUTOFF_DATE_CHANGED

Изменение даты отгрузки отправления

TYPE_DELIVERY_DATE_CHANGED

Изменение даты доставки отправления

TYPE_CREATE_OR_UPDATE_ITEM

Создание и обновление товара или ошибка в процессе

TYPE_CREATE_ITEM

Создание товара или ошибка при его создании

TYPE_UPDATE_ITEM

Обновление товара или ошибка при обновлении

TYPE_STOCKS_CHANGED

Изменение остатков на складах продавца

TYPE_NEW_MESSAGE

Новое сообщение в чате

TYPE_UPDATE_MESSAGE

Изменение сообщения в чате

TYPE_MESSAGE_READ

Ваше сообщение прочитано покупателем или поддержкой

TYPE_CHAT_CLOSED

Чат закрыт

TYPE_DESCRIPTION_CATEGORY_TREE_CHANGED

Изменение дерева категорий

TYPE_FBO_POSTING_NEW

Новое отправление FBO

TYPE_FBO_POSTING_CANCELLED

Отмена отправления FBO

TYPE_FBO_POSTING_STATE_CHANGED

Изменение статуса отправления FBO

TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED

Изменение даты доставки отправления FBO

TYPE_FBO_STOCKS_CHANGED

Изменение остатков на складах Ozon

TYPE_ORDER_NEW

Новый заказ

TYPE_ORDER_CANCELLED

Отмена заказа

TYPE_ORDER_STATE_CHANGED

Изменение статуса заказа

### Новое отправление

При поздней оплате заказа поле in_process_at может быть пустым. Вы можете проверить дату отгрузки через

метод POST /v3/posting/fbs/get в поле result.in_process_at .

Уведомления приходят только для FBS и rFBS отправлений:

```
{
"message_type"  "TYPE_NEW_POSTING"
:
,
"posting_number"  "24319409-0021-1"
:
,
"products"
: [
{
"sku"  147451939
:
,
"offer_id"  "Товар2"
:
,
"quantity"  1
:
}
],
"in_process_at"  "2021-01-26T06:56:36.294Z"
:
,
"warehouse_id"  12850503335000
:
,
"shipment_date"  "2021-01-26T06:56:36.294Z"
:
,
"tpl_integration_type"  "3pl_tracking"
:
,
"is_express"  false
:
,
"tracking_number"  "ZZV-23"
:
,
"delivery_date_begin"  "2025-01-26T06:56:36.294Z"
:
,
"delivery_date_end"  "2025-01-26T06:56:36.294Z"
:
,
"seller_id"  1
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

Тип уведомления — TYPE_NEW_POSTING .

```
posting_number
```

string

—

Номер отправления.

```
products
```

array

—

Информация о товарах.

```
sku
```

integer

int64

Идентификатор товара в системе Ozon — SKU.

```
offer_id
```

string

—

Идентификатор товара в системе продавца — артикул.

```
quantity
```

integer

int64

Количество товара.

```
in_process_at
```

string

date-time

Дата и время начала обработки отправления в формате UTC.

```
warehouse_id
```

integer

int64

Идентификатор склада.

```
shipment_date
```

string

date-time

Дата и время, до которой необходимо собрать отправление.

Тип интеграции со службой доставки:

ozon — доставка службой Ozon;

3pl_tracking — доставка интегрированной службой;

```
tpl_integration_type
```

string

—

non_integrated — доставка сторонней службой;

aggregator — доставка через партнёрскую доставку Ozon;

hybryd — схема доставки Почты России.

```
is_express
```

boolean

—

Признак доставки express.

```
tracking_number
```

string

—

Трек-номер отправления.

```
delivery_date_begin
```

string

date-time

Дата и время начала доставки.

```
delivery_date_end
```

string

date-time

Дата и время конца доставки.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Отмена отправления

Уведомления приходят только для FBS и rFBS отправлений:

```
{
"message_type"  "TYPE_POSTING_CANCELLED"
:
,
"posting_number"  "24219509-0020-1"
:
,
"products"
: [
{
"sku"  147451959
:
,
"quantity"  1
:
}
],
"old_state"  "posting_transferred_to_courier_service"
:
,
"new_state"  "posting_canceled"
:
,
"changed_state_date"  "2021-01-26T06:56:36.294Z"
:
,
"reason"
: {
"id"  0
:
,
"message"  "string"
:
},
"warehouse_id"  0
:
,
"seller_id"  15
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_POSTING_CANCELLED .
posting_number
```

string

—

Номер отправления.

```
products
```

array

—

Информация о товарах.

```
sku
```

integer

int64

Идентификатор товара в системе Ozon — SKU.

```
quantity
```

integer

int64

Количество товара.

```
old_state
```

string

—

Предыдущий статус отправления.

```
new_state
```

string

—

Новый статус отправления: posting_canceled — отменено.

date-

```
changed_state_date
```

string

Дата и время изменения статуса отправления в формате UTC.

time

```
reason
```

object

—

Информация о причине отмены.

```
id
```

integer

int64

Идентификатор причины отмены.

```
message
```

string

—

Причина отмены.

Идентификатор склада, на котором хранятся товары для этого

```
warehouse_id
```

integer

int64

отправления.

```
seller_id
```

integer

int64

Идентификатор продавца.

Статусы отправлений

```
posting_acceptance_in_progress  — идёт приёмка,
posting_created  — создано,
posting_transferring_to_delivery  — передаётся в доставку,
posting_in_carriage  — в перевозке,
posting_not_in_carriage  — не добавлен в перевозку,
posting_in_client_arbitration  — клиентский арбитраж доставки,
posting_on_way_to_city  — на пути в город,
posting_transferred_to_courier_service  — передаётся курьеру,
posting_in_courier_service  — курьер в пути,
posting_on_way_to_pickup_point  — на пути в пункт выдачи,
posting_in_pickup_point  — в пункте выдачи,
posting_conditionally_delivered  — условно доставлено,
posting_driver_pick_up  — у водителя,
```

posting_not_in_sort_center — не принят на сортировочном центре.

### Изменение статуса отправления

Соответствие статусных моделей Seller API и статусов пуш-модели.

Seller API

Push-модель

Статус

Описание

Статус

Описание

Seller API

Push-модель

```
acceptance_in_pro
posting_acceptance_in_progre
```

Идёт приёмка.

Идёт приёмка.

```
gress
ss
awaiting_approve
```

Ожидает подтверждения.

```
posting_created
```

Создана.

```
awaiting_packagin
```

Ожидает упаковки.

```
posting_created
```

Создана.

```
g
awaiting_registra
posting_awaiting_registratio
```

Ожидает регистрации.

Ожидает регистрации.

```
tion
n
posting_transferring_to_deli
awaiting_deliver
```

Ожидает отгрузки.

Передаётся в доставку.

```
very
posting_in_carriage
```

В перевозке.

```
posting_not_in_carriage
```

Не добавлен в перевозку.

```
arbitration
```

Арбитраж.

```
posting_in_arbitration
```

Арбитраж.

```
client_arbitratio
```

Клиентский арбитраж

```
posting_in_client_arbitratio
```

Клиентский арбитраж.

```
n
```

доставки.

```
n
delivering
```

Доставляется.

```
posting_on_way_to_city
```

На пути в ваш город.

```
posting_transferred_to_couri
```

Передаётся курьеру.

```
er_service
posting_in_courier_service
```

Курьер в пути.

```
posting_on_way_to_pickup_poi
```

На пути в пункт выдачи.

```
nt
posting_in_pickup_point
```

В пункте выдачи.

```
posting_conditionally_delive
```

Условно доставлено.

```
red
driver_pickup
```

У водителя.

```
posting_driver_pick_up
```

У водителя.

```
delivered
```

Доставлено.

```
posting_delivered
```

Доставлено.

```
posting_received
```

Получено.

```
cancelled
```

Отменено.

```
posting_canceled
```

Отменено.

Не принято на сортировочном

Не принято на

```
not_accepted
posting_not_in_sort_center
```

центре.

сортировочном центре.

Уведомления приходят только для FBS и rFBS отправлений.

```
{
"message_type"  "TYPE_STATE_CHANGED"
:
,
"posting_number"  "24219509-0020-2"
:
,
"new_state"  "posting_delivered"
:
,
"changed_state_date"  "2021-02-02T15:07:46.765Z"
:
,
"warehouse_id"  0
:
,
"seller_id"  15
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_STATE_CHANGED .
posting_number
```

string

—

Номер отправления.

```
new_state
```

string

—

Новый статус отправления.

date-

```
changed_state_date
```

string

Дата и время изменения статуса отправления в формате UTC.

time

Параметр

Тип

Формат

Описание

Идентификатор склада, на котором хранятся товары для этого

```
warehouse_id
```

integer

int64

отправления.

```
seller_id
```

integer

int64

Идентификатор продавца.

Статусы отправлений

```
posting_acceptance_in_progress  — идёт приёмка,
posting_transferring_to_delivery  — передаётся в доставку,
posting_in_carriage  — в перевозке,
posting_not_in_carriage  — не добавлен в перевозку,
posting_in_arbitration  — арбитраж,
posting_in_client_arbitration  — клиентский арбитраж доставки,
posting_on_way_to_city  — на пути в город,
posting_transferred_to_courier_service  — передаётся курьеру,
posting_in_courier_service  — курьер в пути,
posting_on_way_to_pickup_point  — на пути в пункт выдачи,
posting_in_pickup_point  — в пункте выдачи,
posting_conditionally_delivered  — условно доставлено,
posting_driver_pick_up  — у водителя,
posting_delivered  — доставлено,
```

posting_not_in_sort_center — не принят на сортировочном центре.

### Изменение даты отгрузки отправления

Уведомление работает в тестовом режиме. Рекомендуем проверять дату отгрузки через метод POST

Поле new_cutoff_date может приходить пустым из-за удаления интервала доставки. Дождитесь назначения новой

даты — после этого придёт новое уведомление.

Иногда уведомления этого типа могут приходить после сборки заказа — игнорируйте их.

Уведомления приходят только для FBS и rFBS отправлений:

```
{
"message_type"  "TYPE_CUTOFF_DATE_CHANGED"
:
,
"posting_number"  "24219509-0020-2"
:
,
"new_cutoff_date"  "2021-11-24T07:00:00Z"
:
,
"old_cutoff_date"  "2021-11-21T10:00:00Z"
:
,
"warehouse_id"  0
:
,
"seller_id"  15
:
}
```

Параметр

Тип

Формат

Описание

string

—

```
Тип уведомления — TYPE_CUTOFF_DATE_CHANGED .
message_type
posting_number
```

string

—

Номер отправления.

date-

```
new_cutoff_date
```

string

Новые дата и время отгрузки в формате UTC.

time

date-

```
old_cutoff_date
```

string

Предыдущие дата и время отгрузки в формате UTC.

time

Идентификатор склада, на котором хранятся товары для этого

```
warehouse_id
```

integer

int64

отправления.

Параметр

Тип

Формат

Описание

```
seller_id
```

integer

int64

Идентификатор продавца.

### Изменение даты доставки отправления

Уведомление, которое отправляет Ozon:

Уведомление будет приходить, если товары в отправлении продаются по схемам rFBS и FBS.

Поля new_delivery_date_begin и new_delivery_date_end могут приходить пустыми из-за удаления интервала

доставки. Дождитесь назначения новой даты — после этого придёт новое уведомление.

```
{
"message_type"  "TYPE_DELIVERY_DATE_CHANGED"
:
,
"posting_number"  "24219509-0020-2"
:
,
"new_delivery_date_begin"  "2021-11-24T07:00:00Z"
:
,
"new_delivery_date_end"  "2021-11-24T16:00:00Z"
:
,
"old_delivery_date_begin"  "2021-11-21T10:00:00Z"
:
,
"old_delivery_date_end"  "2021-11-21T19:00:00Z"
:
,
"warehouse_id"  0
:
,
"seller_id"  15
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_DELIVERY_DATE_CHANGED .
posting_number
```

string

—

Номер отправления.

```
new_delivery_date_begi
```

date-

string

Новые дата и время начала доставки в формате UTC.

```
n
```

time

date-

```
new_delivery_date_end
```

string

Новые дата и время окончания доставки в формате UTC.

time

```
old_delivery_date_begi
```

date-

string

Предыдущие дата и время начала доставки в формате UTC.

```
n
```

time

date-

```
old_delivery_date_end
```

string

Предыдущие дата и время окончания доставки в формате UTC.

time

Идентификатор склада, на котором хранятся товары для этого

```
warehouse_id
```

integer

int64

отправления.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Создание или обновление товара

Уведомление, которое отправляет Ozon:

```
{
"message_type"  "TYPE_CREATE_OR_UPDATE_ITEM"
:
,
"seller_id"  0
:
,
"offer_id"  "string"
:
,
"product_id"  0
:
,
"is_error"  false
:
,
"changed_at"  "2022-09-01T14:15:22Z"
:
}
```

Параметр

Тип

Формат

Описание

```
seller_id
```

integer

int64

Идентификатор продавца.

```
message_type
```

string

—

```
Тип уведомления — TYPE_CREATE_OR_UPDATE_ITEM .
offer_id
```

string

—

Идентификатор товара в системе продавца — артикул.

```
product_id
```

integer

int64

Идентификатор товара в системе Ozon — product_id .

Признак, что при создании или обновлении товара возникли

ошибки:

```
is_error
```

boolean

—

- true — были ошибки, товар не создан или не обновлён;

- false — товар создан или обновлён без ошибок.

date-

```
changed_at
```

string

Дата и время изменения.

time

### Создание товара

Отправка пуш-уведомлений TYPE_CREATE_ITEM будет приостановлена 15 июля 2023 года.

Настройте свой сервис для получения уведомлений TYPE_CREATE_OR_UPDATE_ITEM.

Уведомление, которое отправляет Ozon:

```
{
"message_type"  "TYPE_CREATE_ITEM"
:
,
"seller_id"  0
:
,
"offer_id"  "string"
:
,
"product_id"  0
:
,
"is_error"  false
:
,
"changed_at"  "2021-09-01T14:15:22Z"
:
}
```

Параметр

Тип

Формат

Описание

```
seller_id
```

integer

int64

Идентификатор продавца.

```
message_type
```

string

—

Тип уведомления — TYPE_CREATE_ITEM .

```
offer_id
```

string

—

Идентификатор товара в системе продавца — артикул.

```
product_id
```

integer

int64

Идентификатор товара в системе Ozon — product_id .

Признак, что при создании товара возникли ошибки:

```
is_error
```

boolean

—

- true — были ошибки, товар не создан;

- false — товар создан без ошибок.

```
changed_at
```

string

date-time

Дата и время изменения.

### Обновление товара

Отправка пуш-уведомлений TYPE_UPDATE_ITEM будет приостановлена 15 июля 2023 года.

Настройте свой сервис для получения уведомлений TYPE_CREATE_OR_UPDATE_ITEM.

Уведомление, которое отправляет Ozon:

```
{
"message_type"  "TYPE_UPDATE_ITEM"
:
,
"seller_id"  0
:
,
"offer_id"  "string"
:
,
"product_id"  0
:
,
"is_error"  false
:
,
"changed_at"  "2021-09-01T14:15:22Z"
:
}
```

Параметр

Тип

Формат

Описание

```
seller_id
```

integer

int64

Идентификатор продавца.

```
message_type
```

string

—

Тип уведомления — TYPE_UPDATE_ITEM .

```
offer_id
```

string

—

Идентификатор товара в системе продавца — артикул.

```
product_id
```

integer

int64

Идентификатор товара в системе Ozon — product_id .

Признак, что при обновлении товара возникли ошибки:

```
is_error
```

boolean

—

- true — были ошибки, товар не создан;

- false — товар создан без ошибок.

```
changed_at
```

string

date-time

Дата и время изменения.

### Изменение остатков на складах продавца

Уведомление, которое отправляет Ozon:

```
{
"message_type"  "string"
:
,
"seller_id"  0
:
,
"items"
: [
{
"product_id"  0
:
,
"sku"  0
:
,
"updated_at"  "2021-09-01T14:15:22Z"
:
,
"stocks"
: [
{
"warehouse_id"  0
:
,
"present"  0
:
,
"reserved"  0
:
}
]
}
]
}
```

Параметр

Тип

Формат

Описание

```
seller_id
```

integer

int64

Идентификатор продавца.

```
message_type
```

string

—

```
Тип уведомления — TYPE_STOCKS_CHANGED .
items
```

array

—

Массив с данными товаров.

```
updated_at
```

string

date-time

Дата и время изменения.

```
sku
```

integer

int64

SKU товара при работе по схемам FBS или rFBS.

```
product_id
```

integer

int64

Идентификатор товара в системе Ozon — product_id .

```
stocks
```

array

—

Массив с данными по остаткам товара.

```
warehouse_id
```

integer

int64

Идентификатор склада.

```
present
```

integer

int64

Общее количество товара на складе.

Параметр

Тип

Формат

Описание

```
reserved
```

integer

int64

Количество зарезервированных товаров на складе.

### Новое сообщение в чате

```
{
"message_type"  "TYPE_NEW_MESSAGE"
:
,
"chat_id"  "b646d975-0c9c-4872-9f41-8b1e57181063"
:
,
"chat_type"  "Buyer_Seller"
:
,
"message_id"  "3000000000817031942"
:
,
"created_at"  "2022-07-18T20:58:04.528Z"
:
,
"user"
: {
"id"  "115568"
:
,
"type"  "Сustomer"
:
},
"data"
: [
"Текст сообщения"
],
"seller_id"  "7"
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

Тип уведомления — TYPE_NEW_MESSAGE .

```
chat_id
```

string

—

Идентификатор чата.

Тип чата:

- Seller_Support — чат с поддержкой.

- Buyer_Seller — чат с покупателем.

```
• Seller_Notification  — уведомления Ozon.
```

- Seller_API_Updates — обновления Seller API.

```
• Seller_API_Notifications  — уведомления Seller API.
chat_type
```

string

—

```
• Seller_Notification_Logistics  — уведомления Ozon
```

Доставка.

- Buyer_Seller_Select — чат с покупателем Селект.

```
• Seller_Personal_Manager_Unity_Crm  — чат с персональным
```

менеджером Ozon.

```
• Seller_Business_Development_Group  — чат с группой
```

бизнес-развития Ozon.

```
message_id
```

string

—

Идентификатор сообщения.

date-

```
created_at
```

string

Дата создания сообщения.

time

```
user
```

object

—

Информация об отправителе сообщения.

```
id
```

string

—

Идентификатор отправителя.

Тип отправителя:

- Customer — покупатель.

```
type
```

string

—

- Support — поддержка.

```
• NotificationUser  — Ozon.
```

array of

```
data
```

—

Массив с содержимым сообщения в формате Markdown.

string

```
seller_id
```

integer

int64

Идентификатор продавца.

### Сообщение в чате изменено

```
{
"message_type"  "TYPE_UPDATE_MESSAGE"
:
,
"chat_id"  "b646d975-0c9c-4872-9f41-8b1e57181063"
:
,
"chat_type"  "Buyer_Seller"
:
,
"message_id"  "3000000000817031942"
:
,
"created_at"  "2022-07-18T20:58:04.528Z"
:
,
"updated_at"  "2022-07-18T20:59:04.528Z"
:
,
"user"
: {
"id"  "115568"
:
,
"type"  "Сustomer"
:
},
"data"
: [
"Текст сообщения"
],
"seller_id"  "7"
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_UPDATE_MESSAGE .
chat_id
```

string

—

Идентификатор чата.

Тип чата:

- Seller_Support — чат с поддержкой.

- Buyer_Seller — чат с покупателем.

```
• Seller_Notification  — уведомления Ozon.
```

- Seller_API_Updates — обновления Seller API.

```
• Seller_API_Notifications  — уведомления Seller API.
chat_type
```

string

—

```
• Seller_Notification_Logistics  — уведомления Ozon
```

Доставка.

- Buyer_Seller_Select — чат с покупателем Селект.

```
• Seller_Personal_Manager_Unity_Crm  — чат с персональным
```

менеджером Ozon.

```
• Seller_Business_Development_Group  — чат с группой
```

бизнес-развития Ozon.

```
message_id
```

string

—

Идентификатор сообщения.

date-

```
created_at
```

string

Дата создания сообщения.

time

date-

string

Дата изменения сообщения.

```
updated_at
```

time

```
user
```

object

—

Информация об отправителе сообщения.

```
id
```

string

—

Идентификатор отправителя.

Тип отправителя:

- Customer — покупатель.

```
type
```

string

—

- Support — поддержка.

```
• NotificationUser  — Ozon.
```

array of

```
data
```

—

Массив с содержимым сообщения в формате Markdown.

string

```
seller_id
```

integer

int64

Идентификатор продавца.

### Ваше сообщение прочитано

```
{
"message_type"  "TYPE_MESSAGE_READ"
:
,
"chat_id"  "b646d975-0c9c-4872-9f41-8b1e57181063"
:
,
"chat_type"  "Buyer_Seller"
:
,
"message_id"  "3000000000817031942"
:
,
"created_at"  "2022-07-18T20:58:04.528Z"
:
,
"user"
: {
"id"  "115568"
:
,
"type"  "Сustomer"
:
},
"last_read_message_id"  "3000000000817031942"
:
,
"seller_id"  "7"
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_MESSAGE_READ .
chat_id
```

string

—

Идентификатор чата.

Тип чата:

- Seller_Support — чат с поддержкой.

- Buyer_Seller — чат с покупателем.

```
• Seller_Notification  — уведомления Ozon.
```

- Seller_API_Updates — обновления Seller API.

```
• Seller_API_Notifications  — уведомления Seller API.
chat_type
```

string

—

```
• Seller_Notification_Logistics  — уведомления Ozon Доставка.
```

- Buyer_Seller_Select — чат с покупателем Селект.

```
• Seller_Personal_Manager_Unity_Crm  — чат с персональным
```

менеджером Ozon.

```
• Seller_Business_Development_Group  — чат с группой бизнес-
```

развития Ozon.

```
message_id
```

string

—

Идентификатор сообщения.

date-

string

Дата создания сообщения.

```
created_at
```

time

```
user
```

object

—

Информация о пользователе, прочитавшем сообщение.

```
id
```

string

—

Идентификатор пользователя.

Тип пользователя:

- Customer — покупатель.

```
type
```

string

—

- Support — поддержка.

```
• NotificationUser  — Ozon.
last_read_message_id
```

string

—

Идентификатор последнего прочитанного сообщения.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Чат закрыт

```
{
"message_type"  "TYPE_CHAT_CLOSED"
:
,
"chat_id"  "b646d975-0c9c-4872-9f41-8b1e57181063"
:
,
"chat_type"  "Buyer_Seller"
:
,
"user"
: {
"id"  "115568"
:
,
"type"  "Сustomer"
:
},
"seller_id"  "7"
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

Тип уведомления — TYPE_CHAT_CLOSED .

```
chat_id
```

string

—

Идентификатор чата.

Тип чата:

- Seller_Support — чат с поддержкой.

- Buyer_Seller — чат с покупателем.

```
• Seller_Notification  — уведомления Ozon.
```

- Seller_API_Updates — обновления Seller API.

```
• Seller_API_Notifications  — уведомления Seller API.
chat_type
```

string

—

```
• Seller_Notification_Logistics  — уведомления Ozon Доставка.
```

- Buyer_Seller_Select — чат с покупателем Селект.

```
• Seller_Personal_Manager_Unity_Crm  — чат с персональным
```

менеджером Ozon.

```
• Seller_Business_Development_Group  — чат с группой бизнес-
```

развития Ozon.

```
user
```

object

—

Информация о пользователе, закрывшем чат.

```
id
```

string

—

Идентификатор пользователя.

Тип пользователя:

- Customer — покупатель.

```
type
```

string

—

- Support — поддержка.

```
• NotificationUser  — Ozon.
seller_id
```

integer

int64

Идентификатор продавца.

### Изменение дерева категорий

```
{
"message_type"  "TYPE_DESCRIPTION_CATEGORY_TREE_CHANGED"
:
,
"changed_at"  "2026-04-07T10:27:55.955Z"
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_DESCRIPTION_CATEGORY_TREE_CHANGED .
changed_at
```

string

date-time

Дата и время изменения.

### Новое отправление FBO

```
{
"message_type"  "TYPE_FBO_POSTING_NEW"
:
,
"posting_number"  "24219509-0020-1"
:
,
"order_number"  "24219509-0020"
:
,
"uuid"  "bf354adc-e404-480c-a037-cf865464f1d9"
:
,
"products"
: [
{
"sku"  147451959
:
,
"quantity"  1
:
}
],
"creation_date"  "2026-04-07T10:27:55.955Z"
:
,
"warehouse_id"  18044249781000
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_FBO_POSTING_NEW .
posting_number
```

string

—

Номер отправления.

```
order_number
```

string

—

Номер заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
products
```

array

—

Информация о товарах.

```
sku
```

integer

int64

Идентификатор товара в системе Ozon — SKU.

```
quantity
```

integer

int64

Количество товара.

```
creation_date
```

string

date-time

Дата и время создания отправления в формате UTC.

```
warehouse_id
```

integer

int64

Идентификатор склада.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Отмена отправления FBO

```
{
"message_type"  "TYPE_FBO_POSTING_CANCELLED"
:
,
"posting_number"  ""0574652831-0001-1"
:
,
"order_number"  "0574652831-0001"
:
,
"uuid"  "bf354adc-e404-480c-a037-cf865464f1d9"
:
,
"products"
: [
{
"sku"  147451959
:
,
"quantity"  1
:
}
],
"old_state"  "posting_transferred_to_courier_service"
:
,
"new_state"  "posting_canceled"
:
,
"cancel_date"  "2026-04-07T10:27:55.955Z"
:
,
"reason"
: {
"id"  537
:
,
"message"  "Не вручен"
:
},
"warehouse_id"  18044249781000
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_FBO_POSTING_CANCELLED .
posting_number
```

string

—

Номер отправления.

```
order_number
```

string

—

Номер заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
products
```

array

—

Информация о товарах.

```
sku
```

integer

int64

Идентификатор товара в системе Ozon — SKU.

```
quantity
```

integer

int64

Количество товара.

```
old_state
```

string

—

Предыдущий статус отправления.

```
new_state
```

string

—

Новый статус отправления: posting_canceled — отменено.

Параметр

Тип

Формат

Описание

date-

```
cancel_date
```

string

Дата и время отмены отправления в формате UTC.

time

```
reason
```

object

—

Информация о причине отмены.

```
id
```

integer

int64

Идентификатор причины отмены.

```
message
```

string

—

Причина отмены.

Идентификатор склада, на котором хранятся товары для этого

integer

int64

```
warehouse_id
```

отправления.

```
seller_id
```

integer

int64

Идентификатор продавца.

Статусы отправлений

```
posting_created  — создано;
posting_packing  — на упаковке;
posting_delivered  — доставлено;
posting_transferring_to_delivery  — передаётся в доставку;
posting_on_way_to_city  — на пути в город;
posting_transferred_to_courier_service  — передаётся курьеру;
posting_returned_to_warehouse  — возвращено на склад;
posting_in_courier_service  — курьер в пути;
posting_on_way_to_pickup_point  — на пути в пункт выдачи;
posting_received  — получено;
posting_in_pickup_point  — в пункте выдачи.
```

### Изменение статуса отправления FBO

Соответствие статусных моделей Seller API и статусов пуш-модели.

Seller API

Push-модель

Статус

Описание

Статус

Описание

Ожидает

```
awaiting_approve
posting_created
```

Создана.

подтверждения.

```
awaiting_packagin
```

Ожидает упаковки.

```
posting_created
```

Создана.

```
g
```

На упаковке.

```
posting_packing
```

Передаётся в

```
awaiting_deliver
```

Ожидает отгрузки.

```
posting_transferring_to_delivery
```

доставку.

```
delivering
```

Доставляется.

```
posting_on_way_to_city
```

На пути в ваш город.

```
posting_transferred_to_courier_servi
```

Передаётся курьеру.

```
ce
posting_returned_to_warehouse
```

Возвращено на склад.

```
posting_in_courier_service
```

Курьер в пути.

На пути в пункт

```
posting_on_way_to_pickup_point
```

выдачи.

```
posting_in_pickup_point
```

В пункте выдачи.

```
delivered
```

Доставлено.

```
posting_delivered
```

Доставлено.

```
posting_received
```

Получено.

```
cancelled
```

Отменено.

```
posting_canceled
```

Отменено.

```
{
"message_type"  "TYPE_FBO_POSTING_STATE_CHANGED"
:
,
"posting_number"  "68498622-0815-1"
:
,
"order_number"  "68498622-0815"
:
,
"uuid"  "bf354adc-e404-480c-a037-cf865464f1d9"
:
,
"new_state"  "posting_transferring_to_delivery"
:
,
"changed_state_date"  "2026-04-07T10:27:55.955Z"
:
,
"warehouse_id"  18044249781000
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_FBO_POSTING_STATE_CHANGED .
posting_number
```

string

—

Номер отправления.

```
order_number
```

string

—

Номер заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
new_state
```

string

—

Новый статус отправления.

date-

```
changed_state_date
```

string

Дата и время изменения статуса отправления в формате UTC.

time

Идентификатор склада, на котором хранятся товары для этого

```
warehouse_id
```

integer

int64

отправления.

```
seller_id
```

integer

int64

Идентификатор продавца.

Статусы отправлений

```
posting_created  — создано;
posting_packing  — на упаковке;
posting_delivered  — доставлено;
posting_transferring_to_delivery  — передаётся в доставку;
posting_on_way_to_city  — на пути в город;
posting_transferred_to_courier_service  — передаётся курьеру;
posting_returned_to_warehouse  — возвращено на склад;
posting_in_courier_service  — курьер в пути;
posting_on_way_to_pickup_point  — на пути в пункт выдачи;
posting_received  — получено;
posting_in_pickup_point  — в пункте выдачи.
```

### Изменение даты доставки отправления FBO

```
{
"message_type"  "TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED"
:
,
"posting_number"  "24219509-0020-1"
:
,
"order_number"  "24219509-0020"
:
,
"uuid"  "bf354adc-e404-480c-a037-cf865464f1d9"
:
,
"old_delivery_date_begin"  "2026-04-07T10:27:55.955Z"
:
,
"old_delivery_date_end"  "2026-04-07T10:27:55.955Z"
:
,
"new_delivery_date_begin"  "2026-04-07T10:27:55.955Z"
:
,
"new_delivery_date_end"  "2026-04-07T10:27:55.955Z"
:
,
"warehouse_id"  18044249781000
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED .
```

Параметр

Тип

Формат

Описание

```
posting_number
```

string

—

Номер отправления.

```
order_number
```

string

—

Номер заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
old_delivery_date_begi
```

date-

string

Предыдущие дата и время начала доставки в формате UTC.

time

```
n
```

date-

```
old_delivery_date_end
```

string

Предыдущие дата и время окончания доставки в формате UTC.

time

```
new_delivery_date_begi
```

date-

string

Новые дата и время начала доставки в формате UTC.

```
n
```

time

date-

string

Новые дата и время окончания доставки в формате UTC.

```
new_delivery_date_end
```

time

Идентификатор склада, на котором хранятся товары для этого

```
warehouse_id
```

integer

int64

отправления.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Изменение остатков на складах Ozon

```
{
"message_type"  "TYPE_FBO_STOCKS_CHANGED"
:
,
"sku"  325119272
:
,
"stocks"
: {
"new_present"  321
:
,
"new_reserved"  12
:
,
"old_present"  321
:
,
"old_reserved"  12
:
,
},
"updated_at"  "2026-04-07T10:27:55.955Z"
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_FBO_STOCKS_CHANGED .
sku
```

integer

int64

Идентификатор товара в системе Ozon — SKU.

```
stocks
```

array

—

Массив с данными по остаткам товара.

```
new_reserved
```

integer

int64

Количество зарезервированных товаров на складе.

```
new_present
```

integer

int64

Общее количество товара на складе.

```
old_reserved
```

integer

int64

Предыдущее количество зарезервированных товаров на складе.

```
old_present
```

integer

int64

Предыдущее общее количество товара на складе.

```
updated_at
```

string

date-time

Дата и время изменения.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Новый заказ

```
{
"message_type"  "TYPE_ORDER_NEW"
:
,
"order_number"  "24219509-0020-1"
:
,
"order_id" 35452597966
:
,
"uuid"  "bf354adc-e404-480c-a037-cf865464f1d9"
:
,
"created_at"  "2026-04-07T10:27:55.955Z"
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

Тип уведомления — TYPE_ORDER_NEW .

```
order_number
```

string

—

Номер заказа.

```
order_id
```

integer

int64

Идентификатор заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
creation_date
```

string

date-time

Дата и время создания заказа в формате UTC.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Отмена заказа

```
{
"message_type"  "TYPE_ORDER_CANCELLED"
:
,
"order_number"  "24219509-0020-1"
:
,
"order_id" 35452597966
:
,
"uuid"  "bf354adc-e404-480c-a037-cf865464f1d9"
:
,
"cancelled_at"  "2026-04-07T10:27:55.955Z"
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_ORDER_CANCELLED .
order_number
```

string

—

Номер заказа.

```
order_id
```

integer

int64

Идентификатор заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
cancelled_at
```

string

date-time

Дата и время отмены заказа в формате UTC.

```
seller_id
```

integer

int64

Идентификатор продавца.

### Изменение статуса заказа

```
{
"message_type"  "TYPE_ORDER_STATE_CHANGED"
:
,
"order_number"  "24219509-0020-1"
:
,
"order_id" 35452597966
:
,
"uuid"  "7d65308d-79f2-41d1-8d3e-f2eff46cc3d0"
:
,
"old_state"  "order_in_delivery"
:
,
"new_state"  "order_done"
:
"updated_at"  "2026-04-07T10:27:55.955Z"
:
,
"seller_id"  7376
:
}
```

Параметр

Тип

Формат

Описание

```
message_type
```

string

—

```
Тип уведомления — TYPE_ORDER_STATE_CHANGED .
order_number
```

string

—

Номер заказа.

```
order_id
```

integer

int64

Идентификатор заказа.

```
uuid
```

string

—

Уникальный идентификатор события.

```
old_state
```

string

—

Предыдущий статус заказа.

```
new_state
```

string

—

Новый статус заказа.

```
updated_at
```

string

date-time

Дата и время изменения статуса заказа в формате UTC.

```
seller_id
```

integer

int64

Идентификатор продавца.

## Ответ вашего сервиса

### Если уведомление получено успешно

При успешной обработке уведомления сервис должен вернуть ответ с кодом HTTP 200:

```
{
"result"  true
:
}
```

Параметр

Тип

Формат

Описание

```
result
```

boolean

—

Уведомление получено.

### Если произошла ошибка

При ошибке во время обработки уведомления сервис должен вернуть ответ с кодом HTTP из групп 4xx или 5xx:

```
{
"error"
: {
"code"  "ERROR_UNKNOWN"
:
,
"message"  "ошибка"
:
,
"details"  null
:
}
}
```

Параметр

Тип

Формат

Описание

```
error
```

object

—

Информация об ошибке.

Параметр

Тип

Формат

Описание

Код ошибки:

- ERROR_UNKNOWN — неизвестная ошибка.

- ERROR_PARAMETER_VALUE_MISSED — не указано значение одного или нескольких

```
code
```

string

—

параметров.

```
• ERROR_REQUEST_DUPLICATED  — дублирующийся запрос.
message
```

string

—

Детальное описание ошибки.

```
details
```

string

—

Дополнительная информация.

## Мониторинг доступности уведомлений

Отслеживаем доступность URL-адреса, на который отправляются пуш-уведомления. Если сервис отвечает слишком

долго или перестаёт отвечать, приостанавливаем отправку уведомлений.

Проверка доступности

Каждую ночь анализируем время ответа вашего URL-адреса по каждому подключённому типу уведомлений.

По результатам проверки покажем статус доступности URL-адреса в личном кабинете и в методах Seller API:

Доступен — быстро отвечает. Скорость ответа до 1500 мс.

Нестабилен — отвечает дольше обычного. Скорость ответа от 1500 до 2500 мс.

Недоступен — не отвечает или отвечает долго. Скорость ответа от 2500 мс.

На проверке — недавно менялся или повторно подключался. Статус изменится после следующей проверки.

Автоотключение уведомлений

Если три дня подряд статус URL-адреса остаётся «Недоступен», отключим отправку пуш-уведомлений на этот адрес.

Продолжим отправлять уведомления на другие ваши URL-адреса.

Уведомления о проблемах

Когда статус вашего URL-адреса становится «Нестабилен» или «Недоступен», отправляем сообщение в чат Seller API в

личном кабинете и в чат с уведомлениями Seller API.

Подробнее о настройке чата Seller API на платформе разработчиков Ozon for dev

В сообщении укажем:

URL-адрес с проблемой;

тип уведомлений;

рекомендации по исправлению.

Контроль и оптимизация уведомлений

1. Следите за статусом в личном кабинете или в методах Seller API. Перейдите в раздел Настройки → Интеграции →

Push уведомления или используйте метод /v1/notification/list. В таблице напротив каждого URL-адреса покажем

статус доступности.

2. Проверьте настройки вашего сервиса. Убедитесь, что сервис:

стабильно обрабатывает входящие запросы от Ozon;

отвечает в течение 1500 мс;

не имеет проблем с производительностью.

3. Увеличьте пропускную способность сервиса. Если ваш сервис не справляется с объёмом входящих уведомлений,

рассмотрите возможность масштабирования или оптимизации обработки запросов.

4. Проверьте логи. Просмотрите историю отправок, чтобы определить, какие типы уведомлений вызывают проблемы.

5. Протестируйте приём пуш-уведомлений. Убедитесь, что ваш URL-адрес корректно принимает и обрабатывает

тестовые запросы.

Когда все проблемы устранены, подключите уведомления снова.

Подробнее о повторном подключении

## Обновления

Следите за обновлениями документации на платформе для разработчиков Ozon for dev.

### 28 сентября 2026

Метод

Изменение

Добавили параметр items.price.declared_price в ответ метода.

Добавили параметр items.declared_price в ответ метода.

Добавили параметр prices.declared_price в запрос метода.

### 25 сентября 2026

Метод

Изменение

```
Добавили значение SHOWCASE_SELECT_ACTIVE  параметра filter.visibility  в запросе
```

методов.

—

Добавили раздел Лимиты.

### 24 сентября 2026

Метод

Изменение

В ответе метода:

Отметили устаревшим параметр result.total — отключим его 23 ноября

2026 года. Переключитесь на result.total_items .

```
Добавили параметр result.total_items .
```

В ответе методов:

Отметили устаревшим параметр total — отключим его 23 ноября 2026 года.

Переключитесь на total_items .

Добавили параметр total_items .

label/create

Перенесли методы из бета-раздела в основной.

label/get

label/create

С 5 октября 2026 года методы будут возвращать новые этикетки для отправлений

FBS.

label/create

label/get

### 23 сентября 2026

Метод

Изменение

Добавили бета-метод для получения списка пунктов возврата

складов rFBS и rFBS Express.

Добавили параметр

```
delivery_method.return_settings.return_point_id  в запрос
```

метода.

```
Добавили параметр return_settings.return_point_id  в запрос
```

method/update

метода.

Добавили параметр settings.return_point в ответ метода.

### 22 сентября 2026

Метод

Изменение

add/products/candidates

Добавили новые версии методов для работы с акциями Ozon.

add/products/update

add/products/delete

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

add/products/candidates

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

add/products/delete

Метод устаревает и будет отключён 13 октября 2026 года. Переключитесь на

add/products/update

Добавили параметр postings.scanit в ответ методов.

Добавили параметр result.scanit в ответ метода.

Обновили описание параметра barcode в запросе метода.

Метод устаревает и будет отключён 2 ноября 2026 года. Переключитесь на

Добавили новую версию метода для создания задания на формирование

label/create

этикеток.

Метод

Изменение

Методы устаревают и будут отключены 2 ноября 2026 года. Переключитесь

label/create

на /v3/posting/fbs/package-label/create.

Добавили новую версию метода для получения файла с этикетками.

Метод устаревает и будет отключён 2 ноября 2026 года. Переключитесь на

В разделе Порядок работы с методами обновили методы для работы с

—

этикетками.

### 17 сентября 2026

Метод

Изменение

В ответе метода:

обновили описание параметра errors.error_message ;

```
добавили параметры errors.items_validation.limit  и
errors.items_validation.supply_id .
```

Добавили параметр error_details в ответ метода.

order/content/update/status

### 16 сентября 2026

Метод

Изменение

Добавили бета-методы для работы с локальностью продаж.

Обновили описание метода.

### 14 сентября 2026

Метод

Изменение

Обновили описание параметров items.old_price и items.price в запросе

методов.

```
Обновили описание параметров items.min_price , items.old_price  и
```

items.price в ответе метода.

Обновили описание параметров prices.min_price ,

```
prices.min_price_for_auto_actions_enabled , prices.old_price , prices.price  и
prices.price_strategy_enabled  в запросе метода.
Обновили описание параметров items.price.marketing_seller_price ,
items.price.min_price , items.price.old_price  и items.price.price  в ответе
```

метода.

Метод

Изменение

```
Обновили описание параметров prices.customer_price , prices.price  и
prices.price_indexes  в ответе метода.
```

Добавили бета-метод для получения информации о сравнении категорий.

### 11 сентября 2026

Метод

Изменение

Отметили устаревшими параметры prices.auto_action_enabled и

```
prices.manage_elastic_boosting_through_price  в запросе метода.
```

Добавили бета-метод для обновления информации о доставке сторонней транспортной

dlv/edit

компанией.

```
Добавили параметры items.inbound_replenishment , items.outbound_pending_delivery ,
items.outbound_returns_picking , items.outbound_returns_ready_to_ship ,
items.outbound_returns_return_to_seller  и items.stock_not_being_sold  в ответ
```

метода.

### 10 сентября 2026

Метод

Изменение

Отметили устаревшим параметр items.geo_names в запросе метода.

### 8 сентября 2026

Метод

Изменение

Обновили пример запроса и ответа метода.

Обновили описание метода.

Обновили описание параметра option.name в ответе метода.

Обновили описание параметра params.accordance_type в запросе методов.

Обновили описание параметра params.name в ответе методов.

Тариф «Эконом» отключён, удалили методы из документации.

Обновили описание параметра images в запросе метода.

Обновили описание метода.

Обновили описание параметра items.images в запросе методов.

Обновили описание методов.

### 7 сентября 2026

Метод

Изменение

Добавили параметр prices.weight_index в ответ метода.

### 4 сентября 2026

Метод

Изменение

Добавили параметр products.action_price в запрос метода.

Обновили описание параметра products.discount_percent в запросе метода.

### 3 сентября 2026

Метод

Изменение

Добавили новую версию метода для загрузки или обновления изображений

товара.

Метод устаревает и будет отключён 1 октября 2026 года. Переключитесь на

Добавили бета-метод для получения отчёта о списанных товарах.

goods

Обновили описание параметра params.files.name в запросе методов.

В разделе Частые ошибки добавили описание ошибки file extension is not

—

available для метода /v2/product/certificate/create.

### 2 сентября 2026

Метод

Изменение

28 сентября 2026 года отключим параметры page и page_size в запросе

метода. Используйте параметры last_id и limit .

Обновили описание параметра last_id в запросе метода.

```
Добавили параметры availability_statuses , limit , offset  и sort_dir  в
```

запрос метода.

```
Добавили параметры availability_status_thresholds , total_count ,
urls.availability_status , urls.availability_status_date ,
urls.disable_reason , urls.problematic_type  и urls.reason_details  в ответ
```

метода.

В разделе Авторизация через API-ключ → Как получить API-ключ обновили

—

срок действия API-ключа.

### 1 сентября 2026

Метод

Изменение

Добавили бета-методы для работы с зависимыми

характеристиками.

attributes/values

### 27 августа 2026

Метод

Изменение

Добавили раздел Пуш-уведомления → Мониторинг доступности уведомлений.

—

В раздел Пуш-уведомления → Как подключить добавили информацию о просмотре статуса и повторном

подключении пуш-уведомлений.

### 19 августа 2026

Метод

Изменение

Обновили описание параметра id в запросе метода.

Обновили описание метода.

### 18 августа 2026

Метод

Изменение

Обновили описание параметра chats.chat.chat_type в ответе метода.

В разделе Пуш-уведомления → Новое сообщение в чате, Сообщение в чате изменено, Ваше

—

сообщение прочитано и Чат закрыт обновили значения параметра chat_type .

### 14 августа 2026

Метод

Изменение

Добавили методы для работы с контактными данными продавца для курьера.

### 13 августа 2026

Метод

Изменение

В запросе метода:

```
добавили параметры placement_zone  и unmarked_stocks_only ;
```

обновили описание параметра item_tags .

Метод

Изменение

В ответе метода:

```
добавили параметры items.waiting_docs_to_export_stock_count  и
items.placement_zone ;
```

обновили описание параметра items.item_tags .

Добавили параметр splits.commissions в ответ метода.

В запросе методов:

пометили устаревшим параметр product_id ;

добавили параметр skus .

В запросе метода:

пометили устаревшим параметры page и page_size ;

добавили параметры last_id и limit .

Добавили параметр result.items.sku в ответ метода.

Метод устаревает и будет отключён 31 августа 2026 года.

Добавили бета-методы для создания сертификатов.

### 11 августа 2026

Метод

Изменение

Добавили бета-методы для работы с актами FBO.

order/act/accept/status

Отметили устаревшим параметр returns.return_method_description в ответе

метода.

Методы устарели, удалили их из документации. Используйте

### 6 августа 2026

Метод

Изменение

Пометили обязательным параметр deletion_sku_mode в запросе метода.

### 4 августа 2026

Метод

Изменение

Обновили описание параметра types в запросе методов.

Обновили описание параметра urls.types.type в ответе метода.

Обновили описание параметра types.type в ответе метода.

```
Обновили описание параметра postings.products.is_marketplace_buyout  в ответе
```

методов.

```
Обновили описание параметра result.postings.products.is_marketplace_buyout  в
```

ответе методов.

```
Обновили описание параметра result.products.is_marketplace_buyout  в ответе
```

методов.

Обновили описание метода.

В раздел Пуш-уведомления → Уведомления, которые отправляет Ozon добавили

```
уведомления TYPE_FBO_POSTING_NEW , TYPE_FBO_POSTING_CANCELLED ,
```

—

```
TYPE_FBO_POSTING_STATE_CHANGED , TYPE_FBO_POSTING_DELIVERY_DATE_CHANGED ,
TYPE_FBO_STOCKS_CHANGED , TYPE_ORDER_NEW , TYPE_ORDER_CANCELLED  и
TYPE_ORDER_STATE_CHANGED .
```

### 30 июля 2026

Метод

Изменение

Обновили описание параметров date и last_id в запросе метода.

В ответе метода:

```
добавили параметр accruals.container_fees ;
обновили описание параметров accruals.accrued_category  и last_id .
```

### 28 июля 2026

Метод

Изменение

Добавили параметр result.additional_data в ответ метода.

```
Добавили параметр result.reports.additional_data  в ответ метода.
```

Обновили описание параметра message в теле ошибки 400 метода.

Добавили бета-метод для получения позаказного отчёта о реализации товаров.

### 22 июля 2026

Метод

Изменение

Добавили параметр filter.integration_type_flow в запрос метода.

```
Добавили параметры result.postings.integration_type_flow  и
result.postings.sorting_center  в ответ метода.
```

Метод

Изменение

Добавили параметр filter.integration_type_flow в запрос метода.

```
Добавили параметры postings.integration_type_flow  и postings.sorting_center  в
```

ответ метода.

```
Добавили параметры result.integration_type_flow  и result.sorting_center  в
```

ответ метода.

```
Добавили параметры result.postings.integration_type_flow  и
result.postings.sorting_center  в ответ метода.
Добавили параметры postings.integration_type_flow  и postings.sorting_center  в
```

ответ метода.

С 17 августа 2026 года метод возвращает информацию об остатках в реальном

времени.

### 21 июля 2026

Метод

Изменение

```
Обновили описание параметра accruals.posting.products.delivery.services  в ответе
```

day

метода.

В разделе Частые ошибки добавили описание ошибки PRODUCT_IS_ARCHIVED для метода

—

### 16 июля 2026

Метод

Изменение

Обновили описание метода.

Обновили тело ошибки метода.

### 14 июля 2026

Метод

Изменение

Методы устаревают и будут отключены 8 сентября 2026 года. Переключитесь на

### 10 июля 2026

Метод

Изменение

Удалили параметр items.images360 из запроса метода.

Пометили обязательным параметр items.offer_id в запросе метода.

Обновили описание метода.

Метод

Изменение

Удалили параметр images360 из запроса метода.

Удалили параметр result.pictures.is_360 из ответа метода.

Обновили описание метода.

Удалили параметр items.photo_360 из ответа метода.

Удалили параметр items.images360 из ответа метода.

Обновили описание методов.

Метод устаревает и будет отключён 31 августа 2026 года. Переключитесь на

Метод устаревает и будет отключён 31 августа 2026 года. Переключитесь на

Метод устаревает и будет отключён 31 августа 2026 года. Переключитесь на

Метод устаревает и будет отключён 31 августа 2026 года. Переключитесь на

### 9 июля 2026

Метод

Изменение

Добавили параметр filter.skus в запрос метода.

Добавили параметр result.items.sku в ответ метода.

Обновили описание параметра state в ответе методов.

Обновили тело ошибки метода.

В разделе Порядок работы с методами → Управляйте заказами FBO, FBS и rFBS → Схема

—

FBO добавили информацию о распределении товаров по транспортным грузоместам FBO.

### 8 июля 2026

Метод

Изменение

Перенесли методы из бета-раздела в основной.

Метод

Изменение

### 7 июля 2026

Метод

Изменение

Добавили параметр result.external_order в ответ методов.

Метод устаревает и будет отключён 7 сентября 2026. Переключитесь на

### 2 июля 2026

Метод

Изменение

Добавили новый метод для для получения информации о стоках на

warehouse/fbo

складах FBO.

### 1 июля 2026

Метод

Изменение

Добавили бета-метод для получения информации об отправлении FBP по идентификатору.

### 30 июня 2026

Метод

Изменение

Обновили описание параметра chats.chat.chat_type в ответе

метода.

Добавили параметр

```
delivery_method.is_courier_phone_same_as_warehouse  в запрос
```

метода.

```
Добавили параметр is_courier_phone_same_as_warehouse  в запрос
```

method/update

метода.

Метод

Изменение

Добавили параметры

```
postings.financial_data.products.posting_commission  и
postings.financial_data.products.return_commission  в ответ
```

метода.

### 25 июня 2026

Метод

Изменение

Обновили описание параметра page_size в запросе метода.

Обновляем корневой TLS/SSL-сертификат GlobalSign — вместо него будем

—

использовать HARICA.

Подробнее о переходе на HARICA на платформе разработчиков Ozon for dev

### 22 июня 2026

Метод

Изменение

Обновили описание метода.

Обновили описание параметра item_placement.placement в запросе метода.

### 19 июня 2026

Метод

Изменение

Метод устаревает и будет отключён 19 августа 2026 года. Переключитесь на

order/timeslot/get

order/timeslot/update

Обновили описание параметра errors в ответе методов.

order/timeslot/status

Добавили новую версию метода для получения списка доступных интервалов

order/timeslot/list

поставки.

Добавили раздел Пуш-уведомления → Уведомления, которые отправляет Ozon →

Изменение дерева категорий.

—

```
Добавили тип уведомления TYPE_DESCRIPTION_CATEGORY_TREE_CHANGED  в раздел Пуш-
```

уведомления → Уведомления, которые отправляет Ozon.

### 18 июня 2026

Метод

Изменение

Метод устарел, удалили его из документации. Используйте /v1/draft/crossdock/create,

Метод

Изменение

Метод устарел, удалили его из документации. Используйте /v2/draft/create/info.

Метод устарел, удалили его из документации. Используйте /v2/draft/timeslot/info.

Метод устарел, удалили его из документации. Используйте /v2/draft/supply/create.

Метод устарел, удалили его из документации. Используйте

### 11 июня 2026

Метод

Изменение

Добавили бета-методы для работы с транспортными грузоместами FBO.

order/create

order/status

В разделе Частые ошибки добавили описание ошибок:

```
method is not allowed  — для всех методов;
token must be issued for seller, not oauth-client  и method is not
allowed: OZON logistic is disabled  — для метода
```

—

```
not available with existing subscription  — для метода
```

### 9 июня 2026

Метод

Изменение

Добавили параметр operation_limits в ответ метода.

Метод устарел, удалили его из документации. Используйте /v3/chat/list.

Перенесли метод из раздела Загрузка и обновление товаров в раздел Атрибуты и

zone/info

характеристики Ozon.

```
Изменили название параметра accruals.type_id  на accruals.accrual_id  в ответе
```

метода.

### 4 июня 2026

Метод

Изменение

```
Добавили параметры delivery_method.delivery_costs.min_weight ,
delivery_method.delivery_costs.max_weight ,
delivery_method.delivery_costs.min_order_price ,
delivery_method.delivery_costs.max_order_price  и
delivery_method.delivery_costs.seller_payment  в запрос метода.
Удалили параметры delivery_method.delivery_costs.max_amount ,
delivery_method.delivery_costs.min_amount  и
delivery_method.delivery_costs.percent .
Добавили параметры delivery_costs.min_weight ,
delivery_costs.max_weight , delivery_costs.min_order_price ,
delivery_costs.max_order_price  и delivery_costs.seller_payment  в
```

method/update

запрос метода.

```
Удалили параметры delivery_costs.max_amount ,
delivery_costs.min_amount  и delivery_costs.percent .
```

### 3 июня 2026

Метод

Изменение

Обновили описание параметра id в запросе метода.

### 2 июня 2026

Метод

Изменение

Обновили описание параметра company.currency в ответе метода.

Обновили описание метода.

### 1 июня 2026

Метод

Изменение

Добавили описание метода.

Обновили описание методов.

cluster/create

Перенесли метод из бета-раздела в основной.

В разделе Порядок работы с методами → Управляйте заказами FBO, FBS и rFBS →

—

Схема FBO → Создать заявку на поставку обновили информацию о создании заявки на

поставку по схеме FBO.

### 28 мая 2026

Метод

Изменение

Обновили описание параметров items.marketing_actions ,

```
items.marketing_actions.actions , items.marketing_actions.actions.date_from ,
items.marketing_actions.actions.date_to , items.marketing_actions.actions.title  и
items.marketing_actions.actions.value  в ответе метода.
```

Обновили описание параметров

```
delivery_details.direct_details.timeslot_details.timeslot.timeslot_end ,
delivery_details.direct_details.timeslot_details.timeslot.timeslot_start ,
delivery_details.drop_off_point.timeslot.timeslot_end  и
delivery_details.drop_off_point.timeslot.timeslot_start  в ответе методов.
```

Обновили описание параметров

```
items.delivery_details.direct_details.timeslot_details.timeslot.timeslot_end ,
items.delivery_details.direct_details.timeslot_details.timeslot.timeslot_start ,
items.delivery_details.drop_off_point.timeslot.timeslot_end  и
items.delivery_details.drop_off_point.timeslot.timeslot_start  в ответе методов.
```

### 26 мая 2026

Метод

Изменение

```
Обновили описание параметров orders.supplies.storage_warehouse  и
orders.supplies.storage_warehouse.warehouse_id  в ответе метода.
```

Обновили описание параметров supplies.storage_warehouse и

```
supplies.storage_warehouse.warehouse_id  в ответе метода.
```

discrepancy/pdf

Перенесли методы из бета-раздела в основной.

Обновили описание параметра file_content в ответе методов.

В разделе Частые ошибки обновили описание ошибки

—

```
FLAMMABLE_ONLY_ON_SELF_OR_PROVIDER_DELIVERY  для метода /v2/products/stocks.
```

### 22 мая 2026

Метод

Изменение

Обновили описание параметров item_placement в запросе метода и

```
items.seller_item_placement  в ответе метода.
```

order/content/update

Обновили описание параметра errors в ответе методов.

order/content/update/status

```
Добавили параметр delivery_methods.tpl_dropoff_point  в ответ метода.
```

Метод устарел, удалили его из документации. Используйте /v2/cargoes/create/info.

—

В разделе Частые ошибки добавили описание ошибок SELLER_NO_CONTRACT_FAILED ,

```
error_attribute_values_empty , error_attribute_values_out_of_range ,
missing_dimension , VALUE_MAX_LIMIT , EMPTY_REQUIRED ,
```

Метод

Изменение

```
description_category_invalid , description_category_has_no_description_type ,
description_category_is_legacy , levels_category_not_found ,
description_category_is_empty , description_type_is_empty , vat_invalid ,
name_too_long , all_image_failed , invalid_rich_content_json ,
all_image_unprocessed , price_out_of_range , old_price_less_than_price ,
min_auto_price_too_big , min_auto_price_too_small  и
price_less_than_min_auto_price  для метода /v3/product/import.
```

### 21 мая 2026

Метод

Изменение

Обновили описание метода.

Добавили параметр is_auto_assembly в запрос методов.

integrated/create

В разделе Частые ошибки добавили описание ошибок IsAutoAssembly

```
property is not available for c&c delivery method  для метода
```

—

```
/v1/warehouse/erfbs/update и label not allowed for delivered postings
```

для метода /v2/posting/fbs/package-label.

### 20 мая 2026

Метод

Изменение

Обновили описание параметра skus в запросе метода.

Обновили пример запроса.

### 19 мая 2026

Метод

Изменение

Обновили описание параметра dimension в запросе метода.

Обновили описание методов.

Методы устарели, удалили их из документации.

### 15 мая 2026

Метод

Изменение

Обновили описание метода.

### 14 мая 2026

Метод

Изменение

Обновили описание параметра items.promotions.type в ответе метода.

Обновили описание параметра items.promotions.type в запросе метода.

Добавили описание метода.

Обновили описание параметра order_id в запросе метода.

Обновили описание метода.

### 12 мая 2026

Метод

Изменение

Добавили параметр result.auto_add_dates в ответ метода.

Добавили бета-методы для работы с автодобавлением товаров в акции.

Добавили бета-метод для получения информации о видимости товаров.

Добавили описание метода.

Обновили описание параметра prices.min_price в запросе метода.

Обновили описание параметра statuses.expired_at в ответе метода.

### 6 мая 2026

Метод

Изменение

Добавили бета-метод для получения начислений по отправлениям.

Добавили бета-метод для получения справочника начислений по отправлениям.

Добавили бета-метод для получения начислений по отправлению за день.

Метод устаревает и будет отключён 6 июля 2026 года. Переключитесь на

Метод устаревает и будет отключён 6 июля 2026 года. Переключитесь на

### 5 мая 2026

Метод

Изменение

Обновили описание параметра filter.visibility в запросе методов.

postings

Добавили бета-методы для работы с грузоместами FBS.

```
Добавили параметры result.postings.container  и
result.postings.container_sort_type  в ответ методов.
Добавили параметры postings.container  и postings.container_sort_type  в
```

ответ методов.

```
Добавили параметры result.container  и result.container_sort_type  в
```

ответ метода.

Обновили описание методов.

### 30 апреля 2026

Метод

Изменение

Добавили новую версию метода для получения списка отправлений FBO.

Метод устаревает и будет отключён 1 июня 2026 года. Переключитесь на

Добавили новую версию метода для получения списка необработанных отправлений

FBS.

Метод устаревает и будет отключён 1 июня 2026 года. Переключитесь на

Добавили новую версию метода для получения списка отправлений FBS.

Метод устаревает и будет отключён 1 июня 2026 года. Переключитесь на

Добавили новую версию метода для получения списка отправлений, по которым

нужно загрузить коды цифровых товаров.

Метод устаревает. Переключитесь на /v2/posting/digital/list.

Добавили новый бета-метод для получения списка отправлений FBP.

Обновили описание параметра available_actions в ответе метода.

Добавили параметр with.able_to_set_price в запрос метода.

```
Добавили параметры result.is_able_to_set_price  и result.is_presorted  в ответ
```

Метод

Изменение

метода.

```
Добавили параметр filter.last_changed_status_date  в запрос метода.
Добавили параметры result.postings.is_presortable ,
result.postings.destination_place_id , result.postings.destination_place_name  и
result.postings.customer.customer_email  в ответ метода.
Добавили параметры result.postings.is_presortable ,
result.postings.destination_place_id , result.postings.destination_place_name  и
result.postings.customer.customer_email  в ответ метода.
```

Изменили название параметров orders.data_filling_deadline на

```
orders.data_filling_deadline_utc  и orders.drop_off_warehouse  на
orders.dropoff_warehouse  в ответе метода.
```

### 29 апреля 2026

Метод

Изменение

В ответе метода:

```
добавили параметр prices.price_indexes ;
```

пометили устаревшим параметр prices.discount_percent ;

обновили описание параметра prices.customer_price .

### 28 апреля 2026

Метод

Изменение

Обновили описание параметра min_order_value в запросе метода.

### 24 апреля 2026

Метод

Изменение

off/product/validate

```
Добавили значения NO_SALES , SURPLUS  и AVAILABILITY_IS_EMPTY  параметра
rejected_items.rejection_reasons  в ответе методов.
```

up/product/validate

```
Добавили значения NO_SALES , SURPLUS  и AVAILABILITY_IS_EMPTY  параметра
error.bundle_errors.errors  в ответе методов.
```

### 20 апреля 2026

Метод

Изменение

Обновили название метода.

Добавили параметр filter в запрос метода.

```
Добавили параметры comments.deviation_reason , comments.dislikes_amount ,
comments.is_published , comments.is_rejected  и comments.likes_amount  в ответ
```

метода.

Добавили новую версию метода для удаления комментария на отзыв.

Метод устаревает и будет отключён в будущем. Переключитесь на

Добавили новую версию метода для изменения статуса отзывов.

Метод устаревает и будет отключён в будущем. Переключитесь на /v2/review/change-

status.

Добавили новую версию метода для получения количества отзывов по статусам.

Метод устаревает и будет отключён в будущем. Переключитесь на /v2/review/count.

Добавили новую версию метода для получения информации об отзыве.

Метод устаревает и будет отключён в будущем. Переключитесь на /v2/review/info.

Добавили новую версию метода для получения списка отзывов.

Метод устаревает и будет отключён в будущем. Переключитесь на /v2/review/list.

Добавили параметр answers.status_publication в ответ метода.

Добавили параметры sort_dir и limit в запрос метода.

Добавили параметр has_next в ответ метода.

### 17 апреля 2026

Метод

Изменение

В разделе Пуш-уведомления → Новое сообщение в чате, Сообщение в чате изменено, Ваше сообщение

—

прочитано и Чат закрыт обновили значения параметра chat_type .

### 15 апреля 2026

Метод

Изменение

Обновили название метода.

Обновили описание параметра ozon_logistics_enabled в ответе метода.

```
Обновили описание параметров result.analytics_data.client_delivery_date_begin
и result.analytics_data.client_delivery_date_end  в ответе методов.
```

Обновили описание параметров

```
result.postings.analytics_data.client_delivery_date_begin  и
result.postings.analytics_data.client_delivery_date_end  в ответе методов.
```

Обновили описание параметра chats.chat.chat_type в ответе метода.

Метод

Изменение

Изменили название раздела Порядок работы с методами → Управляйте заказами

FBO, FBS, rFBS и FBP → Ozon Логистика на Порядок работы с методами →

—

Управляйте заказами FBO, FBS, rFBS и FBP → Ozon Доставка.

Изменили название раздела Ozon Логистика на Ozon Доставка.

### 14 апреля 2026

Метод

Изменение

Акция недоступна для использования, удалили методы из

документации.

discount

### 8 апреля 2026

Метод

Изменение

Добавили бета-методы для работы с пуш-уведомлениями.

### 7 апреля 2026

Метод

Изменение

Добавили параметр warehouses.pause_at в ответ метода.

Обновили значение параметра type в ответе метода.

Добавили бета-методы для включения и выключения паузы на rFBS-складе.

### 6 апреля 2026

Метод

Изменение

Добавили бета-метод для настройки видимости товара на витрине Ozon и Ozon

Селект.

Добавили параметр result.tariffication_steps в ответ метода.

Метод

Изменение

```
Добавили параметр result.postings.tariffication_steps  в ответ методов.
```

### 31 марта 2026

Метод

Изменение

Обновили описание методов.

### 26 марта 2026

Метод

Изменение

Обновили описание методов.

### 24 марта 2026

Метод

Изменение

Метод устаревает и будет отключён 7 апреля 2026 года. Переключитесь на

warehouse/fbs

Метод устаревает и будет отключён 7 апреля 2026 года. Переключитесь на

Метод устаревает и будет отключён 7 апреля 2026 года. Переключитесь на

Перенесли метод из бета-раздела в основной.

Обновили описание метода.

В описание метода добавили информацию о загрузке главного изображения

для Ozon Селект.

### 17 марта 2026

Метод

Изменение

time/details

Обновили описание методов.

time/summary

Обновили описание метода. Добавили лимиты для параметра update_offer_id

в запрос метода.

Обновили описание параметров

```
result.analytics_data.client_delivery_date_begin  и
result.analytics_data.client_delivery_date_end  в ответе методов.
```

Обновили описание параметров

```
result.analytics_data.client_delivery_date_begin  и
result.analytics_data.client_delivery_date_end  в ответе метода.
```

Обновили описание параметров

```
result.postings.analytics_data.client_delivery_date_begin  и
result.postings.analytics_data.client_delivery_date_end  в ответе методов.
```

### 13 марта 2026

Метод

Изменение

Обновили описание параметра chats.chat.chat_type в ответе метода.

Обновили описание параметра messages.user.type в ответе метода.

### 12 марта 2026

Метод

Изменение

Добавили бета-метод для получения списка складов Ozon.

### 11 марта 2026

Метод

Изменение

Обновили описание параметра chats.chat.chat_type в ответе метода.

### 10 марта 2026

Метод

Изменение

point/list

Обновили описание параметров search.types в запросе и points.type в

ответе методов.

point/list

```
Обновили описание параметра return_mile_settings.return_point.type  в
```

ответе метода.

Обновили описание метода.

В ответе метода:

- добавили параметр result.file_url ;

- пометили устаревшим параметр result.file_guid .

Метод устаревает и будет отключён 10 апреля 2026 года. Переключитесь на

В разделе Частые ошибки добавили описание ошибки

—

INCORRECT_OVH_FOR_POSTING для метода /v4/posting/fbs/ship.

Добавили параметр splits.items.offer_id в запрос метода.

Добавили параметр items.offer_id в запрос метода и

```
splits.items.offer_id  в ответ метода.
```

Добавили бета-метод для получения информации о макролокальных

кластерах.

Добавили параметр macrolocal_cluster_ids в запрос метода.

Добавили параметр items.macrolocal_cluster_id в ответ метода.

### 6 марта 2026

Метод

Изменение

Изменили название раздела Порядок работы с методами → Участвуйте в акциях на Порядок работы с

методами → Участвуйте в акциях Ozon.

—

Изменили название раздела Акции на Акции Ozon.

Добавили раздел Порядок работы с методами → Работа с акциями продавца.

Добавили описание раздела Акции продавца.

### 4 марта 2026

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 2 марта 2026

Метод

Изменение

condition

discount

discount

with-condition

Добавили бета-методы для работы с акциями продавца.

discount

discount

Методы устаревают и будут отключены 16 марта 2026 года.

- Добавили параметр clusters.supply_type в ответ метода.

```
• Добавили значение MINIMUM_VOLUME_IN_LITRES_INVALID  параметра
errors.error_reasons  в ответе метода.
• Обновили описание параметров clusters.warehouses.storage_warehouse
и clusters.warehouses.total_rank  в ответе метода.
```

- Добавили параметр supply_type в запрос метода.

```
• Добавили значение INVALID_REQUESTED_CLUSTER_IDS  параметра
```

error_reason в ответе метода.

- Обновили описание параметров selected_cluster_warehouses и

```
selected_cluster_warehouses.storage_warehouse_id  в запросе метода.
```

- Добавили параметр supply_type в запрос метода.

```
• Добавили значение MINIMUM_VOLUME_IN_LITRES_INVALID  параметра
```

error_reasons в ответе метода.

- Обновили описание параметра

```
selected_cluster_warehouses.storage_warehouse_id  в запросе метода.
Добавили параметр supplies.macrolocal_cluster_id  в ответ метода.
```

- Добавили параметр supplies.macrolocal_cluster_id в ответ метода.

- Обновили описание параметра vehicle.value в ответ метода.

Перенесли методы из бета-раздела в основной.

### 26 февраля 2026

Метод

Изменение

Обновили описание параметра items.is_kgt в ответе метода.

Добавили бета-метод для получения акта о расхождениях по отгрузке FBS.

discrepancy/pdf

В разделах Порядок работы с методами → Управляйте заказами FBO, FBS, rFBS и FBP →

Схема FBS Стандарт и Порядок работы с методами → Управляйте заказами FBO, FBS,

—

rFBS и FBP → Схема FBS PickUp с доверительной приёмкой обновили порядок работы с

PDF-документами.

В разделе Порядок работы с методами → Получите информацию о складах обновили

—

описание работы с методами.

### 24 февраля 2026

Метод

Изменение

```
Обновили описание параметра delivery_info.drop_off_warehouse.warehouse_type  в
```

запросе методов.

cluster/create

### 20 февраля 2026

Метод

Изменение

—

В разделе Авторизация через API-ключ обновили информацию о работе с API-ключом.

Добавили параметр expires_at в ответ метода.

Метод устарел, удалили его из документации. Используйте /v3/chat/history.

### 17 февраля 2026

Метод

Изменение

Пометили обязательными параметры bundle_id , delivery_details ,

```
delivery_details.driver_name , delivery_details.timeslot_start ,
delivery_details.vehicle_number , delivery_details.vehicle_type ,
package_units_count  и warehouse_id  в запросе метода.
```

Пометили обязательными параметры driver_name , row_version , supply_id ,

```
vehicle_number  и vehicle_type  в запросе метода.
```

Пометили обязательными параметры row_version , supply_id и

timeslot_start в запросе метода.

Пометили обязательными параметры bundle_id , interval_end ,

```
interval_start  и warehouse_id  в запросе метода.
```

Метод

Изменение

Пометили обязательными параметры bundle_id , delivery_details ,

```
delivery_details.timeslot_start , package_units_count  и warehouse_id  в
```

запросе метода.

Пометили обязательным параметр supply_id в запросе методов.

Пометили обязательными параметры skus , skus.count , skus.sku и

off/product/validate

warehouse_id в запросе методов.

up/product/validate

Пометили обязательными параметры row_version и supply_id в запросе

методов.

Пометили обязательными параметры bundle_id , delivery_details ,

```
delivery_details.timeslot_start , delivery_details.tracking_number ,
delivery_details.transport_company_name , package_units_count  и
```

warehouse_id в запросе метода.

Пометили обязательными параметры row_version , supply_id ,

```
tracking_number  и transport_company_name  в запросе метода.
```

Пометили обязательными параметры bundle_id , delivery_details ,

```
delivery_details.drop_off_date , delivery_details.drop_off_point_id ,
delivery_details.drop_off_province_uuid , package_units_count  и
```

warehouse_id в запросе метода.

Пометили обязательными параметры drop_off_date , drop_off_point_id ,

```
drop_off_province_uuid , row_version  и supply_id  в запросе метода.
```

Пометили обязательным параметр warehouse_id в запросе метода.

Пометили обязательными параметры page_size , province_uuid и

warehouse_id в запросе метода.

Пометили обязательными параметры drop_off_point_id , province_uuid и

off/point/timetable

warehouse_id в запросе метода.

Пометили обязательными параметры bundle_id , delivery_details ,

```
delivery_details.address , delivery_details.comment ,
delivery_details.date , delivery_details.sender_name ,
delivery_details.sender_phone , package_units_count  и warehouse_id  в
```

запросе метода.

Пометили обязательными параметры row_version , supply_id ,

```
pickup_details , pickup_details.address , pickup_details.comment ,
pickup_details.date , pickup_details.sender_name  и
pickup_details.sender_phone  в запросе метода.
```

### 16 февраля 2026

Метод

Изменение

Метод устаревает и будет отключён 20 марта 2026 года. Переключитесь на

Методы устаревают и будут отключены 20 марта 2026 года. Переключитесь на

available/list

Метод

Изменение

Добавили параметр result.addressee.pin в ответ метода.

### 12 февраля 2026

Метод

Изменение

Пометили обязательным параметр return_id в запросе метода.

Пометили обязательными параметры base64_content и name в запросе

метода.

Пометили обязательным параметр filter в запросе метода.

Пометили обязательными параметры filter.processed_at_from и

```
filter.processed_at_to  в запросе метода.
```

Пометили обязательными параметры date.from и date.to в запросе

метода.

Пометили обязательным параметр date в запросе методов.

Пометили обязательным параметр limit в запросе методов.

Пометили обязательными параметры stairways , stairways.enabled ,

```
stairways.sku , stairways.stairway , stairways.stairway.steps ,
```

quantity/set

```
stairways.stairway.steps.discount , stairways.stairway.steps.quantity
и stairways.stairway.steps.step  в запросе метода.
```

quantity/get

Пометили обязательным параметр skus в запросе методов.

Пометили обязательными параметры timeslot ,

```
timeslot.from_in_timezone  и timeslot.to_in_timezone  в запросе
```

метода.

Пометили обязательным параметр address_coordinates в запросе

метода.

Пометили обязательным параметр warehouse_id в запросе методов.

Пометили обязательным параметр page в запросе метода.

Пометили обязательным параметр supply_id в запросе метода.

Пометили обязательным параметр count в запросе метода.

Пометили обязательными параметры driver_name , row_version ,

```
supply_id , vehicle_number  и vehicle_type  в запросе метода.
```

Пометили обязательными параметры row_version , supply_id и

timeslot_start в запросе метода.

Пометили обязательными параметры interval_end , interval_start и

supply_id в запросе метода.

Пометили обязательным параметр supply_id в запросе методов.

Метод

Изменение

Пометили обязательными параметры drop_off_date , row_version и

supply_id в запросе метода.

Пометили обязательными параметры drop_off_point_id , province_uuid

и warehouse_id в запросе метода.

Пометили обязательными параметры pickup_details ,

```
pickup_details.sender_name , pickup_details.sender_phone ,
row_version  и supply_id  в запросе метода.
```

Пометили обязательным параметр file_uuid в запросе метода.

Пометили обязательными параметры code и supply_id в запросе

метода.

Пометили обязательным параметр count в запросе метода.

Пометили обязательным параметр order_number в запросе метода.

Пометили обязательным параметр posting_number в запросе метода.

Пометили обязательным параметр client_phone в запросе метода.

Пометили обязательным параметр limit в запросе метода.

warehouse/fbs

Обновили описание методов.

Обновили описание метода.

Обновили описание методов.

Обновили описание параметра draft_id в запросе методов.

Обновили описание параметра draft_id в запросе метода.

### 10 февраля 2026

Метод

Изменение

Обновили описание параметра filter.visibility в запросе методов.

### 9 февраля 2026

Метод

Изменение

```
Отметили устаревшим параметр orders.supplies.storage_warehouse.arrival_date  в
```

ответе метода.

```
Отметили устаревшим параметр supplies.storage_warehouse.arrival_date  в ответе
```

метода.

Обновили описание параметра delivery_method_id в запросе метода.

Обновили описание параметра filter.delivery_method_id в запросе метода.

Метод

Изменение

Изменили название метода.

```
Пометили обязательными параметры delivery_schema , splits.delivery_method ,
splits.delivery_method.delivery_method_id , splits.delivery_method.delivery_type ,
splits.delivery_method.timeslot_id , splits.delivery_method.logistic_date_range ,
splits.delivery_method.logistic_date_range.from ,
splits.delivery_method.logistic_date_range.to , splits.items , items.price ,
items.quantity , items.sku , splits.warehouse_id , delivery.courier.city ,
delivery.courier.country , delivery.courier.house_number  и
delivery.pick_up.map_point_id  в запросе метода.
```

### 5 февраля 2026

Метод

Изменение

Пометили обязательными параметры product_id и certificate_id в

запросе метода.

Пометили обязательным параметр barcode в запросе метода.

Пометили обязательными параметры cancel_reason_id и

posting_number в запросе метода.

Пометили обязательным параметр limit в запросе метода.

Пометили обязательными параметры cargo_ids и supply_id в

запросе метода.

Пометили обязательным параметр operation_id в запросе метода.

Пометили обязательным параметр supply_ids в запросе метода.

Пометили обязательными параметры order_id , supply_id , items ,

```
items.quant , items.quantity  и items.sku  в запросе метода.
```

Пометили обязательным параметр operation_id в запросе метода.

Пометили обязательными параметры posting_number , products ,

```
products.product_id , products.exemplars  и
products.exemplars.exemplar_id  в запросе метода.
```

Пометили обязательным параметр posting_number в запросе методов.

or-get

Пометили обязательными параметры posting_number ,

```
products.product_id  и products.exemplars  в запросе метода.
```

Пометили обязательными параметры carriage_id и posting_numbers

в запросе метода.

Пометили обязательным параметр carriage_id в запросе метода.

Пометили обязательным параметр filter.carriage_id в запросе

методов.

Пометили обязательными параметры sort_dir , filter.cutoff_from и

```
filter.cutoff_to  в запросе метода.
```

Пометили обязательными параметры filter.cutoff_from и

```
filter.cutoff_to  в запросе метода.
```

### 3 февраля 2026

Метод

Изменение

Обновили описание параметра result.report_type в ответе метода.

Обновили описание параметра report_type в запросе метода.

Обновили описание параметра result.reports.report_type в ответе метода.

### 2 февраля 2026

Метод

Изменение

Перенесли методы из бета-раздела в основной.

method/update

Метод

Изменение

Обновили описание параметра delivery_method_id в

запросе методов.

### 27 января 2026

Метод

Изменение

В разделах Порядок работы с методами → Обновите цены и остатки товаров и Порядок

—

работы с методами → Управляйте заказами FBO, FBS, rFBS и FBP обновили описание

работы с методами.

Обновили описание метода.

### 26 января 2026

Метод

Изменение

```
Добавили параметры result.fact_delivery_date  и
result.financial_data.products.customer_currency_code  в ответ методов.
```

Добавили параметр

```
result.postings.financial_data.products.customer_currency_code  в ответ методов.
```

### 23 января 2026

Метод

Изменение

Добавили бета-методы для работы с автоутилизацией.

Добавили бета-метод для получения списка заявок на скидку.

Метод устаревает и будет отключён в будущем. Переключитесь на

### 22 января 2026

Метод

Изменение

Обновили описание параметра visibility в запросе метода.

products/create

Обновили описание методов.

supplies/create

В запросе метода:

обновили описание параметра splits.items.price ;

Метод

Изменение

пометили обязательными параметры splits.items.price ,

```
splits.items.price.currency_code  и splits.items.price.units .
```

Обновили описание метода.

Обновили описание параметра available_actions в ответе метода.

Метод устаревает и будет отключён 22 марта 2026 года. Переключитесь на

status

Обновили описание метода.

Обновили описание параметра id в запросе метода.

Метод устаревает и будет отключён 22 марта 2026 года. Переключитесь на

Обновили описание параметра result.act_type в ответе метода.

В разделах Порядок работы с методами → Управляйте заказами FBO, FBS, rFBS

и FBP → Схема FBS Стандарт и Порядок работы с методами → Управляйте

—

заказами FBO, FBS, rFBS и FBP → Схема FBS PickUp с доверительной приёмкой

обновили порядок работы с файлами.

### 20 января 2026

Метод

Изменение

Метод устарел, удалили его из документации.

by-seller

В разделах Порядок работы с методами → Управляйте заказами FBO, FBS, rFBS и FBP →

Схема rFBS Crossborder и Порядок работы с методами → Управляйте заказами FBO, FBS,

—

rFBS и FBP → Схема rFBS Crossborder с интегрированной службой доставки обновили

описание работы с методами.

### 16 января 2026

Метод

Изменение

Добавили бета-методы для работы с заявками на поставку FBO.

Добавили бета-метод для получения информации о грузоместах.

```
Добавили параметры orders.order_tags.is_pickup  и
orders.order_tags.seller_warehouse_id  в ответ метода.
```

order/timeslot/update

Обновили описание параметра errors в ответе методов.

Обновили описание параметра result.report_type в ответе метода.

Метод

Изменение

Обновили описания параметров report_type в запросе метода и

```
result.reports.report_type  в ответе метода.
```

### 15 января 2026

Метод

Изменение

Добавили бета-метод для получения подробной информации о цене товаров.

### 13 января 2026

Метод

Изменение

Методы устарели, удалили их из документации.

### 30 декабря 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

Обновили описание параметра prices.vat в запросе метода.

Обновили описание параметра items.vat в запросе методов.

### 26 декабря 2025

Метод

Изменение

Параметр returns.client_name в ответе метода устаревает, отключим его 2 февраля 2026

года.

### 25 декабря 2025

Метод

Изменение

Добавили метод для получения отчёта о стоимости размещения по

products/create

товарам.

Добавили метод для получения отчёта о стоимости размещения по

поставкам.

Добавили бета-метод для получения информации о зонах размещения

товаров по их SKU перед поставкой.

Обновили описание параметра result.report_type в ответе метода.

Обновили описание параметра report_type в запросе метода.

Обновили описание параметра result.reports.report_type в ответе

метода.

```
Удалили параметры result.header.doc_amount  и
result.header.vat_amount  из ответа метода.
Удалили параметры header.doc_amount  и header.vat_amount  из ответа
```

метода.

```
Обновили описание параметра products.exemplars.marks.check_status  в
```

ответе метода.

Обновили описание параметра items.price.retail_price в ответе

метода.

Обновили описание параметра result.items.quants в ответе метода.

Метод устарел, удалили его из документации.

### 23 декабря 2025

Метод

Изменение

Обновили описание параметра product_id в запросе метода.

### 18 декабря 2025

Метод

Изменение

Добавили бета-метод для вызова курьера на забор отгрузки pick-up со

склада FBS.

Добавили бета-метод для отмены вызова курьера на забор отгрузки pick-

up со склада FBS.

Добавили бета-метод для получения списка складов для планирования

отгрузок курьеру.

Метод

Изменение

Добавили методы для работы с чеками.

### 16 декабря 2025

Метод

Изменение

Добавили бета-метод для работы с историей отгрузок курьерам.

Обновили описание параметра status в ответе метода.

Добавили параметр has_next в ответ метода.

### 15 декабря 2025

Метод

Изменение

Добавили бета-метод для получения списка складов, на которых есть

products

товары с ограничениями по доставке rFBS.

Добавили бета-метод для получения списка товаров с ограничениями по

доставке rFBS.

### 12 декабря 2025

Метод

Изменение

Добавили бета-метод для получения отчёта о балансе.

Обновили описание метода.

statement/list

```
Удалили значение ReturnCompensated  параметра filter.visual_status_name  в
```

запросе метода.

### 11 декабря 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 9 декабря 2025

Метод

Изменение

Обновили описание параметра ratings в запросе метода.

—

Добавили описание раздела Управление кодами маркировки и сборкой заказов для FBS/rFBS.

### 5 декабря 2025

Метод

Изменение

Добавили бета-метод для получения информации по возвратным настройкам rFBS

method/return/settings/get

и rFBS Express.

В разделах Работа со складами rFBS Express → Доставка «Партнёры Ozon и

—

Работа со складами rFBS Express → Доставка «Вы или сторонняя служба»

обновили порядок работы со складами rFBS Express.

### 4 декабря 2025

Метод

Изменение

```
Добавили параметр clusters.macrolocal_cluster_id  в ответ метода.
```

Добавили бета-метод для получения подробной информации о заявке на

поставку.

point/list

Добавили бета-методы для работы с FBS-складами.

point/list

Добавили параметр return_point_id в запрос метода.

Метод устаревает и будет отключён 22 декабря 2025 года. Переключитесь

на /v1/analytics/stocks.

В разделе Порядок работы с методами → Работа с FBS-складами обновили

—

порядок работы с с FBS-складами.

### 2 декабря 2025

Метод

Изменение

Добавили бета-метод для работы с остатками на складах продавца.

warehouse/fbs

Добавили бета-метод для получения методов доставки на складе.

Добавили бета-метод для получения методов доставки и отгрузок.

Методы устаревают и будут отключены с 2 февраля 2026 года.

Переключитесь на /v2/carriage/delivery/list.

Метод

Изменение

Метод устаревает и будет отключён в будущем. Переключитесь на

warehouse/fbs

Метод устаревает и будет отключён в будущем. Переключитесь на

### 27 ноября 2025

Метод

Изменение

```
Добавили параметры result.products.current_boost ,
result.products.price_min_elastic , result.products.price_max_elastic ,
result.products.min_boost  и result.products.max_boost .
```

В ответе методов:

обновили описание параметра

```
result.analytics_data.payment_type_group_name ;
добавили параметры result.analytics_data.client_delivery_date_begin ,
result.analytics_data.client_delivery_date_end  и result.substatus .
```

В ответе метода:

обновили описание параметра

```
result.analytics_data.payment_type_group_name ;
добавили параметры result.analytics_data.client_delivery_date_begin  и
result.analytics_data.client_delivery_date_end .
```

В ответе методов:

обновили описание параметра

```
result.postings.analytics_data.payment_type_group_name ;
```

добавили параметры

```
result.postings.analytics_data.client_delivery_date_begin  и
result.postings.analytics_data.client_delivery_date_end .
```

Добавили параметры limit и cursor в запрос метода.

Добавили параметр cursor в ответ метода.

Добавили параметры limit и offset в запрос метода.

Пометили устаревшим параметр items.stocks.warehouse_ids в ответе метода.

Обновили описание параметра warehouseId в запросе метода.

Добавили описание методов.

order

Обновили описание параметра reasons.id в ответе методов.

posting

Добавили описание метода.

Обновили описание параметра client_phone в запросе метода.

Добавили описание методов.

Метод

Изменение

В разделе Порядок работы с методами → Управляйте заказами FBO, FBS, rFBS и

—

FBP → Ozon Логистика обновили порядок работы с возвратами.

### 25 ноября 2025

Метод

Изменение

Обновили описание метода.

—

Добавили раздел Порядок работы с методами → Работа со складами rFBS Express.

### 21 ноября 2025

Метод

Изменение

—

Добавили бета-методы для работы с FBP поставками.

Обновили описание параметра items.stocks.type в ответе метода.

### 20 ноября 2025

Метод

Изменение

Добавили бета-методы для работы с индексом ошибок FBS и rFBS.

Добавили параметр filter.compensation_status_id в запрос метода.

Добавили параметр returns.compensation_status в ответ метода.

### 18 ноября 2025

Метод

Изменение

Обновили пример запроса.

Добавили параметр result.expires_at в ответ метода.

Добавили параметр result.reports.expires_at в ответ метода.

Обновили описание метода.

Обновили описание параметра editing_errors в ответе метода.

### 13 ноября 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 12 ноября 2025

Метод

Изменение

Параметр items.marketing_price в ответе метода устарел, удалили его из документации.

Параметр price.marketing_price в ответе метода устарел, удалили его из документации.

### 11 ноября 2025

Метод

Изменение

Добавили бета-метод для получения информации о кабинете продавца.

Добавили бета-метод для получения информации о подключении продавца к Ozon

logistics/info

Логистике.

### 7 ноября 2025

Метод

Изменение

Добавили бета-метод для получения статуса проверки электронной ТТН

на прослеживаемой перевозке FBS.

Добавили бета-метод для получения списка незаполненных атрибутов

для прослеживаемых товаров.

Добавили бета-метод для разделения заказа на прослеживаемые

отправления.

```
Добавили параметр result.postings.require_blr_traceable_attrs  в
```

ответ метода.

```
Добавили параметр result.require_blr_traceable_attrs  в ответ
```

метода.

Добавили параметр filter.is_blr_traceable в запрос метода.

Добавили параметр all_blr_traceable в запрос метода.

Добавили параметр all_blr_traceable в ответ метода.

Добавили раздел Порядок работы с методами → Схема FBS с

—

электронными ТТН.

### 6 ноября 2025

Метод

Изменение

method/update

Добавили бета-методы для работы со складами rFBS

Express.

### 5 ноября 2025

Метод

Изменение

```
Удалили параметр result.financial_data.products.customer_price  из ответа метода.
```

—

Добавили раздел с методами Ozon Логистика.

### 30 октября 2025

Метод

Изменение

Добавили бета-методы для работы с листами подбора FBS.

Перенесли методы из бета-раздела в основной.

order/content/update/validation

Методы устаревают и будут отключены 11 декабря 2025 года.

Переключитесь на новые версии — /v3/supply-order/list и /v3/supply-

order/get.

—

Добавили описание работы с OAuth-токеном.

### 28 октября 2025

Метод

Изменение

Обновили описание параметра filter.is_express в запросе метода.

### 23 октября 2025

Метод

Изменение

Обновили описание параметра accordance_type_code и добавили возможные

значения параметра type_code в запросе метода.

Обновили пример ответа метода.

Добавили параметр offer_id в запрос и параметр results.offer_id в ответ

warehouse/fbs

метода.

Обновили пример метода.

Обновили описание параметра result.substatus в ответе метода.

Обновили описание параметра result.postings.substatus в ответе методов.

Обновили описание методов.

В разделе Частые ошибки добавили описания ошибок POSTING_NOT_FOUND для

—

```
метода /v1/carriage/create и error limiting: acquire limit per item: items
```

limit: limit exceeded для метода /v1/product/import/prices.

### 22 октября 2025

Метод

Изменение

```
Добавили параметр prices.manage_elastic_boosting_through_price  в запрос метода.
```

### 21 октября 2025

Метод

Изменение

Добавили бета-метод для получения отчёта по продажам товаров с

sales/create

маркировкой.

```
Добавили параметр result.postings.shipment_date_without_delay  в ответ
```

методов.

```
Добавили параметр result.shipment_date_without_delay  в ответ метода.
```

В разделе Уведомления, которые отправляет Ozon → Новое отправление

—

обновили пример уведомления для нового отправления.

### 17 октября 2025

Метод

Изменение

Обновили описание методов.

Добавили бета-метод для управления скидкой от количества товаров.

quantity/set

Добавили бета-метод для получения информации о скидке от

quantity/get

количества товаров.

Метод

Изменение

Обновили описание параметра filter.states в запросе метода.

Обновили описание параметра order.state в ответе метода.

### 16 октября 2025

Метод

Изменение

Обновили описание параметра

```
result.financial_data.products.product_id  в ответе метода.
```

Обновили описание параметра

```
result.postings.financial_data.products.product_id  в ответе метода.
```

Обновили описание параметра products.exemplars.marks в ответе

метода.

Обновили описание параметра products.exemplars.marks в запросе

метода.

```
Удалили параметры result.analytics_data  и result.financial_data  из
```

ответа метода.

Обновили описание параметра search в запросе метода.

Обновили описание параметра limit в запросе метода.

### 14 октября 2025

Метод

Изменение

```
Параметры result.header.doc_amount  и result.header.vat_amount  устаревают,
```

отключим их с 14 декабря 2025 года.

Параметры header.doc_amount и header.vat_amount устаревают, отключим их с 14

декабря 2025 года.

### 13 октября 2025

Метод

Изменение

off/timeslot/list

off/timeslot/list

Добавили бета-методы для работы с таймслотами.

up/timeslot/list

up/timeslot/list

```
Добавили параметры warehouses.cut_in_time , warehouses.warehouse_type ,
warehouses.is_comfort  и warehouses.is_express  в ответ метода.
```

Метод

Изменение

Добавили параметры сut_in_time и timeslot_id в запрос методов.

### 10 октября 2025

Метод

Изменение

```
Добавили параметры items.comissions.sales_percent_fbp  и
items.comissions.sales_percent_rfbs  в ответ метода.
Добавили возможное значение SUPER  параметра items.price_indexes.color_index  в
```

ответе метода.

Добавили возможное значение COLOR_INDEX_SUPER параметра

```
items.price_indexes.color_index  в ответе метода.
```

### 8 октября 2025

Метод

Изменение

Добавили новую версию метода для получения информации по установке грузомест.

Метод устаревает и будет отключён в будущем. Переключитесь на новую версию

Добавили параметр cargoes.value.items.offer_id в запрос метода.

Обновили описание параметра items.images в запросе метода.

Обновили описание метода.

Обновили описание параметра images в запросе метода.

Обновили описание метода.

### 7 октября 2025

Метод

Изменение

v1/removal/from-stock/list

Обновили примеры ответов.

v1/removal/from-supply/list

Обновили название метода.

Обновили описание и пример ответа метода.

Обновили описание ответа метода.

Обновили описание параметра sku в ответе метода.

Добавили описания разделов Чаты с покупателями, Аналитические отчёты и

—

Финансовые отчёты.

Добавили методы для работы с поисковыми запросами.

Обновили описание методов.

Метод

Изменение

day

### 6 октября 2025

Метод

Изменение

get

Методы устаревают и будут отключены 3 декабря 2025 года.

Переключитесь на новые версии.

Параметр items.marketing_price устаревает, отключим его 12

ноября 2025 года.

Добавили параметр items.availabilities в ответ метода.

### 3 октября 2025

Метод

Изменение

```
Добавили параметры result.printed_postings_count ,
result.unprinted_postings.msg , result.unprinted_postings.posting_number  и
```

label/get

```
result.unprinted_postings_count  в ответ метода.
```

Параметр items.marketing_price устаревает, отключим его 12 ноября 2025 года.

### 2 октября 2025

Метод

Изменение

Добавили бета-метод для получения остатков на складе FBS и rFBS.

### 29 сентября 2025

Метод

Изменение

```
Добавили параметры filter.warehouse_id , filter.delivery_method_id ,
filter.is_express , with.additional_data , with.analytics_data , with.customer_data  и
with.jewelry_codes  в запрос метода.
```

Параметр items.price.marketing_price устаревает, отключим его 12 ноября 2025 года.

### 24 сентября 2025

Метод

Изменение

Обновили описание параметра last_id в запросе метода.

Обновили пример ответа.

Обновили примеры ответов.

Добавили пример запроса.

Обновили описание параметров result.postings.status ,

```
result.postings.substatus  в ответе методов.
```

В ответе метода:

```
• добавили параметр result.financial_data.products.customer_price ;
```

- обновили описание параметров

```
result.requirements.products_requiring_gtd ,
result.requirements.products_requiring_mandatory_mark ,
result.requirements.products_requiring_jw_uin ,
result.requirements.products_requiring_rnpt , result.status ,
result.substatus  и result.previous_substatus ,
result.financial_data.products.price ,
result.financial_data.products.old_price , result.customer.phone ,
result.addressee.phone  и result.products.is_marketplace_buyout .
```

В ответе метода:

- добавили параметр

```
result.postings.financial_data.products.customer_price ;
```

- обновили описание параметров

```
result.postings.requirements.products_requiring_gtd ,
result.postings.requirements.products_requiring_mandatory_mark ,
result.postings.requirements.products_requiring_jw_uin ,
result.postings.requirements.products_requiring_rnpt ,
result.postings.financial_data.products.price ,
result.postings.financial_data.products.old_price ,
result.postings.customer.phone , result.postings.addressee.phone ,
result.postings.products.is_marketplace_buyout  и
result.postings.products.is_marketplace_buyout .
Обновили описание параметров result.postings.customer.phone ,
result.postings.addressee.phone ,
result.postings.products.is_marketplace_buyout  и
result.products.is_marketplace_buyout  в ответе метода.
```

Обновили описание параметров

```
result.rows.delivery_commission.commission ,
result.rows.delivery_commission.compensation ,
result.rows.return_commission.commission  и
result.rows.return_commission.compensation  в ответе метода.
```

Обновили описание параметров items.available_stock_count и

```
items.valid_stock_count  в ответе метода.
```

Метод

Изменение

```
Обновили описание параметров total.limit , daily_create.limit  и
daily_update.limit  в ответе метода.
```

Обновили описание параметра from_message_id в запросе методов.

```
Обновили описание параметров ratings = rating_reaction_time  и
ratings = rating_average_response_time  в запросе метода.
```

Обновили описание параметров page и page_size в запросе методов.

Обновили пример запроса.

Обновили описание параметра cluster_ids в запросе метода.

Добавили описание метода. Обновили описание параметров

```
clusters.warehouses  и errors.items_validation.reasons  в ответе метода.
```

Обновили описание метода. Обновили описание параметров draft_id и

warehouse_ids в запросе метода. Добавили предупреждение в описание

метода.

Обновили описание параметра items.value.barcode в запросе методов.

Пометили параметр items.price как обязательный в запросе метода.

Обновили описание параметра result.task_id в ответе метода.

Обновили описание параметра items.name в запросе метода.

Обновили описание параметра return_id в запросе метода.

Обновили описание методов.

Обновили описание параметра status в ответе метода.

Добавили лимиты для параметра products в запрос метода.

В разделе Частые ошибки добавили описания ошибок

```
POSTING_NUMBERS_IS_INCORRECT_FOR_COMPANY  для метода
CREATE_ORDER_ERROR_REASON_INVALID_STORAGE_WAREHOUSE  для метода
```

—

```
WAREHOUSE_SCORING_INVALID_REASON_NOT_AVAILABLE_MATRIX ,
ITEM_REJECTION_REASON_OUT_OF_ASSORTMENT  для метода
```

Обновили описание ошибки TRANSITION_IS_NOT_POSSIBLE для метода

### 23 сентября 2025

Метод

Изменение

Добавили бета-метод для проверки нового товарного состава.

В ответе метода:

- добавили параметр new_bundle_id ;

- обновили описание параметра errors .

### 18 сентября 2025

Метод

Изменение

Добавили значение waybill для параметра doc_type в запросе метода.

Обновили описание параметра questions в ответе метода.

### 17 сентября 2025

Метод

Изменение

Добавили бета-метод для получения списка заявок на поставку.

order/list

Добавили бета-метод для получения информации о заявке на поставку.

order/get

Удалили раздел Пуш-уведомления → Уведомления, которые отправляет Ozon → Изменение

ценового индекса товара.

—

Удалили уведомление TYPE_PRICE_INDEX_CHANGED из раздела Пуш-уведомления →

Уведомления, которые отправляет Ozon.

### 15 сентября 2025

Метод

Изменение

Обновили пример запроса.

### 12 сентября 2025

Метод

Изменение

—

Добавили раздел Информация по API-ключу.

Перенесли метод из бета-раздела в основной.

### 10 сентября 2025

Метод

Изменение

v3/posting/fbs/unfulfilled/list

```
Добавили параметры result.postings.products.imei  и
```

v3/posting/fbs/list

```
result.postings.requirements.products_requiring_imei  в ответ метода.
Добавили параметры result.products.has_imei ,
```

v3/posting/fbs/get

```
result.product_exemplars.products.exemplars.imei  и
result.requirements.products_requiring_imei  в ответ метода.
```

Метод

Изменение

v6/fbs/posting/product/exemplar/create-

Обновили описание параметра products.exemplars.marks и добавили

or-get

параметр products.has_imei в ответ метода.

Обновили описание параметра products.exemplars.marks в запросе и

v5/fbs/posting/product/exemplar/validate

ответе метода.

Обновили описание параметра products.exemplars.marks в запросе

v6/fbs/posting/product/exemplar/set

метода.

Обновили описание параметра products.exemplars.marks в ответе

v5/fbs/posting/product/exemplar/status

метода.

### 3 сентября 2025

Метод

Изменение

Методы устарели, удалили их из документации. Используйте /v2/conditional-

cancellation/list.

Метод устарел, удалили его из документации. Используйте /v2/conditional-

cancellation/approve.

Метод устарел, удалили его из документации. Используйте /v2/conditional-

cancellation/reject.

Обновили описание параметра errors в ответе методов.

order/content/update/status

### 2 сентября 2025

Метод

Изменение

Добавили параметр

```
result.postings.requirements.products_requiring_weight  в ответ
```

методов.

Добавили параметры

```
result.product_exemplars.products.exemplars.weight ,
result.products.is_weight_needed , result.products.weight_max ,
result.products.weight_min , result.related_weight_postings  и
result.requirements.products_requiring_weight  в ответ метода.
```

Добавили параметр products.exemplars.weight в запрос и ответ

метода.

```
Добавили параметры products.exemplars.weight ,
products.exemplars.weight_check_status  и
products.exemplars.weight_error_codes  в ответ метода.
```

Добавили параметр products.exemplars.weight в запрос метода.

```
Добавили параметры products.exemplars.weight ,
products.is_weight_needed , products.weight_max  и
```

or-get

```
products.weight_min  в ответ метода.
```

Метод

Изменение

В разделах Порядок работы с методами → Управляйте заказами FBO,

FBS, rFBS и FBP → Схема rFBS Стандарт и Порядок работы с методами

—

→ Управляйте заказами FBO, FBS, rFBS и FBP → Как работать с заказами

с весовыми товарами (rFBS) обновили описание работы с методами.

### 27 августа 2025

Метод

Изменение

В разделе Порядок работы с методами → Работа с FBS-складами описали

—

порядок работы с FBS-складами.

off/list

off/list

Добавили бета-методы для работы с FBS-складами.

Обновили описание метода.

### 15 августа 2025

Метод

Изменение

—

Добавили раздел Premium-методы и перенесли в него методы, доступные с подпиской Premium.

### 14 августа 2025

Метод

Изменение

```
Добавили параметры items.promotions , items.promotions.is_enabled ,
items.promotions.type  и items.sku  в ответ метода.
```

### 8 августа 2025

Метод

Изменение

Обновили описание метода.

### 6 августа 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 5 августа 2025

Метод

Изменение

Обновили описание методов.

Пометили параметр items.is_prepayment_allowed в ответе метода как устаревший.

### 1 августа 2025

Метод

Изменение

Обновили описания методов.

### 30 июля 2025

Метод

Изменение

Добавили бета-метод для получения общей аналитики по среднему

time/summary

времени доставки.

### 28 июля 2025

Метод

Изменение

Добавили новую версию метода для получения информации о чатах по

указанным фильтрам.

Метод устаревает и будет отключён в будущем. Переключитесь на новую

версию /v3/chat/list.

Добавили параметр invoices.buyer_info.name в ответ метода.

sales/json

Обновили описание метода.

Метод

Изменение

В ответе метода:

обновили описание параметра result.status ;

```
удалили параметры result.products.digital_codes  и
result.products.quantity .
```

### 24 июля 2025

Метод

Изменение

Добавили бета-метод для получения отчёта по вывозу и утилизации с поставки FBO.

Добавили бета-метод для получения отчёта по вывозу и утилизации со стока FBO.

Обновили описание методов.

### 23 июля 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 22 июля 2025

Метод

Изменение

Обновили описание параметра result.id в ответе метода.

category/attribute

Обновили описание параметра

```
result.requirements.products_requiring_change_country  в ответе метода.
```

Обновили описание параметров

```
result.postings.requirements.products_requiring_change_country  и
result.postings.financial_data.products.actions  в ответе методов.
Обновили описание параметра result.financial_data.products.actions  в ответе
```

методов.

### 21 июля 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 15 июля 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

### 14 июля 2025

Метод

Изменение

Добавили бета-метод для получения списка ролей и методов по API-ключу.

### 2 июля 2025

Метод

Изменение

```
Добавили параметр result.requirements.products_requiring_change_country  в ответ
```

метода.

Добавили параметр

```
result.postings.requirements.products_requiring_change_country  в ответ метода.
```

Обновили описание метода. Обновили описание параметров dimension и metrics в

запросе метода.

### 1 июля 2025

Метод

Изменение

Добавили бета-метод для получения отчёта по выкупленным товарам.

```
Добавили параметр result.products.is_marketplace_buyout  в ответы
```

методов.

```
Добавили параметр result.postings.products.is_marketplace_buyout  в
```

ответы методов.

Обновили описания методов.

Добавили бета-метод для загрузки кодов цифровых товаров.

Метод

Изменение

Добавили бета-метод для получения списка отправлений, по которым нужно

загрузить коды цифровых товаров.

Добавили бета-метод для обновления количества цифровых товаров.

Методы устарели, удалили их из документации. Используйте методы

В разделе Порядок работы с методами → Загрузите и обновите товары

—

обновили описание работы с методами.

### 26 июня 2025

Метод

Изменение

Методы устарели, удалили их из документации.

Удалили параметры stocks.quant_size из запроса и result.quant_size из ответа метода.

—

В разделе Схема FBS Стандарт обновили порядок работы с эконом-товарами.

### 25 июня 2025

Метод

Изменение

```
В разделе Частые ошибки добавили описание ошибок restore limit exceeded  и total limit exceeded
```

—

для метода /v1/product/unarchive.

### 23 июня 2025

Метод

Изменение

Обновили описание параметра result.shipment_date в ответе метода.

Добавили описание ошибки Stock is updated too frequently и обновили описание ошибки

Частые ошибки

TOO_MANY_REQUESTS для метода /v2/products/stocks.

v1/carriage/create

Обновили описание метода.

### 20 июня 2025

Метод

Изменение

Обновили описание метода.

Метод

Изменение

Обновили описание параметров cluster_ids и

```
drop_off_point_warehouse_id  в запросе метода.
```

Обновили описание параметра warehouse_id в запросе метода.

Перенесли методы из бета-раздела в основной.

В разделе Порядок работы с методами → Управляйте заявками на

—

возврат rFBS-заказов обновили описание работы с методами.

Обновили описание параметра operation_id в запросе метода.

```
Удалили параметры clusters.warehouses.warehouse_id ,
clusters.warehouses.address  и clusters.warehouses.name  из ответа
```

метода.

category/attribute/values/search

Обновили примеры запросов.

### 19 июня 2025

Метод

Изменение

Пометили устаревшим параметр result.strategy_competitor_id в ответе метода.

strategy/product/info

Метод устаревает и будет отключён 3 августа 2025 года. Переключитесь на

cancellation/get

В разделе Управляйте заявками на отмену обновили метод для получения заявок на

—

отмену rFBS.

### 18 июня 2025

Метод

Изменение

```
Добавили параметры data.metrics.exact_impact_share  и
total.exact_impact_share  в ответ метода.
```

time

Пометили устаревшими параметры data.metrics.impact_share и

```
total.impact_share .
```

Добавили параметр data.metrics.exact_impact_share и пометили устаревшим

time/details

```
параметр data.metrics.impact_share  в ответе метода.
```

### 17 июня 2025

Метод

Изменение

```
Добавили параметры items.ads_cluster , items.days_without_sales_cluster ,
items.idc_cluster  и items.turnover_grade_cluster  в ответ метода.
Обновили описание параметров items.ads , items.days_without_sales , items.idc  и
items.turnover_grade  в ответе метода.
```

### 16 июня 2025

Метод

Изменение

Методы устаревают и будут отключены 26 июня 2025 года.

Пометили устаревшими параметры stocks.quant_size в запросе метода и

result.quant_size в ответе метода. 26 июня 2025 они будут отключены.

### 11 июня 2025

Метод

Изменение

Добавили параметр items.stocks.warehouse_ids в ответ метода.

### 5 июня 2025

Метод

Изменение

Добавили параметры with.legal_info в запрос метода и result.legal_info в

ответ метода.

Метод

Изменение

Добавили параметры with.legal_info в запрос метода и

```
result.postings.legal_info  в ответ метода.
```

Добавили параметры with.legal_info в запрос метода и result.legal_info в

ответ метода.

```
Добавили описание ошибки You have reached request rate limit per second  для
```

Частые ошибки

всех методов.

Обновили описание параметра supply_id в запросе метода.

Обновили описание параметра id в запросе метода.

postings

Перенесли метод из бета-раздела в основной.

### 3 июня 2025

Метод

Изменение

cancellation/list

Перенесли методы из бета-раздела в основной.

cancellation/approve

cancellation/reject

Метод устаревает и будет отключён 3 августа 2025 года. Переключитесь на новую

cancellation/list

версию /v2/conditional-cancellation/list.

Метод устаревает и будет отключён 3 августа 2025 года. Переключитесь на новую

cancellation/approve

версию /v2/conditional-cancellation/approve.

Метод устаревает и будет отключён 3 августа 2025 года. Переключитесь на новую

cancellation/reject

версию /v2/conditional-cancellation/reject.

Обновили описание ошибки INVALID_ARGUMENT для метода /v2/posting/fbs/package-

Частые ошибки

label.

### 30 мая 2025

Метод

Изменение

Добавили бета-метод для получения отчёта по продажам юридическим лицам

sales/json

в JSON-формате.

```
Добавили параметр result.attributes_with_defaults  в ответ метода.
```

### 27 мая 2025

Метод

Изменение

Метод устарел, удалили его из документации. Используйте /v2/products/stock.

### 26 мая 2025

Метод

Изменение

Обновили описание параметра turnover_grades в запросе метода.

```
Обновили описание параметров items.turnover_grades  и items.valid_stock_count  в ответе
```

метода.

Пометили обязательным параметр items.type_id в запросе метода.

### 23 мая 2025

Метод

Изменение

Добавили параметр items.price.net_price в ответ метода.

Добавили параметр items.errors в ответ метода.

### 22 мая 2025

Метод

Изменение

Добавили бета-метод для получения аналитики по среднему времени доставки.

delivery-time

Добавили бета-метод для получения детальной аналитики по среднему времени

delivery-time/details

доставки по кластеру.

В разделе Порядок работы с методами увеличили лимит запросов — теперь вы

—

можете отправить не больше 50 запросов в секунду на все методы с одного Client

ID. Раньше — не больше 10.

Добавили параметр items.promotions в запрос метода.

### 20 мая 2025

Метод

Изменение

Добавили параметр items.placement_zone в ответ метода.

Добавили бета-метод для получения чек-листа с правилами по установке

грузомест.

Добавили бета-методы для удаления грузомест в заявке на поставку.

Добавили бета-методы для редактирования товарного состава в заявке на

поставку.

order/content/update/status

### 15 мая 2025

Метод

Изменение

```
Добавили параметры result.products.alert_max_action_price_failed  и
result.products.alert_max_action_price  в ответ методов.
```

### 13 мая 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

Метод устаревает и будет отключён 13 июля 2025 года. Переключитесь на новую

версию /v3/chat/history.

В разделе Порядок работы с методами → Управляйте чатами указали новый метод

—

для получения истории чата.

Добавили бета-метод для передачи действий для возврата rFBS.

Методы будут отключены в будущем. Переключитесь на метод

return

### 6 мая 2025

Метод

Изменение

Метод будет отключён 27 мая 2025 года. Переключитесь на /v2/products/stocks.

### 30 апреля 2025

Метод

Изменение

Добавили бета-метод для подтверждения заявки на отмену rFBS-заказов.

Добавили бета-метод для получения списка заявок на отмену rFBS-заказов.

Добавили бета-метод для отклонения заявки на отмену rFBS-заказов.

### 28 апреля 2025

Метод

Изменение

```
Удалили параметры items.image_group_id  и items.premium_price  из запроса
```

метода.

```
Удалили параметр result.items.errors.optional_description_elements  из
```

ответа метода.

Удалили параметр items.premium_price из запроса метода.

```
Удалили параметры result.postings.financial_data.products.client_price ,
result.postings.financial_data.products.picking  и
result.postings.products.mandatory_mark  из ответа методов.
Удалили параметры result.financial_data.products.client_price ,
result.financial_data.products.picking  и result.products.mandatory_mark  из
```

ответа методов.

```
Удалили параметры result.analytics_data.region ,
result.financial_data.products.client_price  и
result.financial_data.products.picking  из ответа методов.
```

Удалили параметр orders.creation_flow из ответа метода.

Удалили параметр result.rows.idc из ответа метода.

Метод устарел, удалили его из документации. Используйте

### 23 апреля 2025

Метод

Изменение

Добавили бета-метод для получения отчёта о компенсациях.

Добавили бета-метод для получения отчёта о декомпенсациях.

Обновили описание параметра report_type в ответе метода.

Обновили описание параметра report_type в ответе и запросе метода.

### 17 апреля 2025

Метод

Изменение

Добавили бета-метод для получения позаказного отчёта о реализации товаров.

### 16 апреля 2025

Метод

Изменение

Обновили описание параметра filter.stock_types в запросе метода.

### 11 апреля 2025

Метод

Изменение

```
Удалили устаревшие параметры result.financial_data.posting_services  и
result.financial_data.products.item_services  из ответа методов.
```

barcode

```
Удалили устаревшие параметры result.postings.financial_data.posting_services
и result.postings.financial_data.products.item_services  из ответа методов.
```

### 10 апреля 2025

Метод

Изменение

Добавили бета-метод для получения отчёта о реализации товаров за день.

### 9 апреля 2025

Метод

Изменение

Добавили метод для получения аналитики по остаткам на складах.

### 4 апреля 2025

Метод

Изменение

```
Добавили параметр items.price.auto_add_to_ozon_actions_list_enabled  в ответ метода.
```

### 3 апреля 2025

Метод

Изменение

```
Добавили параметр prices.auto_add_to_ozon_actions_list_enabled  в запрос метода.
```

Обновили описание параметра prices.auto_action_enabled в запросе метода.

### 1 апреля 2025

Метод

Изменение

```
Удалили параметр clusters.logistic_clusters.is_archived  из ответа метода.
```

### 31 марта 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

### 27 марта 2025

Метод

Изменение

Добавили параметр is_blr_traceable в ответы методов.

Добавили параметры is_traceable и is_ettn_required в ответ метода.

Добавили параметр item_tags_calculation в запрос метода и параметр tags в

ответ метода.

### 26 марта 2025

Метод

Изменение

Добавили бета-метод для получения списка товаров с некорректными объёмно-

volume

весовыми характеристиками.

### 20 марта 2025

Метод

Изменение

Добавили параметр premium_plus в ответ метода.

Обновили описание параметров limit_by_sku , page и page_size в запросе

queries/details

метода.

### 19 марта 2025

Метод

Изменение

Обновили описание метода.

Добавили возможное значение skipped параметра result.items.status в ответе

метода.

Метод

Изменение

Добавили параметр result.complex_is_collection в ответ метода.

category/attribute

### 18 марта 2025

Метод

Изменение

Перенесли методы из бета-раздела в основной.

### 14 марта 2025

Метод

Изменение

Добавили метод для получения данных по запросам конкретного товара.

### 13 марта 2025

Метод

Изменение

Пометили параметр offset в запросе методов как устаревший и добавили параметр

пагинации last_id .

### 11 марта 2025

Метод

Изменение

Добавили новую версию метода для просмотра истории чата.

Метод

Изменение

Методы устарели, удалили их из документации.

### 10 марта 2025

Метод

Изменение

Метод устарел, удалили его из документации. Используйте /v3/product/info/list.

### 5 марта 2025

Метод

Изменение

Добавили параметр result в ответ метода.

Пометили обязательными параметры filter.date_from , filter.date_to и

filter.status в запросе метода.

### 3 марта 2025

Метод

Изменение

В ответе метода:

```
• добавили параметр result.optional.products_with_possible_mandatory_mark ,
• пометили устаревшим параметр result.products.mandatory_mark .
```

В ответе методов:

- добавили параметр

```
result.postings.optional.products_with_possible_mandatory_mark ,
• пометили устаревшим параметр result.postings.products.mandatory_mark .
```

Значения кодов маркировки можно получить через метод /v3/posting/fbs/get c

```
with.product_exemplars: true  в запросе или метод
```

### 28 февраля 2025

Метод

Изменение

Добавили возможные значения параметра sort_by в запросе метода и добавили

описания параметров result.barcodes и result.sku в ответ метода.

Пометили параметр creation_flow как устаревший.

v2/supply-order/get

### 27 февраля 2025

Метод

Изменение

Обновили описание метода и отметили параметр result.rows.idc как

устаревший, удалили его из примера.

Обновили описание метода.

Добавили параметр result.previous_substatus в ответ метода.

```
Обновили описание параметра result.operations.posting.delivery_schema  в
```

ответе метода.

Добавили бета-метод для получения данных о запросах ваших товаров.

### 26 февраля 2025

Метод

Изменение

```
Обновили описание параметра result.postings.analytics_data.city  в ответе
```

методов.

Обновили описание параметра result.analytics_data.city в ответе методов.

### 24 февраля 2025

Метод

Изменение

Добавили параметр prices.net_price в запрос метода для указания себестоимости

товара.

### 18 февраля 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

Метод устарел, удалили его из документации.

Методы устарели, удалили их из документации. Переключитесь на новую версию

Метод устарел, удалили его из документации. Переключитесь на новую версию

### 17 февраля 2025

Метод

Изменение

Метод устарел, удалили его из документации. Переключитесь на

новую версию /v3/product/info/list.

get

Добавили бета-методы для управления кодами маркировки.

### 14 февраля 2025

Метод

Изменение

```
Добавили параметры orders.can_cancel , orders.is_econom , orders.is_virtual ,
orders.is_super_fbo , orders.product_super_fbo , orders.supplies.supply_state ,
orders.supplies.supply_tags.is_evsd_required ,
```

v2/supply-order/get

```
orders.supplies.supply_tags.is_jewelry ,
orders.supplies.supply_tags.is_marking_possible ,
orders.supplies.supply_tags.is_marking_required  в ответ метода.
```

Перенесли метод из бета-раздела в основной.

Метод устаревает и будет отключён 14 апреля 2025 года. Переключитесь на новую

версию /v2/product/certification/list.

### 11 февраля 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

Метод устарел, удалили его из документации.

### 10 февраля 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

Метод устарел, удалили его из документации.

Метод устарел, удалили его из документации. Переключитесь на новую версию

Метод

Изменение

Метод устарел, удалили его из документации. Переключитесь на новую версию

### 6 февраля 2025

Метод

Изменение

Обновили описание параметра posting_number в запросе метода.

Перенесли методы из бета-раздела в основной.

### 30 января 2025

Метод

Изменение

Добавили бета-метод для отмены заявки на поставку.

Добавили бета-метод для получения статуса отмены заявки на поставку.

### 22 января 2025

Метод

Изменение

Перенесли метод из бета-раздела в основной.

### 17 января 2025

Метод

Изменение

Добавили метод для проверки кода курьера.

code/verify

```
Добавили параметр result.postings.pickup_code_verified_at  в ответы
```

методов.

```
Добавили параметр result.pickup_code_verified_at  в ответ метода.
```

### 15 января 2025

Метод

Изменение

```
Добавили параметр prices.min_price_for_auto_actions_enabled  в запрос метода.
```

Метод

Изменение

Добавили бета-метод для обновления таймера актуальности минимальной цены.

Добавили бета-метод для получения статуса установленного таймера.

### 14 января 2025

Метод

Изменение

Обновили описание параметров filter и filter.posting_numbers в запросе метода.

Перенесли метод из бета-раздела в основной.

### 13 января 2025

Метод

Изменение

Метод устарел, удалили его из документации.

### 28 декабря 2024

Метод

Изменение

Добавили описание метода, изменили описания параметров bundle_ids , last_id и

limit в запросе метода.

Изменили название и описание метода, изменили описание параметра search в

запросе метода.

```
Обновили описание параметров clusters.warehouses.bundle_ids.bundle_id  и
clusters.warehouses.restricted_bundle_id  в ответе метода.
```

Обновили описание параметра cluster_type в запросе метода.

Обновили описание параметра filter_by_supply_type в запросе метода.

status

Добавили бета-методы для работы с вопросами и ответами.

### 27 декабря 2024

Метод

Изменение

Добавили бета-методы для работы с отзывами.

Добавили бета-метод для создания отгрузки.

Добавили бета-метод для подтверждения отгрузки.

Добавили бета-метод для получения списка методов доставки и отгрузок.

```
Добавили параметры result.is_waybill_enabled  и result.is_econom  в ответ метода.
```

### 26 декабря 2024

Метод

Изменение

Добавили параметр result.sla_cut_in в ответ метода.

method/list

Метод устарел, удалили его из документации. Используйте /v3/supply-order/get.

Метод устарел, удалили его из документации. Используйте /v3/supply-order/list.

Метод устарел, удалили его из документации. Используйте /v1/supply-order/bundle.

Метод устаревает и будет отключён 17 февраля 2025 года. Переключитесь на новую

версию /v5/product/info/prices.

Добавили параметр items.is_super в ответ метода.

### 24 декабря 2024

Метод

Изменение

Добавили параметр prices.vat в запрос метода.

Обновили описание параметра items.vat в запросе методов.
