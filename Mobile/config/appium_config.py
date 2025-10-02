import pytest
import subprocess
import time
import allure
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType

def get_connected_devices():
    output = subprocess.check_output("adb devices", shell=True).decode()
    lines = output.strip().split("\n")[1:]
    devices = [line.split("\t")[0] for line in lines if "\tdevice" in line]
    return devices

@pytest.fixture(scope="function", params=get_connected_devices())
def appium_driver(request):
    device_name = request.param
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    global driver
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "deviceName": device_name,
        "appPackage": "id.edot.ework",
        "appActivity": "id.edot.ework.ui.MainActivity",
        "automationName": "UiAutomator2",
        "autoGrantPermissions": True,
        "grantPermissions": ["android.permission.ACCESS_FINE_LOCATION", "android.permission.ACCESS_COARSE_LOCATION"],
        "noReset": False
    }
    url = "http://localhost:4723"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    yield driver
    driver.quit()
    appium_service.stop()

def screenshot():
    screenshot = allure.attach(driver.get_screenshot_as_png(), name="screenshot",attachment_type=AttachmentType.PNG)
    return screenshot

