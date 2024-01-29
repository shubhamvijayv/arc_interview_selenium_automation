import allure
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PageObjects.SubjectPage import Subject
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *

class MultipleImageChoiceQuestion(Subject):
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Click on close button')   
    def click_on_close_button(self):
        time.sleep(1)
        self.elementClick(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)
        
    def input_question_title(self, question_title):
        time.sleep(1)
        return self.sendKeys(question_title, *MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
    
    def input_optionA(self,optionA):
        time.sleep(1)
        return self.sendKeys(optionA, *Locators.INPUT_OPTION_A)
    
    def input_optionB(self,optionB):
        time.sleep(2)
        return self.sendKeys(optionB, *Locators.INPUT_OPTION_B)
    
    def input_optionC(self, optionC):
        time.sleep(2)
        return self.sendKeys(optionC, *Locators.INPUT_OPTION_C)
    
    def input_optionD(self, optionD):
        time.sleep(2)
        return self.sendKeys(optionD, *Locators.INPUT_OPTION_D)
    
    @allure.step('Click on save button')   
    def add_question_button(self):
        time.sleep(2)
        self.elementClick(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
    
    @allure.step('Checked on correct answer')       
    def checked_right_answer_options(self):
        time.sleep(1)
        self.elementClick(*Locators.CHECKED_ON_CORRECT_OPTION)
    
    def search_by_question_title(self, question_title):
        return self.sendKeys(question_title, *MultipleImageChoiceQuestionPageLocators.SEARCH_BY_QUESTION)
    
    @allure.step('Click on search button')
    def click_on_search_button(self):
        time.sleep(2)
        self.elementClick(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)

    def section_open_of_multiple_image_choice_question_section(self):
        self.fill_username_password_input(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        self.click_on_multiple_image_choice_question_section()
        
    def add_new_question_multiple_image_choice_question(self):
        self.section_open_of_multiple_image_choice_question_section()
        old_row = len(self.row_count_of_subject_table())
        self.click_on_add_new_subject_button()
        self.click_on_close_button()
        new_row = len(self.row_count_of_subject_table())
        assert old_row == new_row
            
    def add_new_question_with_all_valid_input(self,question_title, optionA, optionB, optionC, optionD, add_question):
        self.section_open_of_multiple_image_choice_question_section()
        self.click_on_add_new_subject_button()
        self.input_question_title(question_title)
        self.elementClick(*MultipleImageChoiceQuestionPageLocators.INPUT_SUBJECT)
        if optionA: 
            self.input_optionA(optionA)
        if optionB:
            self.input_optionB(optionB)
        if optionC:
            self.input_optionC(optionC)
        if optionD:
            self.input_optionD(optionD)
        if optionA and optionC:
            self.input_optionA(optionA)
            self.input_optionC(optionC)
        if optionA and optionB:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
        if optionA and optionD:
            self.input_optionA(optionA)
            self.input_optionD(optionD)
        if optionA and optionB and optionC:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
            self.input_optionC(optionC)
        if optionA and optionB and optionC and optionD:
            self.input_optionA(optionA)
            self.input_optionB(optionB)
            self.input_optionC(optionC)
            self.input_optionD(optionD)
        self.checked_right_answer_options()
        if add_question:
            self.add_question_button()
        else:
            self.click_on_close_button()
        time.sleep(1)
        
    def display_validation_messsage_required(self):
        assert self.display_error_message_respect_of_subject()
            
    def display_success_message_for_multiple_image_choice_question(self):
        assert self.display_message_respect_of_subject()

    def search_functionality_for_multiple_image_choice_question(self, question_title, subject):
        self.section_open_of_multiple_image_choice_question_section()
        if question_title:
            self.search_by_question_title(question_title)
        if subject:
            wait = WebDriverWait(self.driver, 10)
            select = wait.until(EC.presence_of_element_located((MultipleImageChoiceQuestionPageLocators.SEARCH_BY_SUBJECT)))
            select = Select(select)
            subject = select.select_by_visible_text(subject)
        self.click_on_search_button()
        time.sleep(2)
        return subject
    
    def search_after_row_count(self):
        assert self.row_count_of_subject_table()

    def delete_row_in_existing_table(self, accept):
        self.section_open_of_multiple_image_choice_question_section()
        old_row = len(self.row_count_of_subject_table())
        self.click_on_delete_button()
        if accept:
            self.driver.switch_to.alert.accept()
            assert self.display_message_respect_of_subject()
        else:
            self.driver.switch_to.alert.dismiss()
            new_row = len(self.row_count_of_subject_table())
            assert old_row == new_row
                
    def edit_row_in_existing_table(self, close, clear,clear_subject):
        self.section_open_of_multiple_image_choice_question_section()
        previous_question = self.get_text_on_table_of_subject()
        self.click_on_edit_button()
        if close:
            self.click_on_close_button()
            new_question = self.get_text_on_table_of_subject()
            assert previous_question == new_question
        else:
            if clear and clear_subject:
                time.sleep(5)
                self.clearElement(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
                self.elementClick(*MultipleImageChoiceQuestionPageLocators.CLICK_EDIT_BUTTON_SELECT_SUBJECT_DROPDOWN)
                self.add_question_button()
                time.sleep(2)
                assert self.display_error_message_respect_of_subject()
            elif clear:
                time.sleep(5)
                self.clearElement(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
                self.add_question_button()
                time.sleep(2)
                assert self.display_error_message_respect_of_subject()
            elif clear_subject:
                time.sleep(5)
                self.elementClick(*MultipleImageChoiceQuestionPageLocators.CLICK_EDIT_BUTTON_SELECT_SUBJECT_DROPDOWN)
                self.add_question_button()
                time.sleep(2)
                assert self.display_error_message_respect_of_subject()
            else:
                self.add_question_button()
                assert self.display_message_respect_of_subject()
                    
    def edit_question_of_existing_table_using_change_question(self, question_title, subject):
        self.section_open_of_multiple_image_choice_question_section()
        self.click_on_edit_button()
        time.sleep(2)
        if question_title and subject:
            self.clearElement(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
            self.sendKeys(question_title, *MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
            self.elementClick(*MultipleImageChoiceQuestionPageLocators.UPDATE_INPUT_SUBJECT)
        elif question_title:
            self.clearElement(*MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
            self.sendKeys(question_title, *MultipleImageChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
        elif subject:
            self.elementClick(*MultipleImageChoiceQuestionPageLocators.UPDATE_INPUT_SUBJECT)
        self.add_question_button()
        assert self.display_message_respect_of_subject()
