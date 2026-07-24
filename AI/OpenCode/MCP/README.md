# MCP Servers

MCP-серверы, подключённые к opencode. Конфигурация: `~/.config/opencode/opencode.jsonc`

## Состав

| Сервер | Версия | Назначение | Данные |
| --- | --- | --- | --- |
| `obsidian` | — | Управление заметками Obsidian | — |
| `astra-jira` | 1.5.0 | Jira Data Center: задачи, поиск, комментарии, переходы | Jira PAT |
| `astra-confluence` | 1.0.0 | Confluence Data Center: поиск, чтение (read-only) | Confluence PAT |
| `rupst-calendar` | 1.0.0 | RuPost CalDAV: расписание, слоты, создание событий | Пароль календаря |
| `rupst-mail` | 0.4.0 | RuPost IMAP: чтение почты, черновики (без отправки) | Пароль почты |

## Переменные окружения

Секреты читаются из `~/.config/opencode/secrets/`:
- `jira_pat` — Personal Access Token Jira
- `confluence_pat` — Personal Access Token Confluence
- `calendar_pass` — пароль от учётной записи RuPost

## Команды для обновления

```bash
# Обновить Jira MCP до последней версии
uvx --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ astra-jira-dc-mcp@latest

# Обновить Confluence MCP
uvx --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ astra-confluence-dc-mcp@latest

# Обновить Calendar MCP
uvx --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ rupost-calendar-mcp@latest

# Обновить Mail MCP
uvx --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ rupost-mail-mcp@latest
```

## Заметки

- Confluence подключён в read-only режиме. Для включения записи — `CONFLUENCE_WRITE_ENABLED="true"` в `astra-confluence-mcp.sh`
- RuPost Mail не поддерживает отправку — только чтение IMAP
- `rupst-calendar` MCP не поддерживает участников (`attendees`) в `create_event`. После создания события участники добавляются через `add-attendees.sh`, затем нужно открыть событие в RuPost и сохранить для отправки приглашений
- `uvx` установлен в `/Users/sergeysklabovskiy/Library/Python/3.14/bin/uvx`
- Пакетный индекс — `https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/`

## Вспомогательные скрипты

| Скрипт | Назначение |
| --- | --- |
| `add-attendees.sh` | Добавить участников к существующему событию (через CalDAV PUT) |
