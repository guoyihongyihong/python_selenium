# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox()
url = "https://www.baidu.com/"
driver.get(url)
driver.implicitly_wait(30)
# 鼠标移动到设置按钮
mouse = driver.find_element_by_link_text("设置")
print(mouse)
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()

# 分两步 先定位下拉框，再点击选项
s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()
# 通过select模块来选择
# Select(s).select_by_index(2) # 索引值
# Select(s).select_by_value("20")  # value值

s1 = Select(s)
s1.select_by_value("20")
for select in s1.all_selected_options:  # 已结选择的选项
    print(select.text)

s.click()

driver.find_element_by_link_text("保存设置").click()




