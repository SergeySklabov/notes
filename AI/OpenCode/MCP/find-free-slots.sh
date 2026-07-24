#!/bin/bash
# Проверяет свободные слоты для каждого участника по отдельности
# и возвращает только те, где все свободны.
#
# Usage:
#   ./find-free-slots.sh <since> <until> <duration_min> <email> [<email> ...]
#
# Example:
#   ./find-free-slots.sh "2026-07-16" "2026-07-17" 30 \
#     "ssklabovskii@astralinux.ru" "dtailakov@astralinux.ru"

if [ $# -lt 4 ]; then
  echo "Usage: $0 <since> <until> <duration_min> <email> [<email> ...]"
  exit 1
fi

SINCE="$1"
UNTIL="$2"
DURATION="$3"
shift 3
EMAILS=("$@")

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

# Function to call MCP and extract slots
call_mcp() {
  local email="$1"
  local outfile="$2"
  python3 -c "
import subprocess, json, select, time, sys

proc = subprocess.Popen(
    ['bash', '$SCRIPT_DIR/rupst-calendar-mcp.sh'],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

def call(msg, timeout=30):
    proc.stdin.write(json.dumps(msg) + '\n')
    proc.stdin.flush()
    deadline = time.time() + timeout
    while time.time() < deadline:
        r, _, _ = select.select([proc.stdout], [], [], 0.3)
        if r:
            line = proc.stdout.readline()
            if line:
                return json.loads(line)
    return None

call({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'fs','version':'1.0'}}})
call({'jsonrpc':'2.0','method':'notifications/initialized'})

res = call({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{
    'name':'find_free_slots',
    'arguments':{
        'attendees': ['$email'],
        'since': '$SINCE',
        'until': '$UNTIL',
        'duration_minutes': $DURATION,
        'workday_start': '08:00',
        'workday_end': '19:00',
        'slot_granularity_minutes': 30,
        'include_weekends': False,
        'include_self': True,
        'limit': 50
    }
}}, timeout=60)

proc.terminate()

if res and 'result' in res:
    try:
        text = res['result']['content'][0]['text']
        slots = json.loads(text)
        if isinstance(slots, dict):
            if 'start_local' in slots:
                print(f\"{slots['start_local']}|{slots['end_local']}\")
        elif isinstance(slots, list):
            for s in slots:
                print(f\"{s['start_local']}|{s['end_local']}\")
    except:
        pass
" > "$outfile" 2>/dev/null
}

# Check each attendee
ALL_SLOTS=""
FIRST=true
for EMAIL in "${EMAILS[@]}"; do
  OUTFILE="$TMPDIR/slots_$(echo "$EMAIL" | tr '@.' '_').txt"
  echo "Checking $EMAIL..." >&2
  call_mcp "$EMAIL" "$OUTFILE"

  if $FIRST; then
    ALL_SLOTS=$(cat "$OUTFILE" 2>/dev/null)
    FIRST=false
  else
    # Intersect with existing slots
    INTERSECT=""
    while IFS='|' read -r START END; do
      [ -z "$START" ] && continue
      if echo "$ALL_SLOTS" | grep -q "${START}|${END}"; then
        INTERSECT="${INTERSECT}${START}|${END}"$'\n'
      fi
    done < "$OUTFILE"
    ALL_SLOTS="$INTERSECT"
  fi
done

# Output results
echo ""
echo "=== Свободные слоты для всех участников ==="
echo "$ALL_SLOTS" | while IFS='|' read -r START END; do
  [ -z "$START" ] && continue
  echo "  $START - $END"
done | sort

if [ -z "$ALL_SLOTS" ]; then
  echo "  (нет общих свободных слотов)"
fi
