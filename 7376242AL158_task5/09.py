class Course:
    def __init__(self, name):
        self.name = name
        self.students = set() 

    def add_student(self, student):
        if student in self.students:
            print(f"{student.name} is already registered in {self.name}")
        else:
            self.students.add(student)
            print(f"{student.name} successfully registered in {self.name}")


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = set() 

    def register(self, course):
        if course in self.courses:
            print(f"Already registered for {course.name}")
        else:
            self.courses.add(course)
            course.add_student(self)



course1 = Course("Math")
course2 = Course("Physics")

student1 = Student("Alice")

student1.register(course1)
student1.register(course1)  
student1.register(course2)
