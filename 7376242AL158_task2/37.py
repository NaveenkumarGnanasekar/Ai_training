num = input ("enter the batch number :")
last_digit = int(num)%10
if num[0]!="0" and last_digit%2==0:
    print("valid")
else :
    print("invalid")
