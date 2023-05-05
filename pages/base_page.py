from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


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

    def find_elements(self, by, value):
        return self.find_elements(by, value)

    def page_title(self):
        return self.driver.title

    def page_reload(self):
        self.driver.refresh()

    def execute_script(self, value):
        return self.driver.execute_script(value)

