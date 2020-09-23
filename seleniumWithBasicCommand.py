from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# creating driver object in different browser

driver = webdriver.Chrome(executable_path = "C:\\Web Driver\\chromedriver.exe") # Creating the driver object of chrome
# driver = webdriver.Firefox(executable_path = "Path of the firefox web driver")
# driver = webdriver.Ie(executable_path = "Path of the Inetrnet explorer web driver")


driver.get("https://imerit.net/careers") # calling the get() method to open a url into browser

# ------------------------- Basic web driver command -----------------------------------------------------

titleOfThePage = driver.title  # Title of the page
currentURL = driver.current_url # Current URL of the page
pageSourse = driver.page_source # It will fetch the HTML code of that particular page
print("titleOfThePage : ",titleOfThePage)
print("currentURL : ", currentURL)
print("pagesource : ", pageSourse)


time.sleep(5)
driver.close() # Close() funtion only close one browser at a time
driver.quit() # quite() fuction close all the browsers
