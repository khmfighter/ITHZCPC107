'''
多线程
'''
import threading,time

def work01():
    for i in range(10):
        print("兔子领先...")
        time.sleep(1)

def work02():
    for i in range(10):
        print("乌龟领先...")
        time.sleep(1)

if __name__=="__main__":
    t1=threading.Thread(target=work01,name="tuzi")
    t2=threading.Thread(target=work02,name="wugui")
    t1.start()
    t2.start()

    while True:
        num=len(threading.enumerate())
        print("目前线程的个数为：" ,num)
        if num<=1:
            break

        time.sleep(2)