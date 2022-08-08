#pip install selenium
#pip install pytest-selenium
import pytest
from selenium import webdriver

@pytest.fixture
def testing():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.labirint.ru/')
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
