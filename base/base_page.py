import os
import time
import logging
import datetime
import allure
import requests
import json
import dateutil.parser

from datetime import timezone
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from Utilities.logger import *
from Utilities.constants import *


class BasePage():
    
    log = LogClass.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def get_title(self):
        """
        Get the title of the current page.

        Returns:
            str: The title of the page.

        Raises:
            Exception: If the title cannot be retrieved.
        """
        try:
            return self.driver.title
        except Exception as e:
            self.log.exception("Failed to get title: {}".format(e))
            raise


    def get_by_type(self, locator_type):
        """
        Get element locator type.

        Args:
            locator_type (str): The type of locator.

        Returns:
            locator_type (By): The corresponding Selenium locator type.

        Raises:
            ValueError: If the provided locator_type is not supported.
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            raise ValueError("Locator type '{}' is not supported.".format(locator_type))


    def get_element(self, locator, locator_type="xpath"):
        """
        Get element name
        locator: "It can be id, xpath, css_selector etc.."
        locator_type: by default its xpath.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="xpath"):
        """
        NEW METHOD
        Get list of elements
        """
        element = []
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        column_list = self.driver.find_elements(by_type, locator)
        for x in column_list:
            element.append(x.text)
        return element

    def element_click(self, locator="", locator_type="xpath", element=None):
        """
        Click on an element.
        Either provide element or a combination of locator and locator_type.
        """
        try:
            if locator:  
                element = self.get_element(locator, locator_type)
                assert element is not None, (
                        f"Locator not found. Cannot click on the element with locator: {locator}, locator_type: {locator_type}")
            element.click()
            self.log.info(f"Clicked on element with locator: {locator}, locator_type: {locator_type}")
        except AssertionError as e:
            self.log.error(e)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(f"{locator} not found")
            raise
        except Exception as ex:
            self.log.error(f"An error occurred while clicking on the element with locator: {locator}, locator_type: {locator_type}")
            self.log.error(ex)
            raise

    def send_keys(self, data, locator="", locator_type="xpath", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is not None, (
                        "Locator not found. Cannot send data to the element with locator: {} "
                        "and locator_type: {}".format(locator, locator_type))
            element.send_keys(data)
            self.log.info("Sent data '{}' to element with locator: {} and locator_type: {}".format(
                data, locator, locator_type))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S') + "_send_keys_failure.png"
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(locator + '_send_keys_failure')
            raise
        except Exception as e:
            self.log.exception("Failed to send data to the element with locator: {} and locator_type: {}. Error: {}".format(
                locator, locator_type, e))
            raise


    def clear_field(self, locator="", locator_type="xpath"):
        """
        Clear an element field
        """
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            self.log.info("Cleared field with locator: {} and locator_type: {}".format(locator, locator_type))
        except NoSuchElementException:
            self.log.error("Element not found with locator: {} and locator_type: {}".format(locator, locator_type))
            raise
        except Exception as e:
            self.log.error("Failed to clear field with locator: {} and locator_type: {}. Error: {}".format(
                locator, locator_type, str(e)))
            raise


    def get_text(self, locator="", locator_type="xpath", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is not None, ("Locator not found.")
            text = element.text.strip() if element else None
            if not text:
                text = element.get_attribute("innerText").strip() if element else None
            if text:
                self.log.info("Successfully retrieved text from element: {}".format(info))
                self.log.info("The text is: '{}'".format(text))
            else:
                self.log.info("No text found on element: {}".format(info))
        except NoSuchElementException as e:
            self.log.error("Element not found while trying to get text. Locator: {}, Locator Type: {}. Error: {}".format(
                locator, locator_type, str(e)))
            raise
        except Exception as e:
            self.log.error("Failed to get text on element {}. Error: {}".format(info, str(e)))
            raise
        return text


    def is_element_present(self, locator="", locator_type="xpath", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is None, ("Locator not found. Element not present with locator: " + locator +
                                         " locator_type: " + locator_type)
                return False
            else:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + locator_type)
                return True
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                assert element.is_displayed() == True, "Element is not displaying on the page."
            # else:
            #     self.log.info("Element not displayed")
            # return isDisplayed
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element + ' ' + 'not found')
            raise

    def element_presence_check(self, locator, by_type="xpath"):
        """
        Check if element is present
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + str(by_type))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locator_type: " + str(by_type))
                return False
        except:
            self.log.info("Element not found")

    def wait_for_element(self, locator, locator_type="xpath",
                         timeout=30, poll_frequency=1):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            assert element is not None, ("Element not present with locator: " + locator +
                                         " locator_type: " + locator_type)
            self.log.info("Element appeared on the web page")
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def web_scroll(self, direction="up"):
        """
        To scroll the web page up, down, or center
        """
        try:
            if direction == "up":
                self.driver.execute_script("window.scrollBy(0, -1000);")
            elif direction == "down":
                self.driver.execute_script("window.scrollBy(0, 1000);")
            elif direction == "center":
                self.driver.execute_script("window.scrollBy(0, 300);")
            else:
                raise ValueError("Invalid scroll direction. Supported directions: 'up', 'down', 'center'")
        except Exception as e:
            self.log.error("Error occurred while scrolling the web page. Error: {}".format(str(e)))

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert expected_text.lower() in actual_text.lower(), (
                    f"Actual text mismatched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text contain expected text.")

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify actual text match with the expected text.

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert expected_text.lower() == actual_text.lower(), (
                    f"Actual text mismatched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text matched with the expected text.")


    def not_match_text(self, actual_text, expected_text):
        """
        Verify actual text match with the expected text.

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert actual_text != expected_text, (
                    f"Actual text matched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text not matched with the expected text.")

    def waiting_time_element(self):
        return time.sleep(5)
    
    def slide_element(self, element, start_point, end_point):
        """element slide"""
        try:
            ActionChains(self.driver).click_and_hold(element).move_by_offset(start_point, end_point).release().perform()
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! slide element properly")

    def is_video_played(self, element):
        try:
            self.driver.execute_script("return arguments[0].currentTime > 0", element)
            self.log.info('video play successfully')
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! video play properly")

    def is_element_list_present(self, locator, locator_type="xpath", ):
        try:
            assert len(self.get_element_list(locator, locator_type)) > ZERO, (f"locator not found")
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(locator + ' ' + 'not matching ')
            raise

    def check_element_state(self, locator="", locator_type="xpath", value=False, element_name=''):
        """
        Checks if an element is in a disabled state.
        
        Clicks on an element. Provide either the element or a combination of locator and locator_type.
        
        :param value: Boolean value, default is false, indicating the element is in a disabled state.
        :param element_name: The name of the button or element.
        """
        try:
            if locator:  
                time.sleep(2)
                element = self.get_element(locator, locator_type)
                assert element.is_enabled() == value, (element_name + " is not in a disabled state")
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element_name + ' ' + 'is not in a disabled state')
            raise
        except:
            self.log.info("Locator not found. Cannot click on the element with locator: " + str(locator) + " locator_type: " + str(locator_type))

    def dropdown_value_selected(self, visible_text, locator, locator_type="xpath"):
        try:
            select = Select(self.get_element(locator, locator_type))
            time.sleep(1)
            select.select_by_visible_text(visible_text)
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(visible_text + ' ' + 'not matching ')
            raise
    
    def dropdown_value_selected_by_value(self, value, locator, locator_type="xpath"):
        try:
            select = Select(self.get_element(locator, locator_type))
            time.sleep(1)
            select.select_by_value(value)
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(value + ' ' + 'not matching ')
            raise
