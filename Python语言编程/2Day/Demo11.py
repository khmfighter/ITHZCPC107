'''
线程共享变量
'''

import threading,time

g_num=0
def work01():
    global g_num
    for i in range(10):
        g_num+=1
        print("work01:",g_num)
        time.sleep(1)

def work02():
    global g_num
    for i in range(10):
        g_num+=1
        print("work02:",g_num)
        time.sleep(1.5)

def work03(n):
    n.append("123")
    print("work03:",n)

def work04(n):
    print("work04:",n)

if __name__=="__main__":
    t1=threading.Thread(target=work01)
    t2=threading.Thread(target=work02)
    t1.start()
    #time.sleep(2)
    t2.start()
    # list1=[1,2,3,4]
    # t3=threading.Thread(target=work03,args=(list1,))
    # t4 = threading.Thread(target=work04, args=(list1,))
    # t3.start()
    # time.sleep(1)
    # t4.start()