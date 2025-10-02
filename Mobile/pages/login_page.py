import time

from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.company_id = (AppiumBy.ID, "id.edot.ework:id/tv_company_id")
        self.email = (AppiumBy.ID, "id.edot.ework:id/tv_username")
        self.password = (AppiumBy.ID, "id.edot.ework:id/tv_password")
        self.login_button = (AppiumBy.ID, "id.edot.ework:id/button_text")

    def login(self, company, email, password):
        time.sleep(10)
        self.driver.find_element(*self.company_id).send_keys(company)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
