from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class UserLoginClass:
    Click_Linklogin_LinkText = (By.LINK_TEXT, "Login")
    Text_Email_XPATH = (By.XPATH, "//input[@type='email']")
    Text_Password_CSS = (By.CSS_SELECTOR, "input[name='password']")
    Text_ConfirmPassword_XPATH= (By.ID, "password-confirm")
    Click_LoginButton_XPATH = (By.XPATH, "//button[@class='btn btn-primary']")


    def __init__(self, driver):
        self.driver = driver

    def Click_LinkLogin(self):
        self.driver.find_element(*UserLoginClass.Click_Linklogin_LinkText).click()

    def Enter_Email(self, email):
        self.driver.find_element(*UserLoginClass.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*UserLoginClass.Text_Password_CSS).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*UserLoginClass.Click_LoginButton_XPATH).click()