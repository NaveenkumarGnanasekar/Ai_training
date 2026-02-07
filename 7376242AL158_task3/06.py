n = input ("enter the size of the 2D list(eg:3x3) :").split("x")
n1 = list(map(int,n))
lst = []
for i in range (n1[0]):
    lst1=[]
    for j in range (n1[1]):
        num = int(input(f"enter number in {i},{j} :"))
        lst1.append(num)
    lst.append(lst1)

for i in range (n1[1]):
    sum = 0
    for j in range(n1[0]):
        sum +=lst[j][i]

    print(f"sum of elements in coloum {i} = {sum}")