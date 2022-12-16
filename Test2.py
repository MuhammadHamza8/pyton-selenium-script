from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe');
#url launch
driver.get("https://www.tutorialspoint.com/index.htm")
#identify edit box with id
l = driver.find_element(By.ID,"search-strings");

#input text
l.send_keys('Selenium')
time.sleep(3);
#obtain value entered
v = l.get_attribute('value')
print('Value entered: ' + v)


#driver quit
driver.quit();