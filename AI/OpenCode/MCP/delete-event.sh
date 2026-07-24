#!/bin/bash
# Удаляет событие из календаря (в т.ч. с участниками).
# MCP delete_event не удаляет события с участниками — этот скрипт делает прямой CalDAV DELETE.
#
# Usage:
#   ./delete-event.sh <UID события>

CAL_PASS="$(cat "$HOME/.config/opencode/secrets/calendar_pass")"
UID="$1"

if [ -z "$UID" ]; then
  echo "Usage: $0 <UID>"
  exit 1
fi

URL="https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal/${UID}.ics"
HTTP_CODE=$(curl -s -w "%{http_code}" -o /dev/null --user "ssklabovskii@astralinux.ru:${CAL_PASS}" -X DELETE "${URL}")

if [ "$HTTP_CODE" = "204" ]; then
  echo "OK: событие ${UID} удалено"
else
  echo "Error: HTTP ${HTTP_CODE}"
  exit 1
fi
