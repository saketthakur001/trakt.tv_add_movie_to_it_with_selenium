
# USING SELENIUM VERSION 4

# Import the selenium webdriver module
from selenium import webdriver
# import the ChromeOptions class
from selenium.webdriver.chrome.options import Options as chromeOptions
# Import the By class for locating elements
from selenium.webdriver.common.by import By
# Import the NoSuchElementException class
from selenium.common.exceptions import NoSuchElementException
# Import the WebDriverWait class
from selenium.webdriver.support.ui import WebDriverWait
# Import the expected_conditions module
from selenium.webdriver.support import expected_conditions as EC

import re

# time
import time

# Create a ChromeOptions object
options = webdriver.ChromeOptions()

# Use the default profile name in the user-data-dir argument
# options.add_argument("--user-data-dir=C:\\Users\\saket\\AppData\\Local\\Google\\Chrome\\User Data")

options.add_argument("--user-data-dir=C:\\Temp\\ChromeProfile")

# Create a webdriver object for chrome with the options
driver = webdriver.Chrome(options=options)

# Open the google.com website
# driver.get("https://trakt.tv/dashboard")


''' GOOGLE SEARCH AND CLICKING ON THE FIRST LINK '''

# Assuming the search text is a string
def generate_google_link(search_text):
  # Replace spaces with plus signs
  search_text = search_text.replace(" ", "+")
  # Add the search text to the base url
  base_url = "https://www.google.com/search?q="
  link = base_url + search_text
  # Return the link
  return link

def find_elements_by_class_name(driver, class_name):
    """Finds all elements with class `class_name`."""
    return driver.find_elements(by=By.CLASS_NAME, value=class_name)

def click_first_link(driver):
  """Clicks on the first link element on the page."""
  # Wait for the page to load and the element to be present
  driver.implicitly_wait(1)
  
  # Use a try-except block to handle possible exceptions
  try:
    # Get the first element from the list of elements with class name "yuRUbf"
    first_div = find_elements_by_class_name(driver, "yuRUbf")[0]
    # Find the child element of the div that has the tag name "a" using the find_element method
    first_link = first_div.find_element(By.TAG_NAME, "a")
    # Execute a script to change the target attribute of the link to "_self"
    driver.execute_script("arguments[0].setAttribute('target', '_self')", first_link)
    first_link.click()
    return True
  except IndexError:
    # If no element is found, return False
    return False


def click_element(element):
    element.click()
    print(f"Successfully clicked element using {element.description}")


# Define a function to click on the element using a given locator
def click_heart(driver, value, locator):
  """Clicks on the heart based on a given value and a locator."""
  # Check if the value is between 1 and 10
  if not 1 <= value <= 10:
    raise ValueError("Value must be between 1 and 10")
  # Use a try-except-else-finally block to handle possible exceptions
  try:
    # Choose different locators based on the locator parameter
    if locator == "id":
      # Find and click the element by id using the value parameter
      element = driver.find_element(By.ID, f"rating-{value}-1688233989567")
    elif locator == "xpath":
      # Find and click the element by xpath using the value parameter
      element = driver.find_element(By.XPATH, f"//input[@name='rating' and @value='{value}']")
    elif locator == "css selector":
      # Find and click the element by css selector using the value parameter
      element = driver.find_element(By.CSS_SELECTOR, f"input[name='rating'][value='{value}']")
    elif locator == "link text":
      # Find and click the element by link text using the value parameter
      element = driver.find_element(By.LINK_TEXT, f"{value} hearts")
    elif locator == "partial link text":
      # Find and click the element by partial link text using the value parameter
      element = driver.find_element(By.PARTIAL_LINK_TEXT, f"{value} hearts")
    elif locator == "class name":
      # Find and click the element by class name using the value parameter
      element = driver.find_element(By.CLASS_NAME, f"rating-{value}")
    else:
      # Raise an exception if the locator is not valid
      raise ValueError("Locator must be one of: id, xpath, css selector, link text, partial link text, class name")

    # Click on the element
    element.click()
  except NoSuchElementException:
    # Handle the case when the element is not found
    print(f"Element not found by {locator}")
  else:
    # Handle the case when the element is clicked successfully
    print(f"Element clicked by {locator}")
  finally:
    # Execute some code regardless of the outcome
    print(f"Finished trying to click by {locator}")
  
  return True

 
# Assuming the file name is movies.csv
import pandas as pd
# time.sleep(1000)
df = pd.read_csv(r"C:\Users\saket\Downloads\movielens-ratings.csv")

for idx, title in enumerate(df['title'][79:]):
    title = title.replace("'", '-').replace('.', '-')
    print(title)
    
    formatted_title = re.sub(r'[^\w\s.-]', '', title).strip().lower().replace(' ', '-').replace('--', '-')
    
    url = f"https://trakt.tv/movies/{formatted_title}"
    print(url)

    print("Index:", idx)
    print("-------------------------")
    driver.get(url)

    # Find the element by its text content using XPath
    try:
        element = driver.find_element(By.XPATH, "//div[contains(text(), 'Add to history')]")
        # Click on the element
        element.click()
        print('added a new movie', df.index)
    except NoSuchElementException:
    # If the element is not found, pass
        pass
        # print('sleeping')
        # time.sleep(10)


# Get the title of the page
print(driver.title)

# time.sleep(60000)

# Close the driver
driver.close()
