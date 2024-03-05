import allure
import pytest

from PageObjects.MultipleImageChoiceQuestionPage import MultipleImageChoiceQuestion
from Utilities.generate_email import *
from Utilities.return_message import *
from Utilities.constants import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestMultipleImageChoiceQuestion:
    
    @pytest.fixture(autouse=True)
    def classSetup(self, setup_and_teardown):
        self.multiple_image_choice_question = MultipleImageChoiceQuestion(self.driver)
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_001(self):
        """This test case run without save new question click on cancel button"""
        self.multiple_image_choice_question.add_new_question_multiple_image_choice_question()
        
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_002(self):
        """This test case run with all valid input"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, IMAGE,IMAGE, IMAGE, ADD)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question()
        
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_003(self):
        """This test case run with only question_title input and remaining input is blank"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, BLANK,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_004(self):
        """This test case run with only question_title and optionA input and remaining input is blank"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, BLANK,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_005(self):
        """This test case run with only question_title and optionA and optionB input and remaining input is blank"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, IMAGE,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_006(self):
        """This test case run with only question_title and optionA and optionB input and optionC input remaining input is blank"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,IMAGE, IMAGE,IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_007(self):
        """This test case run with only optionA input remaining input is blank"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, BLANK,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_008(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, IMAGE,BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_009(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, BLANK, IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_010(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, BLANK, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_011(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, IMAGE, BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_012(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, BLANK, IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_013(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ,BLANK, BLANK, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_014(self):    
        """This test case output is gives required validation""" 
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, IMAGE, BLANK, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_015(self):
        """This test case output is gives required validation""" 
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, BLANK, IMAGE, BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_016(self):
        """This test case output is gives required validation"""      
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,IMAGE, BLANK, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_017(self):
        """This test case output is gives required validation"""    
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, IMAGE, BLANK, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_018(self):
        """This test case output is gives required validation"""      
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK,BLANK, BLANK, IMAGE, IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_019(self):
        """This test case output is gives required validation"""    
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, BLANK,IMAGE,BLANK, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_020(self):    
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, BLANK,BLANK,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_021(self):
        """This test case output is gives required validation"""       
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, IMAGE,BLANK,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_022(self):
        """This test case output is gives required validation"""        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, BLANK,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_023(self):
        """This test case output is gives required validation"""        
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK, IMAGE, BLANK,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_024(self):
        """This test case output is gives required validation"""       
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK, BLANK, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_025(self):
        """This test case output is gives required validation"""       
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_026(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(BLANK, IMAGE, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_027(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, BLANK, IMAGE,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_028(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, BLANK,IMAGE,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_029(self):
        """This test case output is gives required validation"""
        self.multiple_image_choice_question.add_new_question_with_all_valid_input(QUESTION_MICQ, IMAGE, IMAGE,BLANK,IMAGE, ADD)
        self.multiple_image_choice_question.display_validation_messsage_required()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_030(self):
        """This test case run for search using question_title and display searching value row"""
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(SEARCH_QUESTION_MICQ, BLANK)
        self.multiple_image_choice_question.search_after_row_count()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_031(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(BLANK, HINDI)
        self.multiple_image_choice_question.search_after_row_count()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_032(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(SEARCH_QUESTION_MICQ, HINDI)
        self.multiple_image_choice_question.search_after_row_count()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_033(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(BLANK, BLANK)
        self.multiple_image_choice_question.search_after_row_count()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_034(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(WRONG_SEARCH, BLANK)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_035(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(BLANK, MATHS)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_036(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(SEARCH_QUESTION_MICQ, MATHS)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_037(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(THAR, HINDI)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question()
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression    
    def test_038(self):
        self.multiple_image_choice_question.search_functionality_for_multiple_image_choice_question(CASCSA, MATHS)
        self.multiple_image_choice_question.display_success_message_for_multiple_image_choice_question()
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_039(self):
        self.multiple_image_choice_question.delete_row_in_existing_table(BLANK)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression    
    def test_040(self):
        self.multiple_image_choice_question.delete_row_in_existing_table(ACCEPT)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke    
    def test_041(self):
        self.multiple_image_choice_question.edit_row_in_existing_table(CLOSE_BUTTON,BLANK,BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke     
    def test_042(self):
        self.multiple_image_choice_question.edit_row_in_existing_table(BLANK,BLANK,BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke     
    def test_043(self):
        self.multiple_image_choice_question.edit_row_in_existing_table(BLANK,CLEAR_QUESTION,BLANK)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_044(self):
        self.multiple_image_choice_question.edit_row_in_existing_table(BLANK,BLANK,CLEAR_SUBJECT)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke     
    def test_045(self):
        self.multiple_image_choice_question.edit_row_in_existing_table(BLANK,CLEAR_QUESTION,CLEAR_SUBJECT)
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke 
    def test_046(self):
        self.multiple_image_choice_question.edit_question_of_existing_table_using_change_question(UPDATED_QUESTION_MICQ, BLANK )
    
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke     
    def test_047(self):
        self.multiple_image_choice_question.edit_question_of_existing_table_using_change_question(BLANK, HINDI)
    
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression     
    def test_048(self):
        self.multiple_image_choice_question.edit_question_of_existing_table_using_change_question(UPDATED_QUESTION_MICQ, HINDI)
