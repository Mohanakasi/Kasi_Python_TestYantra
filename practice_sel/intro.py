# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome(".\Chromedriver") # opens the browser  # "./" means current class
# # driver.get("httP://demowebshop.tricentis.com") # opens the particular url
# # url = driver.current_url
# # title = driver.title
# # print(url) # prints url of current website
# # print(title) # prints title of the website
# # sleep(10)
# # driver.minimize_window()
# # sleep(10)
# # driver.maximize_window()
# # sleep(10)
# # driver.close()
#
#
# # driver = webdriver.Chrome(".\Chromedriver") # opens the browser  # "./" means current class
# # driver.get("httP://demowebshop.tricentis.com")
# # driver.find_element_by_class_name("ico-register").click()
# # driver.find_element_by_id("gender-male").click()
# # driver.find_element_by_id("gender-female").click()
# # driver.find_element_by_id("FirstName").send_keys("mohana kasi")
# # driver.find_element_by_id("LastName").send_keys("settipalli")
# # driver.find_element_by_class_name("text-box single-line").send_keys("kasi88@k18.com")
# # driver.find_element_by_id("Password").send_keys("Mohana1995")
# # driver.find_element_by_id("ConfirmPassword").send_keys("Mohana1995")
# # driver.find_element_by_id("register-button").click()
# # # driver.find_element_by_css_selector("input[value='Continue']").click()
# # driver.find_element_by_class_name("button-1 register-continue-button").click()
#
# # """any desk download"""
# # driver.get("https://anydesk.com/en")
# # driver.find_element_by_css_selector("p[class='mb-0 d-inline-block']").click()
#
#
# """xpath"""
# """xpath is to locate web element by a html path"""
# """css selecter is more faster then x path"""
# """syntax: //htamltag[@atribute = 'value']"""
# """for text---> //htmltag[text()='value']"""
# # driver.get("httP://demowebshop.tricentis.com")
# # driver.find_element_by_xpath("//a[@class='ico-register']").click() #xpath
# # file:///C:/Users/Hp/Downloads/demo.html
# # driver.get("file:///C:/Users/Hp/Downloads/demo.html")
# # driver.find_element_by_xpath("//input[@class='first_row']").send_keys('hello')
# # fnames = driver.find_elements_by_xpath("//input[@class='first_row']")
# # for fname in fnames:
# #     fname.send_keys("hello")
#
#
# """xpath"""
# # driver.get("http://demowebshop.tricentis.com/")
# # driver.find_element_by_xpath("//a[text()='Build your own cheap computer']/../..//input[@type='button']").click()
# # sleep(5)
# # # driver.find_element_by_id("add-to-cart-button-72").click() # using id
# # # driver.find_element_by_xpath("//[@class='add-to-cart']/../../..//input[@class='qty-input valid']").send_keys(10)
# # driver.find_element_by_xpath("//div[@class='add-to-cart']/../../..//input[@value='Add to cart']").click()
# # driver.find_element_by_xpath("//span[text()='Shopping cart']").click()
# # driver.find_element_by_xpath("//span[@class='cart-label']").click()
#
# # driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
# # import re
# # import csv
# # price_ = driver.find_element_by_xpath("//span[text()='Custom Sunglasses']/../../..//span[@class='art-price']").text
# # print(t)
# """getting only price"""
# """using normal"""
# # for word in t.split():
# #     if word[0].startswith('$'):
# #         print(word[1::])
#
# """using regular exppression"""
# # t = re.findall(r"[\d.]",price_)
# # actual_price_ = float("".join(t))
# # print(actual_price_)
#
#
#
# # """xpath items price validation"""
# # driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
# # import re
# # import csv
# # # price_ = driver.find_element_by_xpath("//span[text()='Custom Sunglasses']/../../..//span[@class='art-price']").text
# #
# #
# # def prices_():
# #     d = {}
# #     with open('items.csv') as csv_file:
# #         read_obj = csv.reader(csv_file)
# #         next(read_obj)
# #         for row in read_obj:
# #             d[row[0]] = row[1]
# #
# #     return d
# # d = prices_()
# # print(d)
# # for glass,expe_price in d.items():
# #     x_path = f"//span[text()='{glass}']/../../..//span[@class='art-price']"
# #     actual_price = driver.find_element_by_xpath(x_path).text
# #     temp = re.findall(r'[\d.]',actual_price)
# #     # print(float("".join(temp)))
# #     # print(float(expe_price))
# #     if float(expe_price) == float("".join(temp)):
# #         print(glass,".....>pass")
# #     else:
# #         print(glass,".....>fail")


"""getting a particular block links in a web page"""
# driver.get("http://demowebshop.tricentis.com/")
# list_ = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# for link in list_:
#     # print(link.text) # prints only link name
#     print(link.get_attribute('href')) # prints all http links
#

"""getting a particular block links in a web page (footer')"""
# driver.get("http://demowebshop.tricentis.com/")
# list_ = driver.find_elements_by_xpath("//div[@class='footer']//a")
# for link in list_:
#     # print(link.text) # prints only link name
#     print(link.get_attribute('href')) # prints all http links

# """example xpath"""
# driver.get("https://www.monsterindia.com/")
# sleep(3)
# driver.find_element_by_id("SE_home_autocomplete").send_keys("Python")
# driver.find_element_by_xpath("//input[@class='btn']/../..//input[@class='btn']").click()

"""checking if in he names coloumn al names are  sorted or not in a table """
# driver.get("file:///C:/Users/Hp/Downloads/demo%20(1).html")
# sleep(3)
# l = driver.find_elements_by_xpath("//table[@name='customers']//td[2]")
# names = []
# for webel in l:
#     names.append(webel.text)
# if sorted(names) == names:
#     print("pass")
# else:
#     print("fail")

# from selenium.webdriver.support.select import Select
# driver.get("file:///C:/Users/Hp/Downloads/demo%20(1).html")

"""selecting element in list box using text"""
# s = Select(driver.find_element_by_id("standard_cars"))
# s.select_by_visible_text("Jaguar")
# sleep(2)
# s.select_by_visible_text("BMW")
"""selecting element in list box using indexing"""


"""fetching all options in list box"""
from selenium.webdriver.support.select import Select
# driver.get("file:///C:/Users/Hp/Downloads/demo%20(1).html")
# s = Select(driver.find_element_by_id("standard_cars"))

# allopt = s.options
# print(allopt) # gives you all options in the form of web elements if you need tex only traverse through for loop
# for option in allopt:
#     print(option.text)


"""checking a particular option is present in the list box or not"""
# from selenium.webdriver.support.select import Select
# car = 'Honda'
# driver.get("file:///C:/Users/Hp/Downloads/demo%20(1).html")
# s = Select(driver.find_element_by_id("standard_cars"))
# allopt = s.options
# text_options = [item.text for item in allopt]
# for index, item in enumerate(text_options):
#     if item == car:
#         print(f"the option {car} is present in side the list box")
#         break
# else:
#     print(f"the option {car} is not present in side the list box")

"""to know the current selected option in a list box"""
# from selenium.webdriver.support.select import Select
# driver.get("file:///C:/Users/Hp/Downloads/demo%20(1).html")
# s = Select(driver.find_element_by_id("standard_cars"))
# s.select_by_visible_text("BMW")
# curre_selection = s.first_selected_option # it returns web element if text needed use .text
# print(curre_selection.text)



"""selecting a option in dropdown box"""
# s = Select(driver.find_element_by_id("multiple_cars"))
# s.select_by_visible_text("Ford")
# s.select_by_visible_text("Toyota")
# current_sel = s.first_selected_option
# print(current_sel.text)

from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.select import Select
# driver.get("file:///C:/Users/Hp/Downloads/demo%20(1).html")
# s = Select(driver.find_element_by_id("multiple_cars"))
# sleep(2)
# s.select_by_visible_text("Jaguar")
# sleep(5)
# s.deselect_by_visible_text("Jaguar")
# sleep(2)
# s.select_by_visible_text("Ford")
# sleep(2)
# s.deselect_by_visible_text("Ford")


"""Select class will work only for list boxes only if you try to pass another web element attribute to Select class it will\n
raise you an error called UN-expected tag name exception"""

"""NOTE:"""
"""when we finding a list box and assign that web element to a variable and using that variable by select class"""
"""when the page is refreshed the id of that particular web element is changes so no longer you cant the same variable for \n
select class usage at that time you will get an error .for that reason after clicking a element in the list box we have \n
to again find the web element and again we have to store it in a variable then we cant get the error"""



# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.we
# driver.get("https://www.goibibo.com/")
# wait = WebDriverWait(driver,360)
# v = expected_conditions.visibility_of_element_located(('xpath',"//a[@href='/hotels/']"))
# wait.until(v)
# driver.find_element_by_xpath("//div[@class='sc-bkkeKt gAqCbJ fswFld ']//p[text()='Enter city or airport']").click()
# driver.find_element_by_xpath("//div[@class='sc-cidDSM dOEpbS']//input[@type='text']").send_keys("gannavram")
# driver.find_element_by_xpath("//div[@class='sc-bkkeKt gAqCbJ fswFld ']//p[text()='Enter city or airport']").click()
# driver.find_element_by_xpath("//div[@class='sc-cidDSM dOEpbS']//input[@type='text']").send_keys("gannavram")
# driver.find_element_by_xpath("//a[@href='/hotels/']").click()
# driver.get("https://www.naukri.com/")
# driver.implicitly_wait(30)
# driver.find_element_by_xpath("//ul[@class='middle-menu menu']//div[text()='Jobs']").click()
"""mouse actions"""
from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://www.naukri.com/")
# driver.implicitly_wait(30)
# actions = ActionChains(driver)
# profile = driver.find_element_by_xpath("//a[@title='Search Jobs']")
# actions.move_to_element(profile).perform()
# driver.find_element_by_xpath("//a[text()='IT jobs']").click()
# empl_ = driver.find_element_by_xpath("//div[text()='For employers']")
# actions.move_to_element(empl_).perform()
# driver.find_element_by_xpath("//a[text()='Buy online']").click()
#
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# option1 = Options()
# option1.add_argument("--disable-notifications")
# driver = webdriver.Chrome(".\chromedriver",options=option1)
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# driver.implicitly_wait(15)
# driver.find_element_by_xpath("//div[@id='corover-close-btn']//img[@style='position: absolute; width: 38px; top: -4px; right: -9px;']").click()
# sleep(5)
# driver.find_element_by_xpath("//div[@class='text-center col-xs-12']//button[@class='btn btn-primary']").click()
# driver.implicitly_wait(10)
# driver.find_element_by_xpath("//p-autocomplete[@id='origin']//input[@type='text']").send_keys("BNC")
# driver.find_element_by_xpath("//span[text()='BENGALURU CANT - BNC']").click()
# driver.find_element_by_xpath("//span[@class='ng-tns-c59-10 ui-calendar']//input[@type='text']").click()
#


# month='March'
# year = '2022'
# day = '20'
# def _date_pick(month, year, day, i=1):
#     while i > 0:
#         try:
#             driver.find_element_by_xpath(f"//span[text()='{month}']")
#             driver.find_element_by_xpath(f"//span[text()='{year}']")
#             driver.find_element_by_xpath(f"//a[text()='{day}']").click()
#             break
#         except NoSuchElementException:
#             driver.find_element_by_xpath("//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c59-10']").click()
#             i += 1
#
# _date_pick(month,year,day)
# driver.find_element_by_xpath("//span[@class='ng-tns-c58-9 ui-autocomplete ui-widget']//input[@type='text']").send_keys("MYS")
# sleep(2)
# driver.find_element_by_xpath("//span[text()='MYSURU JN - MYS']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@class='col-md-3 col-sm-12 col-xs-12 remove-pad']").click()

# driver.get("https://www.facebook.com/")
# driver.implicitly_wait(15)
# driver.find_element_by_xpath("//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@class='_5dbb']//input[@class='inputtext _58mg _5dba _2ph-']").send_keys("Mohana kasi")

