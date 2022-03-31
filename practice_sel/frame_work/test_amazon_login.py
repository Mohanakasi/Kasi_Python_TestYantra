from selenium import webdriver
from selenium.webdriver.common.by import By
import sselenium_wrapper
from time import sleep
from config import config

# def test_logn():
driver = webdriver.Chrome()
driver.get(config.URL)
driver.maximize_window()
s = sselenium_wrapper.selenium_functions(driver)
s.mouse_moove_to_element((By.XPATH,"//a[@id='nav-link-accountList']"))
s.click_elemet((By.XPATH,"//span[text()='Sign in']"))
s.enter_text((By.XPATH,"//input[@id='ap_email']"),config.USER_NAME)
s.click_elemet((By.XPATH,"//input[@id='continue']"))
s.enter_text((By.XPATH,"//input[@id='ap_password']"),config.PASSWORD)
s.click_elemet((By.XPATH,"//input[@id='signInSubmit']"))
# sleepk_elemet((By.XPATH,"//div[@class='a-section a-spacing-base a-text-center']//span[@class='a-size-base-plus a-color-base a-text-normal']"))
    # id = driver.window_handles()



