'''
继承：
超类：Object
1、提高代码的复用性
2、使类和类之间产生关系
3、继承多个父类

'''
class User:
    def eat(self):
        print("user eat...")

    def transMoney(self):
        print("user transmoney...")

class Father:
    def eat(self):
        print("father eat...")

    def sleep(self):
        print("sleep...")

class Boys(Father,User):
    #构造函数只能初始化一次，只能有一个init方法
    def __init__(self,a):
        self.age=a
        print("boys init...",a)

    def play(self):
        print("play...",self.age)

class Girls(Father):
    def shopping(self):
        print("shopping...")

boy=Boys(16)
boy.eat()
boy.transMoney()
boy.play()





