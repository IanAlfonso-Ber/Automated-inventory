import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.set_window_position(-1000, 0)

driver.maximize_window()
driver.get("https://www.google.com")
wait = WebDriverWait(driver, 10)
accept_button = wait.until(EC.element_to_be_clickable((By.ID, 'L2AGLb')))
accept_button.click()
print("accept button pressed")


search_box = driver.find_element(By.ID , 'APjFqb')
print(search_box)

search_box.send_keys("Software Engineer")
search_box.send_keys(Keys.ENTER)
print("Information searched")



input()

driver.quit()



