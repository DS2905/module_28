import pytest
from selenium import webdriver
import time



@pytest.fixture(scope="function")
def driver(request):
    path = str(request.fspath)
    print(request.fspath)
    time.sleep(10)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver