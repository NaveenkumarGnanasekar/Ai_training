angle  = input ("enter the angles with space :").split()
lst = list (map (int , angle))
sum =0
flag =1
for i in lst:
    if i > 0 :
        sum += i 
    else :
        flag = 0 
if flag == 1 and sum == 180 :
    print ("valid triangle")
else :
    print("not a valid triangle")