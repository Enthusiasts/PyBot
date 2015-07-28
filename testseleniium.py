# -*- coding: utf-8 -*-
__author__ = 'User'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r'D:\Python34\chromedriver.exe')

# логинимся на инстаком
driver.get('https://instagram.com/accounts/login/')

driver.implicitly_wait(10)

# ввод логина
elem = driver.find_element_by_class_name('-cx-PRIVATE-Login__formContainer')
elem1 = driver.find_element_by_tag_name('form')
elem2 = driver.find_element_by_class_name('-cx-PRIVATE-LoginForm__field')
login = driver.find_element_by_tag_name('input')
login.send_keys('asivtcov')

# ввод пароля
elem3 = driver.find_element_by_class_name('-cx-PRIVATE-LoginForm__field')
password = driver.find_element_by_name('password')
password.send_keys('kizermyframe')

# сабмит
button = driver.find_element_by_xpath('//input[@type="submit"]')
button.click()

driver.implicitly_wait(10)
# поиск пользователей
el = driver.find_element_by_class_name('-cx-PRIVATE-SearchBox__inactiveSearchCaption')
find = driver.find_element_by_tag_name('input')
find.send_keys('alexashasivtsov')

driver.implicitly_wait(10)
human = driver.find_element_by_class_name('-cx-PRIVATE-Search__resultLink')
human.click()

driver.implicitly_wait(10)


human = driver.find_element_by_class_name('-cx-PRIVATE-ProfilePage__header')
human1 = driver.find_element_by_class_name('-cx-PRIVATE-ProfilePage__authorInfo')
human2 = driver.find_element_by_class_name('-cx-PRIVATE-ProfilePage__usernameAndFollow')
span = driver.find_element_by_tag_name('span')
submit = driver.find_element_by_tag_name('button')
submit.click()