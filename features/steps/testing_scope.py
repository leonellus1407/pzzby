from behave import *
from behave.runner import Context


@given('preset "{val}"')
def set_var(context, val=0):
    context.var = int(val)


@when('set "{val}"')
def set_var(context, val=0):
    write_to_file("var = " + str(context.var) + " + " + str(val) + "\n")
    context.var = int(context.var) + int(val)


@then('eq "{val}"')
def assert_val(context, val=0):
    write_to_file("assert: " + str(context.var) + " = " + str(val) + "\n")
    assert int(context.var) == int(val)


def write_to_file(string_to_write):
    f = open("log.txt", 'a')
    f.write(string_to_write)
    f.close()
