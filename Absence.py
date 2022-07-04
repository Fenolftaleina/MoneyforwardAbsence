from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

threshold = 7

PATH = "DRIVER_PATH"
s = Service(PATH)
option = Options()
option.binary_location = 'BROWSER_PATH_FORCHROME'
driver = webdriver.Chrome(service=s, options=option)

id = "COMPANY_ID"
mail = "ACCOUNT_EMAIL"
pw = "ACCOUNT_PASSWORD"

def checkmonth():
    today = date.today()
    if int(str(today).split("-")[-1]) < threshold :
        back = driver.find_element(by=By.CLASS_NAME, value="attendance-table-header-month-range-previous")
        back.click()
        try:
            popup = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='_btn__2MYp_ _btn-close__2MYp_ karte-close']"))
            )
        finally:
            popup.click()

def fillPersonal(id, mail, pw):
    idField = driver.find_element(by=By.ID, value="employee_session_form_office_account_name")
    idField.send_keys(id)
    mailField = driver.find_element(by=By.ID, value="employee_session_form_account_name_or_email")
    mailField.send_keys(mail)
    passField = driver.find_element(by=By.ID, value="employee_session_form_password")
    passField.send_keys(pw)

def fillNone():
   counter = 0
   rows = driver.find_elements(by=By.CLASS_NAME, value="attendance-table-row-") + driver.find_elements(by=By.CLASS_NAME, value="attendance-table-row-error")
   size = range(len(rows))
   for i in size:
       rows = driver.find_elements(by=By.CLASS_NAME, value="attendance-table-row-") + driver.find_elements(by=By.CLASS_NAME, value="attendance-table-row-error")
       WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//tr/td/span[text()='申請']"))
       )
       words = rows[counter].text.split()
       if '欠勤(申請中)' not in words and '編' not in words and '欠勤' not in words:
            rows[counter].find_element(by=By.XPATH, value=f"//table[@class='attendance-table-contents attendance-table-contents-border attendance-table-layout-fixed']/tbody/tr[{counter}]/td/span[text()='申請']").click()
            try:
                kekkinButton = WebDriverWait(rows[counter], 3).until(
                        EC.element_to_be_clickable((By.XPATH, f"//table[@class='attendance-table-contents attendance-table-contents-border attendance-table-layout-fixed']/tbody/tr[{counter}]/td/ul/li/a[text()='欠勤']"))
                )
            finally: 
                rows[counter].find_element(by=By.XPATH, value=f"//table[@class='attendance-table-contents attendance-table-contents-border attendance-table-layout-fixed']/tbody/tr[{counter}]/td/ul/li/a[text()='欠勤']").click()
            try:
                element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "attendance-text-area"))
                )
            finally: 
                element.send_keys("欠勤")
                driver.find_element(by=By.NAME, value="commit").click()
       counter += 1
       
       
           
driver.get("https://attendance.moneyforward.com/my_page/attendances")
fillPersonal(id, mail, pw)
driver.find_element(by=By.NAME, value="commit").click()
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "attendance-table-header-month-range-previous"))
    )
finally:
    checkmonth()
fillNone()
driver.close()
driver.quit()