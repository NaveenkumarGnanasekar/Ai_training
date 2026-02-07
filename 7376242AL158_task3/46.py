expected = {"python", "data", "analysis", "sql"}
docs = [
    "Python is great for data analysis",
    "I also know machine learning"
]
words_in_docs = set()

for doc in docs:
    words_in_docs.update(doc.lower().split())

    covered = expected & words_in_docs
    missing = expected - words_in_docs

    coverage_percentage = (len(covered) / len(expected)) * 100 if expected else 0


print("Coverage:", coverage_percentage)
print("Missing words:", missing)
