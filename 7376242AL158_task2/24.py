hours = int (input ("enter hours :"))
min = int(input("enter minutes :"))
change = int(input("enter the change in minutes :"))
total_min = hours * 60 + min + change
final_hours = (total_min // 60) % 24
final_min = total_min % 60
print("the new time is {}:{}".format(final_hours,final_min))