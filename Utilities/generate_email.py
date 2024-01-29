import time
import string
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def generate_email_time_stamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "arun"+timestamp+"@arcgate.com"

def generate_username_time_stamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "arun"+timestamp

def generate_random_string_subject():
    number = 7
    result = ''.join(random.choices(string.ascii_lowercase, k=number))
    return result

def generate_random_dynamic_string(number):
    result = ''.join(random.choices(string.ascii_lowercase, k=number))
    return result

def dropdown_input(driver, time_duration, by, locator, input_data):
    wait = WebDriverWait(driver, time_duration)
    select = wait.until(EC.presence_of_element_located((by, locator)))
    select = Select(select)
    select.select_by_visible_text(input_data)
    
def dynamic_explicit_wait(driver, time_duration, by, element_name, message):
    return WebDriverWait(driver, time_duration).until(EC.text_to_be_present_in_element((by, element_name), message))
    
def dynamic_explicit_wait_without_message(driver, time_duration, by, element_name):
    return WebDriverWait(driver, time_duration).until(EC.visibility_of_element_located((by, element_name)))
