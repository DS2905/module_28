#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py

from config import base_url
from selenium.webdriver.common.keys import Keys
import time

#31 Переход на страницу авторизации
def test_auth(selenium):
    selenium.get(base_url)
    time.sleep(2)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[1]/header[1]/div[2]/div[1]/a[1]').click()

#32 Вход или регистрация по смс
def test_auth_sms(selenium):
    selenium.get(base_url)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[1]/header[1]/div[2]/div[1]/a[1]').click
    search_input = selenium.find_element_by_xpath('//*[@id="bx-nextype-authorize"]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')
    search_input.send_keys('9028345687')
    WebElement.sendKeys(Keys.ENTER)


