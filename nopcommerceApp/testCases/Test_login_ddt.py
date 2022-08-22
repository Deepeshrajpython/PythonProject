import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XLUtils
import time


class Test_002_ddt_login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    username = ReadConfig.getUser_email()
    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("**********************Test_002_ddt_Login")
        self.logger.info("*********************Verifying Login Test  *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in a Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.Expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.Expected == "Pass":
                    self.logger.info("*****Passed******")
                    self.lp.Clicklogout()
                    lst_status.append("Pass")
                elif self.Expected == "Fail":
                    self.logger.info("*****Failed******")
                    self.lp.Clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.Expected == 'Pass':
                    self.logger.info("*****Failed******")
                    lst_status.append("Fail")
                elif self.Expected == "Fail":
                    self.logger.info("*****Passed******")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("********* Login DDT test passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("******** Login DDT test Failed ********")
            self.driver.close()
            assert False

        self.logger.info("**************** End of Login DDT Test **************")
        self.logger.info("**************** Completed TC_LoginDDT_002 ************")

