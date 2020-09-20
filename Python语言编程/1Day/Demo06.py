#控制语句
#1、顺序语句
#2、分支语句
#3、循环语句
'''
if 表达式：
    代码块
============
if 表达式：
    代码块
else：
    代码块
============
if 表达式：
    代码块
elif 表达式：
    代码块
    ...
else：
    代码块
'''
if 6<7:
    print(True)
else:
    print(False)

score=eval(input("请输入成绩："))
if score>=90 and score<=100:
    print("Class A")
elif score>=80 and score<90:
    print("Class B")
else:
    print("Class C")