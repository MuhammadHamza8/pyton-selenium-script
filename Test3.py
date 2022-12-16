from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe');
#url launch
driver.get("https://www.tutorialspoint.com/index.htm")
#identify edit box with name
l = driver.find_element(By.NAME,'key')

#input text
l.send_keys('Selenium Java')
time.sleep(5);
#obtain value entered
v = l.get_attribute('value')
print('Value entered: ' + v)
#driver close
driver.close()