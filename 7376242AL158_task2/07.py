n = int(input ("enter a number :"))
b =n 
sum =0
lst = [ 2,3,5,7]
while n !=0:
    digit = n %10
    if digit in lst :
        sum+=digit
    n //=10
print("the sum of all prime digit in the given number :", sum )