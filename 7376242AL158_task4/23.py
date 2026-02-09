n = int (input("enter number of employee:"))
set1=set()
lst=[]
for i in range(1,n+1):
    name = input("enter name of the employee:")
    time = float(input("enter time of entry:"))
    set1.add(time)
    t=(name,time)
    lst.append(t)
if len(set1)==len(lst):
    print("valid log")
else:
    print("Invalid log ")