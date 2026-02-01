n = int(input("enter distance in km :"))
charge = 0 
if n >=0 and n <=5 :
    charge = n *10
elif n >=6 and n <=15:
    charge = n * 8
else :
    charge = n *6
print("total fare = ", charge)