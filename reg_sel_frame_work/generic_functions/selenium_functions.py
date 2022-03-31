from selenium.webdriver.support.select import Select
from reg_sel_frame_work.generic_functions.wat_deco import wait
class selenium_wrapper:
    def __init__(self,driver):
        self.driver = driver
    @wait #click_element = wait(click_element) #click_element becomes wrapper
    def click_element(self,locator):  #locator--->("class name","ico-register")
        self.driver.find_element(*locator).click() #---> *locator---> "class name","ico-register"
    @wait
    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)
    @wait
    def select_items(self,locator,value):
        web_el = self.driver.find_element(*locator)
        s = Select(web_el)
        if isinstance(value, str):
            s.select_by_visible_text(value)
        elif isinstance(value, int):
            s.select_by_index(value)
        else:
            raise TypeError