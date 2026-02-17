class Attendance:
    def __init__(self, student_name):
        self.student_name = student_name
        self.status = "Absent"

    def mark_attendance(self):
        pass 

    def show_status(self):
        print("Student:", self.student_name)
        print("Attendance Status:", self.status)
class ManualAttendance(Attendance):
    def mark_attendance(self):
        self.status = "Present (Marked by Teacher)"
class RFIDAttendance(Attendance):
    def mark_attendance(self):
        self.status = "Present (RFID Scanned)"
class FaceRecognitionAttendance(Attendance):
    def mark_attendance(self):
        self.status = "Present (Face Recognized)"
s1 = ManualAttendance("Alice")
s2 = RFIDAttendance("Bob")
s3 = FaceRecognitionAttendance("Charlie")

s1.mark_attendance()
s2.mark_attendance()
s3.mark_attendance()

s1.show_status()
s2.show_status()
s3.show_status()
