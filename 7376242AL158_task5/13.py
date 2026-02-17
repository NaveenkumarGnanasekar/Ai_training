class Exam:
    def __init__(self, subject_name, maximum_marks):
        self.subject_name = subject_name
        self.maximum_marks = maximum_marks

    def evaluate(self, marks_obtained):
        pass   
class TheoryExam(Exam):
    def evaluate(self, marks_obtained):
        percentage = (marks_obtained / self.maximum_marks) * 100
        if percentage >= 40:
            return "Pass"
        else:
            return "Fail"
class PracticalExam(Exam):
    def evaluate(self, marks_obtained):
        percentage = (marks_obtained / self.maximum_marks) * 100
        if percentage >= 50:
            return "Pass"
        else:
            return "Fail"
class MCQExam(Exam):
    def evaluate(self, correct_answers, wrong_answers):
        marks_obtained = correct_answers - (wrong_answers * 0.25)
        if marks_obtained < 0:
            marks_obtained = 0
        percentage = (marks_obtained / self.maximum_marks) * 100
        return "Pass" if percentage >= 35 else "Fail"

theory = TheoryExam("Mathematics", 100)
practical = PracticalExam("Physics Lab", 50)
mcq = MCQExam("General Knowledge", 100)
print("Theory Result:", theory.evaluate(45))
print("Practical Result:", practical.evaluate(20))
print("MCQ Result:", mcq.evaluate(correct_answers=60, wrong_answers=20))
