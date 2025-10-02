from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import time


def scroll_to_element(driver: WebDriver, locator_type: str, locator_value: str, max_swipes=5, direction="down"):

    for _ in range(max_swipes):
        try:
            element = driver.find_element(locator_type, locator_value)
            return element
        except NoSuchElementException:
            # Scroll/swipe by percentages
            size = driver.get_window_size()
            width = size["width"]
            height = size["height"]

            start_x = width / 2
            start_y = height * 0.8 if direction == "down" else height * 0.2
            end_y = height * 0.2 if direction == "down" else height * 0.8

            driver.swipe(start_x, start_y, start_x, end_y, duration=800)
            time.sleep(1)

    raise NoSuchElementException(f"Element not found: {locator_type}={locator_value} after {max_swipes} swipes")


from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time


def scroll_to_text(driver, text, max_swipes=10, direction="down"):
    for _ in range(max_swipes):
        try:
            element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
            return element
        except NoSuchElementException:
            size = driver.get_window_size()
            width = size['width']
            height = size['height']

            start_x = width / 2
            if direction == "down":
                start_y = height * 0.8
                end_y = height * 0.2
            else:
                start_y = height * 0.2
                end_y = height * 0.8

            driver.swipe(start_x, start_y, start_x, end_y, 800)
            time.sleep(1)

    raise NoSuchElementException(f"Text '{text}' not found after {max_swipes} swipes")


def scroll_down_until_end(driver, sleep_time=1, swipe_duration=800):
    previous_page_source = ""

    while True:
        driver.swipe(500, 1500, 500, 500, swipe_duration)
        time.sleep(sleep_time)

        current_page_source = driver.page_source
        if current_page_source == previous_page_source:
            print("Reached the end of the screen.")
            break
        previous_page_source = current_page_source
