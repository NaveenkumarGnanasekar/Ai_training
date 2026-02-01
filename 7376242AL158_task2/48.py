n = int(input("enter a number :"))
d = int(input ("enter a digit :"))
count =0 
b =n 
while b !=0:
    digit = b %10 
    if digit == d:
        count+=1
    b //=10
print("count of D in N = ", count )