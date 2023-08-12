import time

from pageObjects.endtoEnd import Confirm
from pageObjects.pageObjects import PageObjects
from utilities.baseclass import Baseclass


class TestEndToEnd(Baseclass):

    def test_e_2_e(self):
        home = PageObjects(self.driver)
        home.username('standard_user')
        time.sleep(2)
        log = self.getLogger()
        log.info("first name is ")
        home.password("secret_sauce")
        time.sleep(2)
        home.login_button()
        time.sleep(2)
        end = Confirm(self.driver)
        end.add_to_cart()
        time.sleep(2)
        end.cartButton()
        # time.sleep(2)
        end.checkOutButton()
        end.firstNameTX("praveen")
        time.sleep(2)
        end.secondNameTX("arde")
        time.sleep(2)
        end.postalTX("440012")
        time.sleep(2)
        end.continueB()
        time.sleep(2)
        item = "Sauce Labs Backpack"
        assert "Backpack" in item
