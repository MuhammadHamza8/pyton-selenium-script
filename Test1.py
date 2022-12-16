from selenium import webdriver
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path='File_path/chromedriver.exe');
#url launch
driver.get("https://www.tutorialspoint.com/questions/index.php")
#get page title
print('Page title:' + driver.title)
#quit browser
driver.quit()
