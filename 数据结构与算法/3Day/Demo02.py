import time

start=time.time()
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a**2+b**2==c**2 and a+b+c==1000:
                print(a,b,c)
end=time.time()
print(end-start)