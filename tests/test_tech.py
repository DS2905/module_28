#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_tech.py

import time
from config import base_url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#33 Прокрутка страницы вниз
browser = webdriver.Chrome()
browser.get(base_url)
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)


#33 Прокрутка страницы вниз и возврашение вверх
browser = webdriver.Chrome()
browser.get(base_url)
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.HOME)

#34 Уменьшение масштаба страницы
driver = webdriver.Chrome()
driver.get(base_url)
driver.execute_script("document.body.style.zoom='50%'")

#35 Увеличение масштаба страницы
driver = webdriver.Chrome()
driver.get(base_url)
driver.execute_script("document.body.style.zoom='150%'")