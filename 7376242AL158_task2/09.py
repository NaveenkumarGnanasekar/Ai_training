emp_id = int(input ("enter employee ID :"))
b = emp_id
count =0
while b !=0:
    count +=1
    b //=10
if count ==6 and emp_id%7==0:
    print("valid ID")
else :
    print("invalid ID")    