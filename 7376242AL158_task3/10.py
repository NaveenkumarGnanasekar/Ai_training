n = int(input("enter the number of studends :" ))
names =[]
marks=[]
rank=list(range(1,n+1))
for i in range (1,n+1):
    name = input(f"enter name of student{i}:")
    mark = int(input(f"enter mark of the student {i}:"))
    names.append(name)
    marks.append(mark)
lst = list(zip(names,marks))
sorted_lst = sorted(lst,key=lambda x :x[1],reverse=True)
lst1 =[i[0] for i in sorted_lst ]
final_lst = list(zip(lst1,rank))
print(final_lst)

