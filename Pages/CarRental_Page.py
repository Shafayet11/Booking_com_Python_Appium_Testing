from Pages.Homepage import HomePage
from Locators.Locators import CarRentalLocator
from Locators.Locators import StaysButtonLocator


class CarRent(HomePage):
    def __init__(self, driver):
        self.locator = CarRentalLocator
        self.driver = driver
        super(CarRent, self).__init__(driver)

    def select_signin_save(self):
        self.find_element(*self.locator.signin_and_save).click()

    def select_car_rent_tab(self):
        self.find_element(*self.locator.click_car_rental_locator).click()

    def click_pickup_location(self):
        self.find_element(*self.locator.click_pickup).click()

    def send_location(self, location):
        self.find_element(*self.locator.click_pickup).send_keys(location)

    def click_on_location(self):
        self.find_element(*self.locator.select_location).click()

    def select_date(self):
        self.find_element(*self.locator.click_date).click()

    def click_pickup_date(self):
        self.find_element(*self.locator.select_pick_date).click()

    def click_dropup_date(self):
        self.find_element(*self.locator.select_drop_date).click()

    def click_and_draging(self):
        self.find_element(*self.locator.select_date).click()

    def click_back_button(self):
        self.find_element(*self.locator.go_back).click()

    def click_on_search_button(self):
        self.find_element(*self.locator.click_search).click()