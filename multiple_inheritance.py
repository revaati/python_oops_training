class Teacher:
    def teach(self):
        print("Teach science and math")

class Coach:
    def train(self):
        print("Train inathletics")

class Child(Teacher , Coach):
    def activities(self):
        print("Performs well in both academics and sports")
        self.teach()
        self.train()

c =Child()
c.activities()