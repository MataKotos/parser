from selenium.webdriver.common.by import By
from general import general

class main:
    personal_account_button = (By.XPATH, "//a[@class='horizontal-menu__link'][@href='https://omgtu.ru/ecab/']")


    def clickContactButton(self):
        self.driver.find_element(By.XPATH, self.personal_account_button).click()