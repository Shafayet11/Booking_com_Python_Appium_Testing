from Pages.Homepage import HomePage
from Locators.Locators import RegisterLocators


class LoginPage(HomePage):
    def __init__(self, driver):
        self.locator = RegisterLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_create_account(self):
        self.find_element(*self.locator.Click_register_button).click()

    def Enter_email(self, email):
        self.find_element(*self.locator.Email_textbox).send_keys(email)

    def continue_click(self):
        self.find_element(*self.locator.click_continue).click()

    def new_password(self, password):
        self.find_element(*self.locator.password).send_keys(password)

    def confirm_password(self, password):
        self.find_element(*self.locator.confirm_password).send_keys(password)

    def create_account(self):
        self.find_element(*self.locator.click_create_ac).click()

