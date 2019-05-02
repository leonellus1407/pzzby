from behave import *
from selene import browser, config
from selene.browsers import BrowserName
from selenium import webdriver

from myapplic.Tests.pzzBy import pzzBy


@given('Start test')
def step(context):
    context.pzz = pzzBy()
    config.browser_name = BrowserName.FIREFOX
    driver = webdriver.Chrome("/home/admink/snap/chromedriver")
    browser.set_driver(driver)
    context.my_browser = browser
    config.timeout = 5
    context.NUM_OF_ITERATIONS = 5


@given('Stop test')
def step(context):
    context.my_browser.quit()


@given('open "{site}"')
def open_site(context, site="http://localhost/"):
    context.my_browser.open_url(site)
    pass


@given('set address with street name "{street_name}" and house number "{house_number}"')
def set_addr(context, street_name="", house_number=""):
    context.pzz.set_address(context.my_browser.driver(), street_name, house_number)
    pass


@given('add to cart "{pz_num}" of pizza "{pz_name}". Size: "{pz_size}"')
def add_to_cart(context, pz_num="", pz_name="", pz_size="", iteration=0):
    size = 2 if pz_size == "big" else 1
    context.pzz.add_pizza_to_cart(context.my_browser.driver(), pz_name, int(size), int(pz_num))
    #try:
    assert False
    # except Exception:
    #     iteration += 1
    #     if iteration <= context.NUM_OF_ITERATIONS:
    #         Context.log_capture()
    #         #Context.
    pass


@given('remove from cart "{pz_num}" of pizza "{pz_name}". Size: "{pz_size}"')
def remove_from_cart(context, pz_num="", pz_name="", pz_size=""):
    size = 2 if pz_size == "big" else 1
    context.pzz.remove_pizza_to_cart(context.my_browser.driver(), pz_name, int(size), int(pz_num))
    pass


@when('checkout my order')
def checkout(context):
    context.pzz.checkout(context.my_browser.driver())
    pass


@then('site title should be "{title}"')
def check_open_site(context, title):
    assert context.my_browser.title() == title
