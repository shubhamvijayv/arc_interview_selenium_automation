from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.SubjectiveQuestionPage import SubjectiveQuestion


class ImageBasedSubjectiveQuestion(SubjectiveQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def form_filled_with_all_inputs_after_click_on_save_button(self, subject, question, answer_key, image):
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.INPUT_SUBJECT)
        self.send_keys(question, *ImageBasedSubjectiveQuestionPageLocators.INPUT_QUESTION)
        self.send_keys(answer_key, *ImageBasedSubjectiveQuestionPageLocators.INPUT_ANSWER_KEY)
        self.send_keys(image, *ImageBasedSubjectiveQuestionPageLocators.INPUT_IMAGE)
        self.element_click(*Locators.SAVE_BUTTON)

    def form_filled(self, subject, question, answer_key, image, message):
        self.form_filled_with_all_inputs_after_click_on_save_button(subject, question, answer_key, image)
        self.subjective_question_added_success_message(message)

    def form_filled_up(self, subject, question, answer_key, image, message):
        self.click_on_add_new_question_button()
        self.form_filled(subject, question, answer_key, image, message)
        
    def click_on_save_button_after_display_validation_message_properly(self):
        self.element_click(*Locators.SAVE_BUTTON)
        self.validate_using_parsley_required_method()

    def form_fill_without_image(self, subject, question, answer_key):
        self.click_on_add_new_question_button()
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.INPUT_SUBJECT)
        self.send_keys(question, *ImageBasedSubjectiveQuestionPageLocators.INPUT_QUESTION)
        self.send_keys(answer_key, *ImageBasedSubjectiveQuestionPageLocators.INPUT_ANSWER_KEY)
        self.click_on_save_button_after_display_validation_message_properly()

    def click_on_cancl_button_after_click_on_add_question_button(self):
        self.element_click(*Locators.CLOSE_BUTTON)
        self.click_on_add_new_question_button()

    def form_fill_without_answer_key_input(self, subject, question, image):
        self.click_on_cancl_button_after_click_on_add_question_button()
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.INPUT_SUBJECT)
        self.send_keys(question, *ImageBasedSubjectiveQuestionPageLocators.INPUT_QUESTION)
        self.send_keys(image, *ImageBasedSubjectiveQuestionPageLocators.INPUT_IMAGE)
        self.click_on_save_button_after_display_validation_message_properly()

    def form_fill_without_question(self, subject, answer_key, image):
        self.click_on_cancl_button_after_click_on_add_question_button()
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.INPUT_SUBJECT)
        self.send_keys(answer_key, *ImageBasedSubjectiveQuestionPageLocators.INPUT_ANSWER_KEY)
        self.send_keys(image, *ImageBasedSubjectiveQuestionPageLocators.INPUT_IMAGE)
        self.click_on_save_button_after_display_validation_message_properly()

    def form_fill_without_subject_data(self, question, answer_key, image):
        self.click_on_cancl_button_after_click_on_add_question_button()
        self.send_keys(question, *ImageBasedSubjectiveQuestionPageLocators.INPUT_QUESTION)
        self.send_keys(answer_key, *ImageBasedSubjectiveQuestionPageLocators.INPUT_ANSWER_KEY)
        self.send_keys(image, *ImageBasedSubjectiveQuestionPageLocators.INPUT_IMAGE)
        self.click_on_save_button_after_display_validation_message_properly()
        self.waiting_time_element()

    def form_filled_with_typing_test_subject(self, subject, question, answer_key, image):
        self.click_on_cancl_button_after_click_on_add_question_button()
        self.form_filled(subject, question, answer_key, image, TYPING_VALIDATION)

    def form_filled_with_invalid_image(self, subject, question, answer_key, image):
        self.click_on_add_new_question_button()
        self.form_filled_with_all_inputs_after_click_on_save_button(subject, question, answer_key, image)
        actual_text = self.get_text(*Locators.PARSLEY_FILEEXTENSION)
        expected_text = PARSLEY_FILEEXTENSION
        self.verify_text_match(actual_text, expected_text)

    def click_on_the_delete_button_after_that_dismiss(self):
        self.element_click(*Locators.CLOSE_BUTTON)
        self.click_delete_button_after_that_dismiss()

    def click_on_the_delete_button_and_click_accept(self):
        actual_text = self.get_text(*ImageBasedSubjectiveQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*ImageBasedSubjectiveQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def search_by_the_question_title_data(self, question_title):
        self.send_keys(question_title, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)

    def search_by_the_subject_data(self, subject):
        self.clear_field(*ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.send_keys(Keys.RETURN, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)

    def search_by_the_question_or_invalid_subject(self, subject):
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.subjective_question_added_success_message(NO_DATA)

    def search_by_the_invalid_question_or_subject(self, subject, question_title):
        self.clear_field(*ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.send_keys(Keys.RETURN, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_SUBJECT)
        self.send_keys(question_title, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.subjective_question_added_success_message(NO_DATA)

    def click_on_edit_button_after_click_on_close_button(self, subject):
        self.clear_field(*ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.send_keys(Keys.RETURN, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_QUESTION)
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*Locators.EDIT_BUTTON)
        time.sleep(5)
        self.element_click(*Locators.CLOSE_BUTTON)

    def click_on_edit_button_then_change_the_subject(self, subject):
        self.element_click(*Locators.EDIT_BUTTON)
        self.dropdown_value_selected(subject, *ImageBasedSubjectiveQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*Locators.SAVE_BUTTON)
        self.subjective_question_added_success_message(QUESTION_UPDATE)

    def click_on_edit_button_then_change_the_question(self, question_title):
        self.element_click(*Locators.EDIT_BUTTON)
        self.clear_field(*ImageBasedSubjectiveQuestionPageLocators.INPUT_QUESTION)
        self.send_keys(question_title, *ImageBasedSubjectiveQuestionPageLocators.INPUT_QUESTION)
        self.element_click(*Locators.SAVE_BUTTON)
        self.subjective_question_added_success_message(QUESTION_UPDATE)

    def click_on_edit_button_then_change_the_answer_key(self, answer_key):
        self.element_click(*Locators.EDIT_BUTTON)
        self.clear_field(*ImageBasedSubjectiveQuestionPageLocators.INPUT_ANSWER_KEY)
        self.send_keys(answer_key, *ImageBasedSubjectiveQuestionPageLocators.INPUT_ANSWER_KEY)
        self.element_click(*Locators.SAVE_BUTTON)
        self.subjective_question_added_success_message(QUESTION_UPDATE)
