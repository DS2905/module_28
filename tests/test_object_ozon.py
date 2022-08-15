#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_object_ozon.py

from pages.ozon_page import OzonPage
from pages.elektronika_page import ElektronikaPage
import time

#1
def test_visit(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_elektronika().is_displayed()
    time.sleep(5)

#2
def test_elektronika(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_elektronika().click()
    elektronika_page = ElektronikaPage(driver)
    time.sleep(5)
    assert elektronika_page.get_elektronika()[1].is_displayed()
    time.sleep(5)