# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
import re
import sys
import traceback
from datetime import datetime
from inspect import getmembers
from pprint import pprint

from behave import fixture, use_fixture
from behave.runner import Context
from selene import config, browser
from selene.browsers import BrowserName
from selenium import webdriver

from myapplic.Tests.pzzBy import pzzBy


@fixture
def browser_chrome(context):
    config.browser_name = BrowserName.CHROME
    driver = webdriver.Chrome("/home/admink/snap/chromedriver")
    browser.set_driver(driver)
    context.browser = browser


def before_all(context):
    #use_fixture(driver_settings, context)
    #use_fixture(browser_chrome, context)
    #context.pzz = pzzBy()
    f = open("log.txt", 'a')
    f.write("\n\n" + "="*10 + "\nStart session: " + str(datetime.now().strftime('%d.%m.%Y %H:%M:%S')) + "\n")
    f.close()
    Context.var = 0
    pass


def after_all(context):
    #context.browser.close()
    f = open("log.txt", 'a')
    f.write("Stop session\n" + "="*10)
    f.close()
    pass


def before_scenario(context, scenario):
    #context.browser.close()
    f = open("log.txt", 'a')
    f.write("Start Scenario\n")
    #f.write("Scenario name: " + str(scenario.name) + "\n")
    f.close()
    pass


def after_scenario(context, scenario):
    #context.browser.close()
    f = open("log.txt", 'a')
    f.write("Stop Scenario\n")
    f.close()
    pass


@fixture
def create_log(context, step, when_happend):
    if re.search(r'^eq', step.name):
        f = open("log.txt", 'a')
        try:
            f.write("\n\n ========== START " + when_happend.upper() + " ==========\n\n")
            f.write("\nName of step: [" + str(step.name) + "]")
            f.write("\nStatus: " + str(step.status))
            f.write("\nhook_failed: " + str(step.hook_failed))
            f.write("\nduration: " + str(step.duration))
            f.write("\nerror_message: " + str(step.error_message))
        except TypeError as ex:
            f.write("\nException: " + str(ex) + "\n")
        finally:
            f.write("\n\n ========== END OF " + when_happend.upper() + " ==========\n\n")
            f.close()


def before_step(context, step):
    #create_log(context, step, "before")

    pass


def after_step(context, step):
    create_log(context, step, "after")
    if str(step.status) == "Status.failed":
        file = open("log.txt", 'a')
        file.write("\n########## ReRUN ##########\n")
        next_step = 'When ' + step.name
        do_next_step = next_step[1:0]
        file.write("Next step: [" + str(next_step) + "]\n")
        try:
            a = context.execute_steps(do_next_step)
            file.write("Result: [" + str(a) + "], Type = [" + str(traceback.print_exc()) + "]\n")
        except Exception as ex:
            file.write("Exception: [" + str(ex) + "]\n")
        file.write("########## END ReRUN ##########\n\n")
        file.close()


@fixture
def browser_firefox(context):
    config.browser_name = BrowserName.FIREFOX
    driver = webdriver.Firefox()
    browser.set_driver(driver)
    context.browser = browser


@fixture
def driver_settings(context):
    config.timeout = 5
    context.NUM_OF_ITERATIONS = 5


