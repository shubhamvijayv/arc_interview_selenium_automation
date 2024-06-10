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
        self.passage.fill_form_of_passage_content(PASSAGE, generate_random_string_subject(), HINDI, generate_random_string_subject(), STATUS)
