# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 配置文件地址
profile_directory = r"C:\Users\wu.guo.7ROAD\AppData\Roaming\Mozilla\Firefox\Profiles\odun03fk.default"
# 加载配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)
# driver = webdriver.Firefox()

# bolgUrl = "http://www.cnblogs.com/"
# yoyobolg = bolgUrl + "yihongyihong"
driver.get("http://www.cnblogs.com/yihongyihong/")
driver.find_element_by_id("blog_nav_newpost").click()

editTile = u"Selenium2 + python自动化23-富文本"
editBody = u"这是发帖的征文"
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(editTile)
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
driver.find_element_by_id("tinymce").send_keys(Keys.TAB)
driver.find_element_by_id("tinymce").send_keys(editBody)


# js处理富文本
js = 'document.getElementById("Editor_Edit_EditorBody_ifr")'\
    '.contentWindow.document.body.innerHTML="%s" %editBody'
driver.execute_script(js)










