import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://automation.credence.in/")
driver.find_element(By.LINK_TEXT, "Login").click()
# Enter EMAIL ID
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
# Enter password using CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
# Click on login button
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
# Click on product-->Apple Macbook Pro
driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple Macbook Pro']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# click continue shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
# Click on product-->Apple iPad Retina
driver.find_element(By.XPATH, "//h3[normalize-space() ='Apple iPad Retina']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
# click continue shopping
driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
# Click on product-->Apple iPad Retina
driver.find_element(By.XPATH, "//h3[normalize-space() ='Headphones']").click()
# Add To Cart
driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()


quantityp1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
quantityp1.select_by_index(2)

quantityp2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]"))
quantityp2.select_by_index(3)

quantityp3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]"))
quantityp3.select_by_index(4)

time.sleep(2)

l = len(driver.find_elements(By.CSS_SELECTOR, "tbody tr"))
# print(l)
Price_List = []
for r in range(1, l - 2):
    Var = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
    Product_Price = (Var[1:])
    Price_List.append(float(Product_Price))

var2 = sum(Price_List)
Exp_SubTotal = round(var2, 2)
# print(Exp_SubTotal)
Exp_Tax = round((Exp_SubTotal * 0.13), 2)
# print(Exp_Tax)
Exp_Total = Exp_SubTotal + Exp_Tax
# print(Exp_Total)

Amount_List = []
for r in range(l - 2, l + 1):
    Var = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
    # print(Var)
    var2 = (Var[1:])
    Amounts = var2.replace(',', '')
    # Amount_List.append(Amounts)
    Amount_List.append(float(Amounts))

Act_SubTotal = Amount_List[0]
# print(Act_SubTotal)
Act_Tax = Amount_List[1]
# print(Act_Tax)
Act_Total = Amount_List[2]
# print(Act_Total)

if Exp_SubTotal == Act_SubTotal:
    print("Subtotal is matched")
else:
    print("Subtotal is wrong")

if Exp_Tax == Act_Tax:
    print("Tax is matched")
else:
    print("Tax is wrong")

if Exp_Total == Act_Total:
    print("Total is matched")
else:
    print("Total is wrong")

# Price_List.append(float(Product_Price))
