from Pages.Homepage import HomePage
from Locators.Locators import TaxiLocators


class Taxibook(HomePage):
    def __init__(self, driver):
        self.locator = TaxiLocators
        self.driver = driver
        super(Taxibook, self).__init__(driver)
    #
    # def click_on_save_and_signIn(self):
    #     self.find_element(*self.locator.signin_and_save).click()

    def click_on_Taxi_button(self):
        self.find_element(*self.locator.select_Taxi_tab).click()

    def click_on_pickup_textbox(self):
        self.find_element(*self.locator.select_pickup_loc).click()

    def input_data_on_pickup_textbox(self, location):
        self.find_element(*self.locator.select_pickup_loc).send_keys(location)

    def click_on_location(self):
        self.find_element(*self.locator.select_location).click()

    def click_on_destination_textbox(self):
        self.find_element(*self.locator.select_destination_loc).click()

    def input_data_on_destination_textbox(self, location):
        self.find_element(*self.locator.select_destination_loc).send_keys(location)

    def click_on_destination_location(self):
        self.find_element(*self.locator.select_location).click()

    def click_on_confirm_date(self):
        self.find_element(*self.locator.select_dates).click()

    def checking_cost(self):
        self.find_element(*self.locator.check_prices).click()


