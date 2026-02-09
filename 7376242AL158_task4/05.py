n = int(input("enter number of students:"))
lst =[]
lst1=[]
lst2=[]
dict1={}
for i in range(1,n+1):
    student=input("enter student name :")
    book = input("enter book name :")
    day=int(input("enter number of days:"))
    dict={"student_name":student,"book_name":book,"days":day}
    lst.append(dict)
for i in lst :
    if i["days"] > 7 :
        lst1.append(i["student_name"])
for i in lst :
    if i["book_name"] in dict1.keys():
        dict1[i["book_name"]] +=1
    else:
        dict1[i["book_name"]] = 1
print(lst1 ,"has borrowed book for more than 7 days")

print(dict1,", dictionary with how many times each book is borrowed.")