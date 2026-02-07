n = input("enter the size of 2D list (eg:3x3):").split("x")
lst=[]
count=1
n1= list(map(int,n))
for i in range(n1[0]):
    lst1=[]
    for j in range(n1[1]):
        num = int(input(f"enter number at {i},{j}:"))
        lst1.append(num)
    lst.append(lst1)

for i in lst :
    max1 = max(i)
    print(f"max in {count} row = {max1}")
    count+=1