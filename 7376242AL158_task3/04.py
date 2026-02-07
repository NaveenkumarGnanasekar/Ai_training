n = int(input("enter number of numbers in the list :"))
lst =[]
for i in range (n):
    num = int(input("enter number :"))
    lst.append(num)
k = int(input("enter the number of rotation :"))
lst1 = lst[-k:]+lst[:-k]
print(lst1)