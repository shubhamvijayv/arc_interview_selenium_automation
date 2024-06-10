import allure
import pytest

from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.ImageBasedSubjectiveQuestionPage import ImageBasedSubjectiveQuestion
from PageObjects.ExcelQuestionPage import ExcelQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *


@pytest.mark.usefixtures("oneTest")
class TestExcelQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.login = Login(self.driver)
        self.subject = Subject(self.driver)
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)
        self.image_based_subjective_question = ImageBasedSubjectiveQuestion(self.driver)
        self.excel_question = ExcelQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_002_Verify_click_on_excel_question_section(self):
        """Verify_click_on_excel_question_section"""
        self.login.click_on_excel_question_section()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_003_Verify_click_on_add_new_question_button(self):
        """Verify_click_on_add_new_question_button"""
        self.multiple_choice_question.click_on_add_new_question_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_004_Verify_click_on_cancel_button(self):
        """Verify_click_on_cancel_button"""
        self.excel_question.click_on_close_the_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_005_Verify_new_excel_question_with_form(self):
        """Verify_new_excel_question_with_form"""
        self.excel_question.fill_form_excel(generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_006_Verify_click_on_delete_button_after_that_the_dismiss(self):
        """Verify_click_on_delete_button_after_that_the_dismiss"""
        self.excel_question.click_on_delete_button_after_that_the_dismiss()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_007_Verify_click_on_delete_button_and_click_the_accept(self):
        """Verify_click_on_delete_button_and_click_the_accept"""
        self.excel_question.click_on_delete_button_and_click_the_accept()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_008_Verify_add_screenshot_in_existing_excel_sheet(self):
        """Verify_add_screenshot_in_existing_excel_sheet"""
        self.excel_question.add_screenshot_in_existing_excel_sheet(IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_009_Verify_new_excel_question_without_description(self):
        """Verify_new_excel_question_without_description"""
        self.excel_question.form_fill_without_description(generate_random_string_subject())

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_010_Verify_click_on_cancel_button(self):
        """Verify_click_on_cancel_button"""
        self.excel_question.click_on_close_the_button()
