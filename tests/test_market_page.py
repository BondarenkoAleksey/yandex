import time

import allure

from pages.market_page import MarketPage


# @allure.feature("Test market page")
class TestMarketPage:

    # @allure.title("Visible of elements")
    def test_visible_of_elements_on_main_page(self, driver):
        market_page = MarketPage(driver, "https://market.yandex.ru/")
        market_page.open()
        market_page.accept_all()
        market_page.elements_are_present()


