import time

import allure

from pages.main_page import MainPage


# @allure.feature("Test main page")
class TestMainPage:

    # @allure.title("Visible of elements")
    def test_visible_of_elements_on_main_page(self, driver):
        main_page = MainPage(driver, "https://ya.ru")
        main_page.open()
        main_page.elements_are_present()
        main_page.click_menu_burger()
        main_page.switch_to_frame_menu()
        main_page.elements_are_present_after_click_menu()
        main_page.switch_to_default_content()
        main_page.type_search_request()
        main_page.elements_are_present_after_type_search_word()

        # time.sleep(5)



