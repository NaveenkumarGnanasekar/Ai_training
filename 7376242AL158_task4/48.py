n = int(input("Enter number of bids: "))
bids = []

for _ in range(n):
    bidder = input("Bidder ID: ")
    amount = float(input("Bid amount: "))
    bids.append((bidder, amount))

highest_per_bidder = {}

for bidder, amount in bids:
    if bidder not in highest_per_bidder:
        highest_per_bidder[bidder] = amount
    else:
        highest_per_bidder[bidder] = max(highest_per_bidder[bidder], amount)

best_bidder = max(bids, key=lambda x: x[1])[0]
best_bid = max(bids, key=lambda x: x[1])[1]

print("Highest bid per bidder:", highest_per_bidder)
print("Highest single bid overall:", best_bidder, "(", best_bid, ")")
