#!/bin/bash
export JIRA_URL="https://jira.astralinux.ru"
export JIRA_API_TOKEN=$(cat "$HOME/.config/opencode/secrets/jira_pat")
export CONFLUENCE_URL="https://life.astralinux.ru"
export CONFLUENCE_API_TOKEN=$(cat "$HOME/.config/opencode/secrets/confluence_pat")
exec node "$(dirname "$0")/index.js"
