class PythonDemo:
    def __init__(self , num = 0):
        self.val = num

    def inc(self):
        self.val+=1

p_demo = PythonDemo(100)
p_demo.inc()
print(p_demo.val)