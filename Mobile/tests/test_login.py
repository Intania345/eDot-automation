import time

import allure
from Mobile.pages.login_page import LoginPage
from Mobile.pages.dashboard_page import DashboardPage
from Mobile.config.appium_config import appium_driver, screenshot


@allure.title("Login to Mobile App Successfully")
def test_login_mobile(appium_driver):
    login_page = LoginPage(appium_driver)
    dashboard = DashboardPage(appium_driver)

    time.sleep(5)
    login_page.login("5049209", "qatestsalesman", "it.QA2025")
    screenshot()
    assert dashboard.is_displayed(), "Dashboard should be visible after login"
    screenshot()
