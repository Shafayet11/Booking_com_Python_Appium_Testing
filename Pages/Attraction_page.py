from Pages.Homepage import HomePage
from Locators.Locators import AttractionsLocator


class Attract(HomePage):
    def __init__(self, driver):
        self.locator = AttractionsLocator
        self.driver = driver
        super(Attract, self).__init__(driver)

    def click_on_attractions_tab(self):
        self.find_element(*self.locator.select_Attractions_locator)

    def click_on_search_destination(self):
        self.find_element(*self.locator.search_destination).send_keys()

    def send_data_on_search_destination(self, destination):
        self.find_element(*self.locator.search_destination).send_keys(destination)

