import numpy as np #科学计算
import pandas as pd #数据预处理
import matplotlib.pyplot as plt #可视化

df_content=pd.read_csv("train.csv")
# print(df_content.shape)
# #print(type(df_content))
print(df_content.info())
# print(df_content.describe())
# print(df_content.head(3))
# print(df_content.tail(3))
# print(df_content["Survived"])

#计算生存率 1代表存活 0代表死亡 count获取的是非空行的个数
print((df_content["Survived"].sum()/df_content["Survived"].count())*100)

#生还和性别是否有关系
#女性的存活人数/女性的总人数
print(df_content["Sex"].head(3))
# print(df_content["Survived"])
# female=df_content[(df_content["Sex"]=="female") & (df_content["Survived"]==1)]["Survived"].sum()
# female_count=df_content[df_content["Sex"]=="female"]["Survived"].count()
# print((female/female_count)*100)
# print((df_content.groupby(["Sex"]).sum()/
#        df_content.groupby(["Sex"]).count())["Survived"])
#
# sex_survived=(df_content.groupby(["Sex"]).sum()/
#               df_content.groupby(["Sex"]).count())["Survived"]
# sex_survived.plot(kind='bar') #kind=bar 柱状图 kind=pie 饼图
# plt.show()

#生还是否和船舱等级有关
# print(df_content["Pclass"].head(3))
# pclass_survived=(df_content.groupby(["Pclass"]).sum()/
#               df_content.groupby(["Pclass"]).count())["Survived"]
# pclass_survived.plot(kind='bar') #kind=bar 柱状图 kind=pie 饼图
# plt.show()

#生还和年龄是否有关系
print(df_content["Age"].head(3))
#获取年龄非空列
df_age=df_content[~np.isnan(df_content['Age'])]
print(df_age)
#分区年龄段
age_num=np.arange(0,81,5)   #划分5岁为一个区间
age_cut=pd.cut(df_age['Age'],age_num)   #将年龄按照区间分割

age_group=df_age.groupby(age_cut)   #进行分组
age_Survived=(age_group.sum()/age_group.count())["Survived"]
age_Survived.plot(kind='bar')
plt.show()

#生还和性别，船舱有关系
sex_class_survived=(df_content.groupby(['Sex','Pclass']).sum()/df_content.groupby(['Sex','Pclass']).count())['Survived']

