from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
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