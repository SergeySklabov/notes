#!/bin/bash
export JIRA_BASE_URL="https://jira.astralinux.ru"
export JIRA_PAT=$(cat "$HOME/.config/opencode/secrets/jira_pat")
export JIRA_JQL_SEARCH_ENABLED="true"
export JIRA_ATTACHMENTS_ENABLED="false"
export JIRA_LOG_LEVEL="info"
exec /Users/sergeysklabovskiy/Library/Python/3.14/bin/uvx \
  --default-index https://artifactory.astralinux.ru/artifactory/api/pypi/ai-pypi/simple/ \
  astra-jira-dc-mcp@1.5.0
