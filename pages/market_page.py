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

        self.element_is_present(MarketPageLocators.HOW_TO_CHOOSE_PRODUCT_FOOTER)
        self.element_is_present(MarketPageLocators.PAYMENT_AND_DELIVERY_FOOTER)
        self.element_is_present(MarketPageLocators.FEEDBACK_FOOTER)
        self.element_is_present(MarketPageLocators.BUY_AS_LEGAL_ENTITY_FOOTER)
        self.element_is_present(MarketPageLocators.ABOUT_THE_SERVICE_FOOTER)
        self.element_is_present(MarketPageLocators.PARTICIPATION_IN_RESEARCH_FOOTER)
        self.element_is_present(MarketPageLocators.RETURNS_FOOTER)

        self.element_is_present(MarketPageLocators.SELLERS_PERSONAL_OFFICE_FOOTER)
        self.element_is_present(MarketPageLocators.SELL_ON_MARKET_FOOTER)
        self.element_is_present(MarketPageLocators.DOCUMENTATION_FOR_PARTNERS_FOOTER)
        self.element_is_present(MarketPageLocators.SITE_FOR_PARTNERS_FOOTER)

        self.element_is_present(MarketPageLocators.COMPANYS_NEWS_FOOTER)
        self.element_is_present(MarketPageLocators.AFFILIATE_PROGRAM_FOOTER)
        self.element_is_present(MarketPageLocators.PROGRAM_FOR_BLOGGERS_FOOTER)
        self.element_is_present(MarketPageLocators.FOR_MANUFACTURERS_FOOTER)
        self.element_is_present(MarketPageLocators.POINT_OF_ISSUANCE_OF_ORDERS_FOOTER)
        self.element_is_present(MarketPageLocators.MARKET_HIRING_FOOTER)

        self.element_is_present(MarketPageLocators.MOBILE_VERSION_FOOTER)
        self.element_is_present(MarketPageLocators.STATISTICS_FOOTER)
        self.element_is_present(MarketPageLocators.TERMS_OF_USE_FOOTER)

        self.element_is_present(MarketPageLocators.ADVISER_FOOTER)

