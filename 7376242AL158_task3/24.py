n = input("enter size of the 2D List(eg:3x3):").split("x")
n1 = list (map(int,n))
lst=[]
for i in range(n1[0]):
    lst1=[]
    for j in range(n1[1]):
        num = int(input(f"enter element at {i},{j}:"))
        lst1.append(num)
    lst.append(lst1)
n = len(lst)
primary = sum(lst[i][i] for i in range(n))
secondary = sum(lst[i][n - 1 - i] for i in range(n))
print("primary:",primary)
print("secondary:",secondary)