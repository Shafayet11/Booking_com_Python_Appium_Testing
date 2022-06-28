import time

from Pages.Basepage import BasePage
from Pages.CarRental_Page import CarRent


class Carrental(BasePage):
    def test_car_rent(self):
        car = CarRent(self.driver)
        time.sleep(10)
        # car.select_signin_save()
        # time.sleep(3)
        car.select_car_rent_tab()
        time.sleep(3)
        car.click_pickup_location()
        time.sleep(3)
        car.send_location("New york")
        time.sleep(3)
        car.click_on_location()
        time.sleep(3)
        car.select_date()
        time.sleep(3)
        car.click_pickup_date()
        time.sleep(10)
        car.click_dropup_date()
        time.sleep(3)
        car.select_date()
        time.sleep(3)
        car.click_back_button()
        time.sleep(3)
        car.click_on_search_button()
        time.sleep(3)



































































        car.click_back_button()
        time.sleep(3)
        car.click_on_search_button()
        time.sleep(3)

