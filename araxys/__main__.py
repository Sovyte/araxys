import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def google_search(query):
    # Set up the Chrome driver
    driver = webdriver.Chrome()
    
    # Go to Google
    driver.get("https://www.google.com")
    
    # Enter the search query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    
    # Submit the search
    search_box.submit()
    
    # Wait for the results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rso")))
    
    # Get the top result
    top_result = driver.find_element(By.ID, "rso").find_element(By.XPATH, ".//div[@class='yuRUbf']/a")
    
    # Print the top result
    print(top_result.text)
    
    # Close the browser
    driver.quit()

# Ask for the search query
query = input("Enter a search query: ")

# Search for the query
google_search(query)
