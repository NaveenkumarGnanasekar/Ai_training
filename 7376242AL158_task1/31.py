n = int(input ("enter a number :"))
cotev=0
cotodd=0
for i in range(1,n+1):
    if i % 2 == 0:
        cotev +=1
    else:
        cotodd +=1
print("the count of even numbers is :", cotev)
print("the count of odd numbers is :", cotodd)