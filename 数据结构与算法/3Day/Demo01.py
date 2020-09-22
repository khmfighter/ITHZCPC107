import requests
# import BeautifulSoup

# 1、获取网页代码
from bs4 import BeautifulSoup

r=requests.get("http://www.baidu.com")
r.encoding="utf-8"
print(r.status_code)

#解析html 1、解析的html网页 2、解析的文件格式
soup=BeautifulSoup(r.text,"html.parser")
#获取网页中的超链接 a
# a_tag=soup.find("a")
a_tag=soup.findAll("a")
for a in a_tag:
    #获取标签内容
    print(a.text,a['href'])

div=soup.find('div',attrs={"id":"wrapper"})
print(div)