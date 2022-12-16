from selenium import webdriver
from selenium.webdriver.common.by import By
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe');

#url launch
driver.get("https://www.tutorialspoint.com/index.htm")
#identify edit box with tagname
l = driver.find_element(By.TAG_NAME,'input')
#input text
l.send_keys('Selenium Python')
#obtain value entered
v = l.get_attribute('value')
print('Value entered: ' + v)
#driver close
driver.close();