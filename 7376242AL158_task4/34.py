n = int(input("Enter number of reviews: "))
lst = []

for _ in range(n):
    rid = input("Review ID: ")
    sentiment = input("Sentiment (POS/NEG/NEU): ")
    lst.append({"review_id": rid, "sentiment": sentiment})

count = {}
for r in lst:
    s = r["sentiment"]
    count[s] = count.get(s, 0) + 1

max_sentiment = max(count, key=count.get)

print("Sentiment counts:", count)
print("Sentiment with maximum occurrence:", max_sentiment)
