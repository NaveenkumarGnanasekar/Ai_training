n = int(input("enter number of message:"))
lst=[]
for i in range(1,n+1):
    str=input("enter message:")
    lst.append(str)
for i in range(len(lst)+1):
    for j in range(len(lst)-1,i,-1):
        if lst[i]==lst[j]:
            lst.remove(lst[j])
        if lst[j]=="":
            lst.remove(lst[j])
print(lst, "after cleanup")
