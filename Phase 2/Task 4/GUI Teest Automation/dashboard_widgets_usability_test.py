import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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

widget1 = driver.find_element_by_id("widget1")  
widget2 = driver.find_element_by_id("widget2")  

widget1.click()

hover = ActionChains(driver)
hover.move_to_element(widget2).perform()

time.sleep(2)

driver.quit()
