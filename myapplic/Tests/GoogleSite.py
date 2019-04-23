from selene.api import *
from selene.browser import driver


class GoogleSite:

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def run_test():
        browser.open_url('http://google.com')
        return browser.title()
