#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
#使用组合键ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
#使用组合键ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
#输入框重新输入内容，搜索
#输入框输入中文问题：
# selenium2 python在send_keys()中输入中文一直报错，其前面加个小u 就解决了：
#即：send_keys(u"输入中文")
driver.find_element_by_id("kw").send_keys(u"虫师cnblogs")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
