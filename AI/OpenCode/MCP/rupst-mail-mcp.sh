#!/bin/bash
export RUPOST_IMAP_HOST="mail.astralinux.ru"
export RUPOST_IMAP_PORT="993"
export RUPOST_IMAP_USE_TLS="true"
export RUPOST_IMAP_USERNAME="ssklabovskii@astralinux.ru"
export RUPOST_IMAP_PASSWORD=$(cat "$HOME/.config/opencode/secrets/calendar_pass")
export RUPOST_LOG_LEVEL="info"
exec /Users/sergeysklabovskiy/Library/Python/3.14/bin/uvx \
  --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ \
  rupost-mail-mcp@0.4.0
