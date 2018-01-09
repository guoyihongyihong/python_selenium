# coding : utf-8
import random
from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
s = driver.find_elements_by_xpath("//h3[@class='t']/a")
# s = driver.find_elements_by_css_selector("h3.t>a")
# for i in s:
#     print(i.get_attribute("href"))

t = random.randint(0, 9)
s[t].click()
