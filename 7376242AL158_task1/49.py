n = int(input("enter a number :"))
largest =0
sec_largest=0
while n !=0 :
    digit = n%10
    if digit > sec_largest:
        if digit > largest:
            sec_largest = largest
            largest = digit
        else:
            sec_largest = digit
    n//=10
print("the second largest digit is :", sec_largest)