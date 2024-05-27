from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion

class ImageBasedMultipleChoiceQuestion(MultipleChoiceQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_on_image_based_multiple_choice_question_section(self):
        self.wait_for_element(*LoginPageLocators.CLICK_TEXT_IMAGE_BASED_MULTIPLE_CHOICE_QUESTION_XPATH)
        self.element_click(*LoginPageLocators.CLICK_TEXT_IMAGE_BASED_MULTIPLE_CHOICE_QUESTION_XPATH)

    def form_with_save_button(self, question_title, optionA, optionB, optionC, optionD, image):
        self.send_keys(question_title, *ImageBasedMultipleChoiceQuestionPageLocators.QUESTION_TITLE)
        self.form_option(optionA, optionB, optionC, optionD)
        self.send_keys(image, *ImageBasedMultipleChoiceQuestionPageLocators.IMAGE)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)

    def fill_form_data(self, question_title, optionA, optionB, optionC, optionD, image):
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.form_with_save_button(question_title, optionA, optionB, optionC, optionD, image)

    def image_fill_form(self, question_title, optionA, optionB, optionC, optionD, image):
        self.fill_form_data(question_title, optionA, optionB, optionC, optionD, image)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = QUESTION_ADDED
        self.verify_text_match(actual_text, expected_text)

    def validate_using_parsley_required_method(self):
        actual_text = self.get_text(*Locators.PARSLEY_REQUIRED)
        expected_text = PARSLEY_REQUIRED_NEW
        self.verify_text_match(actual_text, expected_text)

    def validate_of_actual_text_or_expected_text(self, question_title, optionA, optionB, optionC, optionD, image):
        self.form_with_save_button(question_title, optionA, optionB, optionC, optionD, image)
        self.validate_using_parsley_required_method()
    
    def fill_form_without_subject(self, question_title, optionA, optionB, optionC, optionD, image):
        self.click_on_add_new_question_button()
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.WITHOUT_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.WITHOUT_SUBJECT)
        self.validate_of_actual_text_or_expected_text(question_title, optionA, optionB, optionC, optionD, image)

    def fill_form_without_question_title(self, question_title, optionA, optionB, optionC, optionD, image):
        self.click_on_close_button()
        self.click_on_add_new_question_button()
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.validate_of_actual_text_or_expected_text(question_title, optionA, optionB, optionC, optionD, image)

    def click_add_new_question_button_and_click_cancel_button(self):
        self.click_on_close_button()
        self.click_on_add_new_question_button()
        self.wait_for_element(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)
        self.click_on_close_button()

    def click_on_delete_button_and_click_accept(self):
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def check_typing_test_validation(self):
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = TYPING_VALIDATION
        self.verify_text_match(actual_text, expected_text)

    def form_fill_with_typing_test_subject(self,question_title, optionA, optionB, optionC, optionD, image):
        self.click_on_add_new_question_button()
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.TYPING_TEST_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.TYPING_TEST_SUBJECT)
        self.form_with_save_button(question_title, optionA, optionB, optionC, optionD, image)
        self.check_typing_test_validation()

    def check_excel_validation(self):
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = EXCEL_VALIDATION
        self.verify_text_match(actual_text, expected_text)

    def form_fill_with_Excel_subject(self,question_title, optionA, optionB, optionC, optionD, image):
        self.click_on_add_new_question_button()
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.form_with_save_button(question_title, optionA, optionB, optionC, optionD, image)
        self.check_excel_validation()

    def form_fill_with_invalid_question_title(self, question_title, optionA, optionB, optionC, optionD, image):
        self.click_on_add_new_question_button()
        self.fill_form_data(question_title, optionA, optionB, optionC, optionD, image)
        actual_text = self.get_text(*Locators.PARSLEY_MAXLENGTH)
        expected_text = PARSLEY_MAXLENGTH
        self.verify_text_match(actual_text, expected_text)

    def form_fill_with_invalid_option(self, question_title, optionA, optionB, optionC, optionD, image):
        self.click_on_close_button()
        self.click_on_add_new_question_button()
        self.fill_form_data(question_title, optionA, optionB, optionC, optionD, image)
        actual_text = self.get_text(*Locators.PARSLEY_MAXLENGTH)
        expected_text = PARSLEY_MAXLENGTH_ANOTHER
        self.verify_text_match(actual_text, expected_text)

    def search_by_question_title(self, question_title):
        self.click_on_close_button()
        self.send_keys(question_title, *ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE).replace(REPLACE_DATA, BLANK)
        self.verify_text_match(actual_text, question_title)

    def search_by_subject(self):
        self.clear_field(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.is_element_list_present(*Locators.TABLE_ROW_COUNT)

    def validate_actual_text_or_expected_text(self):
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = NO_DATA
        self.verify_text_match(actual_text, expected_text)

    def search_by_invalid_question_title(self, question_title):
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.send_keys(question_title, *ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.validate_actual_text_or_expected_text()

    def search_by_invalid_subject(self):
        self.clear_field(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.WRONG_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.validate_actual_text_or_expected_text()

    def search_by_valid_question_title_invalid_subject(self, question_title):
        self.send_keys(question_title, *ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.validate_actual_text_or_expected_text()

    def search_by_invalid_question_title_valid_subject(self, question_title):
        self.clear_field(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.send_keys(question_title, *ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.validate_actual_text_or_expected_text()

    def click_edit_button_after_click_cancel_button(self):
        self.clear_field(*ImageBasedMultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*Locators.EDIT_BUTTON)
        self.element_click(*MultipleChoiceQuestionPageLocators.CANCEL_BUTTON)
        expected_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_edit_button_then_change_subject_excel(self):
        self.element_click(*Locators.EDIT_BUTTON)
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
        self.check_excel_validation()

    def click_edit_button_then_change_typing_test(self):
        self.element_click(*Locators.EDIT_BUTTON)
        self.wait_for_element(*ImageBasedMultipleChoiceQuestionPageLocators.TYPING_TEST_SUBJECT)
        self.element_click(*ImageBasedMultipleChoiceQuestionPageLocators.TYPING_TEST_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
        self.check_typing_test_validation()

    def click_edit_button_then_blank_of_question_title(self):
        self.element_click(*Locators.EDIT_BUTTON)
        self.clear_field(*ImageBasedMultipleChoiceQuestionPageLocators.QUESTION_TITLE)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
        self.validate_using_parsley_required_method()
