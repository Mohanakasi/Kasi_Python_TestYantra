
"""using find_element"""
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome(".\Chromedriver")
#
# driver.get("httP://demowebshop.tricentis.com")
# driver.implicitly_wait(15)
# driver.find_element_by_class_name("ico-register").click()
# sleep(2)
# driver.find_element_by_id("gender-male").click()
# sleep(2)
# # driver.find_element_by_id("gender-female").click()
# driver.find_element("id","FirstName").send_keys("mohana kasi")
# sleep(2)
# driver.find_element("id","LastName").send_keys("settipalli")
# sleep(2)
# driver.find_element("name","Email").send_keys("fdgSG@k18.com")
# sleep(2)
# driver.find_element("id","Password").send_keys("Mohana1995")
# sleep(2)
# driver.find_element_by_id("ConfirmPassword").send_keys("Mohana1995")
# sleep(2)
# driver.find_element("id","register-button").click()
# sleep(2)
# driver.find_element("xpath","//div[@class='center-2']//input[@class='button-1 register-continue-button']").click()


"""by defining a class for click, sel;ect, send_keys"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome(".\Chromedriver")

def click_element(loc_type, loc_value):
    driver.find_element(loc_type,loc_value).click()

def enter_text(loc_type, loc_value, value):
    driver.find_element(loc_type, loc_value).send_keys(value)

def select_item(loc_type, item):
    element_ = driver.find_element(loc_type,loc_type)
    s = Select(element_)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise TypeError

driver.get("httP://demowebshop.tricentis.com")
sleep(15)
click_element("class name","ico-register")
sleep(3)
click_element("id","gender-male")
sleep(3)
enter_text("id","FirstName","mohana kasi")
sleep(3)
enter_text("id","LastName","settipalli")
sleep(3)
enter_text("name","Email","ka8@k18.com")
sleep(3)
enter_text("id","Password","Mohana1995")
sleep(3)
enter_text("id","ConfirmPassword","Mohana1995")
sleep(3)
click_element("id","register-button")
sleep(3)
click_element("css selector","input[value='Continue']")
sleep(3)
click_element("css selector","input[value='Continue']")
sleep(3)
click_element("xpath","//div[@class='center-2']//input[@class='button-1 register-continue-button']")
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.remote.webelement import WebElement
# driver = webdriver.Chrome(".\Chromedriver")
#
class _visibility_of_element_located(expected_conditions.visibility_of_element_located):
#     def __call__(self, driver):
#         displayed = super().__call__(driver)
#         if isinstance(displayed, WebElement):
#             return displayed.is_enabled()
#         else:
#             return False
# def wait(func):
#     def wrapper(*args, **kwargs):
#         locator = args[0]
#         wait = WebDriverWait(driver,50)
#         v =_visibility_of_element_located(driver)
#         wait.until(v)
#         return func(*args, **kwargs)
#     return wrapper
# @wait
# def click_element(locator):
#     driver.find_element(*locator).click()
# @wait
# def enter_text(locator, value):
#     driver.find_element(*locator).send_keys(value)
#
# @wait
# def select_item(*locator):
#     element_ = driver.find_element(*locator)
#     s = Select(element_)
#     if isinstance(locator[-1], str):
#         s.select_by_visible_text(locator[-1])
#     elif isinstance(locator[-1], int):
#         s.select_by_index(locator[-1])
#     else:
#         raise TypeError
#
driver.get("httP://demowebshop.tricentis.com")
click_element(("class_name","ico-register"))
click_element(("id","gender-male"))
enter_text(("id","FirstName"),"mohana kasi")
enter_text(("id","LastName"),"settipalli")
enter_text(("name","Email"),"ka8@k18.com")
enter_text(("id","Password"),"Mohana1995")
click_element(("id","register-button"))
click_element(("css_selector","input[value='Continue']"))
click_element(("css_selector","input[value='Continue']"))





