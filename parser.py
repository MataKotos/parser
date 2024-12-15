from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from general import general
from main import main
from login import login


from upload import upload
from addWorks import addWorks

url = "https://omgtu.ru/"
file_path = "J:\ЯИО"
username = "Ekaterina_Motos_8270"
password = "8236178f"


subject_name = "Языки информационного обмена"


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)


driver.get(url)

main_page = main(driver)

main_page.go_to_login_page()

login_page = login(driver)

login_page.login(username=username,password=password)

upload_page = upload(driver)

upload_page.go_to_uploading_report_page()

uploading_report_page = addWorks(driver)

uploading_report_page.upload(file_path=file_path,subject_name=subject_name)

time.sleep(300)
driver.quit()