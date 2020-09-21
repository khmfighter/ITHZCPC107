import time
print("time.time(): %f"%time.time())
t=time.localtime(time.time())
print(t)
print(t.tm_year,"年",t.tm_mon,"月",t.tm_mday,"日")

