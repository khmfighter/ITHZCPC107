'''
猜拳游戏
'''
game_player01="孙悟空"
game_player02="猪八戒"
game_player03="唐僧"
import random    #先导入随机数
class game():         #创建一个游戏的类 里面分为两个属性一个玩家名 一个电脑名
    def __init__(self,playername,computername):
        self.playername=playername
        self.computername=computername
        self.playerscore=0    #玩家得分
        self.comscore=0       #电脑得分
        self.sum=0            #平局数
    def startgame(self):
        print("-------猜拳游戏开始---------")
        print("游戏规则为：1.剪刀，2.石头，3.布")
        newname=input("英雄请输入你的姓名：")
        self.playername=newname
        dnname=input("请选择你的对手：1.%s，2.%s，3.%s"%(game_player01,game_player02,game_player03))
        if dnname=="1":
            print("你的对手为%s"%game_player01)
            self.computername=game_player01
        elif dnname=="2":
            print("你的对手为%s"%game_player02)
            self.computername = game_player02
        elif dnname=="3":
            print("你的对手为%s"%game_player03)
            self.computername = game_player03
        else:
            print("输入有误，系统以为你随机挑选%s"%game_player01)
            self.computername = game_player01
        count=0
        while True:
            count+=1
            if count==6:
                break
            print("游戏开始请出拳")
            player=int(input("请输入1.剪刀，2.石头，3.布："))
            computer=random.randint(1,3)
            if computer==1:
                print("%s出拳为剪刀"%self.computername)
            elif computer==2:
                print("%s出拳为石头"%self.computername)
            else:
                print("%s出拳为布"%self.computername)
            if(player==computer):
                print("平局")
                self.sum+=1
            elif(player==1 and computer==3) or(player==2 and computer==1) or(player==3 and computer==2):
                print("%s获得了胜利"%self.playername)
                self.playerscore+=1
            else:
                print("%s获得了胜利"%self.computername)
                self.comscore+=1
            tag=input("是否继续y/n ")
            if tag.lower()=='n':
                break
        print("%s VS %s" % (self.playername, self.computername))
        print("%s赢了%d局" % (self.playername, self.playerscore))
        print("%s赢了%d局" % (self.computername, self.comscore))
        print("%d次平局" % self.sum)


lx=game("khm","computer") #传入的参数数量必须和定义参数的数量相等
lx.startgame()      #调用游戏开始的方法