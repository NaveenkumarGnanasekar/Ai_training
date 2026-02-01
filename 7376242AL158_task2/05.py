ticket_no = int(input("enter ticket number :"))
odd =0 
even =0
while ticket_no !=0:
    digit = ticket_no%10
    if digit%2==0:
        even +=1
    else :
        odd +=1
    ticket_no //=10
print("number of even  numbers in the ticket number :", even )
print("number of odd numbers in the ticket number :", odd)