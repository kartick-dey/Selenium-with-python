from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\\Web Driver\\chromedriver.exe")
driver.get("https://imerit.net/careers")
print("First page title : ", driver.title)
time.sleep(5)
driver.get("https://imerit.net/contact-us/?utm_campaign=brand&utm_medium=home&utm_source=organic&utm_content=contact")
print("Second pahe title : ", driver.title)
time.sleep(5)

driver.back() # back to first page
print("Previous page title : ", driver.title)
time.sleep(5)

driver.forward() # forward to 2nd page
print("Forward page title : ", driver.title)
time.sleep(5)

driver.close()
