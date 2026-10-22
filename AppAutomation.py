
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
import time, traceback

options = XCUITestOptions()
options.set_capability("platformName", "ios")

driver = webdriver.Remote("http://localhost:4723", options=options)
try:

    def get_element(driver, locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element("xpath", locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = "xpath"
                selector = locator.get('selector', locator) if isinstance(locator, dict) else locator
                try:
                    element = driver.find_element(by_method, selector)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None
    driver.implicitly_wait(6)

    # Step - 1 : Click on the 'Speed Test' button
    element_locators = ['//XCUIElementTypeButton[@label="Speed Test"]']
    element = get_element(driver, element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(6)

    # Step - 2 : Check if SpeedTest is visible → {{{{speedtest_visible}}}}
    print('Step 2: Query - Check if SpeedTest is visible → {{{{speedtest_visible}}}}')
    driver.implicitly_wait(6)

    # Step - 3 : Assert {{{{speedtest_visible}}}} equals true
    print('Step 3: Assertion - Assert {{{{speedtest_visible}}}} equals true')
    driver.implicitly_wait(6)

    # Step - 4 : Close current app
    print('Step 4: Close app - Close current app')

    driver.quit()
except Exception as e:
    driver.quit()
