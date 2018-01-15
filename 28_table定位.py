# coding = utf-8

from selenium import webdriver
import time


driver = webdriver.Firefox()

driver.get("file:///D:/pytest/table.html")
time.sleep(3)
t = driver.find_element_by_xpath("//*[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)










