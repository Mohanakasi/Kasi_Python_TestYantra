from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver = webdriver.Chrome(".\chromedriver")
# # driver.get("http://demowebshop.tricentis.com/")
# # actions = ActionChains(driver)
# # sleep(5)
# # sleep(8)
# # computers_link = driver.find_element_by_xpath("//a[contains(text(),'Computers')]")
# # sleep(5)
# # actions.move_to_element(computers_link).perform()
# # sleep(5)
# # # actions.click(computers_link).perform()
# # accesories_page = driver.find_element_by_xpath("//a[contains(text(),'Accessories')]")
# # sleep(3)
# # actions.move_to_element(accesories_page).perform()
# # sleep(3)
# # actions.click(driver.find_element_by_xpath("//a[contains(text(),'Accessories')]")).perform()
# # sleep(5)
# # actions = ActionChains(driver)
# # actions.send_keys(Keys.PAGE_DOWN)
# # item = driver.find_element_by_xpath("//a[text()='TCP Self-Paced Training additional month']/../..//input[@type='button']")
# # item.click()
#
#
#
#
# # categi = driver.find_element_by_xpath("//strong[text()='Categories']")
# # actions.double_click(categi).perform()
# # actions.send_keys(Keys.PAGE_DOWN).perform()
# # actions.send_keys(Keys.ARROW_UP).perform()
# # actions.send_keys(Keys.PAGE_DOWN).perform()
# # element = driver.find_element_by_xpath("//a[text()='Register']")
# # actions.context_click(element).perform()
# actions1 = ActionChains(driver)
# driver.get("https://www.mastersindia.co/")
# driver.maximize_window()
# sleep(5)
# wait = WebDriverWait(driver,100)
# v = visibility_of_element_located((By.XPATH,"//jdiv[@class='closeIcon_a2b2']"))
# wait.until(v)
# driver.find_element_by_xpath("//div[@class='sp-prompt-buttons']//button[@class='sp-prompt-btn sp-disallow-btn']").click()
# driver.find_element_by_xpath("//jdiv[@class='closeIcon_a2b2']").click()
# sleep(5)
# gst_ = driver.find_element_by_xpath("//li[@class='dropdown']//a[contains(text(),'GST')]")
# actions1.move_to_element(gst_).perform()
# sleep(5)
# gst_se_api = driver.find_element_by_xpath("//span[contains(text(),'GST Search API ')]")
# sleep(5)
# actions1.click(gst_se_api).perform()
# # wind_id = driver.window_handles
# # print(wind_id)
# # driver.switch_to.window(wind_id[-1])
# # driver.get("https://www.mastersindia.co/gst-number-verification-api-bulk-utility/")
# actions2 = ActionChains(driver)
# # driver.find_element_by_xpath("//span[text()='Get API Details']").click()
# actions2.move_to_element(driver.find_element_by_xpath("//span[text()='Get API Details']")).perform()
# actions2.click(driver.find_element_by_xpath("//span[text()='Get API Details']")).perform()
# sleep(5)
# driver.find_element_by_id("partnerName").send_keys("abc")
# driver.find_element_by_id("partnerPhoneNumber").send_keys("1234567894")
# driver.find_element_by_id("partnerEmail").send_keys("abc@gmail.com")
# driver.find_element_by_id("partnerCompanyName").send_keys("xyzcompany")
# driver.find_element_by_id("partnerDesignation").send_keys("no role")
# driver.find_element_by_xpath("//button[text()='Submit']").click()
# driver.get("http://demowebshop.tricentis.com/")
# wait = WebDriverWait(driver,30)
# v = visibility_of_element_located(("id","small-searchterms"))
# wait.until(v)
# actions1 = ActionChains(driver)
# search_box_el = driver.find_element_by_id("small-searchterms")
# actions1.click(search_box_el).perform()
# actions1.click(driver.find_element_by_xpath("//input[@class='button-1 search-box-button']")).perform()
# driver.switch_to.alert.accept()
# driver.find_element_by_id("small-searchterms").click()
# driver.find_element_by_xpath("//input[@class='button-1 search-box-button']").click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()

# driver.get("https://crossbrowsertesting.github.io/drag-and-drop")
# source_web_el = driver.find_element(By.XPATH,"//div//p[text()='Drag me to my target']")
# desti_ele = driver.find_element(By.ID,"droppable")
# mouse_action1 = ActionChains(driver)
# mouse_action1.drag_and_drop(source_web_el,desti_ele).perform()
# dest_2 = driver.find_element(By.XPATH,"//html[@lang='en']")
# mouse_action1.drag_and_drop(source_web_el,dest_2)
# mouse_action1.context_click()
# mouse_action1.send_keys(Keys.ENTER)

# driver.get("https://www.google.com/")
# search_box = driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']")
# search_box.send_keys("book a ticket for chandana alias pichhi from bangalore to mysore")
# search_box.send_keys(Keys.CANCEL)
# # search_box.send_keys(Keys.ENTER)
# driver.get("file:///C:/Users/Hp/Downloads/demo.html")
# from selenium.webdriver.support.select import Select
# list_box = driver.find_element(By.ID,"multiple_cars")
# s = Select(list_box)
# s.select_by_visible_text("Land Rover")
# s.select_by_visible_text("Mercedes")
# s.select_by_visible_text("Nissan")
# print(s.options)
# res = [item.text for item in s.options]
# print(*res)
# print(s.first_selected_option.text)
# s.deselect_all()
# print(s.first_selected_option)


driver.get("file:///C:/Users/Hp/Downloads/demo.html")
driver.find_element_by_id("resume").send_keys(r"C:\Users\Hp\Downloads\kasi_cv_final.pdf")
driver.find_element_by_id("u_b_b_/2").send_keys("hello")