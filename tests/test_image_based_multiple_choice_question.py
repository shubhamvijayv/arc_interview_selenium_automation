import allure
import pytest

from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.ImageBasedMultipleChoiceQuestionPage import ImageBasedMultipleChoiceQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *


@pytest.mark.usefixtures("oneTest")
class TestImageBasedMultipleChoiceQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)
        self.image_based_multiple_choice_question = ImageBasedMultipleChoiceQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002_Verify_of_click_on_image_based_multiple_choice_question_section(self):
        """Verify_of_click_on_image_based_multiple_choice_question_section"""
        self.image_based_multiple_choice_question.click_on_image_based_multiple_choice_question_section()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003_Verify_of_click_on_add_new_question_button(self):
        """Verify_of_click_on_add_new_question_button"""
        self.multiple_choice_question.click_on_add_new_question_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004_Verify_fill_form(self):
        """Verify_of_click_on_add_new_question_button"""
        self.image_based_multiple_choice_question.image_fill_form(generate_random_string_subject(), generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_005_Verify_fill_form_without_subject(self):
        """Verify_fill_form_without_subject"""
        self.image_based_multiple_choice_question.fill_form_without_subject(generate_random_string_subject(), generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_006_Verify_fill_form_without_question_title(self):
        """Verify_fill_form_without_question_title"""
        self.image_based_multiple_choice_question.fill_form_without_question_title(BLANK, generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_007_Verify_fill_form_without_optionA(self):
        """Verify_fill_form_without_optionA"""
        self.image_based_multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), BLANK, generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_008_Verify_fill_form_without_optionB(self):
        """Verify_fill_form_without_optionB"""
        self.image_based_multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), generate_random_string_subject(), BLANK, generate_random_string_subject(), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_009_Verify_fill_form_without_optionC(self):
        """Verify_fill_form_without_optionC"""
        self.image_based_multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), BLANK, generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_010_Verify_fill_form_without_optionD(self):
        """Verify_fill_form_without_optionD"""
        self.image_based_multiple_choice_question.fill_form_without_question_title(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), BLANK, IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_011_Verify_click_add_new_question_button_and_click_cancel_button(self):
        """Verify_click_add_new_question_button_and_click_cancel_button"""
        self.image_based_multiple_choice_question.click_add_new_question_button_and_click_cancel_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_012_Verify_click_on_delete_button_click_dismiss(self):
        """Verify_click_on_delete_button_click_dismiss"""
        self.multiple_choice_question.click_on_delete_button_after_that_dismiss()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_013_Verify_click_on_delete_button_click_accept(self):
        """Verify_click_on_delete_button_click_accept"""
        self.image_based_multiple_choice_question.click_on_delete_button_and_click_accept()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_014_Verify_form_fill_with_typing_test_subject(self):
        """Verify_form_fill_with_typing_test_subject"""
        self.image_based_multiple_choice_question.form_fill_with_typing_test_subject(generate_random_string_subject(), generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_015_Verify_form_fill_with_Excel_subject(self):
        """Verify_form_fill_with_Excel_subject"""
        self.image_based_multiple_choice_question.form_fill_with_Excel_subject(generate_random_string_subject(), generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_016_Verify_form_fill_with_invalid_question_title(self):
        """Verify_form_fill_with_invalid_question_title"""
        self.image_based_multiple_choice_question.form_fill_with_invalid_question_title(generate_random_dynamic_string(LENGTH), generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(),generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_017_Verify_form_fill_with_invalid_optionA(self):
        """Verify_form_fill_with_invalid_optionA"""
        self.image_based_multiple_choice_question.form_fill_with_invalid_option(generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_018_Verify_form_fill_with_invalid_optionB(self):
        """Verify_form_fill_with_invalid_optionB"""
        self.image_based_multiple_choice_question.form_fill_with_invalid_option(generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject(), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_019_Verify_form_fill_with_invalid_optionC(self):
        """Verify_form_fill_with_invalid_optionC"""
        self.image_based_multiple_choice_question.form_fill_with_invalid_option(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), generate_random_string_subject(), IMAGE)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_020_Verify_form_fill_with_invalid_optionD(self):
        """Verify_form_fill_with_invalid_optionD"""
        self.image_based_multiple_choice_question.form_fill_with_invalid_option(generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_string_subject(), generate_random_dynamic_string(OPTION_LENGTH), IMAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_021_click_on_close_button(self):
        """click_on_close_button"""
        self.multiple_choice_question.click_on_close_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_022_Verify_search_by_question_title(self):
        """Verify_search_by_question_title"""
        self.image_based_multiple_choice_question.search_by_question_title(MCQ_QUESTION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_023_Verify_search_by_subject(self):
        """Verify_search_by_subject"""
        self.image_based_multiple_choice_question.search_by_subject()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_024_Verify_search_by_invalid_question_title(self):
        """Verify_search_by_invalid_question_title"""
        self.image_based_multiple_choice_question.search_by_invalid_question_title(WRONG_SEARCH)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_025_Verify_search_by_invalid_subject(self):
        """Verify_search_by_invalid_subject"""
        self.image_based_multiple_choice_question.search_by_invalid_subject()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_026_Verify_search_by_valid_question_title_invalid_subject(self):
        """Verify_search_by_valid_question_title_invalid_subject"""
        self.image_based_multiple_choice_question.search_by_valid_question_title_invalid_subject(MCQ_QUESTION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_027_Verify_search_by_invalid_question_title_valid_subject(self):
        """Verify_search_by_invalid_question_title_valid_subject"""
        self.image_based_multiple_choice_question.search_by_invalid_question_title_valid_subject(WRONG_SEARCH)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_28_Verify_click_edit_button_after_click_cancel_button(self):
        """Verify_click_edit_button_after_click_cancel_button"""
        self.image_based_multiple_choice_question.click_edit_button_after_click_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_29_Verify_click_edit_button_then_change_subject_excel(self):
        """Verify_click_edit_button_then_change_subject_excel"""
        self.image_based_multiple_choice_question.click_edit_button_then_change_subject_excel()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_30_Verify_click_edit_button_then_change_subject_typing_test(self):
        """Verify_click_edit_button_then_change_typing_test"""
        self.image_based_multiple_choice_question.click_edit_button_then_change_typing_test()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_31_Verify_click_edit_button_then_blank_of_question_title(self):
        """Verify_click_edit_button_then_blank_of_question_title"""
        self.image_based_multiple_choice_question.click_edit_button_then_blank_of_question_title()
