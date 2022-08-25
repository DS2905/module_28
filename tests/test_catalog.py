#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_catalog.py

from config import base_url
import time

#48 Переход в каталог товаров
def test_menu(selenium):
    selenium.get(base_url)
    time.sleep(5)
    search_input = selenium.find_element_by_id('open-menu').click()

#49 Закрытие всплывающего окна
def test_close_window(selenium):
    selenium.get(base_url)
    time.sleep(25)
    search_input = selenium.find_element_by_id('open-menu').click()
    search_input = selenium.find_element_by_id('mgo-mcw-leadgen-close').click()

#50 Поиск бренда и переход на его страницу
def test_brand(selenium):
    selenium.get(base_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_3218110189_10084').click()