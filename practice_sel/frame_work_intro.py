
"""using find_element"""

"""finding the web elements by using find_element"""
"""when we are using find_element in the arguments we have to pass two arguments"""
"""one is locator name, another one is locator value"""
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome(".\Chromedriver")
# driver.get("httP://demowebshop.tricentis.com")
# driver.maximize_window()
# sleep(3)
# driver.maximize_window()
# driver.implicitly_wait(15)
# driver.find_element("class name","ico-register").click()
# sleep(2)
# driver.find_element("id","gender-male").click()
# sleep(2)
# driver.find_element("id","FirstName").send_keys("mohana kasi")
# sleep(2)
# driver.find_element("id","LastName").send_keys("settipalli")
# sleep(2)
# driver.find_element("name","Email").send_keys("fSG@k18.com")
# sleep(2)
# driver.find_element("id","Password").send_keys("Mohana1995")
# sleep(2)
# driver.find_element_by_id("ConfirmPassword").send_keys("Mohana1995")
# sleep(2)
# driver.find_element("id","register-button").click()
# sleep(2)
# driver.find_element("xpath","//div[@class='center-2']//input[@class='button-1 register-continue-button']").click()

"""registration example for frame work"""
"""by defining a function for click, send_keys, select"""
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.common.exceptions import *
# driver = webdriver.Chrome(".\chromedriver")
#
# def click_element(loc_type, loc_value):
#     driver.find_element(loc_type,loc_value).click()
#
# def enter_text(loc_type, loc_value, value):
#     driver.find_element(loc_type, loc_value).send_keys(value)
#
# def select_item(locator, item): #--> ("xpath","//select[@id='multiple_cars']")
#     element_ = driver.find_element(*locator) #---> "xpath", "//select[@id='multiple_cars']"
#     s = Select(element_)
#     if isinstance(item, str):
#         s.select_by_visible_text(item)
#     elif isinstance(item, int):
#         s.select_by_index(item)
#     else:
#         raise TypeError
#
# driver.get("httP://demowebshop.tricentis.com")
# driver.maximize_window()
# sleep(15)
# click_element("class name","ico-register")
# sleep(3)
# click_element("id","gender-male")
# sleep(3)
# enter_text("id","FirstName","mohana kasi")
# sleep(3)
# enter_text("id","LastName","settipalli")
# sleep(3)
# enter_text("name","Email","dgsg@k18.com")
# sleep(3)
# enter_text("id","Password","Mohana1995")
# sleep(3)
# enter_text("id","ConfirmPassword","Mohana1995")
# sleep(3)
# click_element("id","register-button")
# sleep(3)
# click_element("xpath","//div[@class='center-2']//input[@class='button-1 register-continue-button']")
# sleep(3)
# select_item(("xpath","//select[@id='multiple_cars']"),"Jaguar")

"""registration example for frame work"""
"""by taking locator type and locator value as a single tuple and un packing in argument place while finding elem"""
"""here we are creating a decorator function that applied to each click or send_keys or Select that checks\n
each webelement is loaded in the dom and it is visible or not and it checks whether it was enabled or not"""
"""if that decorator giving us a error means may be it was not loaded in the dom or if it is not visible or\n
if it is not enabled """
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *
driver = webdriver.Chrome(".\chromedriver")

class element_enabled(visibility_of_element_located):
    def __call__(self, locat_):
        displayed = super().__call__(locat_)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False
def wait(func):
    def wrapper(*args, **kwargs): #---> args----> (("class name","ico-register"),)
        locat_ = args[0]
        wait = WebDriverWait(driver,50)
        # v = visibility_of_element_located(locat_)
        v =element_enabled(locat_)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper
@wait
def click_element(locator):
    driver.find_element(*locator).click()
@wait
def enter_text(locator, value):
    driver.find_element(*locator).send_keys(value)

@wait
def select_item(*locator, selecting_element):
    element_ = driver.find_element(*locator)
    s = Select(element_)
    if isinstance(selecting_element, str):
        s.select_by_visible_text(selecting_element)
    elif isinstance(selecting_element, int):
        s.select_by_index(selecting_element)
    else:
        raise TypeError

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


"""final main frame work example"""
"""here we are importing a class By if you dont know exact locator name the we use By class"""
"""syntax: By.locator name"""



from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *







from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
driver = webdriver.Chrome(".\chromedriver")
class element_enable_check(visibility_of_element_located):
    def __call__(self, locat_):
        displayed = super().__call__(locat_)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False


def wait(func):
    def wrapper(*args, **kwargs):
        locat_ = args[0]
        wait = WebDriverWait(driver, 50)
        v = element_enable_check(locat_)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper

@wait
def click_elemet(locat_): #locat_ ---> ("xpath","//span[text()='Sign in']")
    driver.find_element(*locat_).click() #*locat_--->"xpath","//span[text()='Sign in']"
    #driver.find_element("xpath","//span[text()='Sign in']").click()

@wait
def enter_text(locat_, value):
    driver.find_element(*locat_).send_keys(value)
@wait
def select(locat_, selecting_item):
    web_element = driver.find_element(*locat_)
    s = Select(web_element)
    if isinstance(selecting_item, str):
        s.select_by_visible_text(selecting_item)
    elif isinstance(selecting_item, int):
        s.select_by_index(selecting_item)
    else:
        raise TypeError


def selec_check_boxes(list_names):
    for check_box_name in list_names:
        xpath_ = f"//td[text()='{check_box_name}']/..//input[@type='checkbox']"
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(xpath_).click()


def select_item_list_box_dropdown(selecting_item):
    s = Select(driver.find_element(By.XPATH, "//td//select[@id='multiple_cars']"))
    s.select_by_visible_text(selecting_item)

@wait
def mouse_moove_to_element(locator):
    actions = ActionChains(driver)
    web_element = driver.find_element(*locator)
    actions.move_to_element(web_element).perform()
driver.get("https://www.amazon.in/")
driver.maximize_window()
mouse_moove_to_element((By.XPATH,"//a[@id='nav-link-accountList']"))
click_elemet(("xpath","//span[text()='Sign in']"))

