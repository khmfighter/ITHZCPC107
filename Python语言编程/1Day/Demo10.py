'''
模块导入：
1、import
2、from
'''
import keyword
import random

'''
os：系统包
random：随机数
re：正则表达式
爬虫：requests、BeautifulSoup、scrapy
服务器开发：flask、django
科学计算包：numpy、scipy、pandas、matplotlib
人工智能：sk-learn
深度学习框架：tensorflow、keras、cntk
自然语言：jieba
词云库：wordcloud
计算机视觉库：opencv
'''

r=random.random()
print(r)    #0~1之间的随机数
r=random.randrange(30,40)
print(r)

list1=[1,3,4,5,6,7,8]
random.shuffle(list1)   #打乱数据集
print(list1)


print(random.choice([2,4,5]))

