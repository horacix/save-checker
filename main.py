import time
import os
import os.path
import smtplib
import ssl
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

load_dotenv()

# Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)


def checkCase(browser, caseNumber, dob):
    # Get page
    browser.get("https://save.uscis.gov/CaseCheck/")

    # 1st page
    browser.find_element(
        By.ID, 'ctl00_MainContentPlaceHolder_chkIAgree').click()
    browser.find_element(By.ID, 'ctl00_MainContentPlaceHolder_btnNext').click()

    # 2nd page
    browser.find_element(
        By.ID, 'ctl00_MainContentPlaceHolder_txtCaseNumber_TextBox').send_keys(caseNumber)
    browser.find_element(
        By.ID, 'ctl00_MainContentPlaceHolder_txtDob_dateTextBox').send_keys(dob)
    browser.find_element(
        By.ID, 'ctl00_MainContentPlaceHolder_btnSubmit').click()

    # 3rd page
    imgStatus = browser.find_element(
        By.ID, 'ctl00_MainContentPlaceHolder_CasesGrid_ctl02_imgStatus')

    return imgStatus.get_attribute('alt')


hglCase = checkCase(browser, '0022209181410TP', '11/01/1979')
print(f"HGL: {hglCase}")
time.sleep(10)
mfgoCase = checkCase(browser, '0022182182647VZ', '09/16/1981')
print(f"MFGO: {mfgoCase}")

browser.quit()

# # context = ssl.create_default_context()
# with smtplib.SMTP(os.environ['SMTP_SERVER'], os.environ['SMTP_PORT']) as server:
#     server.login(os.environ['SMTP_LOGIN'], os.environ['SMTP_PASSWORD'])
#     server.sendmail('hgonzalezl@gmail.com', ['hgonzalezl@gmail.com', 'mfguzmao@gmail.com'], f"""Case Status:
#     0022209181410TP (HGL): {hglCase}
#     0022182182647VZ (MFGO): {mfgoCase}
# """)
