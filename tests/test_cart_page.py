#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_cart_page.py

from config import base_url, cart_url
from selenium.webdriver.common.keys import Keys
import time

#15 Поиск на странице по существующему названию
def test_search(selenium):
    selenium.get(base_url)
    search_input = selenium.find_element_by_id('title-search-input')
    search_input.clear()
    search_input.send_keys('Лаборатория "Наураша в стране Наурандии"')
    WebElement.sendKeys(Keys.ENTER)

#16 Поиск на странице по не существующему названию
def test_search_not(selenium):
    selenium.get(base_url)
    search_input = selenium.find_element_by_id('title-search-input')
    search_input.clear()
    search_input.send_keys('Цемент')
    WebElement.sendKeys(Keys.ENTER)

#17 Поиск названия в карточке товара
def test_cart(selenium):
    selenium.get(cart_url)
    time.sleep(5)
    search_input = selenium.find_element_by_id('pagetitle')
    selenium.save_screenshot('result.png')

#18 Поиск цены в карточке товара
def test_cart_price(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_price')
    selenium.save_screenshot('result.png')

#19 Поиск артикула в карточке товара
def test_cart_art(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_class('code')
    selenium.save_screenshot('result.png')

#20 Поиск по тексту в карточке товара
def test_cart_name(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_text('Tinkamo Tinker kit')

#21 Складываем товар в корзину
def test_cart_basket(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()

#22 Делаем покупку в 1 клик
def test_cart_buy_one_click(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_1_click').click()

#23 Добавление больше одного товара в корзину
def test_cart_basket_two(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()

#24 Добавление нескольких твоаров в корзину,а потмо уменьшение количества товара
def test_cart_basket_tree(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_up').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_quant_down').click()
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()

#25 Переход в коризину из карточки товара
def test_cart_basket_all(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_basketFKauiI').click()

#26 Переход в корзину с главной страницы
def test_basket_all(selenium):
    selenium.get(base_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_basketFKauiI').click()

#27 Проверка "Заказать звонок"
def test_call(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_class('callback-popup-btn').click()

#28 Добавление товара в корзину, очистка корзины
def test_basket_clean(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_buy_link').click()
    search_input = selenium.find_element_by_id('bx_basketFKauiI').click()
    search_input = selenium.find_element_by_xpath('//*[@id="basket-items-list-wrapper"]/div[1]/a[1]').click()

#29 Добавление нескольких товаров в коризну
def test_basket_other_lot(selenium):
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/lego_duplo_education87/378/')
    search_input = selenium.find_element_by_id('bx_117848907_378_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/443/')
    search_input = selenium.find_element_by_id('bx_117848907_443_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_id('bx_117848907_14266_buy_link').click()

#30 Добавление нескольких товаров в коризну и удаление одного из
def test_basket_other_lot_clean_one_lot(selenium):
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/lego_duplo_education87/378/')
    search_input = selenium.find_element_by_id('bx_117848907_378_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/443/')
    search_input = selenium.find_element_by_id('bx_117848907_443_buy_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_xpath('//*[@id="basket-item-45066"]/td[5]/div[1]/span[1]').click()

#31 Переход с картчоки товара на главную страницу с помощью логотипа
def test_retuet_main_page(selenium):
    selenium.get(cart_url)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[1]/header[1]/div[2]/div[1]/div[2]/a[2]/img[1]').click()

#32 Добавляем 1 товар в сравнение
def test_cart_comparison_one(selenium):
    selenium.get(cart_url)
    time.sleep(2)
    search_input = selenium.find_element_by_id('bx_117848907_10220_compare_link').click()

#33 Добавляем несколько товаров в сравнение
def test_cart_comparison(selenium):
    selenium.get(cart_url)
    search_input = selenium.find_element_by_id('bx_117848907_10220_compare_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_id('bx_117848907_14266_compare_link').click()
    time.sleep(2)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]').click()

#34 В карточке сравнения переключение на различающиеся
def test_cart_comparison_char(selenium):
    selenium.get(cart_url)
    search_input = selenium.find_element_by_id('bx_117848907_10220_compare_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_id('bx_117848907_14266_compare_link').click()
    time.sleep(2)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]').click()
    search_input = selenium.find_element_by_xpath('//*[@id="bx_catalog_compare_block"]/div[1]/div[1]/a[2]').click()

#35 В карточке сравнения удаление 1го товара
def test_cart_comparison_del(selenium):
    selenium.get(cart_url)
    search_input = selenium.find_element_by_id('bx_117848907_10220_compare_link').click()
    selenium.get('https://edusnab.ru/catalog/robototekhnika_i_lego_education/konstruktor_lego_education/14266/')
    search_input = selenium.find_element_by_id('bx_117848907_14266_compare_link').click()
    time.sleep(2)
    search_input = selenium.find_element_by_xpath('body/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]').click()
    search_input = selenium.find_element_by_xpath('//*[@id="bx_catalog_compare_block"]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/a[2]').click()


