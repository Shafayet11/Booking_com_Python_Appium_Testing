import time

from Pages.Basepage import BasePage
from Pages.SignIn_Page import SignIn


class Signin(BasePage):
    def test_email(self):
        sign = SignIn(self.driver)
        time.sleep(10)
        sign.click_email_button()
        time.sleep(10)
        sign.Insert_email("qups@gmail.com")
        time.sleep(10)
        sign.Continue_but()
        time.sleep(10)
        sign.Insert_password("Qups123456789")
        time.sleep(10)
        sign.Click_signIn()
        time.sleep(10)
        sign.click_start_search()
        time.sleep(10)
