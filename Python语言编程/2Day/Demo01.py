'''
try:保存有可能出现异常的代码
except:捕获异常
    :raise:抛出异常
else:没有异常的时候执行
finally:有没有异常都会执行
自定义异常
'''

try:
    print(5 / 0)
    print("try...")
except ZeroDivisionError as e: #子类放在前面
    raise e
    print("ZeroDivisionError",e)
except Exception as ex:
    print ("Exception",ex)
finally:    #必须和try...except...同时存在
    print("finally")
print("结束！")

