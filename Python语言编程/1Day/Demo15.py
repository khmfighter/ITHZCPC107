'''
多态：
必须有继承存在

'''
class Who:
    def who(self,x):
        x.say()

class C:
    def say(self):
        print("C say...")

class JAVA(C):
    def say(self):
        print("JAVA say...")


class PYTHON(C):
    def say(self):
        print("PYTHON say...")

# p=C()
# p.say()
# p=JAVA()
# p.say()
# p=PYTHON()
# p.say()

w=Who()
w.who(C())
w.who(JAVA())
w.who(PYTHON())