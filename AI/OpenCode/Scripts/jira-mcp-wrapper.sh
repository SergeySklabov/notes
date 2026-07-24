#!/bin/bash
# Wrapper to launch Jira & Confluence MCP with tokens from secrets file
export JIRA_URL="https://jira.astralinux.ru"
export JIRA_API_TOKEN=$(cat "$HOME/.config/opencode/secrets/jira_pat")
export CONFLUENCE_URL="https://life.astralinux.ru"
export CONFLUENCE_EMAIL="ssklabovskii@astralinux.ru"
export CONFLUENCE_API_TOKEN=$(cat "$HOME/.config/opencode/secrets/confluence_pat")
exec npx -y mcp-jira-confluence 2>/tmp/jira-mcp-err.log