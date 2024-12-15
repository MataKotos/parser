from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class general:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_element(self, locator):
      try:
        return self.wait_for_element(locator)
      except (TimeoutException, NoSuchElementException):
        return None

    def click_element(self, locator):
        element = self.find_element(locator)
        if element:
          element.click()
        else:
          raise NoSuchElementException(f"Element not found: {locator}")

    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        if element:
          element.send_keys(text)
        else:
          raise NoSuchElementException(f"Element not found: {locator}")