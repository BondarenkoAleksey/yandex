from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.ID, "text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[type=submit]")