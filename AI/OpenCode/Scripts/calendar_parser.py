import sys, re, datetime

def parse_date_arg(s):
    if s == 'today':
        return datetime.date.today()
    elif s == 'tomorrow':
        return datetime.date.today() + datetime.timedelta(days=1)
    elif s == 'week':
        return None
    else:
        try:
            return datetime.datetime.strptime(s, '%Y-%m-%d').date()
        except:
            return datetime.date.today()

target = parse_date_arg(sys.argv[1] if len(sys.argv) > 1 else 'today')

raw = sys.stdin.read()
if not raw.strip():
    print('No data from calendar')
    sys.exit(0)

raw = re.sub(r'\r\n', '\n', raw)
unfolded = []
for line in raw.split('\n'):
    if not line:
        continue
    if line[0] in (' ', '\t') and unfolded:
        unfolded[-1] += line[1:]
    else:
        unfolded.append(line)

events = []
current = None
depth = 0

for line in unfolded:
    s = line.strip()
    if s == 'BEGIN:VEVENT':
        current = {'ATTENDEES': []}
        depth = 1
    elif s == 'BEGIN:VALARM':
        depth += 1
    elif s == 'END:VALARM':
        depth -= 1
    elif s == 'END:VEVENT':
        if current is not None:
            events.append(current)
        current = None
        depth = 0
    elif current is not None and depth == 1 and ':' in s:
        key_part, _, val = s.partition(':')
        key = key_part.split(';')[0]
        if key == 'ATTENDEE':
            for p in key_part.split(';')[1:]:
                if '=' in p:
                    pk, pv = p.split('=', 1)
                    if pk == 'CN':
                        current['ATTENDEES'].append(pv.strip('"'))
        else:
            current[key] = val

def parse_dt(v):
    v = v.replace('Z', '')
    if 'T' in v:
        return datetime.datetime.strptime(v[:15], '%Y%m%dT%H%M%S')
    else:
        return datetime.datetime.strptime(v[:8], '%Y%m%d')

def expand_rrule(dt_start, dt_end, rrule_str, until=None):
    """Expand recurring event into instances within target date range."""
    import calendar as cal_mod
    instances = [(dt_start, dt_end)]
    if not rrule_str:
        return instances

    # Parse RRULE parts
    parts = {}
    for pair in rrule_str.split(';'):
        if '=' in pair:
            k, v = pair.split('=', 1)
            parts[k] = v

    freq = parts.get('FREQ', '')
    interval = int(parts.get('INTERVAL', 1))
    count = parts.get('COUNT')
    until_str = parts.get('UNTIL')

    if not freq:
        return [(dt_start, dt_end)]

    # Determine the range end for expansion
    range_end = None
    if target:
        range_end = datetime.datetime.combine(target + datetime.timedelta(days=1), datetime.time(0, 0))
    else:
        range_end = dt_start + datetime.timedelta(days=365)

    if until_str:
        try:
            until_dt = datetime.datetime.strptime(until_str[:15], '%Y%m%dT%H%M%S')
            range_end = min(range_end, until_dt)
        except:
            pass

    duration = dt_end - dt_start
    instances = []
    current = dt_start
    instance_count = 0
    max_count = int(count) if count else 365

    while current < range_end and instance_count < max_count:
        instance_end = current + duration
        instances.append((current, instance_end))
        instance_count += 1

        if freq == 'DAILY':
            current += datetime.timedelta(days=interval)
        elif freq == 'WEEKLY':
            current += datetime.timedelta(weeks=interval)
        elif freq == 'MONTHLY':
            month = current.month + interval
            year = current.year + (month - 1) // 12
            month = ((month - 1) % 12) + 1
            day = min(current.day, cal_mod.monthrange(year, month)[1])
            current = current.replace(year=year, month=month, day=day, hour=current.hour, minute=current.minute)
        else:
            break

    return instances

def get_org(e):
    v = e.get('ORGANIZER', '')
    if not v:
        return ''
    for p in v.split(';'):
        if p.startswith('CN='):
            return p[3:].strip('"')
    if 'mailto:' in v:
        return v.split('mailto:')[-1]
    return v

def clean(s):
    if not s:
        return ''
    s = s.replace('\\n', '\n').replace('\\N', '\n')
    s = s.replace('\\,', ',').replace('\\;', ';')
    s = s.replace('\\\\', '\\')
    # decode \uXXXX
    s = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)
    # decode %XX
    s = re.sub(r'%([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)
    return s.strip()

# First pass: collect all master events with RRULE
master_events = {}
for e in events:
    uid = e.get('UID', '')
    if uid:
        if uid not in master_events:
            master_events[uid] = e
        else:
            # Keep the one with more info (has SUMMARY)
            if not master_events[uid].get('SUMMARY') and e.get('SUMMARY'):
                master_events[uid] = e

# Second pass: handle overrides (RECURRENCE-ID)
overrides = {}
for e in events:
    if 'RECURRENCE-ID' in e:
        uid = e.get('UID', '')
        rid = e.get('RECURRENCE-ID', '')
        if uid:
            overrides[(uid, rid)] = e

seen = []
processed_masters = set()

# Process non-recurring events first
for e in events:
    if 'RECURRENCE-ID' in e:
        continue
    uid = e.get('UID', '')
    start = e.get('DTSTART', '')
    end = e.get('DTEND', '')
    summary = clean(e.get('SUMMARY', ''))
    location = clean(e.get('LOCATION', ''))
    desc = clean(e.get('DESCRIPTION', ''))
    organizer = get_org(e)
    rrule = e.get('RRULE', '')
    attendees = [a for a in e.get('ATTENDEES', []) if 'Sklabovskii' not in a and 'ssklabovskii' not in a.lower()]

    if not start:
        continue
    if not summary and not desc:
        continue

    try:
        dt_start = parse_dt(start)
        dt_end = parse_dt(end) if end else dt_start + datetime.timedelta(hours=1)
    except:
        continue

    if rrule:
        # Expand recurring event
        instances = expand_rrule(dt_start, dt_end, rrule)
        for inst_start, inst_end in instances:
            if target and inst_start.date() != target:
                continue
            # Check for override
            override_key = None
            for (ouid, orid) in overrides:
                if ouid == uid:
                    rid_clean = orid.replace('Z', '')
                    try:
                        rid_dt = datetime.datetime.strptime(rid_clean[:15], '%Y%m%dT%H%M%S')
                        if rid_dt.date() == inst_start.date():
                            override_key = (ouid, orid)
                    except:
                        pass
            if override_key:
                override = overrides[override_key]
                o_start = override.get('DTSTART', '')
                o_end = override.get('DTEND', '')
                o_summary = clean(override.get('SUMMARY', summary))
                o_location = clean(override.get('LOCATION', location))
                try:
                    if o_start:
                        inst_start = parse_dt(o_start)
                    if o_end:
                        inst_end = parse_dt(o_end)
                    summary = o_summary
                    location = o_location
                except:
                    pass

            dedup = f'{inst_start.date()}_{summary}_{location}_{inst_start.strftime("%H:%M")}'
            if dedup in seen:
                continue
            seen.append(dedup)

            if 'T' in start:
                time_str = f"{inst_start.strftime('%H:%M')}\u2013{inst_end.strftime('%H:%M')}"
            else:
                time_str = 'allday'

            loc_str = f" @ {location}" if location else ''
            print()
            print('=' * 60)
            print(f"[{time_str}]{loc_str}")
            print(summary)
            if organizer:
                print(f"Organizer: {organizer}")
            if attendees:
                print(f"Participants: {', '.join(attendees)}")
            if desc:
                print()
                print(desc[:600])
        continue

    # Non-recurring
    event_date = dt_start.date()
    if target and event_date != target:
        continue

    dedup = f'{event_date}_{summary}_{location}'
    if dedup in seen:
        continue
    seen.append(dedup)

    if 'T' in start:
        time_str = f"{dt_start.strftime('%H:%M')}\u2013{dt_end.strftime('%H:%M')}"
    else:
        time_str = 'allday'

    loc_str = f" @ {location}" if location else ''
    print()
    print('=' * 60)
    print(f"[{time_str}]{loc_str}")
    print(summary)
    if organizer:
        print(f"Organizer: {organizer}")
    if attendees:
        print(f"Participants: {', '.join(attendees)}")
    if desc:
        print()
        print(desc[:600])

print()
print('=' * 60)
label = target.strftime('%d.%m.%Y') if target else 'week'
print(f"Total events on {label}: {len(seen)}")
