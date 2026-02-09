n = int(input("Enter number of documents: "))
docs = []

for _ in range(n):
    doc_id = input("Doc ID: ")
    tags = input("Tags (space-separated): ").split()
    docs.append({"doc_id": doc_id, "tags": tags})


no_tag_docs = [d["doc_id"] for d in docs if len(d["tags"]) == 0]


common_tags = set(docs[0]["tags"])
for d in docs[1:]:
    common_tags &= set(d["tags"])

print("Documents with no tags:", no_tag_docs)
print("Tags present in every document:", common_tags)

