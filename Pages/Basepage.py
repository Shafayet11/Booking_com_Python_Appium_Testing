import unittest
from appium import webdriver


class BasePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "appium:deviceName": "Emulator",
                "appium:platformVersion": "9",
                "appium:app": "D:\\Booking_Appium_testing\\APK\\Booking com Hotels.apk",
                "appium:autoGrantPermissions": "true",
                "appium:automationName": "UiAutomator2",
                "appium:udid": "emulator-5554",
                "appium:noReset": True
            }
        )
        print("Test Started.......")

    def tearDown(self):
        # self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
