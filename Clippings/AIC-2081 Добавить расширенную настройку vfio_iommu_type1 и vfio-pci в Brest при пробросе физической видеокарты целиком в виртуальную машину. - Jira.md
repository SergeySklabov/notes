---
title: "[AIC-2081] Добавить расширенную настройку vfio_iommu_type1 и vfio-pci в Brest при пробросе физической видеокарты целиком в виртуальную машину. - Jira"
source: "https://jira.astralinux.ru/browse/AIC-2081"
author:
published: 2026-06-01
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

На стороне Brest Compute нод к уже существующей автоматической настройке модуля ядра vfio в случае подключения средствами hostdev (PCI) устройства,. выполняемой подсистемой брест, о чём свидетельствуют выводы команд, при отсутствующих статичных файлах конфигурации модуля ядра vfio

```java
dmesg -T | grep vfio
[Чт апр 16 13:06:26 2026] vfio-pci 0000:17:00.0: Enabling HDA controller
[Чт апр 16 13:06:26 2026] vfio-pci 0000:17:00.0: enabling device (0140 -> 0142)
[Чт апр 16 13:06:27 2026] vfio-pci 0000:17:00.0: vfio_ecap_init: hiding ecap 0x19@0x100
....
[Чт апр 16 13:14:39 2026] vfio-pci 0000:17:00.0: Enabling HDA controller
....
[Чт апр 16 13:18:50 2026] vfio-pci 0000:17:00.0: vfio_ecap_init: hiding ecap 0x19@0x100
....
[Пн апр 20 11:53:48 2026] vfio-pci 0000:17:00.0: Enabling HDA controller
....
[Пн апр 20 12:00:33 2026] vfio-pci 0000:ca:00.0: enabling device (0140 -> 0142)
[Пн апр 20 12:00:33 2026] vfio-pci 0000:ca:00.0: vfio_ecap_init: hiding ecap 0x19@0x100
....
[Пн апр 20 12:06:15 2026] vfio-pci 0000:ca:00.0: Enabling HDA controller
....
[Пн апр 20 12:12:53 2026] vfio-pci 0000:ca:00.0: vfio_ecap_init: hiding ecap 0x19@0x100
....
[Пн апр 20 12:14:50 2026] vfio-pci 0000:17:00.0: Enabling HDA controller
[Пн апр 20 12:14:50 2026] vfio-pci 0000:17:00.0: vfio_ecap_init: hiding ecap 0x19@0x100
....
```

```java
# ls -la "/sys/module/vfio_pci/drivers/pci:vfio-pci/"
итого 0
drwxr-xr-x  2 root root    0 апр 16 12:27 .
drwxr-xr-x 43 root root    0 апр 16 12:27 ..
lrwxrwxrwx  1 root root    0 апр 24 11:55 0000:17:00.0 -> ../../../../devices/pci0000:16/0000:16:02.0/0000:17:00.0
lrwxrwxrwx  1 root root    0 апр 24 11:55 0000:ca:00.0 -> ../../../../devices/pci0000:c9/0000:c9:02.0/0000:ca:00.0
--w-------  1 root root 4096 апр 24 11:55 bind
lrwxrwxrwx  1 root root    0 апр 24 11:55 module -> ../../../../module/vfio_pci
--w-------  1 root root 4096 апр 24 11:55 new_id
--w-------  1 root root 4096 апр 24 11:55 remove_id
--w-------  1 root root 4096 апр 16 12:27 uevent
--w-------  1 root root 4096 апр 20 12:06 unbind
```

Добавить настройку включающую и автоматическую настройку параметров ядра:

```java
options vfio-pci enable_sriov=1
options vfio_iommu_type1 allow_unsafe_interrupts=1
```

Для чего это нужно:  
Современные промышленные видеокарты, в частности Nvidia используют MSI/MSI-X ( **Message Signaled Interrupts** ) для управления и повышения производительности.

Включение SR-IOV для vfio\_pci устройства нужно что бы этот бит мог работать для этого устройства - влияет на функциональность виртуализации проброшенного устройства.

Данные настройки имеет смысл устанавливать только в случае если пробрасываем именно видеокарту, для других типов устройств в этих флагах нет необходимости.

Настройка вводилась в рамках работ по пробросу видеокарты целиком в системе Brest в рамках запросов

[https://jira.astralinux.ru/browse/ACIT-2831](https://jira.astralinux.ru/browse/ACIT-2831 "Пройти по ссылке")  
[https://jira.astralinux.ru/browse/ACIT-2559](https://jira.astralinux.ru/browse/ACIT-2559 "Пройти по ссылке")

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

- [Добавить подзадачу](https://jira.astralinux.ru/secure/CreateSubTaskIssue!default.jspa?parentIssueId=1371249 "Добавить подзадачу")
- Опции

| 1. | [\[РЕШЕНИЕ ДИРЕКТОРА ПО ЗАПРОСУ\] Приоритизировать фиче-реквест с директорами вертикалей](https://jira.astralinux.ru/browse/AIC-2181) |  | Готово | [Сергей Склабовский](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ssklabovskii) | [Действия](https://jira.astralinux.ru/rest/api/1.0/issues/1381871/ActionsAndOperations?atl_token=BCF3-299N-BY94-II8F_4d624f647be304c3f7006f740f938f9895dc3a21_lin "Действия (Нажмите '.')") |
| --- | --- | --- | --- | --- | --- |
| 2. | [\[BACKLOG\] Определить компоненты и распределить задачи по ТПМ](https://jira.astralinux.ru/browse/AIC-2287) |  | Готово | [Сергей Склабовский](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=ssklabovskii) | [Действия](https://jira.astralinux.ru/rest/api/1.0/issues/1382284/ActionsAndOperations?atl_token=BCF3-299N-BY94-II8F_4d624f647be304c3f7006f740f938f9895dc3a21_lin "Действия (Нажмите '.')") |
| 3. | [\[РЕВЬЮ ТРЕБОВАНИЯ ТПМ\] Провести ревью требований по подсистеме](https://jira.astralinux.ru/browse/AIC-2366) |  | Backlog | [Дмитрий Попенов](https://jira.astralinux.ru/secure/ViewProfile.jspa?name=dpopenov) | [Действия](https://jira.astralinux.ru/rest/api/1.0/issues/1384972/ActionsAndOperations?atl_token=BCF3-299N-BY94-II8F_4d624f647be304c3f7006f740f938f9895dc3a21_lin "Действия (Нажмите '.')") |

### Активность

Можно закрепить до пяти комментариев, чтобы выделить важную информацию. Закрепленные комментарии отображаются выше всех остальных, поэтому их легко заметить.

[Подробнее о закрепленных комментариях](https://docs.atlassian.com/jira/jcore-docs-0912/Editing+and+collaborating+on+issues#pin-comment)

Для этого запроса еще нет комментариев.

Перенесите файлы чтобы прикрепить их к запросу