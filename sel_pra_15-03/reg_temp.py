from selenium import webdriver
from time import sleep


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import *
driver = webdriver.Chrome(".\chromedriver")



driver.get("httP://demowebshop.tricentis.com")
driver.maximize_window()
click_element(("class name","ico-register"),)
click_element(("id","gender-male"))
enter_text(("id","FirstName"),"mohana kasi")
enter_text(("id","LastName"),"settipalli")
enter_text(("name","Email"),"raomohana8@k18.com")
enter_text(("id","Password"),"Mohana1995")
enter_text(("id","ConfirmPassword"),"Mohana1995")
click_element(("id","register-button"))
click_element(("xpath","//div[@class='center-2']//input[@class='button-1 register-continue-button']"))
