import time

from Pages.Basepage import BasePage
from Pages.SignIn_Page import SignIn
from Pages.Stays_page import stays


class stay(BasePage):
    def test_stay(self):
        stay = stays(self.driver)
        # stay.click_email_button()
        # time.sleep(4)
        # stay.Insert_email("qups@gmail.com")
        # time.sleep(4)
        # stay.Continue_but()
        # time.sleep(4)
        # stay.Insert_password("Qups123456789")
        # time.sleep(4)
        # stay.Click_signIn()
        # time.sleep(4)
        # stay.click_start_search()
        # time.sleep(4)
        time.sleep(10)
        stay.StaysLocator()
        time.sleep(5)
        stay.stay_search()
        time.sleep(4)
        stay.stay_textsearch("Bangladesh")
        time.sleep(4)
        stay.stay_textbox()
        time.sleep(4)
        stay.click_on_date()
        time.sleep(4)
        stay.select_one_date()
        time.sleep(4)
        stay.select_another_date()
        time.sleep(4)
        stay.click_on_select_dates()
        time.sleep(4)
        stay.click_on_person_type()
        time.sleep(4)
        stay.click_on_room_increase()
        time.sleep(4)
        stay.click_on_child_increase()
        time.sleep(4)
        stay.click_on_child_age()
        time.sleep(4)
        stay.click_on_apply()
        time.sleep(4)
        stay.select_search()
        time.sleep(4)

