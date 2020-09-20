'''
递归调用
1、结束条件
2、函数体

5！=5*4*3*2*1
  =5*4！
     =4*3！
       =3*2！
          =2*1！
'''
def method(n):
    if n==1:
        return 1
    else:
        return n*method(n-1)


'''
汉诺塔
n: 圆桩个数 a:原桩 b:目的桩 c:中间桩
'''
def method_A(n,a,b,c):
    if n==1: #结束条件
        print(a,"--->",b)
        return None
    else: #循环函数体
        method_A(n-1,a,c,b)
        method_A(1,a,b,c)
        method_A(n-1,c,b,a)


if __name__=="__main__":
    print(method(5))
    method_A(2, "A", "B", "C")
    print(__name__)

