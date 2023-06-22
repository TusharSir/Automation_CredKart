import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities.Logger import LogGenerator
from utilities.ReadConfigFile import ReadConfig


class Test_Login:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_login_002(self, setup):
        self.log.info("Testcases test_login_002 is started")
        self.driver = setup
        self.log.info("Invoking browser")
        self.log.info("Opening Url")
        self.lp = UserLoginClass(self.driver)
        self.lp.Click_LinkLogin()
        self.log.info("Clicking on login link")
        self.lp.Enter_Email(self.username)
        self.log.info("Entering Email-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.Click_Login_Button()
        self.log.info("Clicking on login button")
        self.rp = UserRegistrationClass(self.driver)
        if self.rp.Status() == True:
            self.log.info("Testcases test_login_002 is passed")
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_pass.png")
            assert True
        else:
            self.log.info("Testcases test_login_002 is failed")
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_fail.png")
            assert False
        self.driver.close()
        self.log.info("Testcases test_login_002 is completed")
    #
    # def test_demolog(self):
    #     self.log.debug("This is debug")
    #     self.log.info("This is info")
    #     self.log.warning("This is warning")
    #     self.log.error("This is error")
    #     self.log.critical("This is critical")

