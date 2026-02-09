n =int(input("enter number of passenger :"))
lst=[]
dup_lst=[]
dict={}
for i in range(1,n+1):
    coach=input("enter coach :")
    seat_number = int(input("enter seat number :"))
    t = (coach,seat_number)
    if t in lst:
        dup_lst.append(t)
    else:
        lst.append(t)
for i in lst:
    if i[0] in dict.keys():
        dict[i[0]]+=1
    else:
        dict[i[0]]=1
print(dup_lst)
print(dict)