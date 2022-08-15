#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_click.py

from config import base_url
from selenium.webdriver.common.keys import Keys

#14
def test_search(selenium):
    selenium.get(base_url)
    search_input = selenium.find_element_by_id('title-search-input')
    search_input.clear()
    search_input.send_keys('Наураша')
    WebElement.sendKeys(Keys.ENTER)
    selenium.save_screenshot('result.png')
