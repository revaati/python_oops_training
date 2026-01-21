class Teacher:
    def teach(self):
        print("Teach math and Science")

class Student(Teacher):
    def activities(self):
        print("Student is performing well in academics .")
        self.teach()


s = Student()
s.activities()