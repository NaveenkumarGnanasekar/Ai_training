n_seat = int(input ("enter the number of seats :"))
n= int(input("enter the number of customers:"))
for i in range (1,n+1):
    if i <=n_seat:
        print("booked")
    else :
        print("housefull")