#!/bin/bash
# Добавляет участников к существующему событию в календаре SOGo.
# После PUT нужно открыть событие в RuPost и сохранить, чтобы ушло приглашение.
#
# Usage:
#   ./add-attendees.sh <UID события> <CN=email> [<CN=email> ...]
#
# Example:
#   ./add-attendees.sh a92d0fad-66ef-4dd1-811b-f9e511a6d4fc \
#     "Дмитрий Тайлаков=dtailakov@astralinux.ru"

CAL_PASS="$(cat "$HOME/.config/opencode/secrets/calendar_pass")"
EVENT_UID="$1"
shift

if [ -z "$EVENT_UID" ]; then
  echo "Usage: $0 <UID> [CN=email ...]"
  exit 1
fi

ICS_URL="https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal/${EVENT_UID}.ics"

# GET current ICS
ICS=$(curl -s --user "ssklabovskii@astralinux.ru:${CAL_PASS}" "${ICS_URL}")

# Remove existing ORGANIZER and ATTENDEE lines, insert new ones after UID
NEW_ICS=$(echo "$ICS" | python3 -c "
import sys
lines = sys.stdin.read().split('\n')
entries = sys.argv[1:]

# Remove old ORGANIZER/ATTENDEE
lines = [l for l in lines if not l.startswith('ORGANIZER') and not l.startswith('ATTENDEE')]

org = 'ORGANIZER;CN=Сергей Склабовский:mailto:ssklabovskii@astralinux.ru'
atts = ['ATTENDEE;PARTSTAT=ACCEPTED;CN=Сергей Склабовский;ROLE=CHAIR:mailto:ssklabovskii@astralinux.ru']
for e in entries:
    cn, email = e.split('=', 1)
    atts.append(f'ATTENDEE;PARTSTAT=NEEDS-ACTION;CN={cn};RSVP=TRUE:mailto:{email}')

result = []
for line in lines:
    result.append(line)
    if line.startswith('UID:'):
        result.append(org)
        for a in atts:
            result.append(a)

print('\n'.join(result))
" "$@")

# PUT updated ICS
RESP=$(curl -s -w "\n%{http_code}" --user "ssklabovskii@astralinux.ru:${CAL_PASS}" \
  -X PUT "${ICS_URL}" -H "Content-Type: text/calendar" -d "${NEW_ICS}")
HTTP_CODE=$(echo "${RESP}" | tail -1)

if [ "$HTTP_CODE" = "204" ]; then
  echo "OK: участники добавлены к событию ${EVENT_UID}"
  echo "Важно: откройте событие в RuPost и сохраните, чтобы ушло приглашение"
else
  echo "Error: HTTP ${HTTP_CODE}"
  echo "${RESP}" | head -n -1
  exit 1
fi
