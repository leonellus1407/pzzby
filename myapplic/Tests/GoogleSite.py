# This Python file uses the following encoding: utf-8

from selene.api import *


class GoogleSite:

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def run_test():
        step = 0
        my_log = 'Start logging<br>'
        step += 1
        my_log += str(step) + '. Opening http://google.com<br>'
        step += 1
        browser.open_url('http://google.com')
        my_log += str(step) + '. Entering in search field [pizza lisica]<br>'
        step += 1
        s("[name='q']").set('pizza lisica').press_enter()
        my_log += str(step) + '. Go search<br>'
        step += 1
        ss('.iUh30').filtered_by(have.exact_text("https://pzz.by/"))[0].click()
        my_log += str(step) + '. Click to link [https://pzz.by/]<br>'
        step += 1
        ss('.goods__list__li')[0].click()

        #.filtered_by(have.exact_text("Грибная"))
        my_log += 'Test complete<br>'
        return my_log
