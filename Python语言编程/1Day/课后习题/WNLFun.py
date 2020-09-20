'''
万年历（控制台输入年和月），打印当月
'''

#判断平年和闰年
def leap_year(year):
    if(year%4==0 and year%100==0) or (year%400==0):
        return True
    else:
        return False

#计算每个月的天数
def monthdays(year,month):
    if month==2:
        if leap_year(year):
            days=29
        else:
            days=28
    elif month in[4,6,9,11]:
        days=30
    else:
        days=31
    return days

'''
获取1990-01-01离现在有多少天，1990-01-01是星期一，以这个为标准来判断星期
'''
#计算总天数
def totaldays(year,month):
    yearday=0
    for i in range(1990,year):#计算输入年份之前的
       if leap_year(i):
           yearday+=366
       else:
           yearday+=365
    for i in range(1,month):#注意不能包括该月份
        yearday+=monthdays(year,i)
    return yearday


if __name__ == '__main__':
    while True:  #循环判断是否输入错误的格式
        print("XXXXXX万年历XXXXXX")
        year = input("请输入年份（如：1990）：")
        month = input("请输入月份（如：1）：")
        try:                                    #捕捉输入异常格式和月份的正确
            year = int(year)
            month = int(month)
            if month <1 or month >12:            #判断月份是否输入错误，错误就重新开始循环
                print("年份或者月份输入错误，请重新输入！")
                continue
        except:                                 #捕捉到转换成整型异常，输出提示，重新开始循环
            print("年份或者月份输入错误，请重新输入！！！")
            continue
        break     #如果没有异常就跳出循环

    week = (totaldays(year, month)) % 7  # 计算该月第一天是周几
    print('日\t一\t二\t三\t四\t五\t六\t')
    for i in range(0, week):  # 前面打印week个空格
        print("\t", end="")
    for i in range(1, monthdays(year, month) + 1):  # c从week+1的位置开始打印数字
        if (totaldays(year, month) + i) % 7 == 0:  # 天数为7的倍数时，记住要换行
            print(i, end="\n")
        else:
            print(i, end="\t")