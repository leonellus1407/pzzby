# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Firefox
import behave_webdriver
from selene import config, browser
from behave.log_capture import capture
from selenium import webdriver

from features.Browser import Browser
from myapplic.Tests.pzzBy import pzzBy
from selene.browsers import BrowserName
from behave.model import Scenario


@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = Firefox()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    #context.browser = Browser()
    #use_fixture(browser_firefox, context)
    pass


def after_all(context):
    context.browser.close()


# def before_scenario(context, scenario):
#     print(scenario.name)
#     config.browser_name = BrowserName.FIREFOX
#     driver = webdriver.Firefox()
#     browser.set_driver(driver)
#     context.browser = browser
#     #context.behave_driver = behave_webdriver.Firefox()

# @fixture
# def setup_browser(context):
#     context.pzz = pzzBy()
#     config.browser_name = BrowserName.FIREFOX
#     driver = webdriver.Firefox()
#     browser.set_driver(driver)
#     config.timeout = 5
#
#
# def before_feature(context):
#     print("hello world!")
#     #use_fixture(setup_browser, context)
#     #use_fixture(selenium_browser_chrome, context)
#     # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.


# def after_all(context):
#     print("Goodbye world!")
#     context.behave_driver.quit()
#     browser.quit()