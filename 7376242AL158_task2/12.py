A = int(input("enter amount :"))
notes = [500, 200, 100, 50, 20, 10, 1]
count = 0

for note in notes:
    count += A // note
    A %= note

print("total number of bills :",count)
