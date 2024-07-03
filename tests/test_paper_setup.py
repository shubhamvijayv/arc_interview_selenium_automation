import allure
import pytest

from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.ImageBasedSubjectiveQuestionPage import ImageBasedSubjectiveQuestion
from PageObjects.ExcelQuestionPage import ExcelQuestion
from PageObjects.PassageContentPage import PassageContentQuestion
from PageObjects.PaperSetupQuestionPage import PaperSetupQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("oneTest")
class TestPaperSetupQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.login = Login(self.driver)
        self.subject = Subject(self.driver)
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)
        self.image_based_subjective_question = ImageBasedSubjectiveQuestion(self.driver)
        self.excel_question = ExcelQuestion(self.driver)
        self.passage = PassageContentQuestion(self.driver)
        self.paper_setup_question = PaperSetupQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)    
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_002_Verify_click_on_paper_setup_section(self):
        """Verify_click_on_paper_setup_section"""
        self.login.click_on_paper_setup_section()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003_Verify_click_on_edit_button_and_task_completed(self):
        """Verify_click_on_edit_button_and_task_completed"""
        self.paper_setup_question.click_on_edit_button_after_task_completed()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004_Verify_display_task_completed_message_and_click_on_save_button(self):
        """Verify_display_task_completed_message_and_click_on_save_button"""
        self.paper_setup_question.display_task_completed_message_and_click_on_save_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_005_Verify_click_on_delete_button_after_dismiss(self):
        """Verify_click_on_delete_button_after_dismiss"""
        self.paper_setup_question.click_on_delete_button_after_dismiss()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_006_Verify_click_on_delete_button_after_accept(self):
        """Verify_click_on_delete_button_after_accept"""
        self.paper_setup_question.click_on_delete_button_after_accept()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_007_Verify_click_on_add_paper_button(self):
        """Verify_click_on_add_paper_button"""
        self.paper_setup_question.click_on_add_paper_button()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_008_Verify_click_on_add_paper_button(self):
        """Verify_click_on_add_paper_button"""
        self.paper_setup_question.click_on_add_paper_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_009_Verify_click_on_edit_button_then_update_the_something(self):
        """Verify_click_on_edit_button_then_update_the_something"""
        self.paper_setup_question.click_on_edit_button_then_update_the_something(TIME_DURATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_010_Verify_click_on_save_button(self):
        """Verify_click_on_edit_button_then_update_the_something"""
        self.paper_setup_question.click_on_the_save_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_011_Verify_click_on_grade_button(self):
        """Verify_click_on_grade_button"""
        self.paper_setup_question.click_on_add_new_grade_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012_Verify_fill_grade_form_to_option(self):
        """Verify_fill_grade_form_to_option"""
        self.paper_setup_question.fill_grade_form_to_option(0, 25, 'd')
