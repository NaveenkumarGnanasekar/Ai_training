angle1 = int(input ("enter angle1:"))
angle2 = int (input ("enter angle2:"))
angle3 = int (input("enter angle3:"))
if angle1 == angle2 == angle3 :
    print("equilateral triangle")
elif (angle1 == angle2) or (angle2 == angle3) or (angle3 == angle1):
    print("isosceles triangle")
else :
    print("scalene triangle")
