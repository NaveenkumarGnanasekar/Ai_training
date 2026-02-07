n = int(input("enter number of tuple:"))
lst=[]
dict={}
for i in range (1,n+1):
    a = int(input(f"enter element in tuple {i}:"))
    b = int(input(f"enter element in tuple {i}:"))
    t = (a,b)
    lst.append(t)
for i in range(len(lst)):
    count=lst.count(lst[i])
    dict.setdefault(lst[i],count)
print(dict)
