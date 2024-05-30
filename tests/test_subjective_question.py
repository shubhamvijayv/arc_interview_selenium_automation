import allure
import pytest

from PageObjects.LoginPage import Login
from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.SubjectiveQuestionPage import SubjectiveQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *


@pytest.mark.usefixtures("oneTest")
class TestSubjectiveQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.login = Login(self.driver)
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)
        self.subjective_question = SubjectiveQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_002_Verify_click_on_subjective_question_section(self):
        """Verify_click_on_subjective_question_section"""
        self.login.click_on_subjective_question_section()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_003_Verify_click_on_add_new_question_button(self):
        """Verify_click_on_subjective_question_section"""
        self.multiple_choice_question.click_on_add_new_question_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_004_Verify_add_new_question(self):
        """Verify_add_new_question"""
        self.subjective_question.form_fill_by_proper(HINDI, PASSAGE_DATA, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_005_Verify_add_new_question_button_without_subject(self):
        """Verify_add_new_question_button_without_subject"""
        self.subjective_question.form_fill_without_subject(PASSAGE_DATA, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_006_Verify_add_new_question_button_without_passage(self):
        """Verify_add_new_question_button_without_passage"""
        self.subjective_question.form_fill_without_passage(HINDI, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_007_Verify_add_new_question_button_without_question_title(self):
        """Verify_add_new_question_button_without_question_title"""
        self.subjective_question.form_fill_without_question_title(HINDI, PASSAGE_DATA, BLANK, generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_008_Verify_add_new_question_button_without_answer_key(self):
        """Verify_add_new_question_button_without_answer_key"""
        self.subjective_question.form_fill_without_answer_key(HINDI, PASSAGE_DATA, generate_random_string_subject(), BLANK, generate_random_string_subject())

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_009_Verify_add_new_question_button_without_instruction(self):
        """Verify_add_new_question_button_without_instruction"""
        self.subjective_question.form_fill_without_instruction(HINDI, PASSAGE_DATA, generate_random_string_subject(), generate_random_string_subject(), BLANK)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_010_Verify_add_new_question_with_typing_test_subject(self):
        """Verify_add_new_question_with_typing_test_subject"""
        self.subjective_question.form_fill_with_typing_test_subject_or_excel_subject(TYPING_TEST, PASSAGE_DATA, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), TYPING_VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_011_Verify_add_new_question_with_excel_subject(self):
        """Verify_add_new_question_with_excel_subject"""
        self.subjective_question.form_fill_with_typing_test_subject_or_excel_subject(EXCEL, PASSAGE_DATA, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), EXCEL_VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_012_Verify_add_new_question_with_question_title_validation(self):
        """Verify_add_new_question_with_question_title_validation"""
        self.subjective_question.add_new_question_with_question_title_validation(EXCEL, PASSAGE_DATA, generate_random_dynamic_string(INVALID_LENGTH_STRING), generate_random_string_subject(), generate_random_string_subject(), PARSLEY_MAXLENGTH)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_013_Verify_add_new_question_with_answer_key_validation(self):
        """Verify_add_new_question_with_answer_key_validation"""
        self.subjective_question.add_new_question_with_answer_key_validation(EXCEL, PASSAGE_DATA, generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject(), PARSLEY_MAXLENGTH_ANOTHER)
        
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_014_Verify_add_new_question_with_instruction(self):
        """Verify_add_new_question_with_instruction"""
        self.subjective_question.add_new_question_with_answer_key_validation(EXCEL, PASSAGE_DATA, generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), PARSLEY_MAXLENGTH_HUNDRED)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_015_Verify_search_by_question_title(self):
        """search_by_question_title"""
        self.subjective_question.search_by_the_question_title(MCQ_QUESTION)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_016_Verify_search_by_subject(self):
        """Verify_search_by_subject"""
        self.subjective_question.search_by_the_subject(HINDI)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_017_Verify_search_by_invalid_question_title(self):
        """Verify_search_by_te_invalid_question_title"""
        self.subjective_question.search_invalid_question_title(SELECT_SUBJECT, WRONG_SEARCH)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_018_Verify_search_invalid_subject(self):
        """Verify_search_by_te_invalid_question_title"""
        self.subjective_question.search_invalid_subject(EXCEL)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_019_Verify_search_valid_question_title_with_invalid_subject(self):
        """Verify_search_valid_question_title_with_invalid_subject"""
        self.subjective_question.search_valid_question_title_with_invalid_subject(MCQ_QUESTION)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_020_Verify_search_invalid_question_title_with_valid_subject(self):
        """Verify_search_invalid_question_title_with_valid_subject"""
        self.subjective_question.search_invalid_question_title_with_valid_subject(HINDI, WRONG_SEARCH)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_021_Verify_click_on_delete_button_accept(self):
        """Verify_click_on_delete_button_accept"""
        self.subjective_question.click_delete_button_and_click_accept(SELECT_SUBJECT)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_022_Verify_click_on_delete_button_dismiss(self):
        """Verify_click_on_delete_button_dismiss"""
        self.subjective_question.click_delete_button_after_that_dismiss()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_023_Verify_click_edit_button_then_click_cancel_button(self):
        """Verify_click_on_delete_button_dismiss"""
        self.subjective_question.click_on_edit_button_after_that_cancel_button()
