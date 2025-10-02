import allure
import time
from faker import Faker
from Mobile.pages.login_page import LoginPage
from Mobile.pages.dashboard_page import DashboardPage
from Mobile.pages.customer_page import CustomerPage
from Mobile.config.appium_config import appium_driver, screenshot
from Mobile.tests.test_login import test_login_mobile

fake = Faker()

@allure.title("Create Customer Successfully")
def test_create_customer(appium_driver):
    login_page = LoginPage(appium_driver)
    customer_page = CustomerPage(appium_driver)
    dashboard_page = DashboardPage(appium_driver)

    # Login first
    # test_login_mobile(appium_driver)
    time.sleep(10)
    login_page.login("5049209", "qatestsalesman", "it.QA2025")
    screenshot()

    # Create new customer
    outlet_name = fake.company()
    outlet_phone = fake.phone_number()
    outlet_email = fake.email()
    outlet_cp = fake.name()
    address = fake.address()
    longitude = str(fake.longitude())
    latitude = str(fake.latitude())
    ktp = fake.ssn()

    customer_page.go_to_customer_page()
    customer_page.create_customer_basic(outlet_name, outlet_phone, outlet_email, outlet_cp)
    customer_page.create_customer_locations(address, longitude, latitude)
    customer_page.create_customer_documents(ktp)
    customer_page.verify_created_customer()
    screenshot()
