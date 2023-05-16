from selenium.webdriver.common.by import By


class MarketPageLocators:
    ACCEPT_ALL = (By.CSS_SELECTOR, '[data-id="button-all"]')

    LOGO = (By.CSS_SELECTOR, '[data-baobab-name="home"]')
    CATALOG_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="catalog"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-zone-name="search-input"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-auto="search-button"]')
    PLUS_BUTTON = (By.CSS_SELECTOR, '[data-auto="headerPlusBalance"]')
    ORDERS_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="orders"]')
    FAVORITES_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="favorites"]')
    CART_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="cart"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-zone-name="headerLoginButton"]')

    LOCATION_BUTTON = (By.CSS_SELECTOR, '#hyperlocation-unified-dialog-anchor')
    BUY_AS_A_LEGAL_ENTITY_BUTTON = (By.CSS_SELECTOR,
                                    "a[href='https://business.market.yandex.ru/pokupayte-dlya-biznesa']")
    SELL_ON_MARKET_BUTTON = (By.XPATH, "//span[contains(text(),'Продавайте на Маркете')]")

    # to buyer
    HOW_TO_CHOOSE_PRODUCT_FOOTER = (By.XPATH, "//a[contains(text(),'Как выбрать товар')]")
    PAYMENT_AND_DELIVERY_FOOTER = (By.XPATH, "//a[contains(text(),'Оплата и доставка')]")
    FEEDBACK_FOOTER = (By.XPATH, "//a[contains(text(),'Обратная связь')]")
    BUY_AS_LEGAL_ENTITY_FOOTER = (By.XPATH, "//a[contains(text(),'Покупайте как юрлицо')]")
    ABOUT_THE_SERVICE_FOOTER = (By.XPATH, "//a[contains(text(),'О сервисе')]")
    PARTICIPATION_IN_RESEARCH_FOOTER = (By.XPATH, "//a[contains(text(),'Участие в исследованиях')]")
    RETURNS_FOOTER = (By.XPATH, "//a[contains(text(),'Возвраты')]")
