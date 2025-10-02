import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

@pytest.fixture(scope="function")
def appium_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "devices",
        "appPackage": "id.edot.ework",
        "appActivity": "id.edot.ework.ui.MainActivity",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://localhost:4723/", desired_caps)
    yield driver
    driver.quit()

def setup_function(function):
    global driver
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "deviceName": "Android",
        "appPackage": "id.edot.ework",
        "appActivity": "id.edot.ework.ui.MainActivity",
        "automationName": "UiAutomator2"
    }
    url = "http://localhost:4723/"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

def teardown_function(function):
    driver.quit()

def test_demo():
    print("test demo")
