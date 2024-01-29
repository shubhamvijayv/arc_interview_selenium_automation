import pytest
import allure

from allure_commons.types import AttachmentType
from base.webdriverfactory import WebDriverFactory
from Utilities.logger import logclass
from Utilities.constants import *
from Utilities.generate_email import *
from Utilities.Readconfigurations import *


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    webdriver_data = WebDriverFactory(browser)
    driver = webdriver_data.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.log = logclass(driver)
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    result = outcome.get_result()
    if result.failed:
        allure.attach(item.cls.driver.get_screenshot_as_png(), name=SCREENSHOT + time.strftime('_%Y_%m_%d_%H_%M_%S'), attachment_type=AttachmentType.PNG)
