from pages.main_page import *


class TestMainPage:

    def test_visible_of_elements(self, driver):
        main_page = MainPage(driver, "https://ya.ru")
        main_page.open()
        main_page.elements_are_present()
        # main_page.type_search_request()
        # main_page.click_button()



