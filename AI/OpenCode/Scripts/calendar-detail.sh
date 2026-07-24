#!/bin/bash

CALENDAR_URL="https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal.ics"
AUTH_USER="ssklabovskii@astralinux.ru"
PASS_FILE="$HOME/.config/opencode/secrets/calendar_pass"
DATE=${1:-today}

if [ ! -f "$PASS_FILE" ]; then
  echo "Error: password file not found"
  exit 1
fi

AUTH_PASS=$(cat "$PASS_FILE")

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

curl -s --max-time 10 -u "$AUTH_USER:$AUTH_PASS" "$CALENDAR_URL" -H "Accept: text/calendar" | python3 "$SCRIPT_DIR/calendar_parser.py" "$DATE"