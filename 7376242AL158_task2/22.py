lenght = int(input ("enter the lenght :"))
width = int(input ("enter the width :"))
height = int (input ("enter the height :"))
if lenght > 0 and width > 0 and height > 0:
    if lenght+width+height <= 150:
        print("the package is accepted")
else :
    print("the package is rejected ")