import time
import allure

from base.selenium_driver import BasePage
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.constants import *

class Login(BasePage):
    def __init__(self, driver):
        self.driver = driver
        
    def fill_username_password_input(self, Username, Password):
        self.send_key(Username, *LoginPageLocators.INPUT_USERNAME)
        self.send_key(Password, *LoginPageLocators.INPUT_PASSWORD)
        self.element_click(*LoginPageLocators.LOGIN_BUTTON)
        time.sleep(3)

    @allure.step('Display success message')
    def display_successfully_login_message(self):
        assert self.is_element_displayed(*Locators.DISPLAY_MESSAGE)

    @allure.step('Display invalid login message')
    def display_invalid_crediential_message(self):
        assert self.is_element_displayed(*Locators.DISPLAY_MESSAGE)

    @allure.step('Display login text')
    def display_admin_login_text(self):
        assert self.is_element_displayed(*LoginPageLocators.LOGIN_BUTTON)

    def click_on_allow_authenticated_user_section(self):
        self.element_click(*LoginPageLocators.CLICK_TEXT_ALLOW_AUTHENTICATED_USER_XPATH)

    def click_on_add_subject_section(self):
        self.element_click(*LoginPageLocators.CLICK_TEXT_ADD_SUBJECT_XPATH)

    def click_on_multiple_image_choice_question_section(self):
        self.element_click(*LoginPageLocators.CLICK_TEXT_MULTIPLE_IMAGE_CHOICE_QUESTION_XPATH)

    def click_on_multiple_choice_question_section(self):
        return self.element_click(*LoginPageLocators.CLICK_TEXT_MULTIPLE_CHOICE_QUESTION_XPATH)

    def click_on_image_based_multiple_choice_question_section(self):
        return self.element_click(*LoginPageLocators.CLICK_TEXT_IMAGE_BASED_MULTIPLE_CHOICE_QUESTION_XPATH)

    def click_on_subjective_question_section(self):
        return self.element_click(*LoginPageLocators.CLICK_TEXT_SUBJECTIVE_QUESTION_XPATH)

    def click_on_image_based_subjective_question_section(self):
        return self.element_click(*LoginPageLocators.CLICK_TEXT_IMAGE_BASED_SUBJECTIVE_QUESTION_XPATH)
    
    def click_on_excel_question_section(self):
        return self.element_click(*LoginPageLocators.CLICK_TEXT_EXCEL_QUESTION_XPATH)
    
    def click_on_passage_content_section(self):
        return self.element_click(*LoginPageLocators.CLICK_TEXT_PASSAGE_CONTENT_XPATH)
