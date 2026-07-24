---
title: "ProductDo"
source: "https://app.productdo.it/module/tech_pm/lesson/techpm_basics"
author:
published:
created: 2026-07-09
description:
tags:
  - "clippings"
---
![](https://app.productdo.it/media/lessons/04_-_%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_%D0%B1%D1%8D%D0%BA%D0%B5%D0%BD%D0%B4%D0%B0_CMF2mfp.png)

## Основы технологий

Время прохождения: 40 минут

100%

100

В этом уроке мы разберем основные кирпичики технологий: фронтенда (HTML, CSS, Javascript) и бэкенда (сервисы, базы данных, API). Это - ДНК, и, понимая его, ты сможешь построить сложнейшие продукты, сохраняя контроль над происходящим. Мы вернемся к большинству кирпичиков позднее и поговорим про более продвинутые темы.  
  
![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Весь IT мир можно грубо поделить на Frontend (FE) - то, что видят пользователи, вершину айсберга и Backend (BE) - основную логику, подводную часть. Большая часть "мозга" продукта живет именно на backend. А связывают эти два мира API (до них мы чуть позже доберемся, пока просто запомни, что API "связывают").

Хорошая аналогия для запоминания - ресторан. На backend трудятся повара, при этом кухня и секреты приготовления блюд не видны посетителям. Для гостей красиво сервирован стол - frontend, а официанты связывают эти два мира как API между бэком и фронтом. А вот вагончик с хот-догами совмещает все перечисленные слои, и потому он считается full-stack (полная стопка/стэк).

Кстати, такое разделение обязанностей ты можешь явно видеть в титулах программистов: Backend Developer, Frontend Developer, App Developer, Full Stack developer. Именно они определяют, на каком уровне программист работает.

![](https://app.productdo.it/media/tasks/ru/techpm_core_be_and_fe_Screenshot_2025-07-15_at_12.48.46.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Начнем с фронтенда, то есть того, что видят пользователи, когда открывают любую страницу в интернете. Здесь есть три компонента: HTML, CSS и Javascript. Давай посмотрим на все три по очереди.

Любая страница в интернете построена на основе кода HTML. Этот код преобразуется браузером в красивую страничку, которую ты видишь на экране. HTML - это главный каркас: заголовки, кнопки, формы. На картинке ниже ты видишь простейшую страничку: на ней два заголовка и два параграфа текста.

Обязательно "потрогай" HTML сам. Зайди [сюда](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_intro), скопируй код ниже и нажми "Run".

***Простой HTML***  
<!DOCTYPE html>  
\<html>  
\<head>  
\</head>  
  
\<body>  
\<h1>This is a heading\</h1>  
\<p>This is a paragraph.\</p>  
\<h1>This is another heading\</h1>  
\<p>This is another paragraph.\</p>  
  
\</body>  
\</html>

Поменяй текст второго параграфа слева, нажми "Run" и убедись, что он отобразился справа. Получилось?

![](https://app.productdo.it/media/tasks/en/proto_intro_fe_structure1_Screenshot_2025-05-02_at_13.58.01.png)

Отлично, продолжаем.

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Второй ингредиент frontend-а - это CSS-стили (сокращение от Cascading Style Sheets – каскадные таблицы стилей). Они отвечают за стилизацию (цвета, шрифты, расположение элементов). Их удобство в том, что ты можешь один раз задать стиль кнопки, и все кнопки станут такими же (такого же цвета, размера, с таким же скруглением углов и так далее).

Я добавил стили для всех заголовков (h1), и моментально все заголовки окрасились в красный цвет. Представь, что на нашем сайте 100 заголовков, удобно же? Скопируй весь код опять и жми "Run".

***Простой HTML + CSS***  
<!DOCTYPE html>  
\<html>  
\<head>  
\<style>  
h1 { color: red; } \</style>  
\</head>  
  
\<body>  
\<h1>This is a heading\</h1>  
\<p>This is a paragraph.\</p>  
\<h1>This is another heading\</h1>  
\<p>This is another paragraph.\</p>  
  
\</body>  
\</html>

Догадаешься сам, как **поменять цвет всех заголовков на синий**?

![](https://app.productdo.it/media/tasks/en/proto_intro_fe_structure2_Screenshot_2025-05-02_at_14.08.13.png)

Молодец!

Корректное решение - просто заменить в CSS "red" на "blue". Магия CSS в том, что все заголовки (h1) сразу же поменяют цвет.

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Последний кирпичик фронтенда - Javascript. Это язык программирования, отвечающий за интерактивность HTML: обработку кликов, отправку форм, анимации и за все, что на странице двигается и реагирует.

Скопируй этот код и посмотри, что получится:

***Простой HTML + CSS + Javascript***  
<!DOCTYPE html>  
\<html>  
\<head>  
\<style>  
h1 {color: blue;}  
\</style>  
\</head>  
\<body>  
  
\<h1>This is a heading\</h1>  
\<p>This is a paragraph.\</p>  
\<h1>This is another heading\</h1>  
\<p>This is another paragraph\</p>  
  
\<button type="button"  
onclick="myFunction()">  
Click me to display Date and Time.  
\</button>  
  
\<p id="demo">\</p>  
  
\<script>  
function myFunction() {  
document.getElementById('demo').innerHTML = Date()  
}  
\</script>  
  
\</body>  
\</html>

Скопируй код, опять нажми на Run, а потом нажми на появившуюся **новую серую кнопку справа** и скажи, что ты видишь?

![](https://app.productdo.it/media/tasks/en/proto_intro_fe_structure3_Screenshot_2025-05-02_at_14.13.42.png)

Не совсем.

При нажании кнопки ты должен увидеть текущую дату и время. Что же произошло?

Мы создали с помощью HTML тэга " **button** " кнопку и (внимание!) привязали Javascript-код **MyFunction** к событию **onClick**. Поэтому при клике на кнопку вызывается тот самый код, который просто вставляет в пустой параграф "demo" текущую дату и время. В реальных приложениях здесь будет находиться настоящий запрос к бэкенду - "дай мне что-то сложное" (например, список товаров, величину скидки и тд).

Все, теперь ты знаешь три основных кирпичика фронтенда - HTML (каркас), CSS (стили) и Javascript (интерактивность). Продакту этого понимания достаточно.

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Ты разобрался с основами фронтенда (HTML, CSS, Javascript), но не торопись присваивать себе звание Sr. Frontend Developer. В примерах выше у нас был один-единственный небольшой файлик. Но дело в том, что по мере усложнения логики, единственный файлик выше начнет расти. Потом появится второй, третий. Потом появятся бэкенд (с базами данных) и наш JavaScript начнет "ходить" в бэкенд и так далее. В этот момент "один файлик" превратится в двадцать и обрастет взаимосвязями.

Когда код становится сложным (много HTML, много CSS, много JS), программисты используют еще один инструмент, чтобы держать это все под контролем - **фронтенд-фреймворки**. Ты наверняка слышал про **React**, **Angular** и так далее. Они позволяют чуть более умно организовать код и реагировать на действия пользователя. Продакт не принимает решения о выборе фреймворков - это территория программистов ("как").

Отлично, с Frontend-ом разобрались. Давай посмотрим на бэкенд.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Если спуститься на один уровень детализации, то можно увидеть, что **backend** состоит из:

- **Сервисов**, которые делают какую-то работу / логику. Именно для них твои программисты весь день пишут код.
- **Баз данных**, которые позволяют сервисам запоминать данные пользователя, покупок и так далее. Если удалить базу данных, сервис (а с ним и весь сайт) сразу забудет все (имейлы, пароли, твои заказы и прочее).
- **API**, которые позволяют сервисам разговаривать. Каждый сервис может сообщить всем, как он хочет, чтобы к нему обращались ("выставить API"). После этого как frontend, так и другие сервисы могут его о чем-то попросить (к сожалению для сервиса, обычно просят сделать какую-то работу).

В аналогии с рестораном, повар - это **сервис** (делает работу по приготовлению блюд) с **базой данных** (помнит все виды блюд и текущие заказы), к которому можно обратиться по **API** ("Два салата Цезарь").

А когда **главный повар дает команду помощнику** ("Свари 2 кг картошки"), это что?

Именно.

В данном случае, "Помощник" - тоже сервис, просто более простой, он меньше умеет. Но сервис "Главный повар" все равно может его попросить (по API) сделать для себя (скучную) работу. Обрати внимание, что опять прослеживается структура:

- Сервис помощник выполняет **действия** (простые задания)
- Он что-то хранит **в базе данных** (последовательность шагов по каждому заданию и детали текущего задания)
- К нему можно **обратиться по API** ("сделай простое действие X")

Запомни эти три свойства: они нам понадобятся для каждого сервиса, с которым мы будем иметь дело.

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Сейчас ты уже достаточно понимаешь, чтобы усложнить мемасное понимание мира и задаться экзистенциальным вопросом: официанты - это все-таки API, или же **сервисы**?

Не совсем.

"Бездумный" официант и правда похож на API - он просто передает запрос. А вот у "нормального" официанта опять прослеживается структура:

- Сервис Официант выполняет **действия**: во-первых, понимает расплывчатые требования клиента: "А мне бы рыбы", "А есть что-то без молока?" и т.д. В этом смысле можно назвать его модным термином "agentic service". Потом интерпретирует это повару на его языке ("Блюдо 14, аллергены - соя, стейк средней прожарки"). Потом заносит в систему, что столик 21 заказал то и то, и что они ожидают еще одного гостя. Более того, каждые 10 минут проверяет, все ли ок.
- Сервис Официант что-то хранит **в базе данных**: в данном случае это... блокнотик
- К сервису можно обратиться по API, которое принимает как точные заказы, так и менее определенные пожелания

Тянет на отдельный сервис!

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Да, настало время все это добавить на картинку - **Диаграмму Сервисов (Service Diagram)**. Удобство ее в том, что она позволяет отбросить всю шелуху и увидеть главное:

- какие сервисы существуют в системе
- что они хранят
- как к ним можно обратиться
- как все это связано между собой

Вот так может выглядеть Service Diagram для нашего ресторана:

![](https://app.productdo.it/media/tasks/ru/techpm_core_cafe_diagram_techpm_core_cafe_diagram_Screenshot_2025-05-29_at_11.52.37.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Давай попрактикуем важнейшие концепции (фронтенд, бэкенд, сервис, база данных, API) на еще одном примере из жизни. Представь себе процесс получения **новых автомобильных прав**. Что есть что в данном случае? Выбери все корректные утверждения.

- **Фронтенд**: окошко приема в гос. учреждении или сайт для электронной подачи
- **Бэкенд**: невидимая часть организации, которая производит документ
- **API**: инициализация процесса создания документа
- **Сервисы**: проверки данных, создания физической карточки и так далее. Обрати внимание, что клиент не может просто так взять и обратиться к скрытому сервису напрямую - будь добр использовать официальную дверь (фронтенд)!
- **Базы данных**: личная информация и номер выданного документа сохраняются

Обрати внимание, что данный "продукт" смешанный - что-то делают люди, а что-то - программы, при этом, все понятия (сервисы, фронтенд, бэкенд, базы данных) взаимозаменяемые. Для нас, продактов, это значит, что даже сложный сервис - это просто последовательность понятных человеческих действий: сделал, проверил, сохранил, достал и так далее. Очень удобно, потому что позволяет демистифицировать сложные технологии.

Ну и давай визуализируем получение прав на Service Diagram.

![](https://app.productdo.it/media/tasks/ru/correct_solution_techpm_core_services_document_correct_solution_techpm_core_ser_3HgK6DF.png)

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Предположим, что данный документ (права) делают на пластиковой карточке. Откуда государственному учреждению взять карточки?

Да.

Здесь мы встречаемся с еще одним полезным свойством сервисов: им не обязательно делать всю работу самостоятельно. Вместо этого они могут обратиться к внешнему миру (по API), чтобы часть работы была сделана за них. За это, конечно, другие сервисы (фирма пластиковых изделий в данном случае) будут брать плату.

Обрати внимание: в примере с поваром это было взаимодействие внутреннего сервиса (Главный повар) с другим внутренним (Помощник), а здесь именно внутреннего сервиса (Создание документа) с внешним (Другая фирма).

![](https://app.productdo.it/media/tasks/ru/correct_solution_techpm_core_services_document2_correct_solution_techpm_core_se_3OaFtbs.png)

[Сообщить об ошибке](#)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Так, с сервисами немного разобрались. Давай немного углубим понимание API, пока процентов на 10%. К остальным 90% мы вернемся позже: будем вызывать API, строить Sequence Diagrams, читать документацию и много чего еще. А пока - основы!

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Если когда-нибудь будешь объяснять понятие API нетехническому коллеге, делюсь удобной метафорой из жизни - покупкой мороженого в киоске.

В данном случае "вызов API" - это процесс обмена денег и пожеланий (**input** или **request**) на мороженое определенного вкуса и размера (response) из меню киоска (API contract или API documentation), которое содержит ассортимент и цены. Например, за 2 евро можно попросить рожок с 2-мя шариками ванильного мороженого, подождать 2 минуты и получить именно то, что ты хотел. Заметь важные особенности:

- Нельзя попросить что-то вне меню (например, салат), потому что такого API (меню) не предусматривает.
- Тебе не интересно, что сервис (киоск) делает для того, чтобы получить результат: где и по какой цене они покупают молоко, используют свои или арендованные холодильники, как именно смешивают ингредиенты. Важен только API response - рожок мороженого.
- Если ванильный вкус закончился, то тебе придется ждать довольно долго, пока продавец принесет новую коробку из дальнего холодильника - задержка вызова API растянется до 10 минут.
- Может так получиться, что сонный работник ошибется, и ты получишь шоколадный рожок вместо ванильного - это API вернуло ошибку.
Вот как могла бы выглядеть API-документация (развернуть)

```
API-endpoint:
/icecream/buy

Request:
- polite_prefix ("Пожалуйста")
- cash (купюра 10 евро)
- base ("рожок" или "стаканчик")
- flavours (e.g. "1 vanilla" and "1 chocolate")

Response:
- change (8 евро, потому что цена мороженого - 2 евро)
- ice-cream (которое можно есть!)
```

Обрати внимание, что вводные данные определяются набором параметров (**parameters** или **keys**) - они задают структуру того, что нужно API для выполнения своей работы. При этом каждый параметр может иметь множество значений (**values**), которые меняются в зависимости от ситуации, в которой вызывают API. Например, Алекс пришел с купюрой 10 евро и купил шоколадный рожок (**cash** =10, **flavours** =chocolate), а Джейн - ванильный ровно за 2.5 евро (**cash** =2.5, **flavours** =vanilla). Те же параметры, разные значения.

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Давай посмотрим на еще один пример. Вот так могло бы выглядеть описание API оплаты какого-то платежного шлюза:

**API оплаты** (развернуть)

```
API-endpoint:
/cards/pay

Request:
- credit_card_number (e.g. “1111222233334444”)
- amount (e.g. “100”)
- currency (e.g. “EUR”)

Response:
- “Success, paid”
- “Not enough funds on card”
- “Error while processing”
```

Тот же самый API можно описать еще проще, при условии, что все названия параметров и возвращаемых значений говорят сами за себя:

```
/cards/pay(credit_card_number, amount, currency) -> {"Paid", "Not enough funds", "Error"}
```

Это, конечно, будет не настоящий код, но, в отличие от программистов, продакт менеджеру не нужно быть идеально точным в описании деталей, зато важно уметь коротко передать смысл API понятными и говорящими за себя параметрами, обозначая суть. После такого описания уже можно говорить не просто об абстрактном "давайте подключим платежку", а более предметно: что нам нужно (карта пользователя, сумма, валюта) и что может пойти не так (например, на карте не хватит денег). И все в одной строчке!

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Теперь давай немного разверну тему баз данных. Это сильно проще, чем кажется. Продакту достаточно думать про БД, как про файлик, в котором хранится информация в **структурированном виде** (а-ля Google Sheets). На картинке ниже - визуализация настоящей (но маленькой) таблицы покупателей онлайн-магазина. Как видишь, там хранится уникальный id клиента (все остальные поля могут меняться, а id - никогда), имя, имейл, телефон и так далее. С БД можно говорить на [языке SQL](https://productdo.it/sql_pm?utm_source=sim_ai_proto), например, " *посчитай число пользователей по странам* " или " *посчитай процент активных пользователей по годам* ".

Когда структура определена и зафиксирована (колонки таблички), машине становится неважно, сколько у бизнеса клиентов - 10 или 100000. Забавный факт: такая табличка на 1 миллион пользователей будет занимать на диске только... 100 мб! База данных огромного бизнеса влезает на допотопную флешку!

Конечно, когда характеристик пользователя (колонок) становится сильно больше и число записей переваливает за сотни миллионов, такая простая структура начинает путаться и тормозить. Но, по своей сути все современные базы данных (MySQL, Postgres, MongoDB, Cassandra и тд) - это все те же, только очень сложные файлики с кучей ускоряющих алгоритмов над ними. **Но для нас, продактов, главное помнить, что это просто табличка с определенными (нами, продактами) полями.**

![](https://app.productdo.it/media/tasks/en/tech_core_db_basics_Screenshot_2025-06-20_at_08.58.57.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

А теперь посмотри на другую таблицу - **покупок**. Первая колонка здесь - уникальный идентификатор покупки **purchase\_id**, есть всякие детали покупки (название, адрес, цена) и самое главное - внешний ключ **user\_id**, который **связывает** таблицы пользователей и покупок. Например, видно, что Alice (user\_id = 1) сделала 2 покупки, а Clara (user\_id = 3) сделала 1 покупку. Для нас тут два вывода:

- **Разные данные должны лежать в разных табличках**: таблица пользователей, таблица покупок, таблица поставщиков товаров, таблица дискаунт-кампаний по товарам, и т.д. И именно эти данные мы будем показывать на нашем фронтенде в разных местах: имя пользователя в его личном кабинете, список покупок - в его корзине, список дискаунтов - в рассылке-имейле и так далее.
- **Данные из разных таблиц можно связывать через ключи**: так мы понимаем, какие товары купил пользователь, и какие пользователи купили данный товар. Это позволит нам показывать на фронтенде именно то, что мы хотим, а не весь список. Например, для кейса Todo-листа, таски только проекта на экране, а не всех. Проекты только залогиненного пользователя, а не всех.
![](https://app.productdo.it/media/tasks/en/tech_core_db_basics2_Screenshot_2025-06-20_at_09.00.10.png)

![](https://app.productdo.it/media/persona/c768fb3f-f6f0-4f01-825f-83b6a23c1b41.webp)

Mike  
Lead Product Manager, mentor

Давай подведем итоги нашего мини-путешествия по основам технологий:

- **Фронтенд и Бэкенд** - две важнейшие стороны любого продукта. 90% логики / "мозга" / сложности находится на бэкенде
- **Бэкенд состоит из сервисов**, которые: a) **делают** какую-то работу, b) **помнят** за счет баз данных, c) **общаются** друг с другом по API - как внутри продукта, так и обращаясь к внешним сервисам. Продакт должен уметь описывать сервис в базовых понятиях: что делает, что хранит, какое API предоставляет другим и какие API вызывает сам. Мы будем отрабатывать это на куче примеров.
- **У API есть понятная структура**: что он принимает, что возвращает и что может пойти не так.
- **Базы данных** хранят всю информацию о пользователях, их покупках, товарах, статусах и т.д. в структурированном виде. Для продактов база - это просто большая табличка..
- **Крайне важно понимать картину всех кирпичиков продукта (Диаграмму Сервисов)**, чтобы лидить проекты с уверенностью, что ты видишь все элементы издалека и можешь углубиться в каждый из них при необходимости (например, чтобы написать детальные требования). Данный скилл настолько важен, что мы будем его оттачивать на протяжении нескольких следующих уроков.

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