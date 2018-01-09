# coding = utf-8

from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://mail.126.com/")
driver.implicitly_wait(30)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("guoxicen2015")
driver.find_element_by_name("password").send_keys("guo1314")
driver.find_element_by_id("dologin").click()

# 释放iframe。重新回到主页面上
driver.switch_to_default_content()

