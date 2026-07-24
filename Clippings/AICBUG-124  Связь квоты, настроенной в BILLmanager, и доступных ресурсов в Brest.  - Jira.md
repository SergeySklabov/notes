---
title: "[AICBUG-124]  Связь квоты, настроенной в BILLmanager, и доступных ресурсов в Brest.  - Jira"
source: "https://jira.astralinux.ru/browse/AICBUG-124"
author:
published: 2026-06-05
created: 2026-07-06
description:
tags:
  - "clippings"
---
[Работа](#)

[Планирование времени](#)

[Старт счетчика](#)

[Просмотр записей о работе](https://jira.astralinux.ru/secure/Tempo.jspa#/reports/logged-time?taskKey=AICBUG-124)

[Создать подзадачу](https://jira.astralinux.ru/secure/CreateSubTaskIssue!default.jspa?parentIssueId=889475)

[Преобразовать в подзадачу](https://jira.astralinux.ru/secure/ConvertIssue.jspa?id=889475)

[Создать ветку](#devstatus.cta.createbranch)

[Удалить](https://jira.astralinux.ru/secure/DeleteIssue!default.jspa?id=889475)

[XML](https://jira.astralinux.ru/si/jira.issueviews:issue-xml/AICBUG-124/AICBUG-124.xml)

[Word](https://jira.astralinux.ru/si/jira.issueviews:issue-word/AICBUG-124/AICBUG-124.doc)

[Для печати](https://jira.astralinux.ru/si/jira.issueviews:issue-html/AICBUG-124/AICBUG-124.html)

### Детали задачи

- Предложение
- **Решение:** Нет решения
- Средний
- Не заполнено
- Не заполнено
- Не заполнено
- - [Platform](https://jira.astralinux.ru/issues/?jql=labels+%3D+Platform "Platform")

### Описание

Необходимо реализовать связь квоты, настроенной в BILLmanager, и доступных ресурсов в Brest.

\- в настоящий момент если из BillManager завазывается больше ресурсов, чем есть, создание машин зависает

\- требуется синхронизировать общий доступный объем ресурсов и показывать это пользователю на экране BillManager

### Вложенные файлы

Перенесите файлы, чтобы прикрепить, или обзор.

### Активность

Можно закрепить до пяти комментариев, чтобы выделить важную информацию. Закрепленные комментарии отображаются выше всех остальных, поэтому их легко заметить.

[Подробнее о закрепленных комментариях](https://docs.atlassian.com/jira/jcore-docs-0912/Editing+and+collaborating+on+issues#pin-comment)

### Свернуть комментарий: Сергей Склабовский добавил(а) комментарий - 05.июн.2026 19:32

[Сергей Склабовский](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ssklabovskii) добавил(а) комментарий -

[Александр Шадрин](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ashadrin) посмотри плиз на сколько данная задача закрывается тем, что ты прорабатываешь.

Пока для бизнеса это не Deal breaker, но круто если мы для себя сами будем понимать сроки.

[Редактировать](https://jira.astralinux.ru/secure/EditComment!default.jspa?id=889475&commentId=5033512 "Редактировать") [Удалить](https://jira.astralinux.ru/secure/DeleteComment!default.jspa?id=889475&commentId=5033512 "Удалить")

### Раскрыть комментарий: Сергей Склабовский добавил(а) комментарий - 05.июн.2026 19:32

[Сергей Склабовский](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ssklabovskii) добавил(а) комментарий - Александр Шадрин посмотри плиз на сколько данная задача закрывается тем, что ты прорабатываешь. Пока для бизнеса это не Deal breaker, но круто если мы для себя сами будем понимать сроки.

### Свернуть комментарий: Виктория Агафонова \[X\] (Неактивный) добавил(а) комментарий - 28.мар.2025 11:25

[Виктория Агафонова \[X\] (Неактивный)](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=vagafonova) добавил(а) комментарий -

Иван - предлагает решать административно (админ следит за отчётностью и доступностью ресурсов)

[Редактировать](https://jira.astralinux.ru/secure/EditComment!default.jspa?id=889475&commentId=3290979 "Редактировать") [Удалить](https://jira.astralinux.ru/secure/DeleteComment!default.jspa?id=889475&commentId=3290979 "Удалить")

### Раскрыть комментарий: Виктория Агафонова \[X\] (Неактивный) добавил(а) комментарий - 28.мар.2025 11:25

[Виктория Агафонова \[X\] (Неактивный)](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=vagafonova) добавил(а) комментарий - Иван - предлагает решать административно (админ следит за отчётностью и доступностью ресурсов)

### Свернуть комментарий: Виктория Агафонова \[X\] (Неактивный) добавил(а) комментарий - 28.мар.2025 11:23

[Виктория Агафонова \[X\] (Неактивный)](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=vagafonova) добавил(а) комментарий -

Нет возможности зарезервировать ресурсы на стороне Бреста? (уточнить с Арсением)

Предложение Андрея - при заказе VDC - провести проверку, доступны ли ресурсы к заказу?

[Редактировать](https://jira.astralinux.ru/secure/EditComment!default.jspa?id=889475&commentId=3290972 "Редактировать") [Удалить](https://jira.astralinux.ru/secure/DeleteComment!default.jspa?id=889475&commentId=3290972 "Удалить")

### Раскрыть комментарий: Виктория Агафонова \[X\] (Неактивный) добавил(а) комментарий - 28.мар.2025 11:23

[Виктория Агафонова \[X\] (Неактивный)](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=vagafonova) добавил(а) комментарий - Нет возможности зарезервировать ресурсы на стороне Бреста? (уточнить с Арсением) Предложение Андрея - при заказе VDC - провести проверку, доступны ли ресурсы к заказу?

Перенесите файлы чтобы прикрепить их к запросу