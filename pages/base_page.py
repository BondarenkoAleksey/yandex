from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_present(self, locator, time=20):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f"Can't find element by locator {locator}")

    def type_text(self, locator, text):
        element = self.element_is_present(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def find_elements(self, by, value):
        return self.find_elements(by, value)

    def page_title(self):
        return self.driver.title

    def page_reload(self):
        self.driver.refresh()

    def execute_script(self, value):
        return self.driver.execute_script(value)

