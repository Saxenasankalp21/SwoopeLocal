
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.BookingFlowElements import BookingFlowElements
from PageObject.LoginPageElements import LoginPage
from TestData.TestBookingData import BookingCaseData, BookingSearch
from TestData.TestLoginData import LoginCasesData
from Utilities.BaseClass import BaseClass



@pytest.mark.order(8)
class TestValidBookingFlow(BaseClass):
    def test_ValidBookingFlow(self, getValidLoginData, getBookingData, getBookingSearch):
        self.driver.implicitly_wait(20)
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
        booking = BookingFlowElements(self.driver)
        booking.YourlocationButton().click()
        booking.postalCodeInput().send_keys(getBookingData["postcode"])
        booking.postalCodeSearch().click()
        time.sleep(3)
        log.info("desired Postal code is set")
        searchDropDown = Select(booking.searchDropdown())
        searchDropDown.select_by_visible_text("Eat")
        booking.searchInputBoX().send_keys(getBookingSearch["restaurant"])
        booking.clickSearchButton().click()
        log.info("Searched for the restaurants")
        self.verifyIDisPresent("nav-profile-tab")
        venuelist = booking.venueSearchList()
        for venue in venuelist:
            if venue.text == "The Barbary Automation":
                venue.click()
                log.info("restaurant found and accessible")
            else:
                log.info("restaurant is different")
        persondropdown = Select(booking.selectPersons())
        persondropdown.select_by_value('2')
        log.info("Persons selected")
        for i in range(3, 30):
            time.sleep(2)
            if booking.getSlotWarning().is_displayed():
                log.info(booking.getSlotWarning().is_displayed())
                booking.slotOk().click()
                time.sleep(1)
                Select(booking.selectTimeSlots()).select_by_index(f'{i}')
                i += 1
            else:
                booking.clickBookButton().click()
                overL = self.driver.find_element(by=By.ID, value="guestModal")
                self.wait_for_element_to_vanish(overL)
                tnccheck = booking.clicktncCheck()
                self.driver.execute_script("arguments[0].click();", tnccheck)
                log.info("Clicked T&C checkbox")
                overlay_element = self.driver.find_element(by=By.ID, value='guestlistbut')
                self.wait_for_element_to_vanish(overlay_element)
                cbutton = booking.clickConfirmBooking()
                self.driver.execute_script("arguments[0].click();", cbutton)
                log.info("Clicked confirm booking button")
                time.sleep(7)
                self.wait_for_element_to_vanish(overlay_element)
                gotomybooking = booking.clickGotoBooking()
                self.driver.execute_script("arguments[0].click();", gotomybooking)
                log.info("clicked on go to my bookings button")
                confirm = booking.getRestConfirm()
                self.verifyXpathisPresent("/html[1]/body[1]/div[2]/div[4]/section[1]/div[1]/div[2]/ul[1]/li[2]/div[1]/h2[1]")
                log.info(confirm.is_displayed())
                log.info(confirm.text)
                break

    @pytest.fixture(params=LoginCasesData.test_valid_credentials)
    def getValidLoginData(self, request):
        return request.param

    @pytest.fixture(params=BookingCaseData.test_postalCode)
    def getBookingData(self, request):
        return request.param

    @pytest.fixture(params=BookingSearch.test_searchInput)
    def getBookingSearch(self, request):
        return request.param

@pytest.mark.order(9)
class TestSlotFullBookingFlow(BaseClass):
    def test_SlotFullFlow(self, getValidLoginData, getBookingData, getBookingSearch):
        self.driver.implicitly_wait(20)
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
        booking = BookingFlowElements(self.driver)
        booking.YourlocationButton().click()
        booking.postalCodeInput().send_keys(getBookingData["postcode"])
        booking.postalCodeSearch().click()
        time.sleep(3)
        log.info("desired Postal code is set")
        for i in range(0, 60):
            searchDropDown = Select(booking.searchDropdown())
            searchDropDown.select_by_visible_text("Eat")
            booking.searchInputBoX().send_keys(getBookingSearch["restaurant"])
            booking.clickSearchButton().click()
            log.info("Searched for the restaurants")
            self.verifyIDisPresent("nav-profile-tab")
            venuelist = booking.venueSearchList()
            for venue in venuelist:
                if venue.text == "The Barbary Automation":
                    venue.click()
                    log.info("restaurant found and accessible")
                else:
                    log.info("restaurant is different")
            persondropdown = Select(booking.selectPersons())
            persondropdown.select_by_value('2')
            log.info("Persons selected")
            time.sleep(2)
            if booking.getSlotWarning().is_displayed():
                log.info(booking.getSlotWarning().is_displayed())
                booking.slotOk().click()
                log.info("Reservation Slots are now full for the time")
                log.info("This is deve branc check")
                break
            else:
                booking.clickBookButton().click()
                overL = self.driver.find_element(by=By.ID, value="guestModal")
                self.wait_for_element_to_vanish(overL)
                tnccheck = booking.clicktncCheck()
                self.driver.execute_script("arguments[0].click();", tnccheck)
                log.info("Clicked T&C checkbox")
                overlay_element = self.driver.find_element(by=By.ID, value='guestlistbut')
                self.wait_for_element_to_vanish(overlay_element)
                cbutton = booking.clickConfirmBooking()
                self.driver.execute_script("arguments[0].click();", cbutton)
                log.info("Clicked confirm booking button")
                time.sleep(7)
                self.wait_for_element_to_vanish(overlay_element)
                gotomybooking = booking.clickGotoBooking()
                self.driver.execute_script("arguments[0].click();", gotomybooking)
                log.info("clicked on go to my bookings button")
                confirm = booking.getRestConfirm()
                self.verifyXpathisPresent("/html[1]/body[1]/div[2]/div[4]/section[1]/div[1]/div[2]/ul[1]/li[2]/div[1]/h2[1]")
                log.info(confirm.is_displayed())
                log.info(confirm.text)
                i = i + 1




    @pytest.fixture(params=LoginCasesData.test_valid_credentials)
    def getValidLoginData(self, request):
        return request.param

    @pytest.fixture(params=BookingCaseData.test_postalCode)
    def getBookingData(self, request):
        return request.param

    @pytest.fixture(params=BookingSearch.test_searchInput)
    def getBookingSearch(self, request):
        return request.param