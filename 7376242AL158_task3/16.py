lst = [0,1,2,3,4,5,6,7,8,9]
n = int(input("enter a number :"))
b =n 
while b !=0:
    digit = b %10
    if digit in lst :
        lst.remove(digit)
    b //=10
print(f"the missing digit in the given number = {lst}")