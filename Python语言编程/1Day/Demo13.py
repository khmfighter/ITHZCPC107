'''
面向对象：封装、继承、多态
对象：万物皆对象
对象：属性、方法（特征和功能）
类：抽象
对象--->类--->父类

类：
class 类名()：
    属性
    方法
'''

class Person():
    name=None
    age=0

    def eat(self):
        print(self.name,"eat...")
    def swim(self):
        print(self.name,"swim...")
    def sleep(self):
        print(self.name,"sleep...")

#对象的创建 对象名=类名()
lily=Person()
lily.age=32
lily.name="lily"
lily.sleep()
lily.sex="男"

lisi=Person()
#print(lily.sex,lisi.sex)   对象外添加属性只属于该对象

