import re
#1、匹配模式 2、即将匹配的字符串

r=re.search("Hello","1Hello world")
if r is None:
    print("匹配失败")
else:
    print("匹配成功")

phone="400-200-823 #这是一个注释"
result=re.sub("#.*","",phone)
print(result)

result=re.sub("\D","",phone)    #匹配非数字
print(result)

name="123xiaoming"
result=re.search("[a-zA-Z0-9]{4}",name)
print(result)
result=re.search("[a-zA-Z0-9]{2}","1m+a")
print(result)