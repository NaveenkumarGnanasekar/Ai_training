h = int(input("enter hours :"))
if h < 0 or h >=24:
    print("invalid hours")
else :
    if h <= 21 and h >=9:
        print("open")
    else :
        print("closed")