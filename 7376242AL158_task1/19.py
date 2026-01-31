balance = int(input ("enter balance :"))
withdraw = int(input ("enter withdraw amount :"))
if withdraw % 100 !=0 :
    print("please enter the amonut in multiple of 100")
else :
    if withdraw <= balance :
        balance = balance - withdraw
        print("withdrawal successful")
       
        if balance <=500:
            print("minimum balance alert")
        else:
            print("the remaining balance is :", balance)

    else :
        print("insufficient balance")
