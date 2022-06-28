from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    loginElement = (By.XPATH, "//*[contains(text(),'Login') and @data-target = '#loginsignup' ]")
    username = (By.ID, "email")
    password = (By.ID, "password")
    loginbutton = (By.ID, "login")
    welcomeheader = (By.CSS_SELECTOR, ".profile-name")
    invalidwarning = (By.CSS_SELECTOR, "#warning_msg")
    okbutton = (By.CSS_SELECTOR, "body.loaded.modal-open:nth-child(2) div.modal.fade.sucessmodal.show:nth-child(13) div.modal-dialog.modal-dialog-centered div.modal-content div.modal-body div.row.align-items-center div.col-md-12 > a.btnbottom.error:nth-child(4)")
    profilebutton = (By.XPATH, "//header/div[1]/div[1]/div[4]/div[1]/ul[1]/li[1]/a[1]/img[1]")
    logoutbutton = (By.XPATH, "//span[contains(text(),'Logout')]")
    forgotpasswordlink = (By.XPATH, "//body/div[@id='loginsignup']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/span[2]/a[1]")
    resetpasswordInput = (By.XPATH, "//body/div[@id='reset_password_model']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]")
    resetpasswordsendbutton = (By.ID, "reset_password_btn")
    resetinvalidmailwarning = (By.ID, "warning_msg")
    resetboxokbutton = (By.CSS_SELECTOR, "body.loaded.modal-open:nth-child(2) div.modal.fade.sucessmodal.show:nth-child(13) div.modal-dialog.modal-dialog-centered div.modal-content div.modal-body div.row.align-items-center div.col-md-12 > a.btnbottom.error:nth-child(4)")
    resetpasswordclosebutton = (By.CSS_SELECTOR, "body.loaded:nth-child(2) div.modal.fade.new_modal_ds.show:nth-child(20) div.modal-dialog.modal-dialog-centered div.modal-content > button.closebtnnew")
    resetsuccessfull = (By.LINK_TEXT, "OK")

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.loginElement)

    def getUserName(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickLoginButton(self):
        return self.driver.find_element(*LoginPage.loginbutton)

    def getWelcomeHeader(self):
        return self.driver.find_element(*LoginPage.welcomeheader)

    def getInvalidWarning(self):
        return self.driver.find_element(*LoginPage.invalidwarning)

    def clickOkButton(self):
        return self.driver.find_element(*LoginPage.okbutton)

    def clickProfileButton(self):
        return self.driver.find_element(*LoginPage.profilebutton)

    def clickLogOut(self):
        return self.driver.find_element(*LoginPage.logoutbutton)

    def clickForgotPass(self):
        return self.driver.find_element(*LoginPage.forgotpasswordlink)

    def resetPasswordInput(self):
        return self.driver.find_element(*LoginPage.resetpasswordInput)

    def resetPasswordSendButton(self):
        return self.driver.find_element(*LoginPage.resetpasswordsendbutton)

    def resetInvalidMailWarning(self):
        return self.driver.find_element(*LoginPage.resetinvalidmailwarning)

    def resetPasswordOk(self):
        return self.driver.find_element(*LoginPage.resetboxokbutton)

    def resetPasswordClose(self):
        return self.driver.find_element(*LoginPage.resetpasswordclosebutton)

    def getresetSuccess(self):
        return self.driver.find_element(*LoginPage.resetsuccessfull)
