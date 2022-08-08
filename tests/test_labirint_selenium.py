#pytest -v --driver Chrome --driver-path C:\Users\0\Desktop\finaltests_module_28\app\chromedriver.exe

#1 Тестирование поиска книги по названию
def test_field_search():
    page.field_search.send_keys('Преступление и наказание')
    page.button_search.click()
