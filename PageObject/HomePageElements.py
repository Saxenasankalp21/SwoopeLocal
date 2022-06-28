from selenium.webdriver.common.by import By


class HomePageElements:

    def __init__(self, driver):
        self.driver = driver
    #test case1 test_HeaderPage
    Location = "/Users/sankalp/PycharmProjects/SwoopeLocal/Screenshots/HomePage/"
    producttitle = (By.XPATH, "html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]")
    yourlocationtext = (By.XPATH, "//h6[contains(text(),'Your Location')]")
    searchbox = (By.XPATH, "//input[@id='input-search']")
    searchbutton = (By.XPATH, "//button[contains(text(),'SEARCH')]")
    hearticon = (By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[4]/div[1]/a[2]/i[1]")
    bagicon = (By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[4]/div[1]/div[1]/a[1]/i[1]")
    profileicon = (By.XPATH, "/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[4]/div[1]/ul[1]/li[1]/a[1]/div[1]/img[1]")
    #test case2 test_TopBanners
    actualheadercategory = ['Chocolates', 'Clothing', 'Electroincs', 'Fashion', 'Gifts', 'Mobile', 'Sports & Active Wear', 'Topwear1', "Women's", 'Confectionery', 'Cleaning', 'Food & Drink', 'Sports']
    categories = (By.XPATH, "//ul[@class='menu']/li/a")
    topbanner1 = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]")
    bannernextbutton = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]/span[1]")
    topbanner2 = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/img[1]")
    topbanner3 = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[2]/a[1]/img[1]")
    topbanner4 = (By.XPATH, "/html[1]/body[1]/div[2]/div[4]/div[1]/div[1]/div[2]/a[2]/img[1]")
    localshopstitle = (By.XPATH, "//h3[contains(text(),'DISCOVER LOCAL SHOPS IN YOUR AREA')]")
    localshopcategories = (By.XPATH, "//div[@class='bot-wp']/div[@class='row']/div/div/a/div/div/div/h4")
    actualcategory = ['Clothing', 'Beauty', 'Hobbies & Craft', 'Restaurants, Cafes & Bars', 'Alcohol', 'Groceries']
    featuredlocalmarkettitle = (By.XPATH, "//h3[contains(text(),'FEATURED LOCAL SUPERMARKETS')]")
    featuredresturants = (By.XPATH, "//h3[contains(text(),'FEATURED RESTAURANTS')]")
    bookingtitle = (By.XPATH, "//h4[contains(text(),'Safe Entry Booking in favourite Restaurant')]")
    searchtablebutton = (By.XPATH, "//button[contains(text(),'Search Tables')]")



    def getProductTitle(self):
        return self.driver.find_element(*HomePageElements.producttitle)

    def getYourlocation(self):
        return self.driver.find_element(*HomePageElements.yourlocationtext)


    def getSearchBox(self):
        return self.driver.find_element(*HomePageElements.searchbox)

    def getSearchButton(self):
        return self.driver.find_element(*HomePageElements.searchbutton)

    def getHeartIcon(self):
        return self.driver.find_element(*HomePageElements.hearticon)

    def getBagIcon(self):
        return self.driver.find_element(*HomePageElements.bagicon)

    def getProfileIcon(self):
        return self.driver.find_element(*HomePageElements.profileicon)

    def getCategories(self):
        return self.driver.find_elements(*HomePageElements.categories)

    def getTopBanner1(self):
        return self.driver.find_element(*HomePageElements.topbanner1)

    def getTopBanner2(self):
        return self.driver.find_element(*HomePageElements.topbanner2)

    def getTopBanner3(self):
        return self.driver.find_element(*HomePageElements.topbanner3)

    def getTopBanner4(self):
        return self.driver.find_element(*HomePageElements.topbanner4)

    def clickNextBannerButton(self):
        return self.driver.find_element(*HomePageElements.bannernextbutton)

    def getLocalShopTitle(self):
        return self.driver.find_element(*HomePageElements.localshopstitle)

    def getLocalShopCategories(self):
        return self.driver.find_elements(*HomePageElements.localshopcategories)

    def getFeaturedLocalTitle(self):
        return self.driver.find_element(*HomePageElements.featuredlocalmarkettitle)

    def getFeaturedResturantsTitle(self):
        return self.driver.find_element(*HomePageElements.featuredresturants)

    def getBookingTitle(self):
        return self.driver.find_element(*HomePageElements.bookingtitle)

    def getTableSearchButton(self):
        return self.driver.find_element(*HomePageElements.searchtablebutton)

