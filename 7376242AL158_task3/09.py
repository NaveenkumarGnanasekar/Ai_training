n = int(input("enter the number of elements :"))
lst =[]
for i in range (n):
    num = int(input("enter number :"))
    lst.append(num)
lst1=[]
for i in range(len(lst)):
    if i ==0 or lst[i]!=lst[i-1]:
        lst1.append(lst[i])
print(lst1)
