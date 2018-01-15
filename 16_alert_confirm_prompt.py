# coding : utf-8
from selenium import webdriver
import time


def alert():
    url = "file:///D:/pytest/alert.html"
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(4)
    driver.find_element_by_id("alert").click()
    time.sleep(3)
    t = driver.switch_to_alert()
    # 打印警告框文本内容
    print(t.text)
    # 点警告框确认按钮
    t.accept()
    # t.dismiss()  相当于点了x按钮


def confirm():
    url = "file:///D:/pytest/alert.html"
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(4)
    driver.find_element_by_id("confirm").click()
    time.sleep(3)
    t = driver.switch_to_alert()
    # 打印警告框文本内容
    print(t.text)
    # 点警告框确认按钮
    t.accept()
    # t.dismiss()  相当于点了x按钮


def prompt():
    url = "file:///D:/pytest/alert.html"
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(4)
    driver.find_element_by_id("prompt").click()
    time.sleep(3)
    t = driver.switch_to_alert()
    # 打印警告框文本内容
    print(t.text)
    t.send_keys("hello selenium2")
    # 点警告框确认按钮
    t.accept()
    # t.dismiss()  相当于点了x按钮


def main():
    # alert()
    # confirm()
    prompt()


if __name__ == "__main__":
    main()
