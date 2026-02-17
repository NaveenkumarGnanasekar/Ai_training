class Student():
    def __init__(self,name , dept,cgpa,year):
        self.name = name 
        self.dept=dept
        self.cgpa=cgpa
        self.year=year
    def placement(self):
        if self.cgpa > 7.5 and self.year >=3:
            return f"{self.name} is eligible for placement"
        else :
            return f"{self.name} is not eligible for placement"
student1=Student("naveen","aiml",7.8,3)
student2=Student("bruce","aids",8.0,2)
print(student1.placement())
print(student2.placement())