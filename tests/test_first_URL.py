import time

import pytest
from pageObjects.pageObjects import PageObjects
from pageObjects.endtoEnd import Confirm
from utilities.baseclass import Baseclass


class TestHomepageValidation(Baseclass):

    def test_URL(self):
        req = "https://www.saucedemo.com/"
        act = self.driver.current_url
        time.sleep(2)
        assert act == req
        time.sleep(2)


