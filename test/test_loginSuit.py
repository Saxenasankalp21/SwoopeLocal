import threading
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.LoginPageElements import LoginPage
from TestData.TestLoginData import LoginCasesData
from Utilities.BaseClass import BaseClass


@pytest.mark.order(3)
class TestLoginValidFlow(BaseClass):
    def test_ValidLoginFlow(self, getValidLoginData):
        self.driver.implicitly_wait(5)
        log = self.getLogger()
        login = LoginPage(self.driver)
        login.getLoginButton().click()
        log.info("User info to enter")
        time.sleep(3)
        login.getUserName().send_keys(getValidLoginData["email"])
        login.getPassword().send_keys(getValidLoginData["password"])
        login.clickLoginButton().click()
        log.info("Logged into the system")
        time.sleep(6)
        profilewelcome = login.getWelcomeHeader().text
        log.info("This is the loggged in profile welcome: " + profilewelcome)
        assert "HI" in profilewelcome
        login.clickProfileButton().click()
        login.clickLogOut().click()
        logintext = login.getLoginButton().text
        log.info("This is to check if user logged out" + logintext)
        assert "Login" in logintext

    @pytest.fixture(params=LoginCasesData.test_valid_credentials)
    def getValidLoginData(self, request):
        return request.param


@pytest.mark.order(4)
class TestLoginInvalidFlow(BaseClass):
    def test_InvalidLoginFlow(self, getInValidLoginData):
        self.driver.implicitly_wait(5)
        log = self.getLogger()
        login = LoginPage(self.driver)
        login.getLoginButton().click()
        log.info("User info to enter")
        time.sleep(3)
        login.getUserName().send_keys(getInValidLoginData["email"])
        login.getPassword().send_keys(getInValidLoginData["password"])
        login.clickLoginButton().click()
        time.sleep(3)
        war = login.getInvalidWarning().text
        log.info(war)
        assert "Please enter a valid email and password" in war
        login.clickOkButton().click()
        log.info("Invalid credentials")

    @pytest.fixture(params=LoginCasesData.test_Invalid_credentials)
    def getInValidLoginData(self, request):
        return request.param

@pytest.mark.order(5)
class TestForgotPassValidFlow(BaseClass):
    def test_ForgotPassValid(self, getResetData):
        log = self.getLogger()
        login = LoginPage(self.driver)
        login.getLoginButton().click()
        time.sleep(3)
        log.info("About to click forgot password")
        time.sleep(3)
        login.clickForgotPass().click()
        log.info("Forgot password clicked")
        time.sleep(4)
        login.resetPasswordInput().send_keys(getResetData["email"])
        log.info("Mail Entered")
        time.sleep(5)
        login.resetPasswordSendButton().click()
        log.info("reset sent")
        self.verifyLinkTextisPresent("OK")
        txt = login.getresetSuccess().text
        log.info(txt)
        assert "OK" in txt

    @pytest.fixture(params=LoginCasesData.test_forgot)
    def getResetData(self, request):
        return request.param


@pytest.mark.order(6)
class TestForgotPassInvalidFlow(BaseClass):
    def test_ForgotPassInvalid(self, getResetInvalidData ):
        log = self.getLogger()
        login = LoginPage(self.driver)
        login.getLoginButton().click()
        time.sleep(3)
        log.info("About to click forgot password")
        time.sleep(3)
        login.clickForgotPass().click()
        log.info("Forgot password clicked")
        time.sleep(4)
        login.resetPasswordInput().send_keys(getResetInvalidData["email"])
        log.info("Mail Entered")
        time.sleep(5)
        login.resetPasswordSendButton().click()
        log.info("reset sent")
        self.verifyLinkTextisPresent("OK")
        warning = login.getInvalidWarning().text
        log.info(warning)
        assert "We can not find a user" in warning

    @pytest.fixture(params=LoginCasesData.test_invalidforgot)
    def getResetInvalidData(self, request):
        return request.param

@pytest.mark.order(7)
class TestForgotPassClose(BaseClass):
    def test_ForgotPassClosebutton(self):
        log = self.getLogger()
        login = LoginPage(self.driver)
        login.getLoginButton().click()
        time.sleep(3)
        log.info("About to click forgot password")
        time.sleep(3)
        login.clickForgotPass().click()
        log.info("Forgot password clicked")
        login.resetPasswordClose().click()
        log.info("Reset password page is closed")
