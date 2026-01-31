number = int(input ("enter a number :"))
n = int (input("enter the number to find the occurrences :"))
count =0 
while number !=0:
    digit = number %10
    if digit == n:
        count +=1
    number //=10
print("the occurrences of", n , "in the given number is :", count)