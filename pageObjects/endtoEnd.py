from selenium.webdriver.common.by import By


class Confirm:
    bag_Id_Add_to_Cart = "add-to-cart-sauce-labs-backpack"
    cart_Button_Xpath = '//*[@id="shopping_cart_container"]/a'
    check_Out_Button_Id = "checkout"
    first_Name_TxBox_Id = "first-name"
    last_Name_TxBox_Id = "last-name"
    postal_Code_TxBox_Id = "postal-code"
    continue_Button_Id = "continue"
    finish_Button_Id = "finish"

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, self.bag_Id_Add_to_Cart).click()

    def cartButton(self):
        self.driver.find_element(By.XPATH, self.cart_Button_Xpath).click()

    def checkOutButton(self):
        self.driver.find_element(By.ID, self.check_Out_Button_Id).click()

    def firstNameTX(self, first):
        fsN = self.driver.find_element(By.ID, self.first_Name_TxBox_Id)
        fsN.clear()
        fsN.send_keys(first)

    def secondNameTX(self, second):
        ssN = self.driver.find_element(By.ID, self.last_Name_TxBox_Id)
        ssN.clear()
        ssN.send_keys(second)

    def postalTX(self, postal):
        psN = self.driver.find_element(By.ID, self.postal_Code_TxBox_Id)
        psN.clear()
        psN.send_keys(postal)

    def continueB(self):
        self.driver.find_element(By.ID, self.continue_Button_Id).click()

    def finish(self):
        self.driver.find_element(By.ID, self.finish_Button_Id).click()
