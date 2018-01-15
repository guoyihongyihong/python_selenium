# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

driver.get("https://kyfw.12306.cn/otn/index/init")
# 去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)

# 用js方法输入日期
# js_value = 'document.getElementById("train_date").value= "2018-11-22"'
# driver.execute_script(js_value)

# 设置出发地和目的地
driver.find_element_by_id("fromStationText").clear()
driver.find_element_by_id("fromStationText").send_keys("szb")

driver.find_element_by_xpath("//*[@id='form_cities']/*[@id='panel_cities']/div[2]").click()


driver.find_element_by_id("toStationText").clear()
driver.find_element_by_id("toStationText").send_keys("csn")
driver.find_element_by_xpath("//div[@id='panel_cities']/*[4]").click()

# 清空文本后输入值
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2018-1-18")

driver.find_element_by_id("a_search_ticket").click()







