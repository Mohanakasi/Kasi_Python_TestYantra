from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('./Chromedriver')
# driver.get("http://demowebshop.tricentis.com/")
# sleep(5)
# """registration"""
# driver.find_element_by_link_text("Register").click()
3# sleep(2)
# driver.find_element_by_id("gender-male").click()
# sleep(2)
# driver.find_element_by_css_selector("input[id='FirstName']").send_keys("kasi")
# sleep(2)
# driver.find_element_by_id("LastName").send_keys("s")
# sleep(2)
# driver.find_element_by_xpath("//input[@id='Email']").send_keys("kas@gh.com")
# sleep(2)
# driver.find_element_by_css_selector("input[id='Password']").send_keys("Kasi18")
# sleep(2)
# driver.find_element_by_id("ConfirmPassword").send_keys("Kasi18")
# sleep(2)
# driver.find_element_by_name("register-button").click()
# sleep(2)
# driver.find_element_by_xpath("//input[@class='button-1 register-continue-button']").click()

"""login"""
# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
# driver.find_element_by_link_text("Log in").click()
# sleep(2)
# driver.find_element_by_css_selector("input[id='Email']").send_keys("kas@gh.com")
# sleep(2)
# driver.find_element_by_id("Password").send_keys("Kasi18")
# sleep(2)
# driver.find_element_by_css_selector("input[id='RememberMe']").click()
# sleep(2)
# driver.find_element_by_css_selector("input[class='button-1 login-button']").click()

"""adding single item to cart"""
# driver.find_element_by_css_selector("a[href='/books']").click()
# sleep(5)
# driver.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@type='button']").click()
# sleep(4)
# driver.find_element_by_link_text("Shopping cart").click()
# sleep(4)
# driver.find_element_by_id("termsofservice").click()
# sleep(4)
# driver.find_element_by_id("checkout").click()
# sleep(4)
# s = Select(driver.find_element_by_id("BillingNewAddress_CountryId"))
# sleep(8)
# s.select_by_visible_text("India")
# sleep(2)
# driver.find_element_by_id("BillingNewAddress_City").send_keys("guntur")
# sleep(2)
# driver.find_element_by_id('BillingNewAddress_Address1').send_keys("guntur")
# sleep(2)
# driver.find_element_by_id('BillingNewAddress_ZipPostalCode').send_keys(522003)
# sleep(2)
# driver.find_element_by_id('BillingNewAddress_PhoneNumber').send_keys(8886213059)
# sleep(2)
# driver.find_element_by_xpath("//input[@title='Continue']").click()
# sleep(2)
# driver.find_element_by_xpath("//p[@class='back-link']/..//input[@class='button-1 new-address-next-step-button']").click()
# sleep(2)
# driver.find_element_by_id("shippingoption_2").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='shipping-method-buttons-container']//input[@class='button-1 shipping-method-next-step-button']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='payment-method-buttons-container']//input[@class='button-1 payment-method-next-step-button']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='payment-info-buttons-container']//input[@class='button-1 payment-info-next-step-button']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='confirm-order-buttons-container']//input[@class='button-1 confirm-order-next-step-button']").click()
# sleep(2)
# driver.find_element_by_link_text("Click here for order details.").click()

"""adding multiple items into cart at a time"""
# driver.find_element_by_css_selector("a[href='/books']").click()
# sleep(5)
# list_items = ['Computing and Internet','Fiction','Health Book']
# for item in list_items:
#     x_path = f"//a[text()='{item}'] /../..// input[@class ='button-2 product-box-add-to-cart-button']"
#     driver.find_element_by_xpath(x_path).click()
#     sleep(4)
# driver.find_element_by_link_text("Shopping cart").click()
# sleep(4)
# driver.find_element_by_id("termsofservice").click()
# sleep(4)
# driver.find_element_by_id("checkout").click()
# sleep(4)
# driver.find_element_by_xpath("//div[@id='billing-buttons-container']//input[@class='button-1 new-address-next-step-button']").click()
# sleep(4)
# driver.find_element_by_xpath("//div[@id='shipping-buttons-container']//input[@class='button-1 new-address-next-step-button']").click()
# sleep(4)
# driver.find_element_by_xpath("//div[@id='shipping-method-buttons-container']//input[@class='button-1 shipping-method-next-step-button']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='payment-method-buttons-container']//input[@class='button-1 payment-method-next-step-button']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='payment-info-buttons-container']//input[@class='button-1 payment-info-next-step-button']").click()
# sleep(2)
# driver.find_element_by_xpath("//div[@id='confirm-order-buttons-container']//input[@class='button-1 confirm-order-next-step-button']").click()
# sleep(2)
# driver.find_element_by_link_text("Click here for order details.").click()


# driver.get("https://www.goibibo.com/")
# driver.find_element_by_xpath("//p[@cLASS='sc-dJjYzT cjzxWN fswWidgetTitle']").click()
# month = 'March 2023'
# day = "18"
# i = 1
# while i > 0 :
#     try:
#         sleep(1)
#         driver.find_element_by_xpath(f"//div[text()='{month}']/../..//p[text()='{day}']").click()
#         break
#     except :
#         sleep(1)
#         driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
# s = 'kasi'
# for index in range(len(s)-1,-1,-1):
#     print(s[index])
# print(list(range(3,-1)))