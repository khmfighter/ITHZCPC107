'''
继承线程
'''

from threading import Thread
import time

class myThread(Thread):
    def run(self):
        num=0
        for i in range(100):
            time.sleep(1)
            print("现在数值是：",i)

if __name__=="__main__":
    t=myThread()
    t.start()

