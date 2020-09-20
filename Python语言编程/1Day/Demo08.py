'''
函数
def 函数名称([参数]):
    代码块
1、参数可以设置，也可以不设置
2、函数可以有返回值，需要通过return进行返回，也可以没有
'''

#只是定义
def method01():
    print("method01")

#执行
method01()

#带参数的函数
def method02(a,b,c):
    print(a,b,c)

method02(1,2,3)
method02(b=6,c=7,a=5)

#带参数的返回函数
def method03(a,b):
    return a+b
print(method03(3,5))

#def method04(a,b,c=2,d,e=3,f=3):  默认值后面的所有参数都得赋值
def method04(a,b,c,d,e=3,f=3):
    print(a,b,c,d,e,f)
method04(1,2,3,4,5)
method04(1,2,3,4,5,6)

def method05():
    pass

def method06(*args):
    pass

method06(1,2,3,"abc")

def method07(**kwargs):
    print(kwargs)

method07(name="xiaomin",age=23)

def method08(*args,**kwargs):
    print(args,kwargs)
method08(1,2,3,name="xiaomin")
#method08(1,2,3,name="xiaomin",3,4) 必须有顺序，先元组，再字典

def method09(a,b,c,d):
    print(a,b,c,d)
method09(1,3,c = method03(1,6),d = 9)