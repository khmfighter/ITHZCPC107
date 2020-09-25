a=int(input())
b=0
c=a
while a>0:
    b=b*10+a%10
    a=a // 10
if c==b:
    print("true",end="")
else:
    print("false",end="")