# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("file:///D:/pytest/radio.html")

def radio():
    s = driver.find_element_by_id("girl").is_selected()
    print(s)
    driver.find_element_by_id("girl").click()
    s = driver.find_element_by_id("girl").is_selected()
    print(s)


def checkbox():
    checkboxs = driver.find_element_by_xpath("//*[@type='checkbox']")
    for i in checkboxs:
        i.click()


def main():
    checkbox()


if __name__ == "__main__":
    main()
