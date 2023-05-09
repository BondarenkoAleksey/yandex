from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


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

    def click_menu_burger(self):
        self.click_element_with_action(MainPageLocators.BURGER_BUTTON)

    def switch_to_frame_menu(self):
        self.switch_to_frame(*MainPageLocators.FRAME_MENU)

    def elements_are_present_after_click_menu(self):
        self.element_is_present(MainPageLocators.ACCOUNT_MENU_BUTTON)
        self.element_is_present(MainPageLocators.CLOSE_MENU_BUTTON)
        self.element_is_present(MainPageLocators.AUTH_MENU_BUTTON)
        self.element_is_present(MainPageLocators.MAIL_MENU_BUTTON)
        self.element_is_present(MainPageLocators.WRITE_MAIL_MENU_BUTTON)
        self.element_is_present(MainPageLocators.FAVORITES_MENU_BUTTON)
        self.element_is_present(MainPageLocators.GET_PLUS_BUTTON)
        self.element_is_present(MainPageLocators.ACCOUNT_MANAGEMENT_MENU_BUTTON)
        self.element_is_present(MainPageLocators.MY_FEEDBACK_MENU_BUTTON)
        self.element_is_present(MainPageLocators.SKIN_MENU_BUTTON)
        self.element_is_present(MainPageLocators.SETTINGS_MENU_BUTTON)
        self.element_is_present(MainPageLocators.SUPPORT_MENU_BUTTON)
        self.element_is_present(MainPageLocators.LEGAL_RULES_MENU_BUTTON)
        self.element_is_present(MainPageLocators.CONFIDENTIAL_MENU_BUTTON)
        self.element_is_present(MainPageLocators.BLOG_MENU_BUTTON)
        self.element_is_present(MainPageLocators.ABOUT_COMPANY_MENU_BUTTON)

    def switch_to_main(self):
        self.switch_to_default_content()

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
