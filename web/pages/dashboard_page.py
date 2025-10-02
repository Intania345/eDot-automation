from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

        # locator for dashboard marker
        self.dashboard_welcome = (By.XPATH, "//*[@class='text-md text-gray-400']")

    # keyword for dashboard page
    def check_dashboard_welcome(self):
        assert self.driver.find_element(*self.dashboard_welcome).is_displayed(), "Dashboard should be displayed after login"
