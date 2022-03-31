from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium_wrapper import selenium_wrap
from configeration import config
driver = webdriver.Chrome(".\chromedriver")
driver.get(config.url)



s = selenium_wrap(driver)
s.mouse_moove_to_element((By.XPATH,"//a[@id='nav-link-accountList']"))
s.click_elemet((By.XPATH,"//span[text()='Sign in']"))
s.enter_text((By.XPATH,"//input[@id='ap_email']"),config.user_name)
s.click_elemet((By.XPATH,"//input[@id='continue']"))
s.enter_text((By.XPATH,"//input[@id='ap_password']"),config.pass_word)
s.click_elemet((By.XPATH,"//input[@id='signInSubmit']"))

