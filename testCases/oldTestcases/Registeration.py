from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/")

# LINK TEXT, ID, NAME, CLASS NAME, XPATH, CSS

# Click on Register button on homepage
# LINK_TEXT
driver.find_element(By.LINK_TEXT, "Register").click()

# Enter Name
# ID
driver.find_element(By.ID, "name").send_keys("Test User")

# Enter Email
# NAME
driver.find_element(By.NAME, "email").send_keys("test1@credence.in")

# Enter Password
# ID
driver.find_element(By.ID, "password").send_keys("test@123")

# Enter Confirm Password
# ID
driver.find_element(By.ID, "password-confirm").send_keys("test@123")

# Click on Register Button
# CLASS NAME
driver.find_element(By.CLASS_NAME, "btn").click()
try:
    driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    print("Login Test Case is Passed")
except NoSuchElementException:
    print("Login Test Case is Failed")