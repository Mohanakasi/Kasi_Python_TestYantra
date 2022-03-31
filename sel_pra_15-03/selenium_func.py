from selenium.webdriver.support.select import Select
class Selenium_functions:
    def __init__(self, driver):
        self.driver = driver
    @wait
    def click_element(locator):
        self.driver.find_element(*locator).click()
    @wait
    def enter_text(locator, value):
        self.driver.find_element(*locator).send_keys(value)

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
