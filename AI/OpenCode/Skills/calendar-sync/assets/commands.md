# Calendar Sync - команды

Все скрипты в `Scripts/`.

## Просмотр

```
bash Scripts/calendar.sh today|tomorrow|week|YYYY-MM-DD
bash Scripts/calendar-detail.sh today|tomorrow|week|YYYY-MM-DD
```

## Создание

```bash
bash Scripts/calendar-create.sh "Тема" "2026-07-06 10:00" "2026-07-06 11:00" \
  --location "https://dion.vc/event/..." \
  --description "Адженда..." \
  --attendee "email@astralinux.ru"
```

## Удаление

UID события - в detail-выводе.

```
bash Scripts/calendar-modify.sh delete <UID>
```

## Изменение recurring-события (Обед, daily и т.д.)

1. Найти UID события (grep в ICS или detail-вывод)
2. GET мастер-событие:
   `https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal/{UID}.ics`
3. Добавить VEVENT-блок с RECURRENCE-ID для нужной даты
4. PUT обратно

## Параметры

- Пароль: `~/.config/opencode/secrets/calendar_pass` (Basic Auth)
- SOGo CalDAV: `https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal/`
- Календарь: `personal.ics`
