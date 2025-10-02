from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        #locator for login page
        self.email_button = (By.XPATH, "//button[contains(text(), 'Use Email or Username')]")
        self.email_field = (By.NAME, "username")
        self.login_button = (By.XPATH, "//button[contains(text(), 'Log In')]")
        self.password_field = (By.NAME, "password")


    #keyword for login flow

    def open(self, url):
        self.driver.get(url)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_email_button(self):
        self.driver.find_element(*self.email_button).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.login_button).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

