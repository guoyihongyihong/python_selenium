# coding = utf-8

from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")
h = driver.current_window_handle
print(h)
driver.find_element_by_link_text("租房").click()

all_h = driver.window_handles
print(all_h)

driver.switch_to.window(all_h[1])
print(driver.title)
driver.close()
driver.switch_to.window(h)
print(driver.title)
