from timeit import  Timer
def method1():
    list1=[]
    for i in range(3000):
        list1.append(i)

def method2():
    list1=[]
    for i in range(3000):
        list1.insert(0,i)
def method3():
    list1=[]
    for i in range(3000):
        list1=list1+[i]


m1 = Timer("method1()","from __main__ import method1")
print(m1.timeit(number=2000))  #测试2000次，总共花费的时间
m2 = Timer("method2()","from __main__ import method2")
print(m2.timeit(number=2000))  #测试2000次，总共花费的时间
m3 = Timer("method3()","from __main__ import method3")
print(m3.timeit(number=2000))  #测试2000次，总共花费的时间