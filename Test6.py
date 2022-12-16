from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe');
driver.maximize_window()
#url launch
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")

#identify link with link text
l = driver.find_element(By.LINK_TEXT,'Privacy Policy')
time.sleep(3);
#perform click
l.click()
print('Page navigated after click: '+ driver.title)
#driver quit
driver.quit()
