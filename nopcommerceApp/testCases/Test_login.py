import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser_email()
    Password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self, setup):
        self.logger.info("*********************Test_001_login *********** ")
        self.logger.info("*********************Verifying Home Page Title *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close
            self.logger.info("********************* Home Page Title is passed*********** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("********************* Home Page Title is Failed *********** ")
            assert False

    def test_login(self, setup):
        self.logger.info("*********************Verifying Login Test  *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********************Login Test is Passed *********** ")
            self.driver.close
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*********************Login Test is Failed *********** ")
            assert False
