from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver