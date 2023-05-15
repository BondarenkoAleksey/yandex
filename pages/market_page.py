from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.market_page_locators import MarketPageLocators


class MarketPage(BasePage):

    def accept_all(self):
        try:
            self.click_element(MarketPageLocators.ACCEPT_ALL)
        except TimeoutException:
            print("\nБез показа модалки сохранения куки")

    def elements_are_present(self):
        self.element_is_present(MarketPageLocators.LOGO)
        self.element_is_present(MarketPageLocators.CATALOG_BUTTON)
        self.element_is_present(MarketPageLocators.SEARCH_INPUT)
        self.element_is_present(MarketPageLocators.SEARCH_INPUT)
        self.element_is_present(MarketPageLocators.SEARCH_BUTTON)
        self.element_is_present(MarketPageLocators.PLUS_BUTTON)
        self.element_is_present(MarketPageLocators.ORDERS_BUTTON)
        self.element_is_present(MarketPageLocators.FAVORITES_BUTTON)
        self.element_is_present(MarketPageLocators.CART_BUTTON)
        self.element_is_present(MarketPageLocators.LOGIN_BUTTON)

        self.element_is_present(MarketPageLocators.LOCATION_BUTTON)
        self.element_is_present(MarketPageLocators.BUY_AS_A_LEGAL_ENTITY_BUTTON)
        self.element_is_present(MarketPageLocators.SELL_ON_MARKET_BUTTON)

