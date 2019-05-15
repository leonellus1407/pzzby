from behave import *
from selene import browser, config
from selene.browsers import BrowserName
from selenium import webdriver


@Given(u'open "{site}"')
def open_site(context, site="http://localhost/"):
    context.browser.open_url(site)
    pass


@Given(u'set address with street name "{street_name}" and house number "{house_number}"')
def set_address(context, street_name="", house_number=""):
    context.pzz.set_address(context.browser.driver(), street_name, house_number)
    pass


@when(u'add to cart "{pz_num}" of pizza "{pz_name}". Size: "{pz_size}"')
def add_to_cart(context, pz_num="", pz_name="", pz_size="", iteration=0):
    size = 2 if pz_size == "big" else 1
    context.pzz.add_pizza_to_cart(context.browser.driver(), pz_name, int(size), int(pz_num))
    #try:
    #assert False
    # except Exception:
    #     iteration += 1
    #     if iteration <= context.NUM_OF_ITERATIONS:
    #         Context.log_capture()
    #         #Context.
    pass


@when('remove from cart "{pz_num}" of pizza "{pz_name}". Size: "{pz_size}"')
def remove_from_cart(context, pz_num="", pz_name="", pz_size=""):
    size = 2 if pz_size == "big" else 1
    context.pzz.remove_pizza_to_cart(context.browser.driver(), pz_name, int(size), int(pz_num))
    pass


@when(u'checkout my order')
def checkout(context):
    context.pzz.checkout(context.browser.driver())
    pass


@then(u'site title should be "{title}"')
def check_open_site(context, title):
    assert context.browser.title() == title
