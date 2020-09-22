import requests
from bs4 import  BeautifulSoup
#不同浏览器的UA
header_list = [{"user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
               {"user-agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
               {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}]
#不同的代理IP(该代理ip可能已经失效)
proxy_list = [{"http": "182.39.6.245:38634"},
              {'http': '115.210.181.31:34301'},
              {'http': '123.161.152.38:23201'},
              {'http': '123.161.152.31:23127'},]


#1.获取网页代码
r = requests.get("http://www.baidu.com",header=header_list,proxy=proxy_list)
# print(r.status_code)
r.encoding="utf-8"
#获取网页源代码
# print(r.text)
#解析html  1.解析的html网页 2.解析的文件格式
soup = BeautifulSoup(r.text,"html.parser")
#获取网页中的超链接 a
a_tag = soup.findAll("a")
for a in a_tag:
    #a.text获取标签内容
    print(a.text,a['href'])

div=soup.find("div",attrs={"id":"wrapper"})
print(div)




