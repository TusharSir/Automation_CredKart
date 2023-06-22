from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class UserRegistrationClass:
    Click_LinkRegister_LinkText = (By.LINK_TEXT, "Register")
    Text_UserName_ID = (By.ID, "name")
    Text_Email_ID = (By.NAME, "email")
    Text_Password_ID = (By.ID, "password")
    Text_ConfirmPassword_Id = (By.ID, "password-confirm")
    Click_Register_CLassName = (By.CLASS_NAME, "btn")
    Status_text_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Click_LinkRegister(self):
        self.driver.find_element(*UserRegistrationClass.Click_LinkRegister_LinkText).click()

    def Enter_Username(self, username):
        self.driver.find_element(*UserRegistrationClass.Text_UserName_ID).send_keys(username)

    def Enter_Email(self, email):
        self.driver.find_element(*UserRegistrationClass.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*UserRegistrationClass.Text_Password_ID).send_keys(password)

    def Enter_ConfirmPassword(self, confirm_password):
        self.driver.find_element(*UserRegistrationClass.Text_ConfirmPassword_Id).send_keys(confirm_password)

    def Click_Register_Button(self):
        self.driver.find_element(*UserRegistrationClass.Click_Register_CLassName).click()

    def Status(self):
        try:
            self.driver.find_element(*UserRegistrationClass.Status_text_XPATH)
            return True
        except NoSuchElementException:
            return False
