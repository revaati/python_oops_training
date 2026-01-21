class Teacher:
    def teach(self):
        print("Teach math and Science")

class Coach:
    def train(self):
        print("Trains in foootball and athletics")

class Student(Teacher , Coach):
    def activities(self):
        print("Student is performingin both academics and sports.")
        self.teach()
        self.train()


s = Student()
s.activities()