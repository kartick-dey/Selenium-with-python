from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\\Web Driver\\chromedriver.exe")
driver.implicit_wait(5) #
