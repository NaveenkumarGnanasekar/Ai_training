n = int(input("enter the password:"))
count =0
b = n 
seven = False
while b !=0:
    digit = b %10
    if digit == 7:
        seven = True
    count +=1
    b //=10
if seven and count>=6:
    print("strong password")
else:
    print("weak password")
