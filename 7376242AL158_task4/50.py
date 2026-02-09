n = int(input("Enter number of papers: "))
papers = {}

for _ in range(n):
    pid = input("Paper ID: ")
    keywords = input("Keywords (space-separated): ").split()
    papers[pid] = keywords


all_keywords = set()
for kw in papers.values():
    all_keywords |= set(kw)


common_keywords = None
for kw in papers.values():
    if common_keywords is None:
        common_keywords = set(kw)
    else:
        common_keywords &= set(kw)


unique_count = {pid: len(set(kw)) for pid, kw in papers.items()}
max_paper = max(unique_count, key=unique_count.get)

print("Total unique keywords:", len(all_keywords))
print("Keywords common to every paper:", common_keywords)
print("Paper with maximum unique keywords:", max_paper, "(", unique_count[max_paper], ")")
