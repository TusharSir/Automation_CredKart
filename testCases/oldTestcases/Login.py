import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://automation.credence.in/")
# Click Login button
# LINK TEXT
driver.find_element(By.LINK_TEXT, "Login").click()
# Enter EMAIL ID
# XPATH--> XPATH(XML Path Language) is used language to select elements
# or attribute from HTML pages
# XPATH --> //tagname[@attribute='value']
# example --> //input[@type='email']
# To check value in browser console -->$x("XPATH")
# example --> $x("//input[@type='email']")
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")

# Enter password using XPATH
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test@123")


# Enter password using CSS_SELECTOR
# CSS--> CSS(Cascading style sheets) is language used to describe
# presentation of HTML pages.
# CSS define visual properties of element like front, front size, colour, layout
# CSS Format --> tagname[attribute='value']
# To check value in browser console -->$$("CSS")
# example --> $$("input[type='email']")


driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")

# Click on login button
# XPATH

driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

# sucess = driver.find_element(By.LINK_TEXT, "CredKart").text
# print(sucess)


try:
    driver.find_element(By.XPATH, "//strong[normalize-space()='These credentials do not match our records.']")
    print("Login Test Case is Failed")
except NoSuchElementException:
    print("Login Test Case is Passed")
    
driver.close()