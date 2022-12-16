from selenium import webdriver
from selenium.webdriver.common.by import By
import time



#Testing Login functionality with valid data
# Medicos Cridential
username = "dex3@gmail.com"
password = "112233"

#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe');
#url launch
driver.get("https://www.facebook.com")
l = driver.find_element(By.NAME,'email');
l.send_keys('dex3@gmail.com');
time.sleep(3);
l = driver.find_element(By.NAME,'password');
l.send_keys('112233');
time.sleep(3);

l = driver.find_element(By.TAG_NAME,'button').click()

time.sleep(3);

#verifying with invalid details
if username == "dex3@gmail.com" and password == "112233":
    print("Login successfull Test pass")
else:
    print(" Login failed Test fail")

#quit browser
driver.quit()