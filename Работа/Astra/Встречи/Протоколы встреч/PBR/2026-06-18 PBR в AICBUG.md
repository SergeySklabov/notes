---
tags:
  - meeting
  - meeting/air-bug
Дата: 2026-06-18
Время: "17:00–18:00"
Событие: PBR в AIR BUG- Разгребаем запросы
Событие_UID: 379E59-6A074100-5-521A6F80
Организатор: ssklabovskii@astralinux.ru
Стенограмма: "[[Работа/Astra/Встречи/Стенограмма встреч/PBR в AICBUG- Разгребаем запросы_2026-06-18.md|PBR в AICBUG 2026-06-18]]"
---

# PBR в AIR BUG - 18.06.2026

**Тема:** Разгребаем предложения на новый функционал
**Событие календаря:** [PBR в AIR BUG- Разгребаем запросы](https://dion.vc/event/ssklabovskii-team) - 18.06.2026, 17:00–18:00
**Участники:** Станислав Черков, Александр Кудрявцев, Максим Балыкин, Дмитрий Тайлаков, Виталий Козловский, Максим Югай, Александр Шадрин, Ольга Милащенко, Дмитрий Попенов, Даниил Копцев, Кристина Тришина, Денис Черкесов, Илья Устинов

Запись встречи: _<ссылка на Dion>_

**Стенограмма:** [[Работа/Astra/Встречи/Стенограмма встреч/PBR в AICBUG- Разгребаем запросы_2026-06-18.md|PBR в AICBUG 2026-06-18]]

## Решения по тикетам

- [AIC-2084](https://jira.astralinux.ru/browse/AIC-2084) - проверить связь задачи с багом [AICBUG-151](https://jira.astralinux.ru/browse/AICBUG-151). Если одно и то же - закрываем в рамках бага - @Кристина Тришина
- [AICBUG-149](https://jira.astralinux.ru/browse/AICBUG-149) - нужно уточнение контекста/ролевой модели (создание элементов, недоступных для всех). Подготовить фактуру: @Кристина Тришина, @Василий Текучев отправить в тикет и тегнуть @Дмитрий Попенов
- [AICBUG-129](https://jira.astralinux.ru/browse/AICBUG-129) - @Станислав Черков, @Василий Текучев уточняют у ИБ возможность обновить Brest 3.3.3 -> 3.3.4. Если ИБ ок - завести FR, слинковать и закрыть
- [AICBUG-154](https://jira.astralinux.ru/browse/AICBUG-154) - берём в проработку в 2.2 при наличии капасити команды (учёт занимаемого пространства CEPH)
- [AICBUG-124](https://jira.astralinux.ru/browse/AICBUG-124) - берём в проработку, нужен FR по шаблону и слинковать с запросом - @Кристина Тришина
- [AICBUG-31](https://jira.astralinux.ru/browse/AICBUG-31) - закрываем запрос, т.к. не ясна цель и нет возможности выяснить (доп. пакеты на гипервизоре)
- [AICBUG-51](https://jira.astralinux.ru/browse/AICBUG-51) - закрываем запрос, т.к. полная переработка сценария автоматизации
- [AICBUG-75](https://jira.astralinux.ru/browse/AICBUG-75) - ждём патча от RuBackup ориентировочно в конце недели, поставить в августовский промежуточный релиз (Brest LVM бэкапы)
- [AICBUG-107](https://jira.astralinux.ru/browse/AICBUG-107) - @Василий Текучев: устраивает ли просто правка конфига или нужна настройка через ЛК? (тип процессора по умолчанию)
- [AICBUG-106](https://jira.astralinux.ru/browse/AICBUG-106) - в работе в рамках TMS, нужны FR, слинкованные с запросом - @Станислав Черков, @Александр Кудрявцев
- [AICBUG-103](https://jira.astralinux.ru/browse/AICBUG-103) - @Дмитрий Попенов запусти проверку сценария в Бресте (диски разной производительности в одном тенанте). Далее завести FR (новый ЛК) и слинковать - @Станислав Черков, @Александр Кудрявцев

## FR'ы (пойдут в новый ЛК), слинковать с запросами - @Станислав Черков, @Александр Кудрявцев

- [AICBUG-120](https://jira.astralinux.ru/browse/AICBUG-120)
- [AICBUG-83](https://jira.astralinux.ru/browse/AICBUG-83)
- [AICBUG-91](https://jira.astralinux.ru/browse/AICBUG-91)
- [AICBUG-99](https://jira.astralinux.ru/browse/AICBUG-99)
- [AICBUG-100](https://jira.astralinux.ru/browse/AICBUG-100)

## Задачи по инсталлятору - @Даниил Копцев (завести FR и слинковать)

- [AICBUG-82](https://jira.astralinux.ru/browse/AICBUG-82)
- [AICBUG-85](https://jira.astralinux.ru/browse/AICBUG-85)
- [AICBUG-87](https://jira.astralinux.ru/browse/AICBUG-87)
- [AICBUG-88](https://jira.astralinux.ru/browse/AICBUG-88)
- [AICBUG-89](https://jira.astralinux.ru/browse/AICBUG-89)
- [AICBUG-90](https://jira.astralinux.ru/browse/AICBUG-90)
- [AICBUG-97](https://jira.astralinux.ru/browse/AICBUG-97)

