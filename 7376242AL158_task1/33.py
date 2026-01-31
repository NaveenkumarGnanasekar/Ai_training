n =int(input("enter a number :"))
rev = 0
b =n 
a=0 
while n!=0:
    a =n %10
    rev =rev *10 +a
    n //= 10 

if rev == b  :
    print("the number given is a palindrome ")
else:
    print("the number given is not a palindrome ")