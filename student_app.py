class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, marks):
        student = Student(student_id, name, marks)
        self.students[student_id] = student
        return student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False