# coding = utf-8

from selenium import webdriver


# 配置文件地址
profile_directory = r"C:\Users\wu.guo.7ROAD\AppData\Roaming\Mozilla\Firefox\Profiles\odun03fk.default"
# 加载配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)
