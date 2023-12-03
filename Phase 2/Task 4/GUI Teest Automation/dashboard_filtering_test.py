import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
time.sleep(2)
date_filter = driver.find_element_by_id("date-filter")  
category_filter = driver.find_element_by_id("category-filter")  

date_filter.send_keys("01/01/2023 - 12/31/2023") 
date_filter.send_keys(Keys.RETURN)

from selenium.webdriver.support.ui import Select

category_dropdown = Select(driver.find_element_by_id("category-dropdown"))
category_dropdown.select_by_visible_text("Your Category")  

time.sleep(2)

driver.quit()
