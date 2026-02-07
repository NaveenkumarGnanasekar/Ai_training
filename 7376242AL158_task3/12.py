def lst(lst):
    sum1 = sum(lst)
    avg = sum1/len(lst)
    max1=max(lst)
    min1=min(lst)
    return max1,min1,avg
n = input("enter a list :").split()
n1 = list(map (int,n))
result = lst(n1)
print(type(result),"is the retrun type.")
print(result)