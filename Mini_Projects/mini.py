import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

import allure





@ allure.title("miniproject_3")
def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(10)
    email = driver.find_element(By.ID, "username")
    email.send_keys("augtest_040823@idrive.com")
    pwd = driver.find_element(By.ID, "password")
    pwd.send_keys("123456")
    sign_in = driver.find_element(By.ID, "frm-btn")
    sign_in.click()
    time.sleep(10)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(),name= "screenshot")
    driver.close()