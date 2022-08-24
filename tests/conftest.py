import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture
def driver():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()