from selenium.webdriver.common.by import By

from general import general


class login:
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.XPATH, "//input[@class='abinput'][@name='USER_LOGIN']")
        self.password_field = (By.XPATH, "//input[@class='abitinput'][@name='USER_PASSWORD']")
        self.login_button = (By.XPATH, "//div[@class='abitsubmitkey'][.='войти']")


    def login(self, username, password):
        self.send_keys_to_element(self.username_field, username)
        self.send_keys_to_element(self.password_field, password)
        self.click_element(self.login_button)