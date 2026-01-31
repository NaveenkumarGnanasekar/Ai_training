lst = [2,3,5,7]
sum =0
n = int(input ("enter a number :"))
while n !=1:
    digit = n%10
    if digit in lst:
        sum+=digit
    n//=10
print("the sum of prime digits is :", sum)