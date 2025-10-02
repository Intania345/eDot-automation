import pytest
import allure
import time

from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from web.pages.login_page import LoginPage
from web.pages.dashboard_page import DashboardPage

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    driver.close()
    driver.quit()

@allure.title("Login to eSuite Successfully")
def test_login_success(driver):
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)

    # test case for login
    login_page.open("https://esuite.edot.id")
    login_page.click_email_button()
    login_page.enter_email("it.qa@edot.id")
    time.sleep(10)
    login_page.enter_password("it.QA2025")
    login_page.click_login_button()
    time.sleep(25)

    # verif assert dashboard
    dashboard.check_dashboard_welcome()

    # screenshot
    allure.attach(driver.get_screenshot_as_png(), name="screenshot",attachment_type=AttachmentType.PNG)


