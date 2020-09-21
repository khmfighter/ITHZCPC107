'''
多线程
'''
import time,threading
#from threading import Thread
def work():
    print("学习")
    time.sleep(2)
    print("结束")

if __name__=="__main__":
    for i in range(5):
        # 1.创建线程
        t=threading.Thread(target=work) # 去掉小括号,否则执行效果跟主线程效果类似
        # work()
        # 2.启动线程
        t.start()
