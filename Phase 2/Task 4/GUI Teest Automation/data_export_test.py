import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:32768/") 

email_field = driver.find_element_by_id("email") 
password_field = driver.find_element_by_id("password")  
login_button = driver.find_element_by_id("login-button")  

email_field.send_keys("f219658@cfd.nu.edu.pk")
password_field.send_keys("f219658")

login_button.click()

time.sleep(2)

dashboard_link = driver.find_element_by_link_text("Dashboard")  
dashboard_link.click()

time.sleep(2)

export_button = driver.find_element_by_id("export-button")  

export_button.click()

time.sleep(5)

driver.quit()
