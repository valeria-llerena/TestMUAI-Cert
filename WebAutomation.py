
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://ecommerce-playground.lambdatest.io/
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Type 'iPhone' in search box
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'iPhone':
            element.send_keys(char)
    else:
        element.send_keys('iPhone')
    driver.implicitly_wait(6)

    # Step - 3 : Click 'Search' botton
    element_locators = ["//div[@id='entry_217822']/div[1]/form[1]/div[1]/div[2]/button[1]", "//button[text()='Search']", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)', "//button[contains(text(),'Search')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 4 : Read title text of each item in results → {{item_titles}}
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        item_titles = result
    
    print("item_titles:", item_titles)
    driver.implicitly_wait(6)

    # Step - 5 : Assert {{item_titles}} contains 'iPhone'
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        item_titles = result
    
    print("item_titles:", item_titles)

    driver.quit()
except Exception as e:
    driver.quit()
