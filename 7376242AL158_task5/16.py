from abc import ABC, abstractmethod
class GradingPolicy(ABC):
    @abstractmethod
    def calculate_grade(self, marks):
        pass
class PercentageGrading(GradingPolicy):
    def calculate_grade(self, marks):
        average = sum(marks) / len(marks)
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"
class RelativeGrading(GradingPolicy):
    def calculate_grade(self, marks):
        total = sum(marks)
        if total >= 250:
            return "A"
        elif total >= 200:
            return "B"
        elif total >= 150:
            return "C"
        else:
            return "Fail"
class Student:
    def __init__(self, name, marks, grading_policy):
        self.name = name
        self.marks = marks
        self.grading_policy = grading_policy  
    def get_grade(self):
        return self.grading_policy.calculate_grade(self.marks)
    def display_result(self):
        grade = self.get_grade()
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")
marks = [85, 90, 78]
student1 = Student("Alice", marks, PercentageGrading())
student2 = Student("Bob", marks, RelativeGrading())
student1.display_result()
student2.display_result()
