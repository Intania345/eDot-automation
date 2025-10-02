import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
from web.pages.login_page import LoginPage
from web.pages.dashboard_page import DashboardPage
from web.pages.company_page import CompanyPage
from web.tests.test_login import test_login_success

fake = Faker()

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    driver.close()
    driver.quit()

@allure.title("Create New Company Successfully")
def test_create_company(driver):
    login_page = LoginPage(driver)
    company_page = CompanyPage(driver)

    # Login
    test_login_success(driver)

    # Create company
    # variable fake
    company_name = fake.company()
    company_email = fake.email()
    company_phone = fake.phone_number()
    company_address = fake.address()

    company_page.go_to_company_page()
    time.sleep(5)
    company_page.verify_company_page()
    company_page.complete_register_company_step1(company_name, company_email, company_phone, company_address)
    company_page.take_screenshot()
    company_page.click_next_button()
    company_page.take_screenshot()
    company_page.complete_register_company_step2()
    company_page.take_screenshot()
    company_page.click_next_button()
    company_page.take_screenshot()
    company_page.complete_register_company_step3()
    company_page.take_screenshot()
    time.sleep(15)
    company_page.take_screenshot()

    # Verify created company
    company_page.verify_after_create_company(company_name)
    company_page.take_screenshot()
