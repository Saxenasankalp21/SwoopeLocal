from selenium.webdriver.common.by import By


class BookingFlowElements:

    def __init__(self, driver):
        self.driver = driver

    yourlocationbutton = (By.ID, "user_postal_code")
    postalcodeinput = (By.NAME, "post_code_address")
    postalcodesearch = (By.ID, "find_post_code_address")
    searchdropdown = (By.ID, "product_type")
    searchBox = (By.ID, "input-search")
    searchbutton = (By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[3]/form[1]/button[1]")
    venuesearchlist = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/a/div/div[2]/div/div/h4")
    persondropdown = (By.ID, "total_guest")
    timeslotdropdown = (By.ID, "timing_slot")
    slotsfullwarning = (By.ID, "warning_msg")
    slotswarningok = (By.XPATH, "//body/div[@id='notificationModalpopup']/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    bookbutton = (By.XPATH, "//body/div[@id='app']/div[5]/section[1]/div[1]/div[1]/form[1]/div[1]/a[1]")
    tncbox = (By.XPATH, "/html[1]/body[1]/div[10]/div[1]/div[1]/div[1]/form[1]/div[3]/label[1]/span[1]")
    confirmbookingbutton = (By.ID, "guestlistbut")
    gotobookings = (By.XPATH, "//body/div[@id='app']/div[@id='sucessModalR']/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/a[1]")
    bookingconfirmation = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/section[1]/div[1]/div[2]/ul[1]/li[2]/div[1]/h2[1]")
    bookingid = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")


    ##Overalt excpetion element
    overlay = (By.ID, "guestModal")






    def YourlocationButton(self):
        return self.driver.find_element(*BookingFlowElements.yourlocationbutton)

    def postalCodeInput(self):
        return self.driver.find_element(*BookingFlowElements.postalcodeinput)

    def postalCodeSearch(self):
        return self.driver.find_element(*BookingFlowElements.postalcodesearch)

    def searchDropdown(self):
        return self.driver.find_element(*BookingFlowElements.searchdropdown)

    def searchInputBoX(self):
        return self.driver.find_element(*BookingFlowElements.searchBox)

    def clickSearchButton(self):
        return self.driver.find_element(*BookingFlowElements.searchbutton)

    def venueSearchList(self):
        return self.driver.find_elements(*BookingFlowElements.venuesearchlist)

    def selectPersons(self):
        return self.driver.find_element(*BookingFlowElements.persondropdown)

    def selectTimeSlots(self):
        return self.driver.find_element(*BookingFlowElements.timeslotdropdown)

    def getSlotWarning(self):
        return self.driver.find_element(*BookingFlowElements.slotsfullwarning)

    def slotOk(self):
        return self.driver.find_element(*BookingFlowElements.slotswarningok)

    def clickBookButton(self):
        return self.driver.find_element(*BookingFlowElements.bookbutton)

    def clicktncCheck(self):
        return self.driver.find_element(*BookingFlowElements.tncbox)

    def getOverlayElement(self):
        return self.driver.find_element(*BookingFlowElements.overlay)

    def clickConfirmBooking(self):
        return self.driver.find_element(*BookingFlowElements.confirmbookingbutton)

    def clickGotoBooking(self):
        return self.driver.find_element(*BookingFlowElements.gotobookings)

    def getRestConfirm(self):
        return self.driver.find_element(*BookingFlowElements.bookingconfirmation)

    def getBookingId(self):
        return self.driver.find_element(*BookingFlowElements.bookingid)
