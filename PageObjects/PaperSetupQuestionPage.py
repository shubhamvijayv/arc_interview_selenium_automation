from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.PassageContentPage import PassageContentQuestion
from PageObjects.SubjectPage import Subject

class PaperSetupQuestion(PassageContentQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subject = Subject(self.driver)

    def click_on_delete_button_after_dismiss(self):
        actual_text = self.get_text(*PaperSetupPageLocators.TABLE_DESCRIPTION_TITLE)
        self.element_click(*PaperSetupPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.dismiss()
        expected_text = self.get_text(*PaperSetupPageLocators.TABLE_DESCRIPTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_on_delete_button_after_accept(self):
        actual_text = self.get_text(*PaperSetupPageLocators.TABLE_DESCRIPTION_TITLE)
        self.element_click(*PaperSetupPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*PaperSetupPageLocators.TABLE_DESCRIPTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def click_on_add_paper_button(self):
        self.element_click(*PaperSetupPageLocators.ADD_PAPER_BUTTON)

    def click_on_edit_button_after_task_completed(self):
        self.wait_for_element(*PaperSetupPageLocators.EDIT_BUTTON)
        self.element_click(*PaperSetupPageLocators.EDIT_BUTTON)
        self.element_click(*PaperSetupPageLocators.NEXT_BUTTON)
        self.subjective_question_added_success_message(TASK_COMPLETED)
        
    def display_task_completed_message_and_click_on_save_button(self):
        self.element_click(*PassageContentPageLocators.ADD_NEW_QUESTION_BUTTON)
        self.subjective_question_added_success_message(QUESTION_LINKED)

    def click_on_edit_button_then_update_the_something(self, data):
        self.wait_for_element(*PaperSetupPageLocators.EDIT_BUTTON)
        self.element_click(*PaperSetupPageLocators.EDIT_BUTTON)
        time.sleep(5)
        self.clear_field(*PaperSetupPageLocators.SUBJECT_MARKS)
        self.send_keys(data, *PaperSetupPageLocators.SUBJECT_MARKS)
        self.element_click(*PaperSetupPageLocators.NEXT_BUTTON)
        self.subjective_question_added_success_message(TASK_COMPLETED)

    def click_on_the_save_button(self):
        self.element_click(*PassageContentPageLocators.ADD_NEW_QUESTION_BUTTON)
