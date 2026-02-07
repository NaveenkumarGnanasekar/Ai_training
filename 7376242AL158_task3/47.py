scores1 = list(map(int, input("enter marks: ").split()))
scores = sorted(scores1, reverse=True)

ranks = []
prev_score = None
prev_rank = 0

for i, score in enumerate(scores):
    if score == prev_score:
        ranks.append(prev_rank)
    else:
        rank = i + 1
        ranks.append(rank)
        prev_rank = rank
        prev_score = score
final = list(zip(scores,ranks))
print(final)
