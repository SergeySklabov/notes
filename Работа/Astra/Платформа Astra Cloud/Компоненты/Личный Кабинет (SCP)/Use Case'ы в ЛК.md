# Портал самообслуживания

## MVP

### Доступ
* [UC-OPP-021](https://life.astralinux.ru/pages/viewpage.action?pageId=554397827) — Войти на Портал. Аутентификация пользователя и вход в рабочее пространство тенанта.
* [UC-OPP-022](https://life.astralinux.ru/pages/viewpage.action?pageId=554399135) — Выйти из Портала. Завершение сессии.

### Виртуальные машины (жизненный цикл)
* [UC-SCP-028](https://life.astralinux.ru/pages/viewpage.action?pageId=561038276) — Создать ВМ на основе образа. Основной сценарий создания: ВМ создаётся из образа, шаблоны от пользователя скрыты.
	* **Нужен метод API для получения списка образов** - сам список образов мы предварительно загружаем
* [UC-SCP-003](https://life.astralinux.ru/pages/viewpage.action?pageId=482136746) — Изменить виртуальную машину. Изменение конфигурации существующей ВМ.
* [UC-SCP-004](https://life.astralinux.ru/pages/viewpage.action?pageId=482136965) — Просмотреть подробную информацию о ВМ.
* [UC-SCP-005](https://life.astralinux.ru/pages/viewpage.action?pageId=482148061) — Удалить виртуальную машину.

### Сети
* [UC-SCP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=661078924) — Создать виртуальную сеть в Бресте. !нужно завести номер UC-SCP! **Под это API нет**
* **Нужен метод API для получения списка сетей**
* **Есть метод API, но НЕТ UC:** - прикрепить уже созданную сеть к ВМ
* **Есть метод API, но НЕТ UC:** - открепить уже созданную сеть от ВМ
* [UC-SCP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=661078986) — Изменить виртуальную сеть в Бресте. !нужно завести номер UC-SCP! **Под это API нет**
**НЕТ UC:** Удалить виртуальную сеть.

### Диски
- Создание
- Список Дисков
- Детальная информация
- Удаление

## Вторая итерация

### Виртуальные машины (жизненный цикл)
* [UC-SCP-002](https://life.astralinux.ru/pages/viewpage.action?pageId=482127296) — Создать виртуальную машину из шаблона. Создание ВМ через портал. **Под это API нет**
 **НЕТ UC:** Создание из диска
### Образы
* [UC-SCP-025](https://life.astralinux.ru/pages/viewpage.action?pageId=561038195) — Просмотреть каталог образов. Список доступных образов для создания ВМ.
* [UC-SCP-029](https://life.astralinux.ru/pages/viewpage.action?pageId=561038344) — Настроить политики доступа к образу. Базовый уровень: кастомный образ, загруженный в тенант, доступен в рамках этого тенанта. Гибкие политики доступа — отдельная проработка.
**НЕТ UC:** Загрузить образ в тенант — импорт кастомного образа.

### Префиксы тенантов (SDN)
==Нужен комментарий от Андрея Иволги. К чему вообще относится? Есть подозрение, что это чисто технический сценарий.==
* [UC-SCP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644096033) — Просмотреть список анонсов префиксов тенанта. !нужно завести номер UC-SCP!
* [UC-SCP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=648267890) — Просмотреть список префиксов внешней сети. !нужно завести номер UC-SCP!
* [UC-SCP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644096145) — Создать анонс префикса тенанта. !нужно завести номер UC-SCP!
* [UC-SCP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644099498) — Удалить анонс префикса тенанта. !нужно завести номер UC-SCP!
### Снимки/снапшоты
* [UC-SCP-006](https://life.astralinux.ru/pages/viewpage.action?pageId=484579012) — Создать мгновенный снимок ВМ. Снапшот состояния ВМ.
* [UC-SCP-007](https://life.astralinux.ru/pages/viewpage.action?pageId=484581011) — Просмотреть список снимков ВМ. Перечень снапшотов.
* [UC-SCP-008](https://life.astralinux.ru/pages/viewpage.action?pageId=484581700) — Удалить снимок ВМ. Удаление снапшота.
* [UC-SCP-009](https://life.astralinux.ru/pages/viewpage.action?pageId=484583272) — Восстановить снимок ВМ. Откат ВМ к снапшоту.

### Резервное копирование
* [UC-SCP-018](https://life.astralinux.ru/pages/viewpage.action?pageId=552305872) — Создать задание резервного копирования. Настройка задания РК.
* [UC-SCP-020](https://life.astralinux.ru/pages/viewpage.action?pageId=552305811) — Выполнить резервное копирование ВМ. Запуск РК.
* [UC-SCP-021](https://life.astralinux.ru/pages/viewpage.action?pageId=558809862) — Просмотреть список резервных копий. Перечень копий.
* [UC-SCP-016](https://life.astralinux.ru/pages/viewpage.action?pageId=552305926) — Восстановить резервную копию ВМ. Восстановление из копии.
* [UC-SCP-017](https://life.astralinux.ru/pages/viewpage.action?pageId=552305898) — Отменить задание резервного копирования. Остановка задания РК.
* [UC-SCP-022](https://life.astralinux.ru/pages/viewpage.action?pageId=558809996) — Удалить резервную копию. Удаление копии.

### Управление образами
* [UC-SCP-024](https://life.astralinux.ru/pages/viewpage.action?pageId=561038145) — Создать пользовательский образ. Есть вопрос востребованности — возможно не во 2-й итерации, а позже. Нужно обсуждение.
* [UC-SCP-026](https://life.astralinux.ru/pages/viewpage.action?pageId=561038231) — Просмотреть детали образа.
* [UC-SCP-027](https://life.astralinux.ru/pages/viewpage.action?pageId=564201734) — Изменить образ.
* [UC-SCP-030](https://life.astralinux.ru/pages/viewpage.action?pageId=561038397) — Создать образ на основе ВМ.
* [UC-SCP-031](https://life.astralinux.ru/pages/viewpage.action?pageId=561038464) — Удалить образ.
* [UC-SCP-032](https://life.astralinux.ru/pages/viewpage.action?pageId=627861039) — Создать копию диска.
### Kubernetes
**НЕТ UC:** Создать Kubernetes-кластер.
**НЕТ UC:** Список Kubernetes-кластеров.
* [UC-SCP-034](https://life.astralinux.ru/pages/viewpage.action?pageId=638500245) — Редактировать Kubernetes-кластер.
* [UC-SCP-035](https://life.astralinux.ru/pages/viewpage.action?pageId=638500268) — Удалить Kubernetes-кластер.
* [UC-SCP-036](https://life.astralinux.ru/pages/viewpage.action?pageId=638500291) — Добавить пул рабочих узлов в кластер.
* [UC-SCP-039](https://life.astralinux.ru/pages/viewpage.action?pageId=638500369) — Скачать kubeconfig.
## Третья итерация

### Отчётность
* [UC-SCP-014](https://life.astralinux.ru/pages/viewpage.action?pageId=493233661) — Сформировать отчёт. Для MVP не актуально.


---

# Портал оператора

## MVP (после MVP Портала Самооблуживания)

### Доступ
* [UC-OPP-021](https://life.astralinux.ru/pages/viewpage.action?pageId=554397827) — Войти на Портал оператора. Вход оператора (см. замечание об SSO).
* [UC-OPP-022](https://life.astralinux.ru/pages/viewpage.action?pageId=554399135) — Выйти из Портала оператора. Завершение сессии.

### Клиенты и тарификация
* [UC-OPP-001](https://life.astralinux.ru/pages/viewpage.action?pageId=480642284) — Создать Клиента.
* [UC-OPP-002](https://life.astralinux.ru/pages/viewpage.action?pageId=480653479) — Удалить Клиента.
* [UC-OPP-003](https://life.astralinux.ru/pages/viewpage.action?pageId=486624417) — Создать Тарифный план.
**НЕТ UC:** Изменить клиента.
**НЕТ UC:** Список клиентов.
**НЕТ UC:** Изменить тарифный план.
**НЕТ UC:** Удалить тарифный план.
**НЕТ UC:** Список тарифных планов.
### Учётные записи и роли
* [UC-OPP-023](https://life.astralinux.ru/pages/viewpage.action?pageId=554398907) — Создать учетную запись.
* [UC-OPP-024](https://life.astralinux.ru/pages/viewpage.action?pageId=554399179) — Изменить учетную запись.
* [UC-OPP-025](https://life.astralinux.ru/pages/viewpage.action?pageId=554399213) — Удалить учетную запись.
* [UC-OPP-026](https://life.astralinux.ru/pages/viewpage.action?pageId=554399244) — Заблокировать учетную запись.
* [UC-OPP-027](https://life.astralinux.ru/pages/viewpage.action?pageId=554399290) — Разблокировать учетную запись.
* [UC-OPP-028](https://life.astralinux.ru/pages/viewpage.action?pageId=557321783) — Создать роль.
* [UC-OPP-029](https://life.astralinux.ru/pages/viewpage.action?pageId=557321823) — Изменить роль.
* [UC-OPP-030](https://life.astralinux.ru/pages/viewpage.action?pageId=557321865) — Удалить роль.

### Мониторинг
* [UC-OPP-008](https://life.astralinux.ru/pages/viewpage.action?pageId=493236388) — Посмотреть информационную панель (Dashboard).

## Вторая итерация

### Работа с тенантами
==Я бы предложил это вынести в MVP+. Без шага создания тенантов у пользователя не будет возможности что-либо сделать на платформе==
**НЕТ UC:** Создать тенант.
**НЕТ UC:** Список тенантов.
* [UC !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=638502029) — Заблокировать тенант. !нужно завести номер!
* [UC !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=638502061) — Разблокировать тенант. !нужно завести номер!
* [UC !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=638501391) — Удалить тенант. !нужно завести номер!

### Ресурсы и шаблоны
**НЕТ UC:** Изменить ресурс.
**НЕТ UC:** Удалить ресурс.
**НЕТ UC:** Список ресурсов.
**НЕТ UC:** Изменить хранилище.
**НЕТ UC:** Удалить хранилище.
**НЕТ UC:** Список хранилищ.
**НЕТ UC:** Удалить виртуальную сеть.
* [UC-OPP-004](https://life.astralinux.ru/pages/viewpage.action?pageId=486625131) — Создать Ресурс.
* [UC-OPP-014](https://life.astralinux.ru/pages/viewpage.action?pageId=513542211) — Создать шаблон ВМ. Уточнить разницу с «образом» в глоссарии.
* [UC-OPP-019](https://life.astralinux.ru/pages/viewpage.action?pageId=513556270) — Создать хранилище.

### Резервное копирование
* [UC-OPP-012](https://life.astralinux.ru/pages/viewpage.action?pageId=513542097) — Выполнить резервное копирование ВМ.
* [UC-OPP-015](https://life.astralinux.ru/pages/viewpage.action?pageId=513542251) — Создать задание резервного копирования.
* [UC-OPP-016](https://life.astralinux.ru/pages/viewpage.action?pageId=513542275) — Отменить задание резервного копирования.
* [UC-OPP-018](https://life.astralinux.ru/pages/viewpage.action?pageId=513549340) — Восстановить резервную копию ВМ.

### APOS/сети
**НЕТ UC:** Изменить APOS-сеть.
* [UC-OPP-031](https://life.astralinux.ru/pages/viewpage.action?pageId=563708063) — Аутентификация (SSO). Оформить как вариант входа/интеграцию, а не отдельный UC.
* [UC-OPP-032](https://life.astralinux.ru/pages/viewpage.action?pageId=604940186) — Создать сеть (APOS).
* [UC-OPP-033](https://life.astralinux.ru/pages/viewpage.action?pageId=604953586) — Удалить сеть (APOS).
* [UC-OPP-034](https://life.astralinux.ru/pages/viewpage.action?pageId=604962317) — Добавить сетевой интерфейс APOS к ВМ.
* [UC-OPP-035](https://life.astralinux.ru/pages/viewpage.action?pageId=604962803) — Удалить сетевой интерфейс APOS у ВМ.
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=661077077) — Создать виртуальную сеть на Портале оператора. !нужно завести номер UC-OPP!
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=661081598) — Изменить виртуальную сеть на Портале оператора. !нужно завести номер UC-OPP!

### Маршрутизация (BGP)
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644095558) — Активировать динамическую маршрутизацию транзитной сети. !нужно завести номер UC-OPP!
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644095702) — Деактивировать динамическую маршрутизацию (BGP) транзитной сети. !нужно завести номер UC-OPP!

## Третья итерация
### Биллинг
* [UC-OPP-005](https://life.astralinux.ru/pages/viewpage.action?pageId=488376657) — Создать акт выполненных работ.
* [UC-OPP-006](https://life.astralinux.ru/pages/viewpage.action?pageId=493240704) — Пересоздать акт выполненных работ.
* [UC-OPP-007](https://life.astralinux.ru/pages/viewpage.action?pageId=493241755) — Удалить акт выполненных работ.

### Мониторинг и журналы
* [UC-OPP-009](https://life.astralinux.ru/pages/viewpage.action?pageId=493237156) — Посмотреть список записей журналов.
* [UC-OPP-010](https://life.astralinux.ru/pages/viewpage.action?pageId=493237182) — Посмотреть список событий.
* [UC-OPP-011](https://life.astralinux.ru/pages/viewpage.action?pageId=495588705) — Создать файл с правилами сбора журналов.

### Префиксы тенантов (SDN)
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644095791) — Просмотреть список анонсов префиксов тенанта. !нужно завести номер UC-OPP!
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=648267711) — Просмотреть список префиксов внешней сети. !нужно завести номер UC-OPP!
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644095866) — Создать анонс префикса тенанта. !нужно завести номер UC-OPP!
* [UC-OPP !нужно завести номер!](https://life.astralinux.ru/pages/viewpage.action?pageId=644095945) — Удалить анонс префикса тенанта. !нужно завести номер UC-OPP!
