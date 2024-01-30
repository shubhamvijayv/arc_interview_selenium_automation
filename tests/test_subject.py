import allure
import pytest

from PageObjects.SubjectPage import Subject
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestSubject:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, setup_and_teardown):
        self.subject = Subject(self.driver)
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_001(self):
        """This test case run with valid in subject column"""
        self.subject.fill_the_form_add_new_subject(generate_random_string_subject())
        self.subject.success_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_002(self):
        """This test case run with blank in subject column"""
        self.subject.fill_the_form_add_new_subject(BLANK)
        self.subject.validation_message_for_required_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003(self):
        """This test case run with number in subject column"""
        self.subject.fill_the_form_add_new_subject(NUMBER)
        self.subject.validation_message_for_subject()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004(self):
        """This test case run with hash_data in subject column"""
        self.subject.fill_the_form_add_new_subject(HASH_DATA)
        self.subject.validation_message_for_subject()
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_005(self):
        """This test case run with name and number in subject column"""
        self.subject.fill_the_form_add_new_subject(NAME_WITH_NUMBER)
        self.subject.validation_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_006(self):
        """This test case run with name and @ in subject column"""
        self.subject.fill_the_form_add_new_subject(NAME_WITH_ATTHERATE)
        self.subject.validation_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke        
    def test_007(self):
        """This test case run with name and ! in subject column"""
        self.subject.fill_the_form_add_new_subject(NAME_WITH_EXCLAMINATION)
        self.subject.success_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke        
    def test_008(self):
        """This test case run with click on cancel button"""
        self.subject.not_save_new_subject_click_on_cancel_button()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke    
    def test_009(self):
        """This test case run for delete subject in the subject table"""
        self.subject.delete_row_in_the_subject_table()
    
    @allure.severity(allure.severity_level.MINOR)    
    @pytest.mark.smoke
    def test_010(self):
        """This test case run for not delete subject in the subject table"""
        self.subject.not_delete_row_in_subject_table()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    def test_011(self):
        """This test case run for click on cancel button"""
        self.subject.update_existing_data_in_the_subject_table_without_change()
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity    
    def test_012(self):
        """This test case run with blank input in this function"""
        self.subject.update_existing_subject_click_on_edit_button(BLANK)
        self.subject.validation_message_for_required_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_013(self):
        """This test case run with valid input in this function and display valid message"""
        self.subject.update_existing_subject_click_on_edit_button(generate_random_string_subject())
        self.subject.success_message_for_subject()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke        
    def test_014(self):
        """This test case run with text and number input in this function and display validation message"""
        self.subject.update_existing_subject_click_on_edit_button(TEXT_WITH_NUMBER)
        self.subject.validation_message_for_subject()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_015(self):
        """This test case run with text and @ input in this function and display validation message"""
        self.subject.update_existing_subject_click_on_edit_button(TEXT_WITH_ATTHERATE)
        self.subject.validation_message_for_subject()
