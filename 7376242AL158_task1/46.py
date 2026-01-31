def factorial(m):
    for i in range(1, m):
        m = m * i
    return m
n = int (input ("enter a number ;"))
sum =0
b =n 
while n !=0:
    r =n %10
    sum +=factorial(r)
    n //=10 
if b == sum :
    print("the number given is a strong number")
else:
    print("the number given is not a strong number ")