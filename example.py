import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.locators import MainPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")
time.sleep(5)
search_input = WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPage.SEARCH_INPUT))
search_input.click()
search_input.send_keys("почта")

search_button = WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(MainPage.SEARCH_BUTTON))
search_button.click()
time.sleep(5)
