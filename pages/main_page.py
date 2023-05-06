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
        self.type_text(MainPageLocators.SEARCH_INPUT, "почта")

    def elements_are_present_after_type_search_word(self):
        self.element_is_present(MainPageLocators.MARKET_BUTTON)
        self.element_is_present(MainPageLocators.GAMES_BUTTON)
        self.element_is_present(MainPageLocators.MAPS_BUTTON)
        self.element_is_present(MainPageLocators.KINOPOISK_BUTTON)
        self.element_is_present(MainPageLocators.TRANSLATE_BUTTON)
        self.element_is_present(MainPageLocators.AUTORU_BUTTON)
        self.element_is_present(MainPageLocators.TRAVEL_BUTTON)
        self.element_is_present(MainPageLocators.ALL_SERVICES_BUTTON)
        self.element_is_present(MainPageLocators.CLEAR_BUTTON)
        self.element_is_present(MainPageLocators.SEARCH_BUTTON)

