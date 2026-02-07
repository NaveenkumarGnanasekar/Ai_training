n = int(input("enter the number of numbers:"))
lst =[]
lst1=[]
for i in range (n):
    num = int(input("enter the number :"))
    lst.append(num)
for i in lst :
    if i in lst1:
        continue
    else:
        lst1.append(i)
print(f"the list given = {lst} and the list without duplicate = {lst1}")
