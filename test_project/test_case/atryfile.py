import unittest,xml.dom.minidom,time,random
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from public_testcase import *

driver = webdriver.Firefox('/home/chenyueming/.mozilla/firefox/mllr6bbp.default')
dom = xml.dom.minidom.parse('register_test')
dom_root = dom.documentElement
url = dom_root.getElementsByTagName('base')
base_url = url[0].getAttribute('url')
    #'''不输入密码进行帐号注册'''
count = 6
info =['admin124u2rjaesitfr','']
driver.implicitly_wait(10)
driver.get(base_url)
driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(info[0])
driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys(info[1])
driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys(info[1])
driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/button').click()
driver.implicitly_wait(10)
text = driver.switch_to_active_element().get_attribute('placeholder')
print(text)