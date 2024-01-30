from selenium.webdriver.common.by import By


class Locators:
    ADD_NEW_QUESTION_BUTTON = ('button.AddRecordBtn', 'css')
    SAVE_BUTTON = ('save-button', 'id')
    CLOSE_BUTTON = ('close-button', 'id')
    DISPLAY_MESSAGE = ('notice', 'id')
    PARSLEY_REQUIRED = ('parsley-required', 'class')
    PARSLEY_MAXFILESIZE = ('parsley-maxFileSize', 'class')
    PARSLEY_FILEEXTENSION = ('parsley-fileextension', 'class')
    GET_QUESTION_TEXT = ('td.EditData', 'css')
    PARSLEY_PATTERN = ('parsley-pattern', 'class')
    TABLE_ROW_COUNT = ('tbody#demo tr', 'css')
    DELETE_BUTTON = ('Delete', 'id')
    PARSLEY_MAXLENGTH = ('parsley-maxlength', 'class')
    EDIT_BUTTON = ('editButton', 'class')
    INPUT_OPTION_A = ('optionA','name')
    INPUT_OPTION_B = ('optionB','name')
    INPUT_OPTION_C = ('optionC','name')
    INPUT_OPTION_D = ('optionD','name')
    CHECKED_ON_CORRECT_OPTION = ('//input[@value="optionB"]', 'xpath')
    
class LoginPageLocators:
    INPUT_USERNAME = ('username', 'name')
    INPUT_PASSWORD = ('password', 'name')
    LOGIN_BUTTON = ('login_button', 'id')
    CLICK_TEXT_ALLOW_AUTHENTICATED_USER_XPATH = ('Allow Authenticated User', "link text")
    CLICK_TEXT_ADD_SUBJECT_XPATH = ('Add Subject', "link")
    CLICK_TEXT_MULTIPLE_IMAGE_CHOICE_QUESTION_XPATH = ('Multiple Image Choice Question', "link")
    CLICK_TEXT_MULTIPLE_CHOICE_QUESTION_XPATH = ('Multiple Choice Question', "link")
    CLICK_TEXT_IMAGE_BASED_MULTIPLE_CHOICE_QUESTION_XPATH = ('Image Based Multiple Choice Questions', "link")
    CLICK_TEXT_SUBJECTIVE_QUESTION_XPATH = ('Subjective Questions', "link")
    CLICK_TEXT_IMAGE_BASED_SUBJECTIVE_QUESTION_XPATH = ('Image Based Subjective Questions', "link")
    
class SubjectPageLocators:
    INPUT_SUBJECT = ('subject', 'name')
    GET_TEXT_SUBJECT = ('//*[@id="demo"]/tr[1]/td[1]', 'xpath')
    
class MultipleImageChoiceQuestionPageLocators:
    INPUT_QUESTION_TITLE = ('MICQ_title', 'id')
    INPUT_SUBJECT = ('//select[@id="MICQ_subject"]/option[5]', 'xpath')
    CHECKED_ON_CORRECT_OPTION = ('//input[@value="optionB"]', 'xpath')
    CLOSE_BUTTON = ('//button[@value="close"]', 'xpath')
    SAVE_BUTTON = ('//button[@value="Save"]', 'xpath')
    SEARCH_BY_QUESTION = ('//input[@name="question_title"]', 'xpath')
    SEARCH_BUTTON = ('//input[@value="Search"]', 'xpath')
    CLICK_EDIT_BUTTON_SELECT_SUBJECT_DROPDOWN = ('//select[@id="MICQ_subject"]/option[1]', 'xpath')
    UPDATE_INPUT_SUBJECT = (By.XPATH, '//select[@id="MICQ_subject"]/option[6]')
    SEARCH_BY_SUBJECT = (By.ID, 'id_subject')
