token_number = int(input("enter the token number :"))
if token_number %4==0 and token_number %100!=0:
    print("allowed")
else :
    print("not allowed")