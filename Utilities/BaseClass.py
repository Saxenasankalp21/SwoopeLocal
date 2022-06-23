import datetime
import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("/Users/sankalp/PycharmProjects/SwoopeLocal/Utilities/logifile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkTextisPresent(self, text):
        element = WebDriverWait(self.driver, 9).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def implicitWait(self):
        self.driver.implicitly_wait(30)

    def bannerScreenshots(self, element, name):
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        file_name = date_stamp + ".png"
        element.screenshot(name + file_name)








