n = int(input("enter the number of students:"))
lst=[]
for i in range(1,n+1):
    name = input(f"enter name of the student {i}:")
    score= int(input(f"enter score of the student {i}:")) 
    t= (name,score)
    lst.append(t)
sort_lst= sorted(lst,key=lambda x : x[1],reverse=True)
print(sort_lst)