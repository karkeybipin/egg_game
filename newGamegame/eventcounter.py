events = [
    {"event": "login", "timestamp": "2024-09-29 10:00:00"},
    {"event": "logout", "timestamp": "2024-09-29 11:00:00"},
    {"event": "login", "timestamp": "2024-09-30 09:00:00"},
    {"event": "login", "timestamp": "2024-09-30 10:30:00"},
    {"event": "purchase", "timestamp": "2024-09-30 11:00:00"},
]

event_counts = {}
for event in events:
    event_name = event["event"]
    if event_name in event_counts:
        event_counts[event_name] += 1
    else:
        event_counts[event_name] = 1
print("Event counts:")
for event_name, count in event_counts.items():
    print(f"{event_name}: {count}")
