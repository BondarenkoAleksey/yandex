from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_present(self, locator, time=25):
        wait = WebDriverWait(self.driver, time)
        return wait.until(EC.presence_of_element_located(locator),
                          message=f"Can't find element by locator {locator}")

    def execute_script(self, value):
        return self.driver.execute_script(value)

    def switch_to_frame(self, *locator):
        frame = self.driver.find_element(*locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def type_text(self, locator, text):
        element = self.element_is_present(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        self.element_is_present(locator).click()

    def click_element_with_action(self, locator):
        element = self.element_is_present(locator)
        actions = ActionChains(self.driver)
        return actions.click(element).perform()

    def find_elements(self, by, value):
        return self.find_elements(by, value)
