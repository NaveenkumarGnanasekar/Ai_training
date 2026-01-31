n = int (input("enter a number:"))
sum =0 
for i in range (0, n+1, 2):
    sum += i
print("the sum of first N even numbers is:", sum)