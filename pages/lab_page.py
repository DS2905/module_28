from config import base_url

class LabPage()

    def _init_(self, driver):
        self.driver= driver

    def visit(self):
        self.driver.get()