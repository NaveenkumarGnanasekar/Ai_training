n = list(map(int,input("enter a list:").split()))
set1 = set(n)
if len(n)==len(set1):
    print("there is no duplicate element in the given list")
else:
    print("there is duplicate elements in the given list")