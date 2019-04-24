# This Python file uses the following encoding: utf-8
import time
import datetime

import selenium
from selene.api import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait


def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)


def action_click_to_element(driver, element, xpath=None):
    action_chains = ActionChains(driver)
    scroll_shim(driver, element)
    if xpath is not None:
        WebDriverWait(
            driver, config.timeout).until(
                element_to_be_clickable(
                    by.xpath(
                        xpath)))
    action_chains.move_to_element(element).click().perform()


class GoogleSite:

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def run_test(driver):
        browser.open_url('https://pzz.by/')
        action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@class="show-preview" and contains(text(), "Опята и курица")]'))
    #   Change pizza size
        action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="p_p_size_2"]'), '//*[@id="p_p_size_2"]')
    #   Add pizza to cart
        action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@class="in-cart popup-in-cart "]'),'//*[@class="in-cart popup-in-cart "]')
    #   Click to enter street
        action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_street-name"]'), '//*[@id="s2id_street-name"]')
    #   Enter Pobeditelei street
        start = time.time()
        s(by.xpath('//*[@id="s2id_autogen1_search"]')).set('Победителей').press_tab()
        prom = time.time()
        time.sleep(4)
    #   Enter House number
        action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_home-number"]'), '//*[@id="s2id_home-number"]')
        s(by.xpath('//*[@id="s2id_autogen2_search"]')).send_keys('7').press_tab()
        # action_click_to_element(driver, driver.find_element_by_xpath(
        #    '//*[@id="p_p_size_1"]'))
        # s(by.xpath('//*[@class="in-cart popup-in-cart "]')).click()

        #.filtered_by(have.attribute('data-size', 'big')).filtered_by(have.exact_text("В корзину"))

        return "Test complete"
