# coding : utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get("http://www.testerhorde.com")
driver.implicitly_wait(10)
driver.find_element_by_id("search-button").click()
driver.find_element_by_id("search-term").clear()
driver.find_element_by_id("search-term").send_keys("selenium")
# 模拟enter键操作回车按钮
driver.find_element_by_id("search-term").send_keys(Keys.ENTER)
# s = driver.find_elements_by_css_selector("h3.t>a")
# for i in s:
#     print(i.get_attribute("href"))

