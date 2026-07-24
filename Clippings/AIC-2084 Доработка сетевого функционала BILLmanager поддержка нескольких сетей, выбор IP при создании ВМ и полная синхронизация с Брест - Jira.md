---
title: "[AIC-2084] Доработка сетевого функционала BILLmanager: поддержка нескольких сетей, выбор IP при создании ВМ и полная синхронизация с Брест - Jira"
source: "https://jira.astralinux.ru/browse/AIC-2084"
author:
published: 2026-06-30
created: 2026-07-06
description:
tags:
  - "clippings"
---
### Детали задачи

- [ACP 2.2.0 (НОЯБРЬ 2026)](https://jira.astralinux.ru/issues/?jql=project%3D%22AIC%22%20AND%20%22%D0%92%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D1%8B%D0%B5+%D1%80%D0%B5%D0%BB%D0%B8%D0%B7%D1%8B%22%3D%22ACP+2.2.0+%28%D0%9D%D0%9E%D0%AF%D0%91%D0%A0%D0%AC+2026%29%22%20ORDER%20BY%20priority%20ASC "ACP 2.2.0 (НОЯБРЬ 2026) - минорный релиз ACP v2.2.0")
- Develop Roadmap
- Cloud Ready
- [AIC: capex](https://jira.astralinux.ru/secure/Tempo.jspa#/accounts/account/253 "Пройти по ссылке") (AIC-CAPEX)

### Описание

---

**Исходные данные**  
клиент ПСБ  
AIC 1.3.1  
Брест 3.3.3.6  
BILLmanager 6.127.0

Требуется реализовать следующие доработки:

1\. Поддержка нескольких сетей при создании ВМ  
Сейчас из BILLmanager виртуальную машину можно создать только с подключением к одной сети.  
Требуется добавить возможность подключения нескольких сетей на этапе создания ВМ.  
2\. Выбор IP-адреса в сети  
Сейчас отсутствует возможность выбрать конкретный IP-адрес из сети при создании ВМ.  
Требуется реализовать выбор свободного IP из доступного пула.  
3\. Полная синхронизация IP-адресов с Брест  
BILLmanager должен получать и отображать все IP-адреса, назначенные ВМ в Брест, включая VIP.  
Требуется реализовать полноценную обратную синхронизацию сетевой конфигурации между системами.

---

**Возможности бизнеса**

---

**Особенности развертывания**

---

**Профили заинтересованных лиц**

---

**Модель бизнес-процесса**

---

**Критерии успеха**

---

**Риски, предположения и зависимости, ограничения**

---

### Покрытие тестирования

No test cases. Create a new test case or add an existing one.

Перенесите файлы, чтобы прикрепить, или обзор.

### Подзадачи

- [Добавить подзадачу](https://jira.astralinux.ru/secure/CreateSubTaskIssue!default.jspa?parentIssueId=1371286 "Добавить подзадачу")
- Опции

| 1. | [\[РЕШЕНИЕ ДИРЕКТОРА ПО ЗАПРОСУ\] Приоритизировать фиче-реквест с директорами вертикалей](https://jira.astralinux.ru/browse/AIC-2171) |  | Готово | [Сергей Склабовский](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ssklabovskii) | [Действия](https://jira.astralinux.ru/rest/api/1.0/issues/1381450/ActionsAndOperations?atl_token=BCF3-299N-BY94-II8F_4d624f647be304c3f7006f740f938f9895dc3a21_lin "Действия (Нажмите '.')") |
| --- | --- | --- | --- | --- | --- |
| 2. | [\[BACKLOG\] Определить компоненты и распределить задачи по ТПМ](https://jira.astralinux.ru/browse/AIC-2283) |  | в работе | [Сергей Склабовский](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ssklabovskii) | [Действия](https://jira.astralinux.ru/rest/api/1.0/issues/1382431/ActionsAndOperations?atl_token=BCF3-299N-BY94-II8F_4d624f647be304c3f7006f740f938f9895dc3a21_lin "Действия (Нажмите '.')") |

### Активность

Можно закрепить до пяти комментариев, чтобы выделить важную информацию. Закрепленные комментарии отображаются выше всех остальных, поэтому их легко заметить.

[Подробнее о закрепленных комментариях](https://docs.atlassian.com/jira/jcore-docs-0912/Editing+and+collaborating+on+issues#pin-comment)

Перенесите файлы чтобы прикрепить их к запросу