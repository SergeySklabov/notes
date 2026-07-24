#!/bin/bash
export CONFLUENCE_BASE_URL="https://life.astralinux.ru"
export CONFLUENCE_PAT=$(cat "$HOME/.config/opencode/secrets/confluence_pat")
export CONFLUENCE_READ_ONLY="true"
export CONFLUENCE_WRITE_ENABLED="false"
export CONFLUENCE_TIMEOUT="30"
export CONFLUENCE_MAX_BODY_CHARS="50000"
export CONFLUENCE_LOG_LEVEL="info"
exec /Users/sergeysklabovskiy/Library/Python/3.14/bin/uvx \
  --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ \
  astra-confluence-dc-mcp@1.0.0
