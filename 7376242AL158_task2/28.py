attend_per= int(input ("enter the attendence percentage of the student :"))
fine =0
if attend_per < 75:
    fine  = (75-attend_per) * 10
else :
    fine =0 
print("the fine amount of student = ", fine )