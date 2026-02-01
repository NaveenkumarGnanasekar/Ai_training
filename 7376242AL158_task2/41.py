n = int(input ("enter the vehicle type(1 for Bike, 2 for Car, 3 for Bus, 4 for Truck):"))
toll = 0 
if n ==1 :
    toll = 20
    print("toll amount = ", toll)
elif n == 2 :
    toll = 50 
    print("toll amount = ",toll)

elif n == 3 :
    toll = 100
    print("toll amount =", toll)
elif n == 4 :
    toll = 150
    print("toll amount = ",toll)
else :
    print("invalid type ")