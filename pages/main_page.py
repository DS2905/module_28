from config import base_url

class EdusnabPage():

    def __init__(self, driver):
        self.driver= driver

    def visit(self):
        self.driver.get(base_url)

    def get_project_nat(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Национальные проекты')]")

    def get_company(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'О нас')]")

    def get_brands(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Бренды')]")

    def get_services(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Услуги')]")

    def get_actions(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Акции')]")

    def get_media(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Медиацентр')]")

    def get_partners(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Производителям')]")

    def get_project(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Проектный раздел')]")

    def get_delivery(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Оплата, сборка и доставка')]")

    def get_resheniya(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Готовые решения')]")

    def get_price(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Прайсы и каталоги')]")

    def get_contacts(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Контакты')]")