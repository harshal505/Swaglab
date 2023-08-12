from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObjects:
    username_Textbox_id = "user-name"
    password_Textbox_id = "password"
    login_Button_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, self.username_Textbox_id).clear()
        self.driver.find_element(By.ID, self.username_Textbox_id).send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, self.password_Textbox_id).clear()
        self.driver.find_element(By.ID, self.password_Textbox_id).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.ID, self.login_Button_id).click()
