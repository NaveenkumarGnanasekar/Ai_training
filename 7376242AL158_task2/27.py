battery = int(input ("enter the battery percentage :"))
drop = int(input("enter the battery drop percentage per hour :"))
hours = battery // drop
if battery <=20 :
    print("the hours left is :", 0)
else :
    print("the hours left to reach 20% of battery is :", hours -2 , "hr")