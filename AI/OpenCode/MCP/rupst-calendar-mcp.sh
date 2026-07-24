#!/bin/bash
export RUPOST_CALDAV_URL="https://mail.astralinux.ru/SOGo/dav/"
export RUPOST_CALDAV_USERNAME="ssklabovskii@astralinux.ru"
export RUPOST_CALDAV_PASSWORD=$(cat "$HOME/.config/opencode/secrets/calendar_pass")
export RUPOST_DEFAULT_TZ="Europe/Moscow"
export RUPOST_LOG_LEVEL="info"
exec /Users/sergeysklabovskiy/Library/Python/3.14/bin/uvx \
  --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ \
  rupost-calendar-mcp@1.0.0
