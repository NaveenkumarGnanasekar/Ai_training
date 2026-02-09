n = int(input("enter number of students:"))
lst=[]
dict={}
for i in range(1,n+1):
    name = input(f"enter name of student {i}:")
    scores=list(map(int,input(f"enter score of student {i}:").split()))
    dict[name]=scores
    lst.append(scores)
lst2 = [j for i in lst for j in i]
total_avg=[]
avg_lst=[]
class_avg=sum(lst2)/len(lst2)
for i,j in dict.items():
    avg = sum(j)/len(j)
    avg_lst.append(avg)
    if avg > class_avg:
        total_avg.append(i)
lst1=list(zip(dict.keys(),avg_lst))
print(f"average score of each student : {lst1}")
print(f"list of student with average more than class avgerage {class_avg} is {total_avg}")
        
