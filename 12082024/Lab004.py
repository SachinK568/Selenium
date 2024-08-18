from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test():
    opt = Options()
    opt.add_argument('--incognito')

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.quit()