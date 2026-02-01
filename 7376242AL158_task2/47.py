n = int(input ("enter number of hours:"))
for i in range (n):
    n_temp= int(input(f"enter temperature at {i} hour:"))
    if n_temp > 45 :
        print("high temperature")
        break 
    else :
        print("safe temperature")