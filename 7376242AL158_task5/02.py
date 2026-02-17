class Bankaccount():
    def __init__(self,acc_no,name):
        self.acc_no=acc_no
        self.name = name 
        self.__balance=0
    def deposite(self,ammount):
        self.__balance=ammount
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount 
            return f"{self.__balance} is the current balance"
        else:
            return "insufficient balance "
    def get_balance (self):
        return self.__balance
usr=Bankaccount(12345,"naveen")
usr.deposite(10000)
print(usr.withdraw(5000))
print(usr.get_balance())