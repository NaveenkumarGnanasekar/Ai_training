parking_hours = int(input ("enter the number of hours parked :"))
if parking_hours <= 2:
    fee = parking_hours * 20 
elif parking_hours <=5:
    fee = 2 *20 + (parking_hours -2) *15
else :
    fee = 2 *20 + 3 *15 + (parking_hours -5) *10
print("the parking fee is :", fee)