import allure
import pytest

from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.ImageBasedSubjectiveQuestionPage import ImageBasedSubjectiveQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("oneTest")
class TestImageBasedSubjectiveQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.login = Login(self.driver)
        self.subject = Subject(self.driver)
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)
        self.image_based_subjective_question = ImageBasedSubjectiveQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_002_Verify_click_on_image_based_subjective_question_section(self):
        """Verify_click_on_image_based_subjective_question_section"""
        self.login.click_on_image_based_subjective_question_section()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_003_Verify_click_on_add_new_question_button(self):
        """Verify_click_on_add_new_question_button"""
        self.multiple_choice_question.click_on_add_new_question_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_004_Verify_click_on_cancel_button_without_fill_the_form(self):
        """Verify_click_on_cancel_button_without_fill_the_form"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_005_Verify_form_filled_up_properly(self):
        """Verify_form_filled_up_properly"""
        self.image_based_subjective_question.form_filled_up(HINDI, generate_random_string_subject(), generate_random_string_subject(), IMAGE, QUESTION_ADDED)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_006_Verify_form_filled_without_image(self):
        """Verify_form_filled_without_image"""
        self.image_based_subjective_question.form_fill_without_image(HINDI, generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_007_Verify_form_filled_without_answer_key(self):
        """Verify_form_filled_without_answer_key"""
        self.image_based_subjective_question.form_fill_without_answer_key_input(HINDI, generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_008_Verify_form_filled_without_question(self):
        """Verify_form_filled_without_question"""
        self.image_based_subjective_question.form_fill_without_question(HINDI, generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_009_Verify_form_filled_without_subject(self):
        """Verify_form_filled_without_subject"""
        self.image_based_subjective_question.form_fill_without_subject_data(generate_random_string_subject(), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_010_Verify_form_filled_with_typing_test_subject(self):
        """form_filled_with_typing_test_subject"""
        self.image_based_subjective_question.form_filled_with_typing_test_subject(TYPING_TEST, generate_random_string_subject(), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_011_Verify_form_filled_with_excel_subject(self):
        """form_filled_with_excel_subject"""
        self.image_based_subjective_question.form_filled_up(EXCEL, generate_random_string_subject(), generate_random_string_subject(), IMAGE, EXCEL_VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_012_Verify_form_filled_with_invalid_image(self):
        """Verify_form_filled_with_invalid_image"""
        self.image_based_subjective_question.form_filled_with_invalid_image(HINDI, generate_random_string_subject(), generate_random_string_subject(), IMAGE_ONE)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_013_Verify_click_on_the_delete_button_after_that_dismiss(self):
        """Verify_click_on_the_delete_button_after_that_dismiss"""
        self.image_based_subjective_question.click_on_the_delete_button_after_that_dismiss()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_014_Verify_click_on_the_delete_button_and_click_accept(self):
        """Verify_click_on_the_delete_button_and_click_accept"""
        self.image_based_subjective_question.click_on_the_delete_button_and_click_accept()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_015_Verify_search_by_the_question_title(self):
        """Verify_search_by_the_question_title"""
        self.image_based_subjective_question.search_by_the_question_title_data(MCQ_QUESTION)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_016_Verify_search_by_the_subject(self):
        """Verify_search_by_the_subject"""
        self.image_based_subjective_question.search_by_the_subject_data(HINDI)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_017_Verify_search_by_the_question_or_subject(self):
        """Verify_search_by_the_question_or_subject"""
        self.image_based_subjective_question.search_by_the_question_title_data(MCQ_QUESTION)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_018_Verify_search_by_the_question_or_invalid_subject(self):
        """Verify_search_by_the_question_or_invalid_subject"""
        self.image_based_subjective_question.search_by_the_question_or_invalid_subject(MATHS)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_019_Verify_search_by_the_invalid_question_or_subject(self):
        """Verify_search_by_the_invalid_question_or_subject"""
        self.image_based_subjective_question.search_by_the_invalid_question_or_subject(HINDI, WRONG_SEARCH)
        time.sleep(5)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_020_Verify_click_on_edit_button_after_click_on_cancel_button(self):
        """Verify_click_on_edit_button_after_click_on_cancel_button"""
        self.image_based_subjective_question.click_on_edit_button_after_click_on_close_button(DASH_DATA)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_021_Verify_click_on_edit_button_then_change_the_subject(self):
        """Verify_click_on_edit_button_then_change_the_subject"""
        self.image_based_subjective_question.click_on_edit_button_then_change_the_subject(ENGLISH)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_022_Verify_click_on_edit_button_then_change_the_question(self):
        """Verify_click_on_edit_button_then_change_the_subject"""
        self.image_based_subjective_question.click_on_edit_button_then_change_the_question(generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_023_Verify_click_on_edit_button_then_change_the_answer_key(self):
        """Verify_click_on_edit_button_then_change_the_answer_key"""
        self.image_based_subjective_question.click_on_edit_button_then_change_the_answer_key(generate_random_string_subject())
