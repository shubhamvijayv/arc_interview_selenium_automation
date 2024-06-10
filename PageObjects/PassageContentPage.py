from base.base_page import *
from PageObjects.locators import *
from Utilities.return_message import *
from Utilities.Readconfigurations import *
from Utilities.generate_email import *

from PageObjects.ExcelQuestionPage import ExcelQuestion


class PassageContentQuestion(ExcelQuestion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_new_question_button_of_passage_content(self):
        self.element_click(*PassageContentPageLocators.ADD_NEW_QUESTION_BUTTON)

    def fill_form_of_passage_content(self, type, question_title, subject, description, status):
        self.dropdown_value_selected(type, *PassageContentPageLocators.INPUT_TYPE)
        self.send_keys(question_title, *PassageContentPageLocators.INPUT_QUESTION)
        self.dropdown_value_selected(subject, *PassageContentPageLocators.INPUT_SUBJECT)
        self.send_keys(description, *PassageContentPageLocators.INPUT_DESCRIPTION)
        self.dropdown_value_selected(status, *PassageContentPageLocators.INPUT_STATUS)
        self.element_click(*Locators.SAVE_BUTTON)
