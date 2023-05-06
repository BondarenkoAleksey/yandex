from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, 'a[aria-label="Яндекс"]')
    ENTER_BUTTON = (By.CSS_SELECTOR, '[data-statlog="headline.enter"]')
    BURGER_BUTTON = (By.CSS_SELECTOR, ".headline__personal-icon>svg")
    VOICE_BUTTON = (By.CSS_SELECTOR, 'button[data-action="voice"]')
    CAMERA_BUTTON = (By.CSS_SELECTOR, '.search3__svg_camera')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    WEATHER_ICON = (By.CSS_SELECTOR, "div.informers3__item-icon")
    USD_MOEX = (By.CSS_SELECTOR, '[title="USD MOEX"]>span')
    EUR_MOEX = (By.CSS_SELECTOR, '[title="EUR MOEX"]>span')
    GEO_HOME = (By.CSS_SELECTOR, '[data-statlog="informers.geo"]')
    ALICE_ICON = (By.TAG_NAME, "circle")

    MARKET_BUTTON = (By.XPATH, "//a[@data-id='market']")
    GAMES_BUTTON = (By.XPATH, "//a[@data-id='games']")
    MAPS_BUTTON = (By.XPATH, "//a[@data-id='maps']")
    KINOPOISK_BUTTON = (By.XPATH, "//a[@data-id='kinopoisk_old']//div[@class='services-suggest__icon']")
    TRANSLATE_BUTTON = (By.XPATH, "//a[@data-id='translate']")
    AUTORU_BUTTON = (By.XPATH, "//a[@data-id='autoru']")
    TRAVEL_BUTTON = (By.XPATH, "//a[@data-id='travel']")
    ALL_SERVICES_BUTTON = (By.CSS_SELECTOR, "a[data-statlog=\"services_suggest.more\"]")
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'button[title="Очистить поисковый запрос"]')
    SEARCH_INPUT = (By.ID, "text")



