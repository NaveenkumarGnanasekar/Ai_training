class employee():
    def __init__(self , name , designation ,basic_sal):
        self.name = name 
        self.designation = designation
        self.basic_sal = basic_sal
    def final_sal(self):
        allowance = {"manager":0.40,"supervisor":0.30,"employee":0.20}
        if self.designation.lower() in allowance:
            final_sal = self.basic_sal + self.basic_sal*allowance[self.designation]
            return f"{final_sal} is the final salary of employee {self.name}"
        else :
            return f"{self.name} is not a emplopyee of company "
employee1 = employee("naveen","manager",40000)
print(employee1.final_sal())