import time

from appium.webdriver.common.appiumby import AppiumBy

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_logo = (AppiumBy.ID, "id.edot.ework:id/img_ework")
        self.add_customer_menu = (AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='id.edot.ework:id/card_icon'])[5]")

    def is_displayed(self):
        time.sleep(5)
        return self.driver.find_element(*self.dashboard_logo).is_displayed()
