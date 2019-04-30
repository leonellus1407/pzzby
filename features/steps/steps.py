from behave import *
from selene import browser, config
from selene.browsers import BrowserName
from selenium import webdriver
from myapplic.Tests.pzzBy import pzzBy

@given('Start test')
def step(context):
    context.pzz = pzzBy()
    config.browser_name = BrowserName.FIREFOX
    driver = webdriver.Firefox()
    browser.set_driver(driver)
    config.timeout = 5

@given('open "{site}"')
def open_site(context, site="http://localhost/"):

    #context.behave_driver.open_url(site)
    context.browser.visit(site)
    pass

@given('set address with street name "{street_name}" and house number "{house_number}"')
def set_addr(context, street_name="", house_number=""):
    context.pzz.set_address(browser.driver(), street_name, house_number)
    pass

@given('add to cart "{pz_num}" of pizza "{pz_name}". Size: "{pz_size}"')
def add_to_cart(context, pz_num="", pz_name="", pz_size=""):
    size = 2 if pz_size == "big" else 1
    context.pzz.add_pizza_to_cart(browser.driver(), pz_name, int(size), int(pz_num))
    pass

@given('remove from cart "{pz_num}" of pizza "{pz_name}". Size: "{pz_size}"')
def remove_from_cart(context, pz_num="", pz_name="", pz_size=""):
    size = 2 if pz_size == "big" else 1
    context.pzz.remove_pizza_to_cart(browser.driver(), pz_name, int(size), int(pz_num))
    pass

@given('checkout my order')
def checkout(context):
    context.pzz.checkout(browser.driver())
    pass

@then('site should be opened')
def check_open_site(context):
    assert browser.title() == "Пицца Лисицца"