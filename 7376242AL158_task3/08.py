n = int(input("enter the number of elements :"))
lst =[]
for i in range (n):
    num = int(input("enter  number :"))
    lst.append(num)
for i in range(len(lst)-1):
    for j in range (i+1,len(lst)):
        if j !=len(lst)-1:
            if lst[j] > lst[i]:
                break
        
    else:
        print(lst[i])