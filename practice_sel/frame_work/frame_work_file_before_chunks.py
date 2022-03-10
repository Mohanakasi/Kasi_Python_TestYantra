from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
driver = webdriver.Chrome(".\chromedriver")
driver.get("https://www.amazon.in/")
class element_enable_check(visibility_of_element_located):
    def __call__(self, locat_):
        displayed = super().__call__(locat_)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False


def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locat_ = args[1]
        wait = WebDriverWait(instance.driver, 50)
        v = element_enable_check(locat_)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper

class selenium_wrapper:
    def __init__(self,driver):
        self.driver = driver

    @wait
    def click_elemet(self,locat_): #locat_ ---> ("xpath","//span[text()='Sign in']")
        self.driver.find_element(*locat_).click() #*locat_--->"xpath","//span[text()='Sign in']"
        #driver.find_element("xpath","//span[text()='Sign in']").click()

    @wait
    def enter_text(self,locat_, value):
        self.driver.find_element(*locat_).send_keys(value)
    @wait
    def select(self,locat_, selecting_item):
        web_element = self.driver.find_element(*locat_)
        s = Select(web_element)
        if isinstance(selecting_item, str):
            s.select_by_visible_text(selecting_item)
        elif isinstance(selecting_item, int):
            s.select_by_index(selecting_item)
        else:
            raise TypeError


    def selec_check_boxes(self,list_names):
        for check_box_name in list_names:
            xpath_ = f"//td[text()='{check_box_name}']/..//input[@type='checkbox']"
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(xpath_).click()


    def select_item_list_box_dropdown(self,locator,selecting_item):
        s = Select(self.driver.find_element(*locator))
        s.select_by_visible_text(selecting_item)

    @wait
    def mouse_moove_to_element(self,locator):
        actions = ActionChains(self.driver)
        web_element = self.driver.find_element(*locator)
        actions.move_to_element(web_element).perform()

s = selenium_wrapper(driver)
s.mouse_moove_to_element((By.XPATH,"//a[@id='nav-link-accountList']"))
s.click_elemet((By.XPATH,"//span[text()='Sign in']"))