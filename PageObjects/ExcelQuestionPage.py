from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.ImageBasedSubjectiveQuestionPage import ImageBasedSubjectiveQuestion


class ExcelQuestion(ImageBasedSubjectiveQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_close_the_button(self):
        self.wait_for_element(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)
        self.element_click(*MultipleImageChoiceQuestionPageLocators.CLOSE_BUTTON)

    def fill_form_excel(self, question_title, description):
        self.click_on_add_new_question_button()
        self.send_keys(question_title, *ExcelQuestionPageLocators.INPUT_QUESTION)
        self.send_keys(description, *ExcelQuestionPageLocators.INPUT_DESCRIPTION)
        self.element_click(*ExcelQuestionPageLocators.SAVE_BUTTON)
        self.subjective_question_added_success_message(QUESTION_ADDED)
    
    def form_fill_without_description(self, question_title):
        self.click_on_add_new_question_button()
        self.send_keys(question_title, *ExcelQuestionPageLocators.INPUT_QUESTION)
        self.element_click(*ExcelQuestionPageLocators.SAVE_BUTTON)
        self.validate_using_parsley_required_method()

    def form_fill_the_without_question_title(self, description):
        self.element_click(*ExcelQuestionPageLocators.ADD_QUESTION_BUTTON)
        self.send_keys(description, *ExcelQuestionPageLocators.INPUT_DESCRIPTION)
        self.element_click(*ExcelQuestionPageLocators.SAVE_BUTTON)
        actual_text = self.get_text(*Locators.PARSLEY_REQUIRED)
        expected_text = PARSLEY_REQUIRED_NEW
        self.verify_text_match(actual_text, expected_text)

    def click_on_delete_button_after_that_the_dismiss(self):
        actual_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.dismiss()
        expected_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.verify_text_match(actual_text, expected_text)

    def click_on_delete_button_and_click_the_accept(self):
        actual_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.element_click(*MultipleChoiceQuestionPageLocators.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()
        expected_text = self.get_text(*SubjectiveQuestionPagelocators.TABLE_QUESTION_TITLE)
        self.not_match_text(actual_text, expected_text)

    def add_screenshot_in_existing_excel_sheet(self, image):
        self.element_click(*Locators.EDIT_BUTTON)
        self.send_keys(image, *ExcelQuestionPageLocators.UPLOAD_IMAGE)
        self.element_click(*ExcelQuestionPageLocators.IMAGE_BUTTON)
        self.subjective_question_added_success_message(QUESTION_UPDATE)
