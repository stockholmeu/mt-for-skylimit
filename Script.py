from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager  # For automatic driver management
import random
import string
import time

def lalala_generate_email_password():
    domain = "@example.com"
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    lalala_email = random_string + domain
    lalala_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return lalala_email, lalala_password

def blablabla_get_api_key(pampampam_driver):
    pampampam_driver.get("https://dash.cloudflare.com/")
    try:
        api_key_element = WebDriverWait(pampampam_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="api-key"]'))
        )
        api_key = api_key_element.text
        return api_key
    except (TimeoutException, NoSuchElementException):
        return None

def blablabla_register_cloudflare_account(pampampam_driver, lalala_email, lalala_password):
    pampampam_driver.get("https://dash.cloudflare.com/sign-up")
    try:
        WebDriverWait(pampampam_driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
    except TimeoutException:
        return False

    email_field = pampampam_driver.find_element(By.ID, "email")
    password_field = pampampam_driver.find_element(By.ID, "password")
    email_field.send_keys(lalala_email)
    password_field.send_keys(lalala_password)
    create_account_button = pampampam_driver.find_element(By.XPATH, '//button[@type="submit"]')
    create_account_button.click()

    try:
        WebDriverWait(pampampam_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "dashboard")]'))
        )
    except TimeoutException:
        return False
    return True

def create_lalala_cloudflare_accounts(number_of_accounts):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    pampampam_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    lalala_accounts = []

    try:
        for _ in range(number_of_accounts):
            lalala_email, lalala_password = lalala_generate_email_password()
            success = blablabla_register_cloudflare_account(pampampam_driver, lalala_email, lalala_password)
            if success:
                api_key = blablabla_get_api_key(pampampam_driver)
                lalala_accounts.append({
                    "email": lalala_email,
                    "password": lalala_password,
                    "api_key": api_key if api_key else "Not Available"
                })
            else:
                print(f"Account creation failed for {lalala_email}")
    finally:
        pampampam_driver.quit()

    return lalala_accounts

if __name__ == "__main__":
    number_of_accounts = int(input("Enter the number of accounts to create: "))
    lalala_accounts = create_lalala_cloudflare_accounts(number_of_accounts)
    for account in lalala_accounts:
        print(f"Email: {account['email']}, Password: {account['password']}, API Key: {account['api_key']}")
