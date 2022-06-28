import time

from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage


class RegisterTest(BasePage):
    def test_register(self):
        login = LoginPage(self.driver)
        login.click_create_account()
        time.sleep(10)
        login.Enter_email("qups@gmail.com")
        time.sleep(10)
        login.continue_click()
        time.sleep(10)
        login.new_password("Qups123456789")
        time.sleep(10)
        login.confirm_password("Qups123456789")
        time.sleep(10)
        login.create_account()
        time.sleep(10)

