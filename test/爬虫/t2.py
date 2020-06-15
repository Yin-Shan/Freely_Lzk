# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

driver = webdriver.Chrome()
driver.get("http://134.96.137.200")
time.sleep(1)
driver.find_element_by_id("sAccount").click()
driver.find_element_by_id("sAccount").clear()
driver.find_element_by_id("sAccount").send_keys("nocjktest")
driver.find_element_by_id("sPasswd").clear()
driver.find_element_by_id("sPasswd").send_keys("Znwg&2018")
driver.find_element_by_id("LoginButton").click()
driver.find_element_by_id("ext-gen73").click()
driver.find_element_by_id("dAlarmTitleImg").click()
driver.quit()

if __name__ == "__main__":
    pass
