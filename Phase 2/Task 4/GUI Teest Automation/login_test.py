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

current_url = driver.current_url
if current_url == "http://localhost:32768/dashboard": 
    print("Login successful - Redirected to the dashboard")
else:
    print("Login failed - Not redirected to the dashboard")

# Close the browser
driver.quit()
