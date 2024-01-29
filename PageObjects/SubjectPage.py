import allure
import time

from PageObjects.LoginPage import Login
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *

class Subject(Login):
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Click on add new button')    
    def click_on_add_new_subject_button(self):
        self.elementClick(*Locators.ADD_NEW_QUESTION_BUTTON)
    
    @allure.step('Fill new subject input')    
    def add_new_subject_input_type(self, subject_data):
        time.sleep(2)
        self.sendKeys(subject_data, *SubjectPageLocators.INPUT_SUBJECT)
    
    @allure.step('Click on save button')     
    def new_subject_add_save_button(self):
        time.sleep(1)
        self.elementClick(*Locators.SAVE_BUTTON)
    
    @allure.step('Display success message')    
    def display_message_respect_of_subject(self):
        return self.isElementDisplayed(*Locators.DISPLAY_MESSAGE)
    
    @allure.step('Display required validation message') 
    def display_error_message_respect_of_subject(self):
        return self.isElementDisplayed(*Locators.PARSLEY_REQUIRED)
    
    @allure.step('Display pattern validation message')
    def display_error_message_respect_of_parsley_pattern(self):
        return self.isElementDisplayed(*Locators.PARSLEY_PATTERN)
    
    @allure.step('Row count of subject table') 
    def row_count_of_subject_table(self):
        return self.getElementList(*Locators.TABLE_ROW_COUNT)
    
    @allure.step('Click on delete button') 
    def click_on_delete_button(self):
        self.elementClick(*Locators.DELETE_BUTTON)
    
    @allure.step('Click on edit button')    
    def click_on_edit_button(self):
        self.elementClick(*Locators.EDIT_BUTTON)
    
    @allure.step('Get text of table')    
    def get_text_on_table_of_subject(self):
        element = self.getText(*SubjectPageLocators.GET_TEXT_SUBJECT)
        return element
    
    @allure.step('Click on cancel button') 
    def click_on_cancel_button(self):
        time.sleep(2)
        self.elementClick(*Locators.CLOSE_BUTTON)
        
    def section_open_of_subject_section(self):
        self.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        self.click_on_add_subject_section()
        
    def fill_the_form_add_new_subject(self,subject_data):
        self.section_open_of_subject_section()
        self.click_on_add_new_subject_button()
        self.add_new_subject_input_type(subject_data)
        self.new_subject_add_save_button()
        
    def not_save_new_subject_click_on_cancel_button(self):
        self.section_open_of_subject_section()
        old_row = len(self.row_count_of_subject_table())
        self.click_on_add_new_subject_button()
        self.click_on_cancel_button()
        new_row = len(self.row_count_of_subject_table())
        assert new_row == old_row

    def delete_row_in_the_subject_table(self):
        self.section_open_of_subject_section()
        self.click_on_delete_button()
        self.driver.switch_to.alert.accept()
        assert self.display_message_respect_of_subject()    
    
    def not_delete_row_in_subject_table(self):
        self.section_open_of_subject_section()
        element = self.get_text_on_table_of_subject()
        self.click_on_delete_button()
        time.sleep(3)
        self.driver.switch_to.alert.dismiss()
        data = self.get_text_on_table_of_subject()
        assert element == data

    def update_existing_data_in_the_subject_table_without_change(self):
        self.section_open_of_subject_section()
        previous_subject = self.get_text_on_table_of_subject()
        self.click_on_edit_button()
        self.click_on_cancel_button()
        time.sleep(2)
        new_subject = self.get_text_on_table_of_subject()
        assert previous_subject == new_subject
            
    def update_existing_subject_click_on_edit_button(self, subject_data):
        self.section_open_of_subject_section()
        self.click_on_edit_button()
        time.sleep(2)
        if subject_data:
            self.clearElement(*SubjectPageLocators.INPUT_SUBJECT)
            self.add_new_subject_input_type(subject_data)
        else:
            self.clearElement(*SubjectPageLocators.INPUT_SUBJECT)
        self.new_subject_add_save_button()

    def validation_message_for_subject(self):
        assert self.display_error_message_respect_of_parsley_pattern()
        
    def validation_message_for_required_subject(self):
        assert self.display_error_message_respect_of_subject()
              
    def success_message_for_subject(self):
        assert self.display_message_respect_of_subject()
