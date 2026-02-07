n = input("enter size of the 2D List(eg:3x3):").split("x")
n1 = list (map(int,n))
lst=[]
for i in range(n1[0]):
    lst1=[]
    for j in range(n1[1]):
        num = int(input(f"enter element at {i},{j}:"))
        lst1.append(num)
    lst.append(lst1)
for i in lst:
    set1= set(i)
    if len(i) == len(set1):
        print(f"the row {lst.index(i)} is unique")
    else :
        print(f"the row {lst.index(i)} is not unique")