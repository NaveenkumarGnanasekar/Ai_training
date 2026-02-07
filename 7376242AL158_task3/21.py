n = list(map(int,input("enter list :").split()))
lst =[]
count=1
max=0
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        count+=1
        if count > max:
            max = count
    else :
        count = 1
print(max)
