'''
猜数游戏
由电脑随机生成0～100之间的数字，当用户猜错之后，提示大了还是小了
如果在10次内猜成功，则提示"恭喜成功！"，否则提示"请继续努力！"
'''
import random
num=random.randint(0,100)
print("电脑已经选择完毕数字，请准备猜数～")
i=1
while i<=5:
    i+=1
    input_num = eval(input("用户输入："))
    if input_num==num:
        print("恭喜成功！")
        break
    elif input_num>num:
        print("您猜的数字大了！")
    else:
        print("您猜的数字小了！")
if i>6:
    print("已经到达5次，猜数字失败，请继续努力！")



