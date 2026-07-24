---
title: "ProductDo"
source: "https://app.productdo.it/module/tech_pm/lesson/techpm_architecture_intro"
author:
published:
created: 2026-07-09
description:
tags:
  - "clippings"
---
![](https://app.productdo.it/media/lessons/02_-_Product_Architecture_-_%D0%B8%D0%B7_%D1%87%D0%B5%D0%B3%D0%BE_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D0%B8%D1%82_%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82.png)

## Product Architecture: из чего состоит продукт

**Уровень**: Senior  

Время прохождения: 30 минут

100%

100

Одно из важных качеств опытного продакта - это умение быстро прикинуть сложность и основные компоненты своего продукта. Это позволяет общаться с командой на одном языке, лучше рассчитывать время и понимать, где могут поджидать риски или скрываться интересные возможности. Отнесись к этой теме максимально серьезно: сейчас ты закладываешь основу 70% своих технических знаний.  
  
![](https://app.productdo.it/media/persona/Jane_from_ProductDo_zU6M7XD.jpg)

Jane  
Principal Product Manager

Привет! Ну что, готов разбираться дальше?

На заре карьеры я не очень понимала, из каких элементов логики (сервисов) состоят продукты, и из-за этого подход к новым проектам был всегда как прыжок в темноту. Тогда я представила бы наш стартап Такси как: "Пассажиры -> приложение". Не очень реалистично, да?

Потом я научилась делать Service Blueprint-ы и Service Diagram-ы, и появилось более детальное понимание того, что же я хочу построить. Да, я все еще опираюсь на своего тимлида (менеджера программистов) для оценки сроков, но теперь гораздо яснее могу донести до него свои требования и спорить с командой на одном языке (на языке сервисов). Более того, я научилась видеть, как мой продукт связан с остальными в большой компании.

Наш Lead Tech PM сейчас расскажет немного теории, детально разберет с тобой первый пример (онлайн-магазин), а потом я тебя жду разбираться с нашим продуктом Такси!

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Мы уже разбирали ранее несколько примеров "из жизни", я принес еще один. Я специально выбрал экосистему прогноза погоды. Этот продукт (да, это тоже продукт!) не из мира классического e-commerce, так что он немного расширит твой кругозор.

Посмотри на сервис-диаграмму. Внизу находится backend-сервис (сервисы в самом низу еще называют infrastructure service), задача которого собирать сырые данные из различных источников (датчики температур воздуха, воды, скорости ветра, течений и тд), сохранять их и уметь работать с историческими срезами и агрегациями.

Этот сервис используют два других сервиса: "простых" и "серьезных" прогнозов. Первый не претендует на высокую точность, потому что используется конечными пользователями типа обычных горожан (в данном случае через iPhone app) или некритическими сайтами, например для бегунов - на их сайте может быть Web widget с иконкой солнца/дождя и температуры.

"Серьезные" прогнозы требуют более научного подхода, сложных систем и используются для критически важных прогнозов, например, в аэропортах или в аграрном секторе.

Зачем это продакту? Буквально пять минут рисования, и вот из абстрактной фразы "прогноз погоды" получается какая-никакая структура, которую можно использовать как базу для общения с технарями и распределения фронтов работы. Это очень мощный скилл, и ты прочувствуешь его силу на более сложных примерах уже очень скоро.

![](https://app.productdo.it/media/tasks/ru/techpm_architecture_weather_Screenshot_2025-02-15_at_17.47.09.png) ![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Хочешь научиться строить такие же сервис диаграммы? Тогда потерпи - сейчас будет немного теории, а потом мы начнем практиковаться. Ниже перечислены основные шаги, которых должен придерживаться продакт при построении архитектуры продукта. Рассмотрим их на примере онлайн-магазина велосипедов.

**Шаг 1: Понять, какие фичи нужны пользователю и какие данные это подтверждают**

При создании архитектуры мы предполагаем, что уже ответили на критически важный продуктовый вопрос: а что мы, собственно, строим, и зачем? Другими словами, ты или кто-то другой уже придумал идею, провел продуктовое исследование (CustDev, market research), посчитал Unit Economics, покопался в данных и нарисовал (на салфетке или в Figma) примерный набросок главных фичей и Customer Journey Map. С этим тебе помогли те самые 50% базовых знаний продакта, о которых мы говорили ранее.

Именно знание “что” и “зачем” позволяет нам полностью сосредоточиться на превращении идей в сервисы. Позже мы дойдем до примеров, когда архитектура сама по себе способна натолкнуть нас на новые идеи, но оставим это на десерт. Итак, после всех брейнстормов мы хотим построить вот такой онлайн-магазин велосипедов:

![](https://app.productdo.it/media/tasks/en/techpm_arch_howto2_App_-_Bike_-_2.png) ![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

**Шаг 2: Строим пошаговую Service Blueprint табличку**

Если у тебя за плечами еще нет десятка построенных проектов, то сразу увидеть взаимосвязь всех сервисов (архитектуру) довольно сложно. Тут много вопросов: сколько сервисов, что они делают, с какими другими сервисами связаны, что хранят, какие внешние интеграции вызывают и так далее. Как одновременно поддерживать и загрузку новых моделей, и поиск велосипедов, и оплату, и доставку... Недаром построение архитектуры - одна из самых сложных тем!

Чтобы упростить себе задачу мы используем очень полезный инструмент Service Blueprint, отвечающий на вопрос: *"Что должно произойти на фронтенде (сайт, приложение) и бэкенде (сервисы, саппорт), чтобы пользователь совершил еще один шаг customer journey.* Давай посмотрим на примере, станет понятнее.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Посмотри на табличку ниже. Можешь ее открыть в новой вкладке, чтобы увеличить. Давай пройдемся по структуре:

- Первый ряд показывает **шаги пользователя по CJM**. В данном случае это процесс покупки, но для другого продукта тут может быть что-то еще (например, процесс заказа такси)
- Второй ряд - **"основная сцена" (Front Stage Interactions)**: те элементы, которые пользователь видит и может "потрогать"
- Третий ряд - **"закулисье" (Back Stage Interactions)**: тут как раз и прячутся действия бэкэнд сервисов, которые позволяют фронтенду делать свою работу
- Наконец, четвертый ряд - **поддерживающие процессы (Support Processes)**: здесь находится все необходимое для функционирования верхних сцен. Сюда обычно попадают звонки в саппорт и реакция на них, всякие ручные действия в админке. Да-да, технологии все еще не могут без нас, человеков!

Service Blueprint - это один из мостиков между нетехническими (дизайнеры, коммерческие продакты, лидеры) и техническими стейкхолдерами. Первые обычно рассуждают в терминах действий пользователя, а вторые - в терминах кода, выполняющего логику. А ты со своей табличкой и будешь их связывать, говорить на обоих языках!

![](https://app.productdo.it/media/tasks/ru/techpm_blue_intro2_sbp_bike.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

**Шаг 3: Выделяем и рисуем frontend-элементы продукта**

Frontend - это то, что видит и с чем может взаимодействовать пользователь. На данном этапе нас интересуют не мелочи (цвет, дизайн, шрифт), а логические элементы интерфейса. Тут у продакт-менеджера есть три варианта диаграммы:

**Высокоуровневая**

Выделить только самые большие интерфейсы: для стандартного e-commerce магазина это web-сайт, иногда мобильное приложение и админка для продавцов, чтобы они могли загружать новые товары.

Если продакт думает над стратегией компании вообще или разговаривает с CEO и не хочет фокусироваться на деталях, то первого варианта вполне достаточно. Он позволяет очень грубо обрисовать все главные интерфейсы, так что сразу ясно: у магазина есть сайт, приложение и что-то внутреннее для поставщиков. **Постраничная**

Нарисовать более детальную схему со страницей поиска товаров, страницей товара, страницей заказов, страницей статуса доставки, страницей загрузки новых велосипедов.

Если продакт работает с командой или клиентом по конкретному кейсу и хочет показать новый функционал или предложить изменения в одном из виджетов, то необходима более детальная диаграмма. Она поможет продемонстрировать связи между элементами. Например, если нужно рассказать про новый виджет "Персональная акция", которая будет появляться на всех страницах, то разумно использовать второй тип диаграммы. **Поэлементная**

Сделать даже еще более детальную схему для каждой страницы. Для страницы поиска это будут виджеты: поиска, автозаполнения введенного текста ("Cann… -> Cannondale"), рекомендаций, текущих распродаж и так далее.

Например, если команда решила ускорить работу всей страницы поиска, то нужно детальное понимание всех элементов - понадобится этот тип диаграммы.

Для данного примера я буду использовать второй тип, но ты всегда можешь добавить на него деталей и превратить в третий.

![](https://app.productdo.it/media/tasks/ru/techpm_arch_howto_fe_bike_fe.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

**Шаг 4: Выделяем и рисуем backend-элементы продукта**

Backend состоит из сервисов, которые как раз и питают фронтенд своей логикой. Это очень важный момент, прочуствуй его: фронт сам по себе очень “глупый”: он не умеет сохранять твой логин, не умеет искать тебе велосипед по фильтрам, не умеет давать тебе рекомендации. Он просто показывает то, что возвращает бэк. Мне очень нравится метафора с телевизором: сам по себе он ничего не решает, а просто транслирует.

Конечно, даже телевизор может делать базовую логику (например, показывать время), точно также как и фронтенд форма имейла не даст ввести имейл без символа “@”. При этом, все сложные проверки, такие как наличие имейла в черном списке или отправки письма с кодом подтверждения будут находиться на бэке.

Чтобы добавить один новый сервис, нужно выполнить 4 шага:

- 4a: Выбрать отдельный бизнес процесс и понятно назвать с помощью него сервис (например, "Сервис поиска")
- 4b: Решить, что сервис должен хранить (базы данных)
- 4c: Решить, как к сервису будут обращаться другие сервисы и фронтенд (API)
- 4d: Выбрать, что сервис будет аутсорсить внешним интеграциям
Эти шаги необходимо повторить для каждого нового сервиса, пока ты не покроешь все бизнес процессы продукта, так что отнесись к теории ниже и первым примерам серьезно.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Давай посмотрим на все четыре шага по порядку.

**Шаг 4a: Выбрать отдельный бизнес-процесс и понятно назвать с помощью него сервис**

С первым пунктом довольно просто: пройдись по CJM или Service Blueprint и обрати внимание на всю нетривиальную логику, помня, что сам по себе фронтенд глупый, так что ему всегда нужна помощь сервиса. Попробуй мысленно разбить эту логику на отдельные бизнес-процессы. Один процесс - один сервис.

Поначалу у тебя могут быть проблемы с понятием "отдельный процесс". Например, оставить отзыв - это отдельный процесс? Похоже. А удалить мат и рекламу из отзыва - это часть этого процесса или отдельный сервис? Скорее, часть. А ML-модель, которая читает все отзывы и строит умное саммари по топикам ("качество", "быстрый в сборке", "легкий") - это все еще этот сервис? Скорее, нет, он уже тянет на отдельный микросервис пост-анализа отзывов, а не добавления их.

Число бизнес-процессов (и сервисов) растет пропорционально сложности проекта. Например, в Uber число сервисов перевалило за... 2200!

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

**Шаг 4b: Решить, что сервис должен хранить (базы данных)**

*Базы данных (databases, storages)* - это память сервиса. Если нет базы данных, сервису не над чем выполнять свою умную логику. Например, сервис поиска должен хранить все загруженные велосипеды, иначе что он будет искать по выбранным фильтрам? Сервис отзывов должен хранить все оставленные отзывы, иначе как он посчитает среднее и найдет самые новые или самые старые?

Или же представь сайт, который постоянно требует ввести твой имейл, адрес доставки, кредитку - это довольно неудобно. Поэтому на большинстве e-commerce сайтов все эти данные аккуратно сохранены в базе данных пользователей, которую охраняет какой-нибудь User Data Service. При следующей покупке данный сервис узнает пользователя по логину/паролю и заполнит все нужные поля.

Выбор нужных для работы сервиса данных заставляет продакта задуматься о границах ответственности сервиса и удостовериться, что такие данные у нас вообще есть. Тут же можно предотвратить будущие проблемы: если сервису нужны 100+ источников данных, то, скорее всего, попахивает огромным монолитом - нужно бить сервис на части и делать его более сфокусированным на одной бизнес-проблеме. О монолитах мы еще поговорим чуть позже.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

**Шаг 4c: Решить, как к сервису будут обращаться другие сервисы и фронтенд (API)**

Следующая критическая часть сервиса - API (Application Programming Interface). Мы отдельно углубимся в эту тему, а пока просто помни, что сервисы умеют между собой “общаться” по определенному протоколу (фронтенд-элемент строки поиска вызывает бэкэнд-сервис поиска, бэкэнд сервис поиска вызывает ML-сервис рекомендаций и так далее).

Другими словами, сервис умеет делать что-то полезное, и он сообщает об этом, открывая API остальным, по аналогии с меню ресторана и официантами, которые доставляют именно то, что написано в меню.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

**Шаг 4d: Выбрать, что сервис будет аутсорсить внешним интеграциям**

Мы не хотим, да и редко можем строить все с нуля, поэтому мы используем и, соответственно, платим за чужой доступный функционал. Например, мы интегрируемся с платежными шлюзами - сами мы кредитные карты клиентов обрабатывать не будем, это слишком сложно и нужна лицензия банка. Внешние интеграции подчеркивают границы нашего продукта - за ними то, на что мы уже мало влияем.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Мы готовы расписывать архитектуру магазина велосипедов! Начнем применять шаги 4a, 4b, 4c, 4d, чтобы добавлять сервисы один за другим.

**Шаг 4а: Выбираем отдельный бизнес-процесс и называем сервис**  
Давай посмотрим на шаги 1 и 2 из Service Blueprint - страницу поиска и деталей конкретной модели. На первой, когда я ввожу цену, категорию и жму "Искать", фронт передает это на бэк ("price < 500 eur", "type: mountain bike", size: “M”). Там должно быть "что-то", что должно быстро пробежаться по всем тысячам моделей, которые доступны в нашем магазине, и выдать только те, которые подходят по критериям. Для страницы деталей конкретной модели велосипеда поиск сильно проще - "что-то" должно просто достать много информации (картинки, описание, ростовки и тд) по одной модели.  
Это и есть наш первый бизнес процесс! Назовем сервис, отвечающий за него, **сервисом поиска**. **Шаг 4b: Добавляем сервису базы данных**  
Логично предположить, что чтобы искать по фильтрам (например, цена или тип), эти данные должны где-то храниться. Поэтому добавляем сервису поиска базу данных с названием велосипеда, его типом (“городской”, “горный”), описанием, картинками, ценой, размером рамы, названием производителя. Обрати внимание, что главный уникальный идентификатор (primary key) **bike\_id**, выделеный жирным. Все может поменяться (цена, название и т.д.), но не он - по нему всегда можно найти тот самый велосипед. Далее, мы также будем хранить уникальный идентификатор покупки (purchase\_id), уникальный идентифактор клиента (user\_id), и т.д. **Шаг 4с: Добавляем сервису API**

Раз сервис занимается поиском, он должен сообщить об этом миру с помощью API. В данном случае сервис должен уметь искать и принимать от фронтенда значения фильтров (price < “500 eur", type: “mountain bike", size:”M”). Поэтому добавим сверху сервиса рыжую коробочку: /search(price, type, size, sorting). Последний параметр определяет, как покупатель хочет видеть список результатов: отсортированым по популярным, самым дешевым, и т.д.

Мы будем отдельно рассматривать (и даже вызывать) API немного позже, так что пока можешь просто писать над сервисом глагол, обозначающий, что этот сервис может делать. Например, “искать” (search), “сохранять отзыв” (add\_review). И помни, что стрелочка от одного элемента архитектуры к другому означает вызов API. **Шаг 4d: Добавляем сервису внешние интеграции**  
В случае с сервисом поиска, кажется, что внешние интеграции нам особо и не нужны - у нас есть все необходимое (наша база данных со всеми данными, нужными для поиска).

Готово! Сервис поиска стал первым на архитектуре магазина велосипедов. Он, кстати, получился довольно простой, но представь себе, например, задачу поиска авиабилетов на сайте авиалинии: постоянно прыгающие цены, автоматическое формирование стыковочных рейсов, часовые пояса… Поэтому в больших компаниях за таким сервисом будет следить целая команда, а иногда и несколько.

![](https://app.productdo.it/media/tasks/ru/techpm_arch_howto_be2_techpm_arch_howto_be2_bike_search1_ru.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Продолжаем! Кстати, ты задумывался, а как велосипеды к нам попадают? Правильно, их загружают производители или наши собственные агенты через админку.

**Шаг 4а: Выбираем отдельный бизнес-процесс и называем сервис**  
Данные не попадают магическим образом в базу данных, нужен сервис - назовем его “Сервисом загрузки товара”. **Шаг 4b: Добавляем сервису базы данных**

Сервис должен хранить все данные о велосипеде, так что логично предположить, что это будет название, детали, цена, производитель, картинки, размер/ростовка, количество (например, 5 одинаковых) и что-то еще. При загрузке нового велосипеда сервис сохранит его в базе данных и присвоит порядковый номер bike\_id.

Как ты, наверное, заметил, мы сохранили ровно те же данные, по которым искали! Поэтому давай не будем усложнять и оставим одну базу данных для Сервиса загрузки товара и Сервиса поиска: первый будет в нее писать, второй - по ней искать. **Шаг 4с: Добавляем сервису API**  
Тут все просто: сервис должен уметь сохранять новый байк (/upload\_new\_bike). Все изменения (например, цены) можно будет делать из админки. **Шаг 4d: Добавляем сервису внешние интеграции**  
Кажется, что для загрузки данных велосипеда нам тоже не нужны никакие внешние интеграции. Можно пофантазировать, что перед сохранением мы хотим прогнать описание через грамматическую проверку (внешний SpellCheck API), но для MVP давай оставим все как есть.  
![](https://app.productdo.it/media/tasks/ru/techpm_arch_howto_be4_techpm_arch_howto_be4_bike_upload1_ru.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Еще один сервис готов - теперь архитектура состоит уже из двух сервисов. Едем дальше. Итак, покупатель готов оплачивать.

**Шаг 4а: Выбираем отдельный бизнес-процесс и называем сервис**  
“Что-то” должно получить оплату покупателя, зафиксировать ее в базе данных, создать заказ и передать его в доставку. Назовем это что-то “Сервисом покупки”. **Шаг 4b: Добавляем сервису базы данных**  
Нам нужно связать все элементы покупки вместе - покупателя (email), его адрес доставки (address), оплаченную цену (price), один или несколько купленных велосипедов (bike\_ids), и, например, дату покупки (date). Кажется, что еще удобен параметр status: “Ожидает оплаты”, “Частично оплачена”, “Передано в доставку”, “Доставлено”. Каждая такая запись будет иметь уникальный идентификатор “purchase\_id”. **Шаг 4с: Добавляем сервису API**  
Сервис должен уметь создать покупку (/create\_purchase), а для этого фронтенд должен ему передать содержимое корзины (bike\_ids), адрес (address), контакт пользователя (email) и т.д. **Шаг 4d: Добавляем сервису внешние интеграции**  
Наконец, наша первая внешняя зависимость - платежное API. Мы передаем в него платежные данные покупателя и ожидаем ответ: “Деньги сняты, отдавайте заказ” или “Оплата не прошла”.  
![](https://app.productdo.it/media/tasks/ru/techpm_arch_howto_be3_techpm_arch_howto_be3_bike_pay1_ru.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Уже три сервиса - архитектура растет! Пропустим процесс доставки - там все просто, скоро покажу. А вот **процесс получения отзыва** давай сделаем вместе. Итак, нам нужен сервис, который умеет:

- Напоминать пользователю оставить отзыв
- Принимать его в форме текста и числа от 1 до 5
- Сохранять отзыв в базе данных
- Возвращать средний отзыв по модели велосипеда
- Удалять мат или рекламу из загруженного текста (“Тут велосипеды плохие, покупай у меня, звони 55555!”)

Подумай самостоятельно и выбери подходящие варианты ниже, используя ту же структуру "Шаг 4a, 4b, 4c, 4d", как мы делали выше. Поскольку это твой первый кейс, ошибки не будут учитываться в общей статистике курса.

Все варианты имеют смысл, кроме одного: нам не обязательно хранить картинку велосипеда в базе данных отзывов - она у нас уже сохранена в базе данных товаров, так что мы можем ее просто взять оттуда по bike\_id.

Работает это так. Где-то в базе данных велосипедов есть такая запись:

```
bike_id=“12345”, title=”Cannondale Topstone", price="1099", picture="picture.jpeg"
```

При этом, Сервису Отзывов тоже нужны данные о велосипеде, чтобы отправить правильный имейл-запрос на отзыв. И вместо того, чтобы создавать копию названия велосипеда, картинки, ростовку и еще 20 полей в реальных сложных магазинах, Сервис Отзывов просто… хранит **bike\_id**, чтобы понимать, что отзыв оставлен именно для данной модели. А когда Сервис Отзывов будет готов отправлять имейл, он попросит Сервис Поиска велосипедов дать ему развернутые данные по **bike\_id** (или сам залезет в базу), и вставит их в письмо ("Пожалуйста, оставьте отзыв о модели *title*, ростовки *size*, картинка *picture* ").**

Запомни этот прием хранения повторяющихся идентификаторов, чтобы связывать данные между сервисами - мы его будем еще не раз использовать.

![](https://app.productdo.it/media/tasks/ru/correct_solution_tech_arch_intro_review_service_correct_solution_tech_arch_intr_soPGyoB.png)

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Так, шаг за шагом мы добавили сервисы, пока не покрыли все фичи и фронтенд-элементы, которые мы запланировали.

Обрати внимание, что такое упражнение может дать разные результаты: там, где один продакт решит сэкономить (например, вообще не инвестируя в функционал отзывов), другой продакт решит вложиться в полноценный сложный сервис, например, требовать видео-ревью покупателей и выплачивать им за это премию. Эта "нематематичность" и делает нашу работу такой интересной, а архитектуры похожих продуктов такими разными!

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Последнее замечание - архитектура должна выглядеть читаемо. Задача продакта - донести очень сложную информацию обо всех требованиях и связях в одной картинке, будь то целая компания или отдельный сервис. Диаграмма должна вызывать чувство понимания структуры и показывать, как отдельные куски логики складываются в цельный продукт. Нечитаемая диаграмма (слишком много деталей, непонятные обозначения) приведет к обратному эффекту и просто всех запутает.

**Я рекомендую**:
- называть сервисы понятными именами - никаких "STLP service"
- соблюдать цветовую схему: пользователи - одним цветом, backend - другим, интеграции - третьим и т.д.
- указывать неочевидные связи стрелочками (например, доставка вызывает сервис нотификаций), но не перебарщивать с ними
- помнить главную цель картинки - показать общую картину или же отдельный бизнес-процесс - и аудиторию (CEO или программисты команды)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Кстати, если ты уже работал с командой или пролистывал всякие технические статьи, то мог сейчас задуматься: а где же на картинке "настоящие" элементы: MongoDb базы данных, load balancer Ngnix, Akamai CDN, memcache, message broker RabbitMQ - я знаю много названий:)

Спешу тебя обрадовать - это все технические детали/конкретные вендоры, и тебе как продакту вообще не обязательно (а чаще и вредно) в них разбираться. Поверь моему опыту: задавая вопросы на уровне "what/why" и рисуя диаграммы, ты будешь на 95% готов к продуктовым вызовам. Про оставшиеся 5% расскажу позже. Конечно, это не сделает тебя программистом и архитектором - но тебе как продакту это и не нужно.

Но чтобы удовлетворить твое любопытство и заодно уметь видеть то, что "за забором" продакта, через пару уроков мы пройдемся и по этим техническим деталям. А пока давай работать над главным навыком!

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Давай подытожим весь алгоритм построения архитектуры для продакта.

Повторю, что к началу построения архитектуры мы уже знаем, какие фичи нужны пользователю и какие данные это подтверждают. Чаще всего это выражается в каком-то наброске дизайна (например, в Figma). Это твои базовые, не технические навыки. А далее мы:

1. Смотрим на требования CJM/Figma (или задаем их сами, если строим с нуля)
2. Строим пошаговую Service Blueprint табличку
3. Строим Service Diagram: выделяем и рисуем frontend-элементы продукта
4. Строим Service Diagram: выделяем и рисуем backend-элементы продукта. Для этого, для всех бизнес-процессов:
	1. Выбираем отдельный бизнес-процесс и называем сервис
		2. Добавляем сервису базы данных
		3. Добавляем сервису API
		4. Добавляем сервису внешние интеграции
5. Полируем Service Diagram под аудиторию: архитектура должна выглядеть читаемо

Это - алгоритм перехода от расплывчатой идеи “магазин велосипедов” к ясной картине того, что нужно построить, чтобы пошли первые продажи, запомни его.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Service Blueprint-ы и Service Diagram-ы можно делать, как в одиночку, так и вместе с тим лидом/командой, используя диаграмму как общий язык общения, который понятен и продактам, и технарям. Этой же картинкой можно убеждать директоров, что у тебя не просто есть идея, но и четкое понимание того, как ее запустить. Именно поэтому, кстати, такие задачки так часто дают продактам на собеседованиях, например, "А нарисуй-ка нам архитектуру WhatsApp/Spotify/LinkedIn".

Ты, скорее всего, слышал многие термины, но не расслабляйся раньше времени: твоя задача не только знать теорию, но и применять ее для всех продуктов, которые тебе встретятся на пути. Именно поэтому тебя впереди ждут пять кейсов, отнесись к ним серьезно.

Передаю тебя обратно Джейн, будете вместе строить Service Blueprint для приложения Такси.

PRIVACY POLICY

Last updated March 11, 2023

This privacy notice for Aleksandr Povarov, FIE (doing business as ProductDo) ('ProductDo', 'we', 'us', or 'our'), describes how and why we might collect, store, use, and/or share ('process') your information when you use our services ('Services'), such as when you:

■ Visit our website at productdo.io, or any website of ours that links to this privacy notice ■ Engage with us in other related ways, including any sales, marketing, or events

Questions or concerns? Reading this privacy notice will help you understand your privacy rights and choices. If you do not agree with our policies and practices, please do not use our Services. If you still have any questions or concerns, please contact us at support@productdo.io.

SUMMARY OF KEY POINTS

*This summary provides key points from our privacy notice, but you can find out more details about any of these topics by clicking the link following each key point or by using our table of contents below to find the section you are looking for. You can also click* *here* *to go directly to our table of contents.*

What personal information do we process? When you visit, use, or navigate our Services, we may process personal information depending on how you interact with ProductDo and the Services, the choices you make, and the products and features you use. Click here to learn more.

Do we process any sensitive personal information? We do not process sensitive personal information.

Do we receive any information from third parties? We do not receive any information from third parties.

How do we process your information? We process your information to provide, improve, and administer our Services, communicate with you, for security and fraud prevention, and to comply with law. We may also process your information for other purposes with your consent. We

process your information only when we have a valid legal reason to do so. Click here to learn more.

In what situations and with which types of parties do we share personal information? We may share information in specific situations and with specific categories of third parties. Click here to learn more.

How do we keep your information safe? We have organisational and technical processes and procedures in place to protect your personal information. However, no electronic transmission over the internet or information storage technology can be guaranteed to be 100% secure, so we cannot promise or guarantee that hackers, cybercriminals, or other unauthorised third parties will not be able to defeat our security and improperly collect, access, steal, or modify your information. Click here to learn more.

What are your rights? Depending on where you are located geographically, the applicable privacy law may mean you have certain rights regarding your personal information. Click here to learn more.

How do you exercise your rights? The easiest way to exercise your rights is by filling out our data subject request form available here: app.productdo.it, or by contacting us. We will consider and act upon any request in accordance with applicable data protection laws.

Want to learn more about what ProductDo does with any information we collect? Click here to review the notice in full.

TABLE OF CONTENTS

1\. WHAT INFORMATION DO WE COLLECT?

2\. HOW DO WE PROCESS YOUR INFORMATION?

3\. WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR PERSONAL INFORMATION?

4\. WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION? 5. WHAT IS OUR STANCE ON THIRD-PARTY WEBSITES?

6\. DO WE USE COOKIES AND OTHER TRACKING TECHNOLOGIES?

7\. HOW LONG DO WE KEEP YOUR INFORMATION?

8\. HOW DO WE KEEP YOUR INFORMATION SAFE?

9\. DO WE COLLECT INFORMATION FROM MINORS?

10\. WHAT ARE YOUR PRIVACY RIGHTS?

11\. CONTROLS FOR DO-NOT-TRACK FEATURES

12\. DO CALIFORNIA RESIDENTS HAVE SPECIFIC PRIVACY RIGHTS?

13\. DO VIRGINIA RESIDENTS HAVE SPECIFIC PRIVACY RIGHTS?

14\. DO WE MAKE UPDATES TO THIS NOTICE?

15\. HOW CAN YOU CONTACT US ABOUT THIS NOTICE?

16\. HOW CAN YOU REVIEW, UPDATE, OR DELETE THE DATA WE COLLECT FROM YOU?

1\. WHAT INFORMATION DO WE COLLECT?

Personal information you disclose to us

*In Short: We collect personal information that you provide to us.*

We collect personal information that you voluntarily provide to us when you register on the Services, express an interest in obtaining information about us or our products and Services, when you participate in activities on the Services, or otherwise when you contact us.

Personal Information Provided by You. The personal information that we collect depends on the context of your interactions with us and the Services, the choices you make, and the products and features you use. The personal information we collect may include the following:

■ phone numbers

■ email addresses

■ names

■ job titles

■ usernames

■ passwords

Sensitive Information. We do not process sensitive information.

Payment Data. We may collect data necessary to process your payment if you make purchases, such as your payment instrument number, and the security code associated with your payment instrument. All payment data is stored by Stripe. You may find their privacy notice link(s) here: https://stripe.com/en-ee/privacy.

All personal information that you provide to us must be true, complete, and accurate, and you must notify us of any changes to such personal information.

Information automatically collected

*In Short: Some information — such as your Internet Protocol (IP) address and/or browser and device characteristics — is collected automatically when you visit our Services.*

We automatically collect certain information when you visit, use, or navigate the Services. This information does not reveal your specific identity (like your name or contact information) but may include device and usage information, such as your IP address, browser and device characteristics, operating system, language preferences, referring URLs, device name, country, location, information about how and when you use our Services, and other technical information. This information is primarily needed to maintain the security and operation of our Services, and for our internal analytics and reporting purposes.

Like many businesses, we also collect information through cookies and similar technologies.

The information we collect includes:

■ *Log and Usage Data.* Log and usage data is service-related, diagnostic, usage, and performance information our servers automatically collect when you access or use our Services and which we record in log files. Depending on how you interact with us, this log data may include your IP address, device information, browser type, and settings and information about your activity in the Services (such as the date/time stamps associated with your usage, pages and files viewed, searches, and other actions you take such as which features you use), device event information (such as system activity, error reports (sometimes called 'crash dumps'), and hardware settings).

■ *Device Data.* We collect device data such as information about your computer, phone, tablet, or other device you use to access the Services. Depending on the device used, this device data may include information such as your IP address (or proxy server), device and application identification numbers, location, browser type, hardware model, Internet service provider and/or mobile carrier, operating system, and system configuration information.

■ *Location Data.* We collect location data such as information about your device's location, which can be either precise or imprecise. How much information we collect depends on the type and settings of the device you use to access the Services. For example, we may use GPS and other technologies to collect geolocation data that tells us your current location (based on your IP address). You can opt out of allowing us to collect this information either by refusing access to the information or by disabling your Location

setting on your device. However, if you choose to opt out, you may not be able to use certain aspects of the Services.

2\. HOW DO WE PROCESS YOUR INFORMATION?

*In Short: We process your information to provide, improve, and administer our Services, communicate with you, for security and fraud prevention, and to comply with law. We may also process your information for other purposes with your consent.*

We process your personal information for a variety of reasons, depending on how you interact with our Services, including:

■ To facilitate account creation and authentication and otherwise manage user accounts. We may process your information so you can create and log in to your account, as well as keep your account in working order.

■ To send administrative information to you. We may process your information to send you details about our products and services, changes to our terms and policies, and other similar information.

■ To save or protect an individual's vital interest. We may process your information when necessary to save or protect an individual’s vital interest, such as to prevent harm.

3\. WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR INFORMATION?

*In Short: We only process your personal information when we believe it is necessary and we have a valid legal reason (i.e. legal basis) to do so under applicable law, like with your consent, to comply with laws, to provide you with services to enter into or fulfil our contractual obligations, to protect your rights, or to fulfil our legitimate business interests.*

*If you are located in the EU or UK, this section applies to you.*

The General Data Protection Regulation (GDPR) and UK GDPR require us to explain the valid legal bases we rely on in order to process your personal information. As such, we may rely on the following legal bases to process your personal information:

■ Consent. We may process your information if you have given us permission (i.e. consent) to use your personal information for a specific purpose. You can withdraw your consent at any time. Click here to learn more.

■ Performance of a Contract. We may process your personal information when we believe it is necessary to fulfil our contractual obligations to you, including providing our Services or at your request prior to entering into a contract with you.

■ Legal Obligations. We may process your information where we believe it is necessary for compliance with our legal obligations, such as to cooperate with a law enforcement body or regulatory agency, exercise or defend our legal rights, or disclose your information as evidence in litigation in which we are involved.

■ Vital Interests. We may process your information where we believe it is necessary to protect your vital interests or the vital interests of a third party, such as situations involving potential threats to the safety of any person.

In legal terms, we are generally the 'data controller' under European data protection laws of the personal information described in this privacy notice, since we determine the means and/or purposes of the data processing we perform. This privacy notice does not apply to the personal information we process as a 'data processor' on behalf of our customers. In those situations, the customer that we provide services to and with whom we have entered into a data processing agreement is the 'data controller' responsible for your personal information, and we merely process your information on their behalf in accordance with your instructions. If you want to know more about our customers' privacy practices, you should read their privacy policies and direct any questions you have to them.

*If you are located in Canada, this section applies to you.*

We may process your information if you have given us specific permission (i.e. express consent) to use your personal information for a specific purpose, or in situations where your permission can be inferred (i.e. implied consent). You can withdraw your consent at any time. Click here to learn more.

In some exceptional cases, we may be legally permitted under applicable law to process your information without your consent, including, for example:

■ If collection is clearly in the interests of an individual and consent cannot be obtained in a timely way

■ For investigations and fraud detection and prevention

■ For business transactions provided certain conditions are met

■ If it is contained in a witness statement and the collection is necessary to assess, process, or settle an insurance claim

■ For identifying injured, ill, or deceased persons and communicating with next of kin

■ If we have reasonable grounds to believe an individual has been, is, or may be victim of financial abuse

■ If it is reasonable to expect collection and use with consent would compromise the availability or the accuracy of the information and the collection is reasonable for purposes related to investigating a breach of an agreement or a contravention of the laws of Canada or a province

■ If disclosure is required to comply with a subpoena, warrant, court order, or rules of the court relating to the production of records

■ If it was produced by an individual in the course of their employment, business, or profession and the collection is consistent with the purposes for which the information was produced

■ If the collection is solely for journalistic, artistic, or literary purposes

■ If the information is publicly available and is specified by the regulations

4\. WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION?

*In Short: We may share information in specific situations described in this section and/or with the following categories of third parties.*

Vendors, Consultants, and Other Third-Party Service Providers. We may share your data with third-party vendors, service providers, contractors, or agents ('third parties') who perform services for us or on our behalf and require access to such information to do that work. We have contracts in place with our third parties, which are designed to help safeguard your personal information. This means that they cannot do anything with your personal information unless we have instructed them to do it. They will also not share your personal information with any organisation apart from us. They also commit to protect the data they hold on our behalf and to

retain it for the period we instruct. The categories of third parties we may share personal information with are as follows:

■ Ad Networks

■ Affiliate Marketing Programs

■ Cloud Computing Services

■ Communication & Collaboration Tools

■ Data Analytics Services

■ Data Storage Service Providers

■ Finance & Accounting Tools

■ Order Fulfilment Service Providers

■ Government Entities

■ Payment Processors

■ Performance Monitoring Tools

■ Product Engineering & Design Tools

■ Retargeting Platforms

■ Sales & Marketing Tools

■ Social Networks

■ Testing Tools

■ User Account Registration & Authentication Services

■ Website Hosting Service Providers

We also may need to share your personal information in the following situations:

■ Business Transfers. We may share or transfer your information in connection with, or during negotiations of, any merger, sale of company assets, financing, or acquisition of all or a portion of our business to another company.

5\. WHAT IS OUR STANCE ON THIRD-PARTY WEBSITES?

*In Short: We are not responsible for the safety of any information that you share with third parties that we may link to or who advertise on our Services, but are not affiliated with, our Services.*

The Services may link to third-party websites, online services, or mobile applications and/or contain advertisements from third parties that are not affiliated with us and which may link to other websites, services, or applications. Accordingly, we do not make any guarantee regarding

any such third parties, and we will not be liable for any loss or damage caused by the use of such third-party websites, services, or applications. The inclusion of a link towards a third-party website, service, or application does not imply an endorsement by us. We cannot guarantee the safety and privacy of data you provide to any third parties. Any data collected by third parties is not covered by this privacy notice. We are not responsible for the content or privacy and security practices and policies of any third parties, including other websites, services, or applications that may be linked to or from the Services. You should review the policies of such third parties and contact them directly to respond to your questions.

6\. DO WE USE COOKIES AND OTHER TRACKING

TECHNOLOGIES?

*In Short: We may use cookies and other tracking technologies to collect and store your information.*

We may use cookies and similar tracking technologies (like web beacons and pixels) to access or store information. Specific information about how we use such technologies and how you can refuse certain cookies is set out in our Cookie Notice.

7\. HOW LONG DO WE KEEP YOUR INFORMATION?

*In Short: We keep your information for as long as necessary to fulfil the purposes outlined in this privacy notice unless otherwise required by law.*

We will only keep your personal information for as long as it is necessary for the purposes set out in this privacy notice, unless a longer retention period is required or permitted by law (such as tax, accounting, or other legal requirements). No purpose in this notice will require us keeping your personal information for longer than thirty six (36) months past the start of the idle period of the user's account.

When we have no ongoing legitimate business need to process your personal information, we will either delete or anonymise such information, or, if this is not possible (for example, because your personal information has been stored in backup archives), then we will securely store your personal information and isolate it from any further processing until deletion is possible.

8\. HOW DO WE KEEP YOUR INFORMATION SAFE?

*In Short: We aim to protect your personal information through a system of organisational and technical security measures.*

We have implemented appropriate and reasonable technical and organisational security measures designed to protect the security of any personal information we process. However, despite our safeguards and efforts to secure your information, no electronic transmission over the Internet or information storage technology can be guaranteed to be 100% secure, so we cannot promise or guarantee that hackers, cybercriminals, or other unauthorised third parties will not be able to defeat our security and improperly collect, access, steal, or modify your information. Although we will do our best to protect your personal information, transmission of personal information to and from our Services is at your own risk. You should only access the Services within a secure environment.

9\. DO WE COLLECT INFORMATION FROM MINORS? *In Short: We do not knowingly collect data from or market to children under 18 years of age.*

We do not knowingly solicit data from or market to children under 18 years of age. By using the Services, you represent that you are at least 18 or that you are the parent or guardian of such a minor and consent to such minor dependent’s use of the Services. If we learn that personal information from users less than 18 years of age has been collected, we will deactivate the account and take reasonable measures to promptly delete such data from our records. If you become aware of any data we may have collected from children under age 18, please contact us at support@productdo.io.

10\. WHAT ARE YOUR PRIVACY RIGHTS?

*In Short: In some regions, such as the European Economic Area (EEA), United Kingdom (UK), and Canada, you have rights that allow you greater access to and control over your personal information. You may review, change, or terminate your account at any time.*

In some regions (like the EEA, UK, and Canada), you have certain rights under applicable data protection laws. These may include the right (i) to request access and obtain a copy of your personal information, (ii) to request rectification or erasure; (iii) to restrict the processing of your personal information; and (iv) if applicable, to data portability. In certain circumstances, you may also have the right to object to the processing of your personal information. You can make such a

request by contacting us by using the contact details provided in the section 'HOW CAN YOU CONTACT US ABOUT THIS NOTICE?' below.

We will consider and act upon any request in accordance with applicable data protection laws.

If you are located in the EEA or UK and you believe we are unlawfully processing your personal information, you also have the right to complain to your local data protection supervisory authority. You can find their contact details here:

https://ec.europa.eu/justice/data-protection/bodies/authorities/index\_en.htm.

If you are located in Switzerland, the contact details for the data protection authorities are available here: https://www.edoeb.admin.ch/edoeb/en/home.html.

Withdrawing your consent: If we are relying on your consent to process your personal information, which may be express and/or implied consent depending on the applicable law, you have the right to withdraw your consent at any time. You can withdraw your consent at any time by contacting us by using the contact details provided in the section 'HOW CAN YOU CONTACT US ABOUT THIS NOTICE?' below.

However, please note that this will not affect the lawfulness of the processing before its withdrawal nor, when applicable law allows, will it affect the processing of your personal information conducted in reliance on lawful processing grounds other than consent.

Opting out of marketing and promotional communications: You can unsubscribe from our marketing and promotional communications at any time by clicking on the unsubscribe link in the emails that we send, or by contacting us using the details provided in the section 'HOW CAN YOU CONTACT US ABOUT THIS NOTICE?' below. You will then be removed from the marketing lists. However, we may still communicate with you — for example, to send you service-related messages that are necessary for the administration and use of your account, to respond to service requests, or for other non-marketing purposes.

Account Information

If you would at any time like to review or change the information in your account or terminate your account, you can:

■ Contact us using the contact information provided.

Upon your request to terminate your account, we will deactivate or delete your account and information from our active databases. However, we may retain some information in our files to prevent fraud, troubleshoot problems, assist with any investigations, enforce our legal terms and/or comply with applicable legal requirements.

Cookies and similar technologies: Most Web browsers are set to accept cookies by default. If you prefer, you can usually choose to set your browser to remove cookies and to reject cookies. If you choose to remove cookies or reject cookies, this could affect certain features or services of our Services. To opt out of interest-based advertising by advertisers on our Services visit http://www.aboutads.info/choices/.

If you have questions or comments about your privacy rights, you may email us at support@productdo.io.

11\. CONTROLS FOR DO-NOT-TRACK FEATURES

Most web browsers and some mobile operating systems and mobile applications include a Do-Not-Track ('DNT') feature or setting you can activate to signal your privacy preference not to have data about your online browsing activities monitored and collected. At this stage no uniform technology standard for recognising and implementing DNT signals has been finalised. As such, we do not currently respond to DNT browser signals or any other mechanism that automatically communicates your choice not to be tracked online. If a standard for online tracking is adopted that we must follow in the future, we will inform you about that practice in a revised version of this privacy notice.

12\. DO CALIFORNIA RESIDENTS HAVE SPECIFIC PRIVACY RIGHTS?

*In Short: Yes, if you are a resident of California, you are granted specific rights regarding access to your personal information.*

California Civil Code Section 1798.83, also known as the 'Shine The Light' law, permits our users who are California residents to request and obtain from us, once a year and free of charge, information about categories of personal information (if any) we disclosed to third parties for direct marketing purposes and the names and addresses of all third parties with which we shared personal information in the immediately preceding calendar year. If you are a California resident

and would like to make such a request, please submit your request in writing to us using the contact information provided below.

If you are under 18 years of age, reside in California, and have a registered account with Services, you have the right to request removal of unwanted data that you publicly post on the Services. To request removal of such data, please contact us using the contact information provided below and include the email address associated with your account and a statement that you reside in California. We will make sure the data is not publicly displayed on the Services, but please be aware that the data may not be completely or comprehensively removed from all our systems (e.g. backups, etc.).

CCPA Privacy Notice

The California Code of Regulations defines a 'resident' as:

(1) every individual who is in the State of California for other than a temporary or transitory purpose and

(2) every individual who is domiciled in the State of California who is outside the State of California for a temporary or transitory purpose

All other individuals are defined as 'non-residents'.

If this definition of 'resident' applies to you, we must adhere to certain rights and obligations regarding your personal information.

What categories of personal information do we collect?

We have collected the following categories of personal information in the past twelve (12) months:

| Category | Examples Collected |
| --- | --- |
| A. Identifiers | Contact details, such as real name, alias, telephone or mobile contact number, unique personal identifier, online identifier, Internet YES Protocol address, email address, and account name |

| B. Personal information categories listed in the California Customer Records statute | Name, contact information, education, employment, employment history, and YES financial information |
| --- | --- |
| C. Protected classification characteristics under California or federal law | Gender and date of birth NO |
| D. Commercial information | Transaction information, purchase history, financial details, and payment information YES |
| E. Biometric information F. Internet or other similar network activity G. Geolocation data | Fingerprints and voiceprints NO Browsing history, search history, online behaviour, interest data, and interactions with NO our and other websites, applications, systems, and advertisements Device location YES |
| H. Audio, electronic, visual, thermal, olfactory, or similar information | Images and audio, video or call recordings created in connection with our business YES activities |
| I. Professional or employment-related information | Business contact details in order to provide you our Services at a business level or job YES title, work history, and professional qualifications if you apply for a job with us |
| J. Education Information | Student records and directory information YES |

| K. Inferences drawn from other personal information | Inferences drawn from any of the collected personal information listed above to create a NO profile or summary about, for example, an individual’s preferences and characteristics |
| --- | --- |
| L. Sensitive Personal Information | NO |

We will use and retain the collected personal information as needed to provide the Services or for:

■ Category A - As long as the user has an account with us

■ Category B - As long as the user has an account with us

We may also collect other personal information outside of these categories through instances where you interact with us in person, online, or by phone or mail in the context of:

■ Receiving help through our customer support channels;

■ Participation in customer surveys or contests; and

■ Facilitation in the delivery of our Services and to respond to your inquiries. How do we use and share your personal information?

Aleksandr Povarov, FIE collects and shares your personal information through:

■ Targeting cookies/Marketing cookies

■ Social media cookies

■ Beacons/Pixels/Tags

More information about our data collection and sharing practices can be found in this privacy notice.

You may contact us or by referring to the contact details at the bottom of this document.

If you are using an authorised agent to exercise your right to opt out we may deny a request if the authorised agent does not submit proof that they have been validly authorised to act on your behalf.

Will your information be shared with anyone else?

We may disclose your personal information with our service providers pursuant to a written contract between us and each service provider. Each service provider is a for-profit entity that processes the information on our behalf, following the same strict privacy protection obligations mandated by the CCPA.

We may use your personal information for our own business purposes, such as for undertaking internal research for technological development and demonstration. This is not considered to be 'selling' of your personal information.

Aleksandr Povarov, FIE has not sold or shared any personal information to third parties for a business or commercial purpose in the preceding twelve (12) months. Aleksandr Povarov, FIE has disclosed the following categories of personal information to third parties for a business or commercial purpose in the preceding twelve (12) months:

■ Category A. Identifiers, such as contact details like your real name, alias, telephone or mobile contact number, unique personal identifier, online identifier, Internet Protocol address, email address, and account name.

■ Category D. Commercial information, such as transaction information, purchase history, financial details, and payment information.

■ Category G. Geolocation data, such as device location.

The categories of third parties to whom we disclosed personal information for a business or commercial purpose can be found under 'WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION?'.

Your rights with respect to your personal data

Right to request deletion of the data — Request to delete

You can ask for the deletion of your personal information. If you ask us to delete your personal information, we will respect your request and delete your personal information, subject to certain exceptions provided by law, such as (but not limited to) the exercise by another consumer of his or her right to free speech, our compliance requirements resulting from a legal obligation, or any processing that may be required to protect against illegal activities.

Right to be informed — Request to know

Depending on the circumstances, you have a right to know:

■ whether we collect and use your personal information;

■ the categories of personal information that we collect;

■ the purposes for which the collected personal information is used;

■ whether we sell or share personal information to third parties;

■ the categories of personal information that we sold, shared, or disclosed for a business purpose;

■ the categories of third parties to whom the personal information was sold, shared, or disclosed for a business purpose;

■ the business or commercial purpose for collecting, selling, or sharing personal information; and

■ the specific pieces of personal information we collected about you.

In accordance with applicable law, we are not obligated to provide or delete consumer information that is de-identified in response to a consumer request or to re-identify individual data to verify a consumer request.

Right to Non-Discrimination for the Exercise of a Consumer’s Privacy Rights We will not discriminate against you if you exercise your privacy rights.

Right to Limit Use and Disclosure of Sensitive Personal Information

We do not process consumer's sensitive personal information.

Verification process

Upon receiving your request, we will need to verify your identity to determine you are the same person about whom we have the information in our system. These verification efforts require us to ask you to provide information so that we can match it with information you have previously provided us. For instance, depending on the type of request you submit, we may ask you to provide certain information so that we can match the information you provide with the information we already have on file, or we may contact you through a communication method (e.g. phone or email) that you have previously provided to us. We may also use other verification methods as the circumstances dictate.

We will only use personal information provided in your request to verify your identity or authority to make the request. To the extent possible, we will avoid requesting additional information from

you for the purposes of verification. However, if we cannot verify your identity from the information already maintained by us, we may request that you provide additional information for the purposes of verifying your identity and for security or fraud-prevention purposes. We will delete such additionally provided information as soon as we finish verifying you.

Other privacy rights

■ You may object to the processing of your personal information.

■ You may request correction of your personal data if it is incorrect or no longer relevant, or ask to restrict the processing of the information.

■ You can designate an authorised agent to make a request under the CCPA on your behalf. We may deny a request from an authorised agent that does not submit proof that they have been validly authorised to act on your behalf in accordance with the CCPA.

■ You may request to opt out from future selling or sharing of your personal information to third parties. Upon receiving an opt-out request, we will act upon the request as soon as feasibly possible, but no later than fifteen (15) days from the date of the request submission.

To exercise these rights, you can contact us or by referring to the contact details at the bottom of this document. If you have a complaint about how we handle your data, we would like to hear from you.

13\. DO VIRGINIA RESIDENTS HAVE SPECIFIC PRIVACY RIGHTS?

*In Short: Yes, if you are a resident of Virginia, you may be granted specific rights regarding access to and use of your personal information.*

Virginia CDPA Privacy Notice

Under the Virginia Consumer Data Protection Act (CDPA):

'Consumer' means a natural person who is a resident of the Commonwealth acting only in an individual or household context. It does not include a natural person acting in a commercial or employment context.

'Personal data' means any information that is linked or reasonably linkable to an identified or identifiable natural person. 'Personal data' does not include de-identified data or publicly available information.

'Sale of personal data' means the exchange of personal data for monetary consideration.

If this definition 'consumer' applies to you, we must adhere to certain rights and obligations regarding your personal data.

The information we collect, use, and disclose about you will vary depending on how you interact with Aleksandr Povarov, FIE and our Services. To find out more, please visit the following links:

■ Personal data we collect

■ How we use your personal data

■ When and with whom we share your personal data

Your rights with respect to your personal data

■ Right to be informed whether or not we are processing your personal data ■ Right to access your personal data

■ Right to correct inaccuracies in your personal data

■ Right to request deletion of your personal data

■ Right to obtain a copy of the personal data you previously shared with us ■ Right to opt out of the processing of your personal data if it is used for targeted advertising, the sale of personal data, or profiling in furtherance of decisions that produce legal or similarly significant effects ('profiling')

Aleksandr Povarov, FIE sells personal data to third parties or processes personal data for targeted advertising. Please see the following section to find out how you can opt out from further selling or sharing of your personal data for targeted advertising or profiling purposes.

Exercise your rights provided under the Virginia CDPA

More information about our data collection and sharing practices can be found in this privacy notice.

You can opt out from the selling of your personal data, targeted advertising, or profiling by disabling cookies in Cookie Preference Settings. You may contact us by email at support@productdo.io, by visiting app.productdo.it, or by referring to the contact details at the bottom of this document.

If you are using an authorised agent to exercise your rights, we may deny a request if the authorised agent does not submit proof that they have been validly authorised to act on your behalf.

Verification process

We may request that you provide additional information reasonably necessary to verify you and your consumer's request. If you submit the request through an authorised agent, we may need to collect additional information to verify your identity before processing your request.

Upon receiving your request, we will respond without undue delay, but in all cases, within forty-five (45) days of receipt. The response period may be extended once by forty-five (45) additional days when reasonably necessary. We will inform you of any such extension within the initial 45-day response period, together with the reason for the extension.

Right to appeal

If we decline to take action regarding your request, we will inform you of our decision and reasoning behind it. If you wish to appeal our decision, please email us at support@productdo.io. Within sixty (60) days of receipt of an appeal, we will inform you in writing of any action taken or not taken in response to the appeal, including a written explanation of the reasons for the decisions. If your appeal if denied, you may contact the Attorney General to submit a complaint.

14\. DO WE MAKE UPDATES TO THIS NOTICE?

*In Short: Yes, we will update this notice as necessary to stay compliant with relevant laws.*

We may update this privacy notice from time to time. The updated version will be indicated by an updated 'Revised' date and the updated version will be effective as soon as it is accessible. If we make material changes to this privacy notice, we may notify you either by prominently posting a notice of such changes or by directly sending you a notification. We encourage you to review this privacy notice frequently to be informed of how we are protecting your information.

15\. HOW CAN YOU CONTACT US ABOUT THIS NOTICE? If you have questions or comments about this notice, you may email us at support@productdo.io.

If you are a resident in the European Economic Area, the 'data controller' of your personal information is Aleksandr Povarov, FIE. Aleksandr Povarov, FIE has appointed Aleksandr Povarov to be its representative in the EEA. You can contact them directly regarding the processing of your information by Aleksandr Povarov, FIE, by email at support@productdo.io.

16\. HOW CAN YOU REVIEW, UPDATE, OR DELETE THE DATA WE COLLECT FROM YOU?

Based on the applicable laws of your country, you may have the right to request access to the personal information we collect from you, change that information, or delete it. To request to review, update, or delete your personal information, please visit: app.productdo.it.

Неудачный вопрос

[Tech для продакта: введение](https://app.productdo.it/module/tech_pm/lesson/techpm_intro)

[Основы технологий](https://app.productdo.it/module/tech_pm/lesson/techpm_basics)

[Product Architecture: из чего состоит продукт](https://app.productdo.it/module/tech_pm/lesson/techpm_architecture_intro)

[Service Blueprint для стартапа такси](https://app.productdo.it/module/tech_pm/lesson/techpm_blueprint)

[Product Architecture для стартапа такси](https://app.productdo.it/module/tech_pm/lesson/techpm_architecture_new)

[Product Architecture: погружение](https://app.productdo.it/module/tech_pm/lesson/architecture_advanced)

[Product API: как продукты общаются между собой](https://app.productdo.it/module/tech_pm/lesson/techpm_api)

[Product API: работа с документацией](https://app.productdo.it/module/tech_pm/lesson/techpm_api_docs)

[Product API: погружение](https://app.productdo.it/module/tech_pm/lesson/techpm_api_advanced)

[Tech Stack: погружение в технологии и новая идея CEO](https://app.productdo.it/module/tech_pm/lesson/techpm_tech_stack)

[Product Monitoring: полное дерево метрик](https://app.productdo.it/module/tech_pm/lesson/techpm_full_metric_tree)

[Product Monitoring: Service Level Indicators](https://app.productdo.it/module/tech_pm/lesson/techpm_slis)

[Product Reliability: здоровье продукта и SLOs](https://app.productdo.it/module/tech_pm/lesson/techpm_slos)

[Product Testing: проверяем продукт на прочность](https://app.productdo.it/module/tech_pm/lesson/techpm_testing)

[Product Security: основы защиты данных](https://app.productdo.it/module/tech_pm/lesson/techpm_security)

[Full Product Review: оцениваем сложность всего продукта](https://app.productdo.it/module/tech_pm/lesson/techpm_complexity)

[Full Product Review: оцениваем сложность сервиса и фичи](https://app.productdo.it/module/tech_pm/lesson/techpm_complexity2)

[Экзамен Tech PM: новая идея CEO](https://app.productdo.it/module/tech_pm/lesson/techpm_music)