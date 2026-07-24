import sys, uuid, datetime, re, urllib.request, urllib.error, base64, ssl

AUTH_USER = "ssklabovskii@astralinux.ru"
PASS_FILE = None
CALENDAR_URL = "https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal"

def get_auth():
    import os
    pf = os.path.expanduser("~/.config/opencode/secrets/calendar_pass")
    with open(pf) as f:
        return f.read().strip()

def request(method, url, data=None, headers=None):
    auth_pass = get_auth()
    auth_str = base64.b64encode(f"{AUTH_USER}:{auth_pass}".encode()).decode()
    hdrs = headers or {}
    req = urllib.request.Request(url, data=data, headers=hdrs)
    req.add_header("Authorization", f"Basic {auth_str}")
    req.get_method = lambda: method
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        resp = urllib.request.urlopen(req, context=ctx)
        return resp
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()[:200]}")
        sys.exit(1)

if len(sys.argv) < 3:
    print("Usage: delete <uid>  |  modify <uid> --set FIELD=VALUE [--date YYYY-MM-DD]")
    sys.exit(1)

cmd = sys.argv[1]
uid = sys.argv[2]

if cmd == "delete":
    url = f"{CALENDAR_URL}/{uid}.ics"
    resp = request("DELETE", url)
    print(f"Deleted: {uid}")
    sys.exit(0)

elif cmd == "modify":
    if "--set" not in sys.argv:
        print("Missing --set FIELD=VALUE")
        sys.exit(1)

    set_idx = sys.argv.index("--set")
    field_val = sys.argv[set_idx + 1]

    if "=" not in field_val:
        print("Use --set FIELD=VALUE")
        sys.exit(1)

    field, value = field_val.split("=", 1)

    date_override = None
    if "--date" in sys.argv:
        di = sys.argv.index("--date")
        date_override = sys.argv[di + 1]

    # For recurring events, we need RECURRENCE-ID
    # First try GET to see the current event
    url = f"{CALENDAR_URL}/{uid}.ics"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    auth_pass = get_auth()
    auth_str = base64.b64encode(f"{AUTH_USER}:{auth_pass}".encode()).decode()
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Basic {auth_str}")
    try:
        resp = urllib.request.urlopen(req, context=ctx)
        ics_data = resp.read().decode()
    except urllib.error.HTTPError as e:
        print(f"Cannot fetch event {uid}: HTTP {e.code}")
        sys.exit(1)

    # Check if it has RRULE
    has_rrule = "RRULE" in ics_data

    if has_rrule and date_override:
        # Find the master DTSTART
        dtstart_match = re.search(r"DTSTART(?:[^:]*):([^\r\n]+)", ics_data)
        if not dtstart_match:
            print("Cannot find DTSTART")
            sys.exit(1)

        dtstart_str = dtstart_match.group(1)
        dtstart_val = dtstart_str.replace("Z", "").replace("T", "T")

        # Parse original DTSTART
        if "T" in dtstart_val:
            orig_dt = datetime.datetime.strptime(dtstart_val[:15], "%Y%m%dT%H%M%S")
        else:
            orig_dt = datetime.datetime.strptime(dtstart_val[:8], "%Y%m%d")

        # Parse override date
        override_date = datetime.datetime.strptime(date_override, "%Y-%m-%d")
        # Keep the same time as original
        override_dt = override_date.replace(hour=orig_dt.hour, minute=orig_dt.minute, second=orig_dt.second)

        # Create a RECURRENCE-ID in the same TZID format as DTSTART
        tzid_match = re.search(r"DTSTART(;[^:]*):", ics_data)
        tzid_str = tzid_match.group(1) if tzid_match else ""

        rid_str = override_dt.strftime("%Y%m%dT%H%M%S")

        # Create override VEVENT
        override_lines = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            "PRODID:-//OpenCode//Calendar//EN",
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"RECURRENCE-ID{tzid_str}:{rid_str}",
            f"DTSTART{tzid_str}:{rid_str}",
            f"DTEND{tzid_str}:{rid_str}",
            f"SUMMARY:{value}",
            f"DESCRIPTION:{value}",
            "END:VEVENT",
            "END:VCALENDAR",
        ]
        ics_content = "\r\n".join(override_lines) + "\r\n"
        override_uid = str(uuid.uuid4())
        override_url = f"{CALENDAR_URL}/{override_uid}.ics"

        resp = request("PUT", override_url, data=ics_content.encode(), headers={"Content-Type": "text/calendar; charset=utf-8"})
        print(f"Modified recurring event {uid} on {date_override}: {field}={value}")

    elif has_rrule:
        # No date specified, modify the master (all instances)
        # Replace SUMMARY/DESCRIPTION in the master
        import urllib.parse

        new_ics = re.sub(
            rf"^{field}.*$",
            f"{field}:{value}",
            ics_data,
            flags=re.MULTILINE
        )

        resp = request("PUT", url, data=new_ics.encode(), headers={"Content-Type": "text/calendar; charset=utf-8"})
        print(f"Modified master event {uid}: {field}={value}")

    else:
        # Simple non-recurring event - just update field
        new_ics = re.sub(
            rf"^{field}.*$",
            f"{field}:{value}",
            ics_data,
            flags=re.MULTILINE
        )

        resp = request("PUT", url, data=new_ics.encode(), headers={"Content-Type": "text/calendar; charset=utf-8"})
        print(f"Modified event {uid}: {field}={value}")

else:
    print(f"Unknown command: {cmd}")
    sys.exit(1)
