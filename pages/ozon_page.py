from config import base_url

class OzonPage():

    def __init__(self, driver):
        self.driver= driver

    def visit(self):
        self.driver.get(base_url)

    def get_elektronika(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Электроника')]")
