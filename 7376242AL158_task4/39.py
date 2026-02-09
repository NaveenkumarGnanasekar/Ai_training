n = int(input("Enter number of leaderboard entries: "))
entries = []

for _ in range(n):
    player = input("Player: ")
    score = int(input("Score: "))
    entries.append((player, score))

seen = set()
invalid = []

final = {}

for player, score in entries:
    if player in seen:
        invalid.append((player, score))
    else:
        seen.add(player)
        final[player] = score

sorted_board = sorted(final.items(), key=lambda x: x[1], reverse=True)

print("Invalid duplicate player entries:", invalid)
print("Final sorted leaderboard:", sorted_board)
