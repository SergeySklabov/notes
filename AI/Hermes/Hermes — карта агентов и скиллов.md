---
tags:
  - reference
  - hermes
Дата: 2026-07-24
---

# Hermes — карта агентов, скиллов и контекстов

> Заметка ведётся агентом **Hermes**. Здесь — читаемое описание всего, что Hermes изучил и взял себе из `AI/OpenCode/`, плюс как это вызывать. Источник истины для скиллов — файлы в vault (`AI/OpenCode/Skills/`); Hermes читает их перед каждым использованием, так что правки в vault подхватываются автоматически.

## Как это работает в Hermes

- Vault синхронизируется через GitHub (`SergeySklabov/obsidian-vault`). Hermes делает `git pull` перед работой и `git push` после правок.
- У Hermes созданы скиллы-обёртки (категория `astra-work`). Каждый указывает на оригинальный SKILL.md в vault и добавляет специфику Hermes (git-цикл, доступность инструментов).
- Вместо субагентов OpenCode (Sisyphus, Hephaestus...) Hermes использует свой механизм делегирования — роли ниже он играет сам или через субагентов.

## Скиллы (перенесены в Hermes)

| Скилл Hermes | Оригинал в vault | Что делает | Как позвать |
|---|---|---|---|
| `meeting-minutes-astra` | `Skills/meeting-minutes` | Минутки из транскрибации: решения по тикетам + @ответственные, стиль протоколов департамента | «сделай минутки по транскрибации» |
| `meeting-protocol-astra` | `Skills/meeting-protocol` | Полный протокол: решения, задачи, риски, DACI, портреты, стейкхолдеры, зависимости, AAR + обновление связанных заметок | «сделай протокол встречи» |
| `meeting-prep-astra` | `Skills/meeting-prep` | Сводная prep-заметка на серию встреч: контекст, незакрытые задачи, Jira-статусы | «подготовь меня к встрече X» |
| `team-meetings-astra` | `Skills/team-meetings` | Brief под тип recurring-встречи: planning, sync, 1-2-1, PBR, арх.ком | «brief к синку команды» |
| `platform-architecture-astra` | `Skills/platform-architecture` | Канонический контекст ACP: границы компонентов, решения, глоссарий, person-to-module | загружается автоматически при анализе ACP |
| `acp-release-astra` | `Skills/acp-release-management` | Эпики релиза ACP 2.2.0, компонентные файлы, блокеры | «собери статус релиза» |
| `obsidian-kanban-astra` | `Skills/obsidian-kanban-agent-ops` | Kanban-доски: колонки, WIP 1-3, linked-notes, DoD | «наведи порядок на доске» |
| `calendar-sync-astra` | `Skills/calendar-sync` | Календарь SOGo/RuPost (CalDAV) — ⚠️ требует доступ во внутреннюю сеть Astra | «что у меня в календаре» |

Не переносился: `meeting-digest` — его функциональность полностью покрыта `meeting-protocol` (см. «Предложения» ниже).

## Контексты

| Файл | Что это |
|---|---|
| `AI/OpenCode/Agents/AGENTS.md` | Главный контекст ACP: описание платформы, компоненты и ответственные, стандарты оформления заметок, глоссарий, правила работы (read-only Jira, замены фамилий → модули), механизм восстановления после сбоев. Hermes читает его при любой серьёзной работе по ACP |
| `AI/OpenCode/Skills/platform-architecture/SKILL.md` | Компактная выжимка архитектуры — для анализа расхождений на встречах |
| `AI/OpenCode/Шпаргалка по агентам и скиллам.md` | Справочник по агентам/скиллам OpenCode (для Mac-сессий) |

## Агенты OpenCode (для справки — в Hermes играются ролями)

| Агент | Роль | Аналог в Hermes |
|---|---|---|
| Sisyphus | Оркестратор: планирует, делегирует, параллелит | Hermes сам + delegate_task |
| Hephaestus | Автономный глубокий исполнитель «сделай полностью» | субагент-leaf |
| Prometheus | Планировщик в режиме интервью | скилл `plan` + clarify |
| Oracle | Архитектор/отладчик сложных проблем | Hermes сам (или субагент) |
| Metis | Ревью планов на риски | субагент-ревьюер |
| Librarian | Поиск документации/примеров | web_search / субагент |
| Momus, Atlas, BA, Multimodal-looker | Роли-описания из AGENTS.md (не субагенты) | Hermes следует описаниям напрямую |

## MCP / Скрипты (работают только с Mac или из сети Astra)

- **Jira** (`astra-jira`, read-only), **Confluence** (`astra-confluence`, read-only), **Календарь** (`rupst-calendar`), **Почта** (`rupst-mail`, только чтение) — секреты в `~/.config/opencode/secrets/` на Mac.
- Скрипты: `AI/OpenCode/Scripts/` (календарь), `AI/OpenCode/MCP/` (слоты, участники, удаление событий).
- ⚠️ Из контейнера Hermes внутренняя сеть Astra недоступна — для Jira/Confluence/календаря Hermes либо просит выполнить команду на Mac, либо работает с локальными копиями в vault.

## Предложения по улучшению (от Hermes, 2026-07-24) — ✅ выполнены 24.07.2026

1. ✅ Дубли kanban-скилла удалены — осталась одна копия `Skills/obsidian-kanban-agent-ops` (взят более свежий шаблон карточки из копии «1»).
2. ✅ `meeting-digest` удалён — функциональность покрыта `meeting-protocol`.
3. ✅ Папка `Агенты/` удалена — осталась `Agents/`.
4. ✅ AGENTS.md, раздел Git обновлён (GitHub-репо, роль Hermes).
5. ✅ Добавлен `.gitignore` (`.DS_Store`, `~$*`, `.env`, `Работа/**/Презентации/`); мусорные файлы убраны из git (на диске и в Dropbox остались).
6. ✅ Презентации исключены из git — синхронизируются только через Dropbox.

## Связанные заметки

- [[AI/OpenCode/Шпаргалка по агентам и скиллам]]
- [[AI/OpenCode/Agents/AGENTS]]
