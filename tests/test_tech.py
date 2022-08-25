#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_tech.py

import time
from config import base_url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#36 Прокрутка страницы вниз
browser = webdriver.Chrome()
browser.get(base_url)
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)


#37 Прокрутка страницы вниз и возврашение вверх
browser = webdriver.Chrome()
browser.get(base_url)
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.HOME)

#38 Уменьшение масштаба страницы
driver = webdriver.Chrome()
driver.get(base_url)
driver.execute_script("document.body.style.zoom='50%'")

#39 Увеличение масштаба страницы
driver = webdriver.Chrome()
driver.get(base_url)
driver.execute_script("document.body.style.zoom='150%'")

#40 Прокрутка страницы вниз с помощью кнопок
browser = webdriver.Chrome()
browser.get(base_url)
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.PAGE_DOWN)

#41 Прокрутка страницы вниз и возвращение вверх с помощью кнопок
browser = webdriver.Chrome()
browser.get(base_url)
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.PAGE_DOWN)
time.sleep(5)
elm.send_keys(Keys.PAGE_UP)