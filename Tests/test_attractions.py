import time

from Pages.Basepage import BasePage
from Pages.Attraction_page import Attract


class attractions(BasePage):
    def test_Taxi(self):

        attr = Attract(self.driver)
        time.sleep(5)
        attr.click_on_attractions_tab()
        time.sleep(5)
        attr.click_on_search_destination()
        time.sleep(5)
        attr.send_data_on_search_destination("Statue of Liberty ")
        time.sleep(5)
