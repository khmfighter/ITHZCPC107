'''
变量：
数据类型 变量名 = 值
数据类型：
    数字：整数、小数、复数
    字符串：str ''或者""
    布尔：bool False或者True
    序列：列表、元组、字典、set集合、range
变量名：变量名的命名格式
'''

#数字
num = 1
print(type(num))
print(id(num))

a=3
b=5
print(id(a),id(b))
a=5
print(id(a),id(b))

money=1_000_00
print(money)

a=1.1
print(type(a))
#实数和虚数
c=5.5+6j
print(type(c),c.real,c.imag)

#布尔类型
flag=6>8
print(flag)


