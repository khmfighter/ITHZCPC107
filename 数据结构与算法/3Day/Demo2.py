from selenium.webdriver import Chrome
from selenium import webdriver
import  time
import  random

#浏览器插件安装 https://blog.csdn.net/weixin_42170439/article/details/90611962
#IE,火狐，谷歌浏览器插件下载https://www.cnblogs.com/qiezizi/p/8632058.html
proxy_list = [
'182.39.6.245:38634',
'115.210.181.31:34301',
'123.161.152.38:23201',
'222.85.5.187:26675',
'123.161.152.31:23127',
]
proxy = random.choice(proxy_list)

proxies = {
'http': 'http://' + proxy,
'https': 'https://' + proxy,
}
prefs = {
    "profile.default_content_setting_values" :
        {
        "notifications" : 2
         },
     "profile.managed_default_content_settings.images" : 2
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server={0}'.format(proxies))
url = "http://www.hzhua.cn/"
driver = Chrome()
driver.get(url)

login = driver.find_element_by_xpath('//*[@id="loginbar"]/a')
login.click()
time.sleep(1)
print(driver.page_source) #获取下一个网页的源代码
user = driver.find_element_by_xpath('//*[@name="account"]')
pwd = driver.find_element_by_xpath('//*[@name="password"]')
#赋值
user.send_keys("123456@qq.com")
pwd.send_keys("root123456")
logoin_btn = driver.find_element_by_xpath('//*[@class="btn btn-danger"]')
logoin_btn.click()