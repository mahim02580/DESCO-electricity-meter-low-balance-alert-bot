import os
import smtplib
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

ACCOUNT_NUMBER = os.getenv("ACCOUNT_NUMBER")
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def send_email(body):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:⚠️Electricity Meter Low Balance Alert!\n\n{body}".encode()
        )

if not EMAIL or not APP_PASSWORD:
    raise ValueError("Missing EMAIL or APP_PASSWORD in environment variables.")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://prepaid.desco.org.bd/customer/#/customer-login")
    wait = WebDriverWait(driver, 15)

    account_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))
    account_input.send_keys(ACCOUNT_NUMBER, Keys.ENTER)

    balance = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/main/div/div/div[5]/div/div[2]/div/footer/p/span[1]')))
    current_balance = int(float(balance.text.split()[0].replace(",", "")))

    if current_balance < 100:
        message = f"Current balance for meter account: {ACCOUNT_NUMBER} is {current_balance} BDT."
        send_email(message)

except Exception as e:
    send_email(f"⚠️ Error occurred: {e}")
    raise

finally:
    driver.quit()
