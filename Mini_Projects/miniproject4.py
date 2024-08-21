import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    appointment = driver.find_element((By.XPATH, "//*[@id='btn-make-appointment']"))
    appointment.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    user_name = driver.find_element(By.XPATH, "//*[@id='txt-username']")
    user_name.send_keys("John Doe")
    pwd = driver.find_element(By.XPATH, "//*[@id='txt-password']")
    pwd.send_keys("ThisIsNotAPassword")
    login = driver.find_element(By.XPATH, "//*[@id='btn-login']")
    login.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    driver.close()
