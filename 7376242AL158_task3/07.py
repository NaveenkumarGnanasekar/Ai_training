n = input("enter the size of 2D list:").split("x")
lst =[]
n1= list(map(int,n))
for i in range (n1[0]):
    lst1=[]
    for j in range (n1[1]):
        num = int(input(f"enter number at {i},{j} :"))
        lst1.append(num)
    lst.append(lst1)
lst2=[j for i in lst for j in i]
print(f"original list:{lst}")
print(f"Flatten Nested List:{lst2}")
