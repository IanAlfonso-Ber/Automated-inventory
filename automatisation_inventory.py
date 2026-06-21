import os
import random
import re
import time

import pandas as pd
import wait
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def load_inventory(file_path):
    # 1. load the data from a CSV file\
    """LOAD INVENTORY"""
    try:
        data = pd.read_csv(file_path)
        print("inventory loaded successfully")
        print('columns found in csv:', data.columns.tolist())
        return data
    except FileNotFoundError:
        print("file not found or corrupted")
        return None
def check_low_stock(df,driver, wait):
            """Filters and prints items that are low stock"""
            low_stock_items = df[df['Quantity'] < df['Threshold']]
            all_scraped_data = []
            if not low_stock_items.empty:
                print("---- RESTOCK NEEDED-----")
                # .iterrows() allows us to loop through the filtered results
                for index, row in low_stock_items.iterrows():
                    item = row['Item_Name']
                    try:
                        print(f"Searching for: {row['Item_Name']}")
                        search_box = wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
                        search_box.clear()
                        for char in row['Item_Name']:
                            search_box.send_keys(char)
                            time.sleep(random.uniform(0.1,0.2))
                        search_box.send_keys(Keys.ENTER)
                        time.sleep(random.uniform(4,5))
                        results_list = wait.until(EC.presence_of_element_located((By.ID, "search")))
                        Produkte_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Produkte')]")))
                        Produkte_box.click()
                        time.sleep(random.uniform(4, 5))
                        print(f"Results loaded for: {row['Item_Name']}")
                        print("SEARCH MADE")
                    except:
                        print("CAPTCHA detected or search failed!")
                        input("Solve the CAPTCHA manually, then press ENTER in the terminal to continue...")
                        print('Resyncing')
                        Produkte_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Produkte')]")))
                        Produkte_box.click()
                    time.sleep(2)
                    data = extract_product_data(driver, item)
                    all_scraped_data.append(data)
                else:
                    print(" inventory levels are fine No restock needed")
            return pd.concat(all_scraped_data, ignore_index=True)



def extract_product_data(driver, item_name):
    product_list = []
    cards = driver.find_elements(By.CLASS_NAME, 'pla-unit-container')
    for card in cards[:20]:
        try:
            raw_price = card.find_element(By.CSS_SELECTOR, 'span.VbBaOe').text
            clean_price = re.sub(r'[^\d,.]', '', raw_price)
        except:
            clean_price = "0"
        try:
            shopname = card.find_element(By.CSS_SELECTOR, "div[aria-label^='Von']").text
        except:
            shopname = "no shopname"
        product_list.append({'Item_Name': item_name, 'shop': shopname, 'price': clean_price})
    return pd.DataFrame(product_list)



if __name__=="__main__":
    file_name = 'inventory.csv'
    df = load_inventory(file_name)
    if df is not None:
        driver = webdriver.Firefox()
        driver.get("https://google.com")
        driver.set_window_position(-1000, 0)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        accept_button = wait.until(EC.element_to_be_clickable((By.ID, 'L2AGLb')))
        accept_button.click()
        print("accept button pressed")

        combined_data = check_low_stock(df,driver, wait)

        combined_data.to_csv('combined_data.csv', index=False, sep=';')
        os.startfile('combined_data.csv')
        user_decision = input("Keep this file (y/n)? ")
        if user_decision == "n":
            try:
                os.remove('combined_data.csv')
                print("file removed")
            except PermissionError:
                print("Could not delete file because it is still open in Excel. Please close it manually.")

        else:
            print("file not removed")
        input('END OF PROGRAM PRESS ENTER TO EXIT')

        driver.close()










