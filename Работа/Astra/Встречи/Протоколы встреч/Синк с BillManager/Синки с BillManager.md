---
tags:
  - prep
  - billmanager
---
**Следующая встреча:** след. неделя (ср) - встреча по Boatsman + регулярный синк
**Прошедшая встреча:** [[2026-07-22 Обсуждение с BillManager по интеграции с Боцманом]] (22.07)
**Участники:** @Сергей Склабовский, @Юлия Луценко, @Иван Мешков, @Александр Шадрин, @Дмитрий Тайлаков

# Содержание
- [[#Контекст (10.07)]]
- [[#Все открытые задачи]]
- [[#Другие встречи]]
- [[#Предыдущие встречи]]

---

# Контекст (22.07)

## Решения
- VDC + пользователь для Boatsman — создаётся через BillManager перед запуском
- IP-адреса — Boatsman решает через свой IPAM, BillManager не участвует
- **Архитектурный диссонанс:** половина логики в BillManager, половина в Boatsman. Иван Мешков обсудит внутри
- Следующая встреча — среда, после получения модуля от Фёдора

## Решения (10.07)
- Boatsman - отдельный тип продукта, не в рамках ВДЦ
- FreeIPA - стенд разворачивается, сценарии проверят
- Тарификация k8s: базовый расчёт, градация - не ранее мая 2027
- TMS - интеграция с BillManager пока не требуется

## Баги (закрыто)
[ACP-1731](https://jira.astralinux.ru/browse/ACP-1731), [ACP-1733](https://jira.astralinux.ru/browse/ACP-1733), [AICBUG-114](https://jira.astralinux.ru/browse/AICBUG-114), [AIC-230](https://jira.astralinux.ru/browse/AIC-230), [AIC-232](https://jira.astralinux.ru/browse/AIC-232), [AICBUG-150](https://jira.astralinux.ru/browse/AICBUG-150), [AICBUG-155](https://jira.astralinux.ru/browse/AICBUG-155), [AICBUG-152](https://jira.astralinux.ru/browse/AICBUG-152)

## Баги (в работе)
- [AICBUG-135: Добавить возможность управлять УЗ системного юзера](https://jira.astralinux.ru/browse/AICBUG-135)
- [AICBUG-151: Создание ВМ с двумя сетевыми интерфейсами](https://jira.astralinux.ru/browse/AICBUG-151) - переформатировать в фича-реквест

## Портал самообслуживания
- [AIC-534: Отчёты по потребляемым ресурсам](https://jira.astralinux.ru/browse/AIC-534) - в работе
- [AIC-1016: Управление пользовательскими образами](https://jira.astralinux.ru/browse/AIC-1016) - оценка сроков
- [AIC-426: Создание и управление снимками дисков](https://jira.astralinux.ru/browse/AIC-426) - нужен пререквизит: управление дисками
- [AIC-536: Управление техническими квотами](https://jira.astralinux.ru/browse/AIC-536) - скорректировать сценарий

---

# Открытые вопросы

- Single Logout в BillManager: [use case на Confluence](https://life.astralinux.ru/pages/viewpage.action?pageId=670463262)

---

# Все открытые задачи

```tasks
not done
tags include #billmanager
sort by due
group by due
```

---

# Другие встречи
- **22.07 - интеграция с Боцманом:** BillManager не хочет быть оркестратором. Половина логики в BillManager, половина в Boatsman - диссонанс. [[2026-07-22 Синк с BillManager по интеграции с Боцманом]]

---

# Предыдущие встречи (регулярные синки)
- [[2026-07-22 Обсуждение с BillManager по интеграции с Боцманом|2026-07-22 Интеграция с Боцманом]]
- [[2026-07-10 Регулярный синк с BillManager|2026-07-10 Синк]]
- [[2026-06-30 Регулярный синк с BillManager|2026-06-30 Синк]]
- [[2026-06-15 Регулярный синк с BillManager|2026-06-15 Синк]]
- [[2026-05-29 Обсуждение тенантов + регулярный синк|2026-05-29 Тенанты]]
