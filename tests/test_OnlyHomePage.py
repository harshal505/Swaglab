import time


from pageObjects.pageObjects import PageObjects

from utilities.baseclass import Baseclass


class TestHomepageValidation(Baseclass):

    def test_homePage(self):
        home = PageObjects(self.driver)
        home.username('standard_user')
        time.sleep(2)
        log = self.getLogger()
        log.info("first name is ")
        home.password("secret_sauce")
        time.sleep(2)
        home.login_button()
        time.sleep(2)
        exp_home_URL = "https://www.saucedemo.com/inventory.html"
        assert exp_home_URL == self.driver.current_url
        time.sleep(2)