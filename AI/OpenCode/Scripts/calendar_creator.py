import sys, uuid, datetime, re, urllib.request, urllib.error, base64, ssl

def usage():
    print("Usage: calendar-create.sh <title> <start> [end] [--location LOC] [--description DESC] [--attendee EMAIL ...]")
    print("  title: event title in quotes")
    print("  start: YYYY-MM-DD HH:MM (24h)")
    print("  end:   YYYY-MM-DD HH:MM (default: start + 1h)")
    print("  --location: venue or link")
    print("  --description: agenda text")
    print("  --attendee: participant email (can be multiple)")
    sys.exit(1)

if len(sys.argv) < 4:
    usage()

auth_user = sys.argv[1]
auth_pass = sys.argv[2]
base_url = sys.argv[3]  # CalDAV base URL (without .ics)

args = sys.argv[4:]
if not args:
    usage()

title = args[0]
start_str = args[1]
end_str = None
location = ''
description = ''
attendees = []

i = 2
while i < len(args):
    if args[i] == '--location' and i + 1 < len(args):
        location = args[i + 1]
        i += 2
    elif args[i] == '--description' and i + 1 < len(args):
        description = args[i + 1]
        i += 2
    elif args[i] == '--attendee' and i + 1 < len(args):
        attendees.append(args[i + 1])
        i += 2
    else:
        end_str = args[i]
        i += 1

try:
    dt_start = datetime.datetime.strptime(start_str, '%Y-%m-%d %H:%M')
    if end_str:
        dt_end = datetime.datetime.strptime(end_str, '%Y-%m-%d %H:%M')
    else:
        dt_end = dt_start + datetime.timedelta(hours=1)
except:
    print("Error: invalid date format. Use YYYY-MM-DD HH:MM")
    sys.exit(1)

event_uid = str(uuid.uuid4())
now = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
dt_start_str = dt_start.strftime('%Y%m%dT%H%M%S')
dt_end_str = dt_end.strftime('%Y%m%dT%H%M%S')

lines = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//OpenCode//Calendar//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    f'UID:{event_uid}',
    f'DTSTART:{dt_start_str}',
    f'DTEND:{dt_end_str}',
    f'DTSTAMP:{now}',
    f'CREATED:{now}',
    f'LAST-MODIFIED:{now}',
    f'SUMMARY:{title}',
]

if location:
    lines.append(f'LOCATION:{location}')
if description:
    # fold long lines
    desc_clean = description.replace('\n', '\\n')
    if len(desc_clean) > 75:
        folded = []
        pos = 0
        while pos < len(desc_clean):
            if pos == 0:
                folded.append(f'DESCRIPTION:{desc_clean[pos:pos+75]}')
            else:
                folded.append(f' {desc_clean[pos:pos+75]}')
            pos += 75
        lines.extend(folded)
    else:
        lines.append(f'DESCRIPTION:{desc_clean}')

for email in attendees:
    lines.append(f'ATTENDEE;ROLE=REQ-PARTICIPANT;PARTSTAT=NEEDS-ACTION;CN={email}:mailto:{email}')

lines.extend([
    'END:VEVENT',
    'END:VCALENDAR',
])

ics_content = '\r\n'.join(lines) + '\r\n'

url = f'{base_url.rstrip("/")}/{event_uid}.ics'
headers = {'Content-Type': 'text/calendar; charset=utf-8'}

auth_str = base64.b64encode(f'{auth_user}:{auth_pass}'.encode()).decode()
req = urllib.request.Request(url, data=ics_content.encode('utf-8'), headers=headers)
req.add_header('Authorization', f'Basic {auth_str}')
req.get_method = lambda: 'PUT'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    resp = urllib.request.urlopen(req, context=ctx)
    if resp.status in (200, 201, 204):
        print(f"Event created: {title}")
        print(f"  When: {dt_start.strftime('%d.%m.%Y %H:%M')} - {dt_end.strftime('%H:%M')}")
        if location:
            print(f"  Where: {location}")
        print(f"  UID: {event_uid}")
    else:
        print(f"Error: HTTP {resp.status}")
        print(resp.read().decode()[:200])
        sys.exit(1)
except urllib.error.HTTPError as e:
    print(f"Error: HTTP {e.code}")
    print(e.read().decode()[:300])
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
