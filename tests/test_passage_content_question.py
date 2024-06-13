import allure
import pytest

from PageObjects.LoginPage import Login
from PageObjects.SubjectPage import Subject
from PageObjects.MultipleChoiceQuestionPage import MultipleChoiceQuestion
from PageObjects.ImageBasedSubjectiveQuestionPage import ImageBasedSubjectiveQuestion
from PageObjects.ExcelQuestionPage import ExcelQuestion
from PageObjects.PassageContentPage import PassageContentQuestion
from Utilities.Readconfigurations import read_configuration
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *
from Utilities.generate_email import *

@pytest.mark.usefixtures("oneTest")
class TestPassageQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTest):
        self.login = Login(self.driver)
        self.subject = Subject(self.driver)
        self.multiple_choice_question = MultipleChoiceQuestion(self.driver)
        self.image_based_subjective_question = ImageBasedSubjectiveQuestion(self.driver)
        self.excel_question = ExcelQuestion(self.driver)
        self.passage = PassageContentQuestion(self.driver)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001_Verify_of_login_functionality(self):
        """Verify of login functionality"""
        self.multiple_choice_question.login(read_configuration("crediential","login_username"), read_configuration("crediential","login_password"))
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_002_Verify_click_on_excel_question_section(self):
        """Verify_click_on_excel_question_section"""
        self.login.click_on_passage_content_section()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_003_Verify_click_on_add_new_question_button(self):
        """Verify_click_on_add_new_question_button"""
        self.passage.add_new_question_button_of_passage_content()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_004_Verify_fill_form_of_passage_content(self):
        """Verify_fill_form_of_passage_content"""
        self.passage.form_successfully_submitted(PASSAGE, generate_random_string_subject(), HINDI, generate_random_string_subject(), STATUS)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_005_Verify_fill_form_of_passage_content_without_status(self):
        """Verify_fill_form_of_passage_content_without_status"""
        self.passage.fill_form_submitted_without_status(PASSAGE, generate_random_string_subject(), HINDI, generate_random_string_subject(), DASH_DATA)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_006_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_007_Verify_fill_form_of_passage_content_without_description(self):
        """Verify_fill_form_of_passage_content_without_description"""
        self.passage.fill_form_submitted_without_status(PASSAGE, generate_random_string_subject(), HINDI, BLANK, STATUS)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_008_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_009_Verify_fill_form_of_passage_content_without_subject(self):
        """Verify_fill_form_of_passage_content_without_subject"""
        self.passage.fill_form_submitted_without_status(PASSAGE, generate_random_string_subject(), DASH_DATA, generate_random_string_subject(), STATUS)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_010_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_011_Verify_fill_form_of_passage_content_without_question(self):
        """Verify_fill_form_of_passage_content_without_question"""
        self.passage.fill_form_submitted_without_status(PASSAGE, BLANK, HINDI, generate_random_string_subject(), STATUS)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_013_Verify_fill_form_of_passage_content_without_types(self):
        """Verify_fill_form_of_passage_content_without_types"""
        self.passage.fill_form_submitted_without_status(DASH_DATA, generate_random_string_subject(), HINDI, generate_random_string_subject(), STATUS)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_014_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_015_Verify_fill_form_of_passage_content_with_instruction_types(self):
        """Verify_fill_form_of_passage_content_with_instruction_types"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_successfully_submitted(INSTRUCTION, generate_random_string_subject(), HINDI, generate_random_string_subject(), STATUS)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_016_Verify_fill_form_of_passage_content_with_typing_type(self):
        """Verify_fill_form_of_passage_content_with_typing_type"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_submitted_with_typing_types(TYPING, generate_random_string_subject(), ENGLISH, generate_random_string_subject(), STATUS, TYPING_TYPE_VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_017_Verify_fill_form_of_passage_content_with_excel_type(self):
        """Verify_fill_form_of_passage_content_with_excel_type"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_submitted_with_typing_types(TYPING, generate_random_string_subject(), EXCEL, generate_random_string_subject(), STATUS, EXCEL_TYPE_VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_018_Verify_form_fill_with_invalid_question_title_data(self):
        """Verify_form_fill_with_invalid_question_title_data"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_fill_with_invalid_question_title_data(PASSAGE, generate_random_dynamic_string(LENGTH), EXCEL, generate_random_string_subject(), STATUS, PARSLEY_MAXLENGTH)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_019_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_020_Verify_form_fill_with_invalid_description(self):
        """Verify_form_fill_with_invalid_description_data"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_fill_with_invalid_question_title_data(PASSAGE, generate_random_string_subject(), HINDI, generate_random_dynamic_string(LENGTH_DATA), STATUS, PARSLEY_MAXLENGTH_VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_021_Verify_click_on_close_button(self):
        """Verify_click_on_close_button"""
        self.subject.click_on_cancel_button()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_022_Verify_form_fill_with_typing_test_subject(self):
        """Verify_form_fill_with_typing_test_subject"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_submitted_with_typing_types(PASSAGE, generate_random_string_subject(), TYPING_TEST, generate_random_string_subject(), STATUS, TYPING_VALIDATION)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_023_Verify_form_fill_with_excel_subject(self):
        """Verify_form_fill_with_excel_subject"""
        self.passage.add_new_question_button_of_passage_content()
        self.passage.form_submitted_with_typing_types(PASSAGE, generate_random_string_subject(), EXCEL, generate_random_string_subject(), STATUS, EXCEL_VALIDATION)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_024_Verify_click_on_delete_button_after_accept(self):
        """Verify_click_on_delete_button_after_accept"""
        self.passage.click_on_delete_button_and_click_the_accept_data()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_025_Verify_click_on_delete_button_and_click_the_dismiss_data(self):
        """Verify_click_on_delete_button_and_click_the_dismiss_data"""
        self.passage.click_on_delete_button_and_click_the_dismiss_data()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_026_Verify_click_on_edit_button_after_click_cancel_button(self):
        """Verify_click_on_edit_button_after_click_cancel_button"""
        self.passage.click_on_edit_button_after_click_cancel_button_data()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_027_Verify_search_by_the_types(self):
        """Verify_search_by_the_types"""
        self.passage.search_by_the_types(PASSAGE)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_028_Verify_search_by_the_question_title(self):
        """Verify_search_by_the_question_title"""
        self.passage.search_by_the_question_title_the_data(DASH_DATA, MCQ_QUESTION)
