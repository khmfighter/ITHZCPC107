import keyword
print(keyword.kwlist)

str='xiaoming'
print(str[0:4])
print(str[-1])
print(str*2,str*3)

#字符串切分
message="name:xiaoming age:18 sex:男"
mes=message.split(" ")
print(mes[0].split(":"))
#字符串变大小写
print(message.upper(),message.lower())
#替换
print(message.replace(" ","|"))


name="xiaoming"
age=18
sex="男"
#print(name+age+sex)
print(name,age,sex)
print("姓名：%s,年龄：%d,性别：%s"%(name,age,sex))

# name=input("输入姓名：")
# print(name)


# age01=input("请输入第一个用户的年龄：")
# age02=input("请输入第二个用户的年龄：")
# print(type(age01),type(age02))
# #字符串转换成整数
# print((int(age01)+int(age02))/2)


# age1,age2=eval(input("请输入两个用户的年龄，并且用，隔开"))
# print(age1,age2)
# print(type(age1),type(age2))

name="小明"
money=123.66956
print('姓名：{0}, 余额：{1:.2f}'.format(name,money))