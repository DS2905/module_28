#pytest -v --driver Chrome --driver-path C:\Users\0\Desktop\finaltests_module_28\chromedriver.exe
import time

from pages.lab_page import LabPage

#1
def test_visit(driver):
    lab_page = LabPage(driver)
    lab_page.visit()
    time.sleep(10)


#2Тестирование поиска книги по названию
#def test_field_search():
#    pages.field_search.send_keys('Преступление и наказание')
#    pages.button_search.click()
