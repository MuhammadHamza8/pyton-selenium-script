from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe')
#url launch
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#identify edit box with class
l = driver.find_element(By.CLASS_NAME,'heading')
#identify text
v = l.text
#text obtained
print('Text is: ' + v)
#driver close
driver.close()
