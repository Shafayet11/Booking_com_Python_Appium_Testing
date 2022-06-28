from Pages.Homepage import HomePage
from Locators.Locators import SignInLocators


class SignIn(HomePage):
    def __init__(self, driver):
        self.locator = SignInLocators
        self.driver = driver
        super(SignIn, self).__init__(driver)

    def click_email_button(self):
        self.find_element(*self.locator.click_SignIn_with_email).click()

    def Insert_email(self, email):
        self.find_element(*self.locator.Insert_email).send_keys(email)

    def Continue_but(self):
        self.find_element(*self.locator.continue_button).click()

    def Insert_password(self, password):
        self.find_element(*self.locator.Insert_password).send_keys(password)

    def Click_signIn(self):
        self.find_element(*self.locator.SignIn_Button_locator).click()

    def click_start_search(self):
        self.find_element(*self.locator.Start_search).click()