n = int(input("Enter number of shows: "))
shows = {}

for _ in range(n):
    time = input("Show time: ")
    seats = set(input("Booked seats (space-separated): ").split())
    shows[time] = seats
total_seats = int(input("Enter total seats in theater: "))
fully_booked = [t for t, s in shows.items() if len(s) == total_seats]
common_seats = None
for s in shows.values():
    if common_seats is None:
        common_seats = s.copy()
    else:
        common_seats &= s
print("Fully booked shows:", fully_booked)
print("Seats booked in every show:", common_seats)
