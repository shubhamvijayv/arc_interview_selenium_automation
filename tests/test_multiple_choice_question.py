import allure
import pytest

from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *


@pytest.mark.usefixtures("oneTest")
class TestMultipleChoiceQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002_Verify_of_click_on_multiple_choice_question_section(self):
        """click on multiple choice question section"""
        self.multiple_choice_question.click_on_multiple_choice_question_section()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003_Verify_of_click_on_add_new_question_button(self):
        """click on add new question button"""
        self.multiple_choice_question.click_on_add_new_question_button()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_004_Verify_fill_form(self):
        """fill form"""
        self.multiple_choice_question.fill_form(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())
        self.multiple_choice_question.success_message()
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_005_Verify_fill_form_without_question_title(self):
        """Verify_fill_form_without_question_title"""
        self.multiple_choice_question.fill_form_without_question_title(BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_006_Verify_click_on_close_button(self):
        """click_on_close_button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_007_Verify_fill_form_without_optionA(self):
        """Verify fill form without optionA"""
        self.multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_008_Verify_click_on_close_button(self):
        """Verify click on close button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_009_Verify_fill_form_without_optionB(self):
        """Verify fill form without optionB"""
        self.multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), generate_random_string_subject(), BLANK, generate_random_string_subject(), generate_random_string_subject())
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_010_Verify_click_on_close_button(self):
        """Verify click on close button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_011_Verify_fill_form_without_optionC(self):
        """Verify fill form without optionC"""
        self.multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), BLANK, generate_random_string_subject())

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_012_Verify_click_on_close_button(self):
        """Verify click on close button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_013_Verify_fill_form_without_optionD(self):
        """Verify fill form without optionD"""
        self.multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), BLANK)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_014_Verify_click_on_close_button(self):
        """Verify click on close button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_015_without_fill_any_data_in_form_then_click_on_close_button(self):
        """without_fill_any_data_in_form_then_click_on_close_button"""
        self.multiple_choice_question.without_fill_any_data_in_form_then_click_on_close_button()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_016_form_fill_with_typing_test_subject(self):
        """form_fill_with_typing_test_subject"""
        self.multiple_choice_question.fill_form_with_typing_test_subject(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_017_fill_form_with_excel_subject(self):
        """fill_form_with_excel_subject"""
        self.multiple_choice_question.fill_form_with_excel_subject(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_018_fill_form_invalid_question_title(self):
        """fill_form_invalid_question_title"""
        self.multiple_choice_question.fill_form_with_invalid_data(generate_random_dynamic_string(LENGTH), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_019_fill_form_invalid_optionA(self):
        """fill_form_with_invalid_optionA"""
        self.multiple_choice_question.fill_form_invalid_option(generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_020_fill_form_invalid_optionB(self):
        """fill_form_with_invalid_optionB"""
        self.multiple_choice_question.fill_form_invalid_option(generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject(), generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_021_fill_form_invalid_optionC(self):
        """fill_form_with_invalid_optionC"""
        self.multiple_choice_question.fill_form_invalid_option(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject())

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_022_fill_form_invalid_optionD(self):
        """fill_form_with_invalid_optionD"""
        self.multiple_choice_question.fill_form_invalid_option(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH))

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_023_click_on_close_button(self):
        """click_on_close_button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_024_Verify_search_with_question_title(self):
        """Verify_search_with_question_title"""
        self.multiple_choice_question.search_with_question_title(MCQ_QUESTION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_025_Verify_search_with_subject(self):
        """Verify_search_with_subject"""
        self.multiple_choice_question.search_with_subject()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_026_Verify_search_with_invalid_question_title(self):
        """Verify_search_with_invalid_question_title"""
        self.multiple_choice_question.search_with_invalid_question_title(WRONG_SEARCH)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_027_Verify_search_with_invalid_subject(self):
        """Verify_search_with_invalid_question_title"""
        self.multiple_choice_question.search_with_invalid_subject()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_028_Verify_search_with_valid_question_title_and_invalid_subject(self):
        """search_with_valid_question_title_and_invalid_subject"""
        self.multiple_choice_question.search_with_valid_question_title_and_invalid_subject(MCQ_QUESTION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_029_Verify_search_with_invalid_question_title_and_valid_subject(self):
        """search_with_invalid_question_title_and_valid_subject"""
        self.multiple_choice_question.search_with_invalid_question_title_and_valid_subject(WRONG_SEARCH)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_030_Verify_click_on_delete_button_after_that_accept(self):
        """click_on_delete_button_after_that_accept"""
        self.multiple_choice_question.click_on_delete_button_after_that_accept()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_031_Verify_click_on_delete_button_after_that_dismiss(self):
        """click_on_delete_button_after_that_dismiss"""
        self.multiple_choice_question.click_on_delete_button_after_that_dismiss()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_032_Verify_click_on_edit_button_after_click_cancel_button(self):
        """click_on_edit_button_after_click_cancel_button"""
        self.multiple_choice_question.click_on_edit_button_after_click_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_033_Verify_click_on_edit_button_then_change_subject_excel(self):
        """Verify_click_on_edit_button_then_change_subject_excel"""
        self.multiple_choice_question.click_on_edit_button_then_change_subject_excel()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_034_Verify_click_on_edit_button_then_change_subject_typing_test(self):
        """click_on_edit_button_then_change_subject_typing_test"""
        self.multiple_choice_question.click_on_edit_button_then_change_subject_typing_test()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_035_Verify_click_on_edit_button_then_change_question_title(self):
        """click_on_edit_button_then_change_question_title"""
        self.multiple_choice_question.click_on_edit_button_then_change_question_title(generate_random_string_subject())
