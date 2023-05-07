import time

from pages.main_page import MainPage


class TestMainPage:

    def test_visible_of_elements_on_main_page(self, driver):
        main_page = MainPage(driver, "https://ya.ru")
        main_page.open()
        main_page.elements_are_present()
        main_page.type_search_request()
        main_page.elements_are_present_after_type_search_word()
        time.sleep(5)



