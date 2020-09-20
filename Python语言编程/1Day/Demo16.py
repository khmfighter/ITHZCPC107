class Person:
    def methodA(self):
        print("methodA")

    @staticmethod
    def methodB():
        print("methodB")

    @classmethod
    def methodC(cls):
        print("methodC")

print(Person.methodB())
print(Person.methodC())