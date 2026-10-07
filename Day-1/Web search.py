
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.bing.com/")
time.sleep(3)
search = driver.find_element(By.NAME, "q")
print("Search displayed:", search.is_displayed())
print("Search enabled:", search.is_enabled())
search.click()
search.send_keys("Grill Chicken Recipe")

search.send_keys(Keys.ENTER)

time.sleep(10)
input("Press Enter to close the browser...")  
driver.quit() 
