# This Python file uses the following encoding: utf-8
import datetime
import time
import selenium
from selene.api import *
from myapplic.CustomAddons.custom_actions import c_actions


class pzzBy:

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def run_test(driver):
        st_time = datetime.datetime.now()
        browser.open_url('https://pzz.by/')
        pzzBy._set_address(driver, 'Победителей', '7/А')  # Russian A
        pzzBy._add_pizza_to_cart(driver, 'Гавайская', 2)
        return "Duration: " + str((datetime.datetime.now() - st_time).seconds) + " seconds"

    @staticmethod
    def _set_address(driver, street, house):
        c_actions.action_click_to_element(driver, driver.find_elements_by_xpath(
            '//*[@class ="pzz-cart__delivery pizza-sending"]/a')[1])
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_street-name"]'), '//*[@id="s2id_street-name"]')
        s(by.xpath('//*[@id="s2id_autogen1_search"]')).send_keys(street).press_tab()
        c_actions.custom_pause()
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_home-number"]'), '//*[@id="s2id_home-number"]')
        s(by.xpath('//*[@id="s2id_autogen2_search"]')).send_keys(house).press_tab()
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="byaddress"]'))
        c_actions.custom_pause()

    @staticmethod
    def _add_pizza_to_cart(driver, pizza_name, size=2):
        #   Open pizza
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@class="show-preview" and contains(text(), "' + pizza_name + '")]'))
        #   Change pizza size
        if size == 2:
            c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                '//*[@id="p_p_size_2"]'), '//*[@id="p_p_size_2"]')
        else:
            c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                '//*[@id="p_p_size_1"]'), '//*[@id="p_p_size_1"]')
        #   Add pizza to cart
        try:
            c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                '//*[@class="in-cart popup-in-cart"]'), '//*[@class="in-cart popup-in-cart"]')
        except selenium.common.exceptions.NoSuchElementException:
            c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                '//*[@class="in-cart popup-in-cart "]'), '//*[@class="in-cart popup-in-cart "]')
        #   Close pizza
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="myModal"]/div/div/span'), '//*[@id="myModal"]/div/div/span')
