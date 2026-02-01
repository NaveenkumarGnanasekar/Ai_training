late = int(input("enter the number of late days :"))
fine =0 
if late >=1 and late <=5:
    fine = late * 2         
elif late >=6 and late <=10:
    fine = late * 3
else :
    fine = late *5
print("the fine for the late submission is :", fine )
