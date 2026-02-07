n = int(input("enter the number of numbers :"))
lst = []
for i in range (n):
    num = int(input("the number :"))
    lst.append(num)
target = int(input("enter the target number :"))
for i in range (len(lst)):
    for j in range (len(lst)):
        if lst[i]+lst[j]==target:
            print("(",i,",",j,")")

