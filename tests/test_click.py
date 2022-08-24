#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_click.py

from config import base_url, cart_url
from selenium.webdriver.common.keys import Keys
import time

#14 Поиск на странице по существующему названию
def test_search(selenium):
    selenium.get(base_url)
    search_input = selenium.find_element_by_id('title-search-input')
    search_input.clear()
    search_input.send_keys('Лаборатория "Наураша в стране Наурандии"')
    WebElement.sendKeys(Keys.ENTER)

#15 Поиск на странице по не существующему названию
def test_search_not(selenium):
    selenium.get(base_url)
    search_input = selenium.find_element_by_id('title-search-input')
    search_input.clear()
    search_input.send_keys('Цемент')
    WebElement.sendKeys(Keys.ENTER)

#16 Поиск названия в карточке товара
def test_cart(selenium):
    selenium.get(cart_url)
    time.sleep(5)
    search_input = selenium.find_element_by_id('pagetitle')
    selenium.save_screenshot('result.png')

#17 Поиск цены в карточке товара
def test_cart_price(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_price')
    selenium.save_screenshot('result.png')

#18 Поиск артикула в карточке товара
def test_cart_art(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_class('code')
    selenium.save_screenshot('result.png')

#19 Поиск по тексту в карточке товара
def test_cart_name(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_text('Tinkamo Tinker kit')

#20 Складываем товар в корзину
def test_cart_basket(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()

#21 Делаем покупку в 1 клик
def test_cart_buy_one_click(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_1_click').click()

#22 Добавление больше одного товара в корзину
def test_cart_basket_two(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()

#23 Добавление нескольких твоаров в корзину,а потмо уменьшение количества товара
def test_cart_basket_tree(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_down').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()

#24 Переход в коризину из карточки товара
def test_cart_basket_all(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_basketFKauiI').click()

#25 Переход в корзину с главной страницы
def test_basket_all(selenium):
    selenium.get(base_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_basketFKauiI').click()

#26 Проверка "Заказать звонок"
def test_call(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_class('callback-popup-btn').click()

#27 Добавление товара в корзину, очистка корзины
def test_basket_clean(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()
    search_input = selenium.find_element_by_id('bx_basketFKauiI').click()
    search_input = selenium.find_element_by_xpath('//*[@id="basket-items-list-wrapper"]/div[1]/a[1]').click()

#28 Добавление нескольких товаров в коризну
def test_basket_other_lot(selenium):
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/lego_duplo_education87/378/')
    search_input = selenium.find_element_by_id('bx_117848907_378_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/443/')
    search_input = selenium.find_element_by_id('bx_117848907_443_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_id('bx_117848907_14266_buy_link').click()

#29 Добавление нескольких товаров в коризну и удаление одного из
def test_basket_other_lot_clean_one_lot(selenium):
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/lego_duplo_education87/378/')
    search_input = selenium.find_element_by_id('bx_117848907_378_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/443/')
    search_input = selenium.find_element_by_id('bx_117848907_443_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_xpath('//*[@id="basket-item-45066"]/td[5]/div[1]/span[1]').click()

#30 Переход с картчоки товара на главную страницу с помощью логотипа
def test_retuet_main_page(selenium):
    selenium.get(cart_url)
    search_input = selenium.find_element_by_xpath("body/div[2]/div[1]/header[1]/div[2]/div[1]/div[2]/a[2]/img[1