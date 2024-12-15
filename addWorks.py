from selenium.webdriver.common.by import By

from general import general

class addWorks:
    add_button = (By.XPATH,"//div[span[.='+'] and span[.=' добавить']]")
    choose_subject_button = (By.XPATH, "//i[.='выберите...']")
    subject_button = (By.XPATH, f"//div[@class='discline' and contains(text(), 'Языки информационного обмена', 'ПИН-231', '3');')]")
    input_name_button = (By.XPATH,"//input[@class='abitinptext']")
    upload_file_button = (By.XPATH,"//input[@class='otherf']")
    exit_button = (By.XPATH,"//div[contains(@onclick, 'getvkrpage') and contains(text(), 'закрыть')]")

    def upload_file(self, file_path, subject_name):
        self.click_element(self.add_button)
        self.click_element(self.choose_subject_button)
        self.click_element(subject_button)
        self.send_keys_to_element(self.input_name_button, subject_name)
        self.send_keys_to_element(self.upload_file_button, file_path)