import datetime
import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
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
        element = WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verifyIDisPresent(self, id):
        element = WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.ID, id)))

    def verifyXpathisPresent(self, Xpath):
        element = WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, Xpath)))

    def implicitWait(self):
        self.driver.implicitly_wait(30)

    def bannerScreenshots(self, element, name):
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        file_name = date_stamp + ".png"
        element.screenshot(name + file_name)


    def get_current_time_in_millis(self) -> int:
        return int(time.time() * 1000)

    def is_time_out(self, start_time_millis: int, waiting_interval_seconds: int) -> bool:
        end_time = start_time_millis + waiting_interval_seconds * 1000
        return self.get_current_time_in_millis() > end_time

    def wait_for_element_to_vanish(self, element: WebElement) -> bool:
        is_displayed = element.is_displayed()
        start_time = self.get_current_time_in_millis()
        while is_displayed and not self.is_time_out(start_time, 6):
            is_displayed = element.is_displayed()

        return not is_displayed








