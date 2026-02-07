required = {
    "python": 0.4,
    "sql": 0.3,
    "ml": 0.3
}

candidate = {
    "python": 4,
    "sql": 3,
    "excel": 5
}

score = 0
for skill, weight in required.items():
    if skill in candidate:
        score += weight * candidate[skill]
print(score)
