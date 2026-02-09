n = int(input("Enter number of votes: "))
lst = []
for _ in range(n):
    voter = input("Voter ID: ")
    candidate = input("Candidate: ")
    lst.append((voter, candidate))

s = set()
i = []
count = {}

for voter, cand in lst:
    if voter in s:
        i.append((voter, cand))
    else:
        s.add(voter)
        count[cand] = count.get(cand, 0) + 1

print("Invalid votes:", i)
print("Final vote count:", count)
