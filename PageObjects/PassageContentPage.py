from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.ExcelQuestionPage import ExcelQuestion
from PageObjects.SubjectPage import Subject

class PassageContentQuestion(ExcelQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.subject = Subject(self.driver)

    def add_new_question_button_of_passage_content(self):
        self.element_click(*PassageContentPageLocators.ADD_NEW_QUESTION_BUTTON)

    def fill_form_of_passage_content(self, types, question_title, subject, description, status):
        self.dropdown_value_selected(types, *PassageContentPageLocators.INPUT_TYPE)
        self.send_keys(question_title, *PassageContentPageLocators.INPUT_QUESTION)
        self.dropdown_value_selected(subject, *PassageContentPageLocators.INPUT_SUBJECT)
        self.send_keys(description, *PassageContentPageLocators.INPUT_DESCRIPTION)
        self.dropdown_value_selected(status, *PassageContentPageLocators.INPUT_STATUS)
        self.element_click(*Locators.SAVE_BUTTON)

    def form_successfully_submitted(self, types, question_title, subject, description, status):
        self.fill_form_of_passage_content(types, question_title, subject, description, status)
        self.subjective_question_added_success_message(PASSAGE_ADDED)

    def fill_form_submitted_without_status(self, types, question_title, subject, description, status):
        self.add_new_question_button_of_passage_content()
        self.fill_form_of_passage_content(types, question_title, subject, description, status)
        actual_text = self.get_text(*Locators.PARSLEY_REQUIRED)
        expected_text = PARSLEY_REQUIRED_NEW
        self.verify_text_match(actual_text, expected_text)

    def form_submitted_with_typing_types(self, types, question_title, subject, description, status, validation):
        self.fill_form_of_passage_content(types, question_title, subject, description, status)
        self.subjective_question_added_success_message(validation)

    def form_fill_with_invalid_question_title_data(self, types, question_title, subject, description, status, validation):
        self.fill_form_of_passage_content(types, question_title, subject, description, status)
        self.validate_parsley_maxlength_validation(validation)

    def click_on_delete_button_and_click_the_accept_data(self):
        actual_text = self.get_text(*PassageContentPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*PassageContentPageLocators.TABLE_QUESTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def click_on_delete_button_and_click_the_dismiss_data(self):
        actual_text = self.get_text(*PassageContentPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.dismiss()
        expected_text = self.get_text(*PassageContentPageLocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_on_edit_button_after_click_cancel_button_data(self):
        actual_text = self.get_text(*PassageContentPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*PassageContentPageLocators.EDIT_BUTTON)
        self.subject.click_on_cancel_button()
        expected_text = self.get_text(*PassageContentPageLocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def search_by_the_types(self, types):
        self.dropdown_value_selected(types, *PassageContentPageLocators.SEARCH_TYPES)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.is_element_list_present(*Locators.TABLE_ROW_COUNT)

    def search_by_the_question_title_the_data(self, types, question_title):
        self.dropdown_value_selected(types, *PassageContentPageLocators.SEARCH_TYPES)
        self.send_keys(question_title, *ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)    
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.is_element_list_present(*Locators.TABLE_ROW_COUNT)
