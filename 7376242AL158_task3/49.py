features = {
    "age": 2,
    "income": 8,
    "education": 5
}

total = sum(features.values())
if total == 0:
    dict={k: 0 for k in features}
else:
    dict = {k: v / total for k, v in features.items()}
print(dict)