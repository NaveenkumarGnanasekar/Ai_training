n = int(input("Enter number of transactions: "))
transactions = []

for _ in range(n):
    acc = input("Account ID: ")
    amt = float(input("Amount: "))
    ttype = input("Type (CREDIT/DEBIT): ")
    transactions.append({"account_id": acc, "amount": amt, "type": ttype})

balance = {}

for tr in transactions:
    acc = tr["account_id"]
    amt = tr["amount"]
    ttype = tr["type"]

    if acc not in balance:
        balance[acc] = 0

    if ttype == "CREDIT":
        balance[acc] += amt
    elif ttype == "DEBIT":
        balance[acc] -= amt

max_acc = max(balance, key=balance.get)

print("Final balance per account:", balance)
print("Account with maximum balance:", max_acc, "(", balance[max_acc], ")")
