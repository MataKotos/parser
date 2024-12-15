from selenium.webdriver.common.by import By

from general import general

class upload:
    def __init__(self, driver):
        super().__init__(driver)
        self.upload_button = (By.XPATH, "//a[@class='sidebar-menu__link'][@href='/ecab/vkr2.php']")

    def go_to_upload_page(self):
        self.click_element(self.upload_link)