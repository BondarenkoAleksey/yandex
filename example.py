import time

from pages.locators import MainPage
from pages.base_page import BasePage

base_page = BasePage()
base_page.open("https://ya.ru")
time.sleep(5)

search_input = base_page.find_element(MainPage.SEARCH_INPUT)
search_input.click()
search_input.send_keys("почта")

search_button = base_page.find_element(MainPage.SEARCH_BUTTON)
search_button.click()
time.sleep(5)

