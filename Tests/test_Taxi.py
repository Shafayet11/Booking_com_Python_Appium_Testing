import time

from Pages.Basepage import BasePage
from Pages.Taxi_page import Taxibook


class TaxiBooking(BasePage):
    def test_Taxi(self):

        taxi = Taxibook(self.driver)
        # time.sleep(10)
        # taxi.click_on_save_and_signIn()
        # time.sleep(5)
        time.sleep(10)
        taxi.click_on_Taxi_button()
        time.sleep(10)
        taxi.click_on_pickup_textbox()
        time.sleep(10)
        taxi.input_data_on_pickup_textbox()
        time.sleep(10)
        taxi.click_on_location()
        time.sleep(10)
        taxi.click_on_destination_textbox()
        time.sleep(10)
        taxi.input_data_on_destination_textbox()
        time.sleep(10)
        taxi.click_on_destination_location()
        time.sleep(10)
        taxi.click_on_confirm_date()
        time.sleep(10)
        taxi.checking_cost()
        time.sleep(10)
