balance = int(input ("enter balance in account :"))
withdraw = int(input ("enter amount :"))
if withdraw %100 !=0:
    print("valid amount of withdraw")
else :
    if withdraw <= balance :
        print("successful withdrawal")
        if balance <= 500:
            print("maintain minimum balance")
    else :
        print("insufficient balance ")
