from selenium import webdriver
from pytest import fixture
@fixture
def _driver():
    driver = webdriver.Chrome(r"./chromedriver.exe")
    driver.get("httP://demowebshop.tricentis.com")
    driver.maximize_window()
    yield driver
    driver.quit()
