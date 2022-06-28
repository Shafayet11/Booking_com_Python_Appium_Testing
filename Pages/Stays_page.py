from selenium.webdriver import Keys

from Pages.Homepage import HomePage
from Locators.Locators import StaysButtonLocator
from Locators.Locators import SignInLocators


class stays(HomePage):
    def __init__(self, driver):
        self.locator1 = StaysButtonLocator
        # self.locator = SignInLocators
        self.driver = driver
        super(stays, self).__init__(driver)

    # def click_email_button(self):
    #     self.find_element(*self.locator.click_SignIn_with_email).click()
    #
    # def Insert_email(self, email):
    #     self.find_element(*self.locator.Insert_email).send_keys(email)
    #
    # def Continue_but(self):
    #     self.find_element(*self.locator.continue_button).click()
    #
    # def Insert_password(self, password):
    #     self.find_element(*self.locator.Insert_password).send_keys(password)
    #
    # def Click_signIn(self):
    #     self.find_element(*self.locator.SignIn_Button_locator).click()
    #
    # def click_start_search(self):
    #     self.find_element(*self.locator.Start_search).click()

    def StaysLocator(self):
        self.find_element(*self.locator1.stays_button).click()

    def stay_search(self):
        self.find_element(*self.locator1.stay_textbox_locator).click()

    def stay_textsearch(self, textsearch):
        self.find_element(*self.locator1.stay_textseacrh_locator).send_keys(textsearch)

    def stay_textbox(self):
        self.find_element(*self.locator1.select_one).click()

    def click_on_date(self):
        self.find_element(*self.locator1.Select_Date).click()

    def select_one_date(self):
        self.find_element(*self.locator1.click_date).click()

    def select_another_date(self):
        self.find_element(*self.locator1.click_another_date).click()

    def click_on_select_dates(self):
        self.find_element(*self.locator1.select_dates_locator).click()

    def click_on_person_type(self):
        self.find_element(*self.locator1.Person_type_locator).click()

    def click_on_room_increase(self):
        self.find_element(*self.locator1.Increase_rooms).click()

    def click_on_child_increase(self):
        self.find_element(*self.locator1.Increase_children).click()

    def click_on_child_age(self):
        self.find_element(*self.locator1.select_child_age).click()

    def click_on_apply(self):
        self.find_element(*self.locator1.Click_Apply).click()

    def select_search(self):
        self.find_element(*self.locator1.click_search).click()