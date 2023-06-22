import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities import XLutilites
from utilities.Logger import LogGenerator
from utilities.ReadConfigFile import ReadConfig


class Test_Login_DDT:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()
    path = "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\testCases\\TestData\\LoginData.xlsx"

    @pytest.mark.regression1
    def test_login_DDT_003(self, setup):
        self.log.info("Testcases test_login_DDT_003 is started")
        self.driver = setup
        self.log.info("Invoking browser")
        self.log.info("Opening Url")
        self.lp = UserLoginClass(self.driver)
        self.rows = XLutilites.getRowCount(self.path, "Sheet1")
        loginStatus = []
        for r in range(2, self.rows + 1):
            self.username = XLutilites.readData(self.path, "Sheet1", r, 1)
            self.password = XLutilites.readData(self.path, "Sheet1", r, 2)
            self.exp_result = XLutilites.readData(self.path, "Sheet1", r, 3)
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
                if self.exp_result == "Pass":
                    loginStatus.append("Pass")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Pass")
                    self.driver.save_screenshot(
                        "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_pass.png")
                    self.driver.find_element(By.XPATH, "//a[@role='button']").click()
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
                elif self.exp_result == "Fail":
                    loginStatus.append("Fail")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Fail")
                    self.driver.save_screenshot(
                        "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_pass.png")
                    self.driver.find_element(By.XPATH, "//a[@role='button']").click()
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

                # assert True
            elif self.rp.Status() == False:
                if self.exp_result == "Pass":
                    loginStatus.append("Fail")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Fail")
                    self.driver.refresh()
                    self.driver.save_screenshot(
                        "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_fail.png")
                elif self.exp_result == "Fail":
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Fail")
                    loginStatus.append("Pass")
                    self.driver.refresh()
                    self.driver.save_screenshot(
                        "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_fail.png")

        print(loginStatus)
        if "Fail" not in loginStatus:
            self.log.info("Testcases test_login_DDT_003 is passed")
            assert True
        else:
            self.log.info("Testcases test_login_DDT_003 is failed")
            assert False
