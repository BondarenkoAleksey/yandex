from pages.base_page import *
from locators.main_page_locators import *


class MainPage(BasePage):

    def elements_are_present(self):
        self.element_is_present(MainPageLocators.LOGO)
        self.element_is_present(MainPageLocators.ENTER_BUTTON)
        self.element_is_present(MainPageLocators.BURGER_BUTTON)
        self.element_is_present(MainPageLocators.SEARCH_INPUT)
        self.element_is_present(MainPageLocators.VOICE_BUTTON)
        self.element_is_present(MainPageLocators.CAMERA_BUTTON)
        self.element_is_present(MainPageLocators.WEATHER_ICON)
        self.element_is_present(MainPageLocators.USD_MOEX)
        self.element_is_present(MainPageLocators.EUR_MOEX)
        self.element_is_present(MainPageLocators.GEO_HOME)
        self.element_is_present(MainPageLocators.ALICE_ICON)

    def type_search_request(self):
        search_input = self.element_is_present(MainPageLocators.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys("почта")

    def click_button(self):
        search_button = self.element_is_present(MainPageLocators.SEARCH_BUTTON)
        search_button.click()
