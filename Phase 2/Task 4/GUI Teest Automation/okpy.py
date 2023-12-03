from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def find_new_movies(query):
    # Set up the WebDriver
    driver = webdriver.Chrome()  # Make sure to replace with the path to your ChromeDriver executable if needed

    try:
        # Navigate to Google
        driver.get("https://www.google.com")

        # Find the search box and input the query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Click on the "Videos" tab to filter results to videos
        videos_tab = driver.find_element(By.XPATH, '//a[text()="Videos"]')
        videos_tab.click()

        # Find and print the titles of the videos (movies)
        video_titles = driver.find_elements(By.XPATH, '//h3[@class="LC20lb DKV0Md"]/span')
        for title in video_titles:
            print(title.text)

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    query = "new movies 2023"
    find_new_movies(query)
