from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.ImageBasedMultipleChoiceQuestionPage import ImageBasedMultipleChoiceQuestion


class SubjectiveQuestion(ImageBasedMultipleChoiceQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def form_fill_with_question_answer_instruction(self, question_title, answer_key, instruction):
        self.send_keys(question_title, *SubjectiveQuestionPagelocators.INPUT_QUESTION_TITLE)
        self.send_keys(answer_key, *SubjectiveQuestionPagelocators.INPUT_ANSWER_KEY)
        self.send_keys(instruction, *SubjectiveQuestionPagelocators.INPUT_INSTRUCTION)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)

    def subjective_question_added_success_message(self, message):
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = message
        self.verify_text_match(actual_text, expected_text)

    def subject_and_passage_both_were_filling(self, subject, passage, question_title, answer_key, instruction):
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.INPUT_SUBJECT)
        self.dropdown_value_selected(passage, *SubjectiveQuestionPagelocators.INPUT_PASSAGE)
        self.form_fill_with_question_answer_instruction(question_title, answer_key, instruction)

    def form_fill_by_proper(self, subject, passage, question_title, answer_key, instruction):
        self.subject_and_passage_both_were_filling(subject, passage, question_title, answer_key, instruction)
        self.subjective_question_added_success_message(SUBJECTIVE_ADDED)

    def form_fill_without_subject(self, passage, question_title, answer_key, instruction):
        self.click_on_add_new_question_button()
        self.dropdown_value_selected(passage, *SubjectiveQuestionPagelocators.INPUT_PASSAGE)
        self.form_fill_with_question_answer_instruction(question_title, answer_key, instruction)
        self.validate_using_parsley_required_method()

    def form_fill_without_passage(self, subject, question_title, answer_key, instruction):
        self.click_on_close_button()
        self.click_on_add_new_question_button()
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.INPUT_SUBJECT)
        self.form_fill_with_question_answer_instruction(question_title, answer_key, instruction)
        self.subjective_question_added_success_message(SUBJECTIVE_ADDED)

    def click_add_new_question_with_form_filled(self, subject, passage, question_title, answer_key, instruction):
        self.click_on_add_new_question_button()
        self.subject_and_passage_both_were_filling(subject, passage, question_title, answer_key, instruction)

    def form_fill_without_question_title(self, subject, passage, question_title, answer_key, instruction):
        self.click_add_new_question_with_form_filled(subject, passage, question_title, answer_key, instruction)
        self.validate_using_parsley_required_method()

    def form_fill_without_answer_key(self, subject, passage, question_title, answer_key, instruction):
        self.click_on_close_button()
        self.form_fill_without_question_title(subject, passage, question_title, answer_key, instruction)

    def form_fill_without_instruction(self, subject, passage, question_title, answer_key, instruction):
        self.click_on_close_button()
        self.click_add_new_question_with_form_filled(subject, passage, question_title, answer_key, instruction)
        self.subjective_question_added_success_message(SUBJECTIVE_ADDED)

    def form_fill_with_typing_test_subject_or_excel_subject(self, subject, passage, question_title, answer_key, instruction, validation):
        self.click_add_new_question_with_form_filled(subject, passage, question_title, answer_key, instruction)
        self.subjective_question_added_success_message(validation)

    def validate_parsley_maxlength_validation(self, maxlength):
        actual_text = self.get_text(*Locators.PARSLEY_MAXLENGTH)
        expected_text = maxlength
        self.verify_text_match(actual_text, expected_text)

    def add_new_question_with_question_title_validation(self, subject, passage, question_title, answer_key, instruction, maxlength):
        self.click_add_new_question_with_form_filled(subject, passage, question_title, answer_key, instruction)
        self.validate_parsley_maxlength_validation(maxlength)
    
    def add_new_question_with_answer_key_validation(self, subject, passage, question_title, answer_key, instruction, maxlength):
        self.click_on_close_button()
        self.add_new_question_with_question_title_validation(subject, passage, question_title, answer_key, instruction, maxlength)

    def click_on_cancel_button_without_fill_any_information(self):
        self.click_on_close_button()
        self.click_on_add_new_question_button()
        self.click_on_close_button()
        
    def search_by_the_question_title(self, question_title):
        self.click_on_close_button()
        self.send_keys(question_title, *SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)

    def search_by_the_subject(self, subject):
        self.clear_field(*SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.SEARCH_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        
    def search_invalid_question_title(self, subject, question_title):
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.SEARCH_SUBJECT)
        self.send_keys(question_title, *SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.subjective_question_added_success_message(NO_DATA)

    def search_invalid_subject(self, subject):
        self.clear_field(*SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.SEARCH_SUBJECT)
        self.subjective_question_added_success_message(NO_DATA)

    def search_valid_question_title_with_invalid_subject(self, question_title):
        self.send_keys(question_title, *SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.subjective_question_added_success_message(NO_DATA)

    def search_invalid_question_title_with_valid_subject(self, subject, question_title):
        self.clear_field(*SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.SEARCH_SUBJECT)
        self.send_keys(question_title, *SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.subjective_question_added_success_message(NO_DATA)

    def click_delete_button_and_click_accept(self, subject):
        self.clear_field(*SubjectiveQuestionPagelocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *SubjectiveQuestionPagelocators.SEARCH_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def click_delete_button_after_that_dismiss(self):
        actual_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.dismiss()
        expected_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_on_edit_button_after_that_cancel_button(self):
        self.element_click(*Locators.EDIT_BUTTON)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)
