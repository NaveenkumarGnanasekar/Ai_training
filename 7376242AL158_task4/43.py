n = int(input("Enter number of attendance logs: "))
logs = []

for _ in range(n):
    session = input("Session ID: ")
    attendee = input("Attendee ID: ")
    logs.append((session, attendee))

session_attendees = {}
attendee_sessions = {}

for session, attendee in logs:
    session_attendees.setdefault(session, set()).add(attendee)
    attendee_sessions.setdefault(attendee, set()).add(session)

total_per_session = {s: len(a) for s, a in session_attendees.items()}
multi_session_attendees = [a for a, s in attendee_sessions.items() if len(s) > 1]

print("Total attendees per session:", total_per_session)
print("Attendees who attended more than one session:", multi_session_attendees)