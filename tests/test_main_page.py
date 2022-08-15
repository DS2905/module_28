#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_main_page.py
import time
from pages.main_page import EdusnabPage

#1 открываем страницу сайта в браузере
def test_visit(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()

#2 открываем раздел "Национальные проекты"
def test_visit_project_nat(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_project_nat().is_displayed()
    time.sleep(2)

#3 открываем раздел "О нас"
def test_visit_company(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_company().is_displayed()
    time.sleep(2)

#4 открываем раздел "Бренды"
def test_visit_brands(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_brands().is_displayed()
    time.sleep(2)

#5 открываем раздел "Услуги"
def test_visit_services(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_services().is_displayed()
    time.sleep(2)

#6 открываем раздел "Акции"
def test_visit_actions(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_actions().is_displayed()
    time.sleep(2)

#7 открываем раздел "Медиацентр"
def test_visit_media(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_media().is_displayed()
    time.sleep(2)

#8 открываем раздел "Производителям"
def test_visit_partners(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_partners().is_displayed()
    time.sleep(2)

#9 открываем раздел "Проектный раздел"
def test_visit_project(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_project().is_displayed()
    time.sleep(2)

#10 открываем раздел "Оплата, сборка и доставка"
def test_visit_delivery(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_delivery().is_displayed()
    time.sleep(2)

#11 открываем раздел "Готовые решения"
def test_visit_resheniya(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_resheniya().is_displayed()
    time.sleep(2)

#12 открываем раздел "Прайсы и каталоги"
def test_visit_price(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_price().is_displayed()
    time.sleep(2)

#13 открываем раздел "Контакты"
def test_visit_contacts(driver):
    main_page = EdusnabPage(driver)
    main_page.visit()
    assert main_page.get_contacts().is_displayed()
    time.sleep(2)
