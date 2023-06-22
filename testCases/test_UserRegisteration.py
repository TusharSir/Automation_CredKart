import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities.Logger import LogGenerator


class Test_registration:

    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_registration_001(self, setup):
        self.log.info("Testcases test_registration_001 is started")
        self.driver = setup
        self.log.info("Invoking browser")
        self.log.info("Opening Url")
        self.rp = UserRegistrationClass(self.driver)
        self.rp.Click_LinkRegister()
        self.log.info("Clicking on Register link")
        self.rp.Enter_Username("Test User")
        self.log.info("Entering username")
        self.rp.Enter_Email("test11231bdfb23@credence.in")
        self.log.info("Entering Email")
        self.rp.Enter_Password("test@123")
        self.log.info("Entering Password")
        self.rp.Enter_ConfirmPassword("test@123")
        self.log.info("Entering Confirm Password")
        self.rp.Click_Register_Button()
        self.log.info("Clicking on Register")
        if self.rp.Status() == True:
            self.log.info("Testcases test_registration_001 is passed")
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar "
                "Sir\\Automation_Credkart\\Screenshots\\test_registration_001_pass.png")
            assert True
        else:
            self.log.info("Testcases test_registration_001 is failed")
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar "
                "Sir\\Automation_Credkart\\Screenshots\\test_registration_001_fail.png")
            assert False
        self.driver.close()
        self.log.info("Testcases test_registration_001 is completed")