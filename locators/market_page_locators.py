from selenium.webdriver.common.by import By


class MarketPageLocators:
    LOGO = (By.CSS_SELECTOR, '[data-baobab-name="home"]')
    CATALOG_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="catalog"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-zone-name="search-input"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-auto="search-button"]')
    PLUS_BUTTON = (By.CSS_SELECTOR, '[data-auto="headerPlusBalance"]')
    ORDERS_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="orders"]')
    FAVORITES_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="favorites"]')
    CART_BUTTON = (By.CSS_SELECTOR, '[data-baobab-name="cart"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-zone-name="headerLoginButton"]')

