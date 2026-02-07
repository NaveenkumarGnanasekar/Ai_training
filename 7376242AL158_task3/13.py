n = int(input("enter the number of pairs :"))
lst =[]
for i in range(n):
    a=int(input("enter element 1:"))
    b=int(input("enter element 2:"))
    t = (a,b)
    lst.append(t)
lst1=[]
for i in lst :
    a,b = i 
    g = (b,a)
    if (b,a) in lst:
        lst.remove((b,a))
print(lst)