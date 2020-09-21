'''
加锁
'''

from threading import Thread,Lock

g_num=0

def work1():
    global g_num
    for i in range(100):
        maux.acquire()  #加锁
        g_num+=1
        print("work1:",g_num)
        maux.release()  #解锁

def work2():
    global g_num
    for i in range(100):
        maux.acquire()  #加锁
        g_num+=1
        print("work2:",g_num)
        maux.release()  #解锁

if __name__=="__main__":
    # 创建锁
    maux = Lock()
    t1=Thread(target=work1)
    t2=Thread(target=work2)
    t1.start()
    t2.start()