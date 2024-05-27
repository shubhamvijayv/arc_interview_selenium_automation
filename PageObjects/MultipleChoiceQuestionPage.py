from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *


class MultipleChoiceQuestion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def login(self, username, password):
        self.send_keys(username, *LoginPageLocators.INPUT_USERNAME)
        self.send_keys(password, *LoginPageLocators.INPUT_PASSWORD)
        self.element_click(*LoginPageLocators.LOGIN_BUTTON)
        self.is_element_displayed(*Locators.DISPLAY_MESSAGE)

    def click_on_multiple_choice_question_section(self):
        self.wait_for_element(*LoginPageLocators.CLICK_TEXT_MULTIPLE_CHOICE_QUESTION_XPATH)
        self.element_click(*LoginPageLocators.CLICK_TEXT_MULTIPLE_CHOICE_QUESTION_XPATH)

    def click_on_add_new_question_button(self):
        self.element_click(*Locators.ADD_NEW_QUESTION_BUTTON)

    def form_option(self, optionA, optionB, optionC, optionD):
        self.send_keys(optionA, *Locators.INPUT_OPTION_A)
        self.send_keys(optionB, *Locators.INPUT_OPTION_B)
        self.send_keys(optionC, *Locators.INPUT_OPTION_C)
        self.send_keys(optionD, *Locators.INPUT_OPTION_D)

    def question_and_options_is_filled(self, question_title, optionA, optionB, optionC, optionD):
        self.send_keys(question_title, *MultipleChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
        self.form_option(optionA, optionB, optionC, optionD)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)

    def fill_form(self, question_title, optionA, optionB, optionC, optionD):
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.question_and_options_is_filled(question_title, optionA, optionB, optionC, optionD)

    def success_message(self):
        self.is_element_displayed(*Locators.DISPLAY_MESSAGE)

    def fill_form_without_question_title(self, question_title, optionA, optionB, optionC, optionD):
        self.click_on_add_new_question_button()
        self.fill_form(question_title, optionA, optionB, optionC, optionD)
        self.is_element_displayed(*Locators.PARSLEY_REQUIRED)

    def click_on_close_button(self):
        self.element_click(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)

    def without_fill_any_data_in_form_then_click_on_close_button(self):
        actual_text = self.get_text(*Locators.ADD_NEW_QUESTION_BUTTON)
        self.element_click(*Locators.ADD_NEW_QUESTION_BUTTON)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)
        expected_text = ADD_QUESTION
        self.verify_text_match(actual_text, expected_text)

    def fill_form_with_typing_test_subject(self, question_title, optionA, optionB, optionC, optionD):
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT_NEW)
        self.element_click(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT_NEW)
        self.question_and_options_is_filled(question_title, optionA, optionB, optionC, optionD)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = TYPING_VALIDATION
        self.verify_text_match(actual_text, expected_text)

    def fill_form_with_excel_subject(self, question_title, optionA, optionB, optionC, optionD):
        self.click_on_add_new_question_button()
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.question_and_options_is_filled(question_title, optionA, optionB, optionC, optionD)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = EXCEL_VALIDATION
        self.verify_text_match(actual_text, expected_text)

    def wait_for_subject_element_section_and_question_and_option_also(self, question_title, optionA, optionB, optionC, optionD):
        self.click_on_add_new_question_button()
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT)
        self.question_and_options_is_filled(question_title, optionA, optionB, optionC, optionD)

    def fill_form_with_invalid_data(self, question_title, optionA, optionB, optionC, optionD):
        self.wait_for_subject_element_section_and_question_and_option_also(question_title, optionA, optionB, optionC, optionD)
        actual_text = self.get_text(*Locators.PARSLEY_MAXLENGTH)
        expected_text = PARSLEY_MAXLENGTH
        self.verify_text_match(actual_text, expected_text)

    def fill_form_invalid_option(self, question_title, optionA, optionB, optionC, optionD):
        self.click_on_close_button()
        self.wait_for_subject_element_section_and_question_and_option_also(question_title, optionA, optionB, optionC, optionD)
        actual_text = self.get_text(*Locators.PARSLEY_MAXLENGTH)
        expected_text = PARSLEY_MAXLENGTH_ANOTHER
        self.verify_text_match(actual_text, expected_text)

    def search_with_question_title(self, data):
        self.send_keys(data, *MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE).replace(DATA_REPLACE, BLANK)
        self.verify_text_match(actual_text, data)

    def search_with_subject(self):
        self.clear_field(*MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        self.is_element_list_present(*Locators.TABLE_ROW_COUNT)

    def search_with_invalid_question_title(self, data):
        self.element_click(*MultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.send_keys(data, *MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = NO_DATA
        self.verify_text_match(actual_text, expected_text)

    def click_search_button_and_display_message(self):
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = NO_DATA
        self.verify_text_match(actual_text, expected_text)

    def search_with_invalid_subject(self):
        self.clear_field(*MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.WRONG_SUBJECT)
        self.click_search_button_and_display_message()

    def search_with_valid_question_title_and_invalid_subject(self, data):
        self.element_click(*MultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.send_keys(data, *MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_SUBJECT)
        self.click_search_button_and_display_message()

    def search_with_invalid_question_title_and_valid_subject(self, data):
        self.clear_field(*MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.send_keys(data, *MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.ENGLISH_SUBJECT)
        self.click_search_button_and_display_message()

    def click_on_delete_button_after_that_accept(self):
        self.clear_field(*MultipleChoiceQuestionPageLocators.SEARCH_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.WITHOUT_SEARCH_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.SEARCH_BUTTON)
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def click_on_delete_button_after_that_dismiss(self):
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.dismiss()
        expected_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_on_edit_button_after_click_cancel_button(self):
        actual_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.EDIT_BUTTON)
        self.element_click(*MultipleChoiceQuestionPageLocators.CANCEL_BUTTON)
        expected_text = self.get_text(*MultipleChoiceQuestionPageLocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_on_edit_button_then_change_subject_excel(self):
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.element_click(*MultipleChoiceQuestionPageLocators.EXCEL_SUBJECT)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = EXCEL_VALIDATION
        self.verify_text_match(actual_text, expected_text)

    def click_on_edit_button_then_change_subject_typing_test(self):
        self.element_click(*MultipleChoiceQuestionPageLocators.EDIT_BUTTON)
        self.wait_for_element(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT_NEW)
        self.element_click(*MultipleChoiceQuestionPageLocators.INPUT_SUBJECT_NEW)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = TYPING_VALIDATION
        self.verify_text_match(actual_text, expected_text)

    def click_on_edit_button_then_change_question_title(self, data):
        self.element_click(*MultipleChoiceQuestionPageLocators.EDIT_BUTTON)
        self.clear_field(*MultipleChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
        self.send_keys(data, *MultipleChoiceQuestionPageLocators.INPUT_QUESTION_TITLE)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.SAVE_BUTTON)
        actual_text = self.get_text(*Locators.DISPLAY_MESSAGE)
        expected_text = QUESTION_UPDATED
        self.verify_text_match(actual_text, expected_text)
