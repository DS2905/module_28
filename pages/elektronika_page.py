from config import base_url

class ElektronikaPage():

    def_init_(self, driver):
        self.driver= driver

    def visit(self):
        self.driver.get(base_url)

    def get_elektronika(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Ноутбуки')]")

    #def get_elektronika(self):
        #return self.driver.find_elements_by_xpath("//*[contains(text(), 'Техника для дома')]")