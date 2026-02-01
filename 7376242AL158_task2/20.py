lst = []
num = int(input("enter a number:"))
b = num 
while b !=0:
    num1 = b %10
    lst.append(num1)
    b //=10
sort = sorted(lst)
for i  in range (0,10):
    if i not in sort:
        print("the least missing digit in the given number is =",i )
        
