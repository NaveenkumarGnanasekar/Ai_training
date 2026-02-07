n = int(input("enter number of numbers :"))
lst =[]
for i in range (n):
    num = int(input("enter the number :"))

    lst.append(num)
min1=lst[0]
min2=lst[0]

for i in lst :
    if i <= min1:
        min2 = min1 
        min1 = i 
print(f"the second minimum element in the list is = {min2}")