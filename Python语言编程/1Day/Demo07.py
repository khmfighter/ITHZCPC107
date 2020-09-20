'''
循环：A、变量初始化，B、循环结束条件，C、循环体，D、变量迭代
1、while循环
    while 结束条件：
        循环体

2、for循环
    for 变量名 in 序列：
        循环体
'''

#1到100之间的和

i=1
sum=0
while i<=100:
    sum+=i
    i=i+1   #迭代变量
print(sum)

#range(1,2,3) 起始位置，结束位置（不包含），变量迭代
for i in range(1,10,2):
    print(i)

print(5 in [4,5,6,9])

'''
contuine：跳过本次循环
break：跳出循环，结束当前所在循环
'''

for i in range(33):
    if i==4:
        continue
    print("电梯到达：",i,"层")
    if i==12:
        break

'''
嵌套循环
'''
print("*")
print("**")
print("***")
print("****")
for i in range(4):
    for j in range(i+1):
        print("*",end="") #单层循环不换行
    print()

for i in range(4):
    print('*'*i)

for x in range(31):
    if x*2+(30-x)*4==90:
        print("鸡的个数：%s"%x,"兔的个数：%s"%(30-x))
