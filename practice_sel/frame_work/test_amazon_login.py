from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_wrapper import selenium_wrapper
from time import sleep
from config import Config

def test_logn():
    driver = webdriver.Chrome(".\chromedriver")
    driver.get(Config.URL)
    driver.maximize_window()
    s = selenium_wrapper(driver)
    s.mouse_moove_to_element((By.XPATH,"//a[@id='nav-link-accountList']"))
    s.click_elemet((By.XPATH,"//span[text()='Sign in']"))
    s.enter_text((By.XPATH,"//input[@id='ap_email']"),Config.USER_NAME)
    s.click_elemet((By.XPATH,"//input[@id='continue']"))
    s.enter_text((By.XPATH,"//input[@id='ap_password']"),Config.PASSWORD)
    s.click_elemet((By.XPATH,"//input[@id='signInSubmit']"))
    sleep(5)
    s.enter_text((By.XPATH,"//div[@class='nav-search-field ']"),"fossil watch for men")
    s.click_elemet((By.XPATH,"//div[@class='nav-search-submit nav-sprite']//input[@id='nav-search-submit-button']"))
    s.click_elemet((By.XPATH,"//div[@class='a-section a-spacing-base a-text-center']//span[@class='a-size-base-plus a-color-base a-text-normal']"))
    # id = driver.window_handles()

