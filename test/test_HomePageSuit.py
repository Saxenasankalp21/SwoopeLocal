import threading
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.HomePageElements import HomePageElements
from PageObject.LoginPageElements import LoginPage
from TestData.TestLoginData import LoginCasesData
from Utilities.BaseClass import BaseClass

@pytest.mark.order(1)
class TestHomePageHeader(BaseClass):
    def test_HeaderPage(self, getValidLoginData):
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
        time.sleep(3)
        homepage = HomePageElements(self.driver)
        productTitle = homepage.getProductTitle()
        self.bannerScreenshots(productTitle, "{}title".format(homepage.Location))
        assert productTitle.is_displayed()
        log.info("Brand Name is present")
        locationTitle = homepage.getYourlocation().text
        log.info(locationTitle)
        assert "Your Location" in locationTitle
        assert homepage.getSearchBox().is_displayed()
        log.info("Searchbox is present")
        assert homepage.getSearchButton().is_displayed()
        log.info("Search Button is present")
        assert homepage.getHeartIcon().is_displayed()
        log.info("Heart icon is present")
        assert homepage.getBagIcon().is_displayed()
        log.info("Bag icon is present")
        profileIcon = homepage.getProfileIcon()
        self.bannerScreenshots(profileIcon, "{}ProfileIcon".format(homepage.Location))
        assert profileIcon.is_displayed()
        log.info("Profile photo is available")


    @pytest.fixture(params=LoginCasesData.test_valid_credentials)
    def getValidLoginData(self, request):
        return request.param

@pytest.mark.order(2)
class TestHomePageBanner(BaseClass):
    def test_HomeBanners(self):
        self.driver.implicitly_wait(5)
        log = self.getLogger()
        homepage = HomePageElements(self.driver)
        log.info("Top banner test cases starts from here")
        categories = homepage.getCategories()
        headercategories = []
        for category in categories:
            headercategories.append(category.text)
        log.info(headercategories)
        if headercategories == homepage.actualheadercategory:
            log.info("The expected category is matching with the actual")
        else:
            log.info("Variance between actual and expected categories")
            assert homepage.actualheadercategory in headercategories
        log.info("Categories are visible")
        topbanner1 = homepage.getTopBanner1()
        self.bannerScreenshots(topbanner1, "{}banner1".format(homepage.Location))
        assert topbanner1.is_displayed()
        log.info("banner 1 is present")
        homepage.clickNextBannerButton().click()
        topbanner2 = homepage.getTopBanner2()
        self.bannerScreenshots(topbanner2, "{}Banner2".format(homepage.Location))
        assert topbanner2.is_displayed()
        log.info("Banner 2 is available")
        topbanner3 = homepage.getTopBanner3()
        self.bannerScreenshots(topbanner3, "{}Banner3".format(homepage.Location))
        assert topbanner3.is_displayed()
        log.info("Banner 3 is available")
        topbanner4 = homepage.getTopBanner4()
        self.bannerScreenshots(topbanner4, "{}Banner4".format(homepage.Location))
        assert topbanner4.is_displayed()
        log.info("Banner 4 is available")
        # DISCOVER LOCAL SHOPS IN YOUR AREA begins from here
        localshoptitle = homepage.getLocalShopTitle()
        log.info(localshoptitle.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", localshoptitle)
        assert "DISCOVER LOCAL SHOPS IN YOUR AREA" in localshoptitle.text
        localshopcategories = homepage.getLocalShopCategories()
        localcategories = []
        for lcategory in localshopcategories:
            localcategories.append(lcategory.text)
        log.info(localcategories)
        if localcategories == homepage.actualcategory:
            log.info("The expected category is matching with the actual")
        else:
            log.info("Variance between actual and expected categories")
            assert homepage.actualcategory in localcategories
        # Feature local market begins from here
        featurelocalmarket = homepage.getFeaturedLocalTitle()
        log.info(featurelocalmarket.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", featurelocalmarket)
        assert "FEATURED LOCAL SUPERMARKETS" in featurelocalmarket.text
        featuredrestu = homepage.getFeaturedResturantsTitle()
        log.info(featuredrestu.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", featuredrestu)
        assert "FEATURED RESTAURANTS" in featuredrestu.text
        bookingtitle = homepage.getBookingTitle()
        log.info(bookingtitle.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", bookingtitle)
        assert "Safe Entry Booking in favourite Restaurant" in bookingtitle.text
        tablesearchbutton = homepage.getTableSearchButton()
        log.info(tablesearchbutton.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", tablesearchbutton)
        assert "Search Tables" in tablesearchbutton.text
        log.info("ADDED FIT TEST")












