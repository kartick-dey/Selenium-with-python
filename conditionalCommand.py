from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\\Web Driver\\chromedriver.exe")
driver.get("https://imerit.net/contact-us/?utm_campaign=brand&utm_medium=home&utm_source=organic&utm_content=contact")

element = driver.find_element_by_name("first_name")


# Both can be used in any HTML element to check status of that element
print(element.is_displayed())
print(element.is_enabled())

# is.selected() is used for checkbox and radio button to check it status and some time it is used for drop downn box as well.
