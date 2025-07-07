# pip install selenium
# pip install webdriver_manager
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


username = input("enter your username: ")
password = input("enter your password: ")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(1)

# login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--h5.orangehrm-login-title")
# login_button.click() # jokhon button thakbe tokhon dibo na hole dorkar nai

username_box = driver.find_element(By.NAME, "username")
username_box.send_keys(username)

password_box = driver.find_element(By.NAME, "password")
password_box.send_keys(password)

final_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
final_login.click()
