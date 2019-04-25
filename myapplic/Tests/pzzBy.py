# This Python file uses the following encoding: utf-8
import time
import datetime

import selenium
from selene.api import *

from myapplic.CustomAddons.Moving import moving


class pzzBy:

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def run_test(driver):
        start = time.time()
        browser.open_url('https://pzz.by/')
        step1 = time.time()
        pzzBy._add_pizza_to_cart(driver, 'Гавайская', 1)
        step2 = time.time()
        pzzBy._set_address(driver, 'Победителей', '7/А')  # Russian A
        step3 = time.time()
        pzzBy._add_pizza_to_cart(driver, 'Гавайская', 2)
        step4 = time.time()


#       TIMING
        str_ret = "1. " + str(step1 - start) + "<br>"
        str_ret += "2. " + str(step2 - step1) + "<br>"
        str_ret += "3. " + str(step3 - step2) + "<br>"
        str_ret += "4. " + str(step4 - step3) + "<br>"
#       str_ret += "5. " + str(step5 - step4) + "<br>"
#       str_ret += "6. " + str(step6 - step5) + "<br>"
#       str_ret += "7. " + str(step7 - step6) + "<br>"
#       str_ret += "8. " + str(step8 - step7) + "<br>"
#       str_ret += "9. " + str(step9 - step8) + "<br>"
        return str_ret + "<br>" + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    @staticmethod
    def _set_address(driver, street, house):
        moving.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_street-name"]'), '//*[@id="s2id_street-name"]')
        s(by.xpath('//*[@id="s2id_autogen1_search"]')).send_keys(street).press_tab()
        time.sleep(1)
        moving.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_home-number"]'), '//*[@id="s2id_home-number"]')
        s(by.xpath('//*[@id="s2id_autogen2_search"]')).send_keys(house).press_tab()
        moving.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="byaddress"]'))

    @staticmethod
    def _add_pizza_to_cart(driver, pizza_name, size=2):
        moving.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@class="show-preview" and contains(text(), "' + pizza_name + '")]'))
        #   Change pizza size
        if size == 2:
            moving.action_click_to_element(driver, driver.find_element_by_xpath(
                '//*[@id="p_p_size_2"]'), '//*[@id="p_p_size_2"]')
        else:
            moving.action_click_to_element(driver, driver.find_element_by_xpath(
                '//*[@id="p_p_size_1"]'), '//*[@id="p_p_size_1"]')
        #   Add pizza to cart
        moving.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@class="in-cart popup-in-cart "]'), '//*[@class="in-cart popup-in-cart "]')
