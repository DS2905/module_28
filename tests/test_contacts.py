#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_contacts.py

from config import contact_url
import time

#44 Нажатие кнопки "Задать вопрос"
def test_ask(selenium):
    selenium.get(contact_url)
    time.sleep(5)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[2]/div[2]/div[1]/main[1]/div[2]/div[1]/a[1]').click()

#45 Нажатие кнопки "Задать вопрос"
def test_write(selenium):
    selenium.get(contact_url)
    time.sleep(5)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[2]/div[2]/div[1]/main[1]/div[2]/div[1]/a[2]]').click()

#46 Наличие адреса на странице
def test_adress(selenium):
    selenium.get(contact_url)
    time.sleep(2)
    search_input = selenium.find_element_by_text('Наш адрес')

#47 Наличие телефона на странице
def test_phone(selenium):
    selenium.get(contact_url)
    time.sleep(2)
    search_input = selenium.find_element_by_text('Контактный телефон')

#47 Наличие email на странице
def test_email(selenium):
    selenium.get(contact_url)
    time.sleep(2)
    search_input = selenium.find_element_by_text('E-mail')


