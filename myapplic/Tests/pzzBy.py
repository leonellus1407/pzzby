# This Python file uses the following encoding: utf-8
import selenium
from selene.api import *
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.common.exceptions import *

from myapplic.CustomAddons.custom_actions import c_actions


class pzzBy:

    def __init__(self):
        # self.driver = self._setup_browser()
        pass

    # METHOD REWRITE UNDER REQUIREMENTS OF BEHAVE
    def _setup_browser(self):
        config.browser_name = BrowserName.FIREFOX
        driver = webdriver.Firefox()
        browser.set_driver(driver)
        config.timeout = 5
        return driver

    # def run_test(driver):
    #     st_time = datetime.datetime.now()
    #     browser.open_url('https://pzz.by/')
    #     pzzBy._set_address(driver, 'Победителей', '1')  # Russian A
    #     pzzBy._add_pizza_to_cart(driver, 'Гавайская', 2, 4)
    #     pzzBy._remove_pizza_to_cart(driver, 'Гавайская', 2, 3)
    #     pzzBy._add_pizza_to_cart(driver, 'Грибная', 1, 5)
    #     pzzBy._remove_pizza_to_cart(driver, 'Грибная', 1, 2)
    #     pzzBy._add_pizza_to_cart(driver, 'Грибная', 2, 2)
    #     pzzBy._checkout(driver)
    #     return "Duration: " + str((datetime.datetime.now() - st_time).seconds) + " seconds"

    def set_address(self, driver, street, house):
        c_actions.action_click_to_element(driver, driver.find_elements_by_xpath(
            '//*[@class ="pzz-cart__delivery pizza-sending"]/a')[1])
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_street-name"]'), '//*[@id="s2id_street-name"]')
        s(by.xpath('//input[@id="s2id_autogen1_search"]')).send_keys(street).press_tab()
        c_actions.custom_pause()
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="s2id_home-number"]'), '//*[@id="s2id_home-number"]')
        s(by.xpath('//input[@id="s2id_autogen2_search"]')).send_keys(house).press_tab()
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="byaddress"]'))
        c_actions.custom_pause()

    def add_pizza_to_cart(self, driver, pizza_name, size=2, num=1):
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
        element = driver.find_element_by_xpath('//*[@id="myModal"]//span[@class="plus-item"]')
        el = s(by.xpath('//*[@id="myModal"]//span[@class="plus-item"]'))
        i = 1
        while i <= num:
            if el.is_displayed():
                c_actions.action_click_to_element(driver, element, '//*[@id="myModal"]//span[@class="plus-item"]')
            else:
                try:
                    c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                        '//*[@class="in-cart popup-in-cart"]'), '//*[@class="in-cart popup-in-cart"]')
                except NoSuchElementException:
                    c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                        '//*[@class="in-cart popup-in-cart "]'), '//*[@class="in-cart popup-in-cart "]')
            i += 1
        #   Close pizza
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="myModal"]//span[contains(text(),"Закрыть")]'),
                                          '//*[@id="myModal"]//span[contains(text(),"Закрыть")]')
        c_actions.custom_pause()

    def checkout(self, driver):
        try:
            ss(by.xpath('//a[contains(text(),"корзина")]'))[0].click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            ss(by.xpath('//a[contains(text(),"корзина")]'))[1].click()
        s(by.xpath('//input[@name="name"]')).send_keys("Тест формы заказа").press_tab()
        s(by.xpath('//input[@name="phoneNumber"]')).send_keys("000000000").press_tab()
        s(by.xpath('//input[@name="flat"]')).send_keys("0").press_tab()
        s(by.xpath('//input[@name="entrance"]')).send_keys("0").press_tab()
        s(by.xpath('//input[@name="floor"]')).send_keys("0").press_tab()
        s(by.xpath('//input[@name="comment"]')).send_keys("Это тестовый заказ. Пожалуйста, проигнорируйте его")
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//div[@class="ips__group payment-cash-button"]'),
            '//div[@class="ips__group payment-cash-button"]'
                                          )

        # //h1[contains(text(), "Заказ принят")] XPATH For order complete

    def remove_pizza_to_cart(self, driver, pizza_name, size=2, num=1):
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
        element = driver.find_element_by_xpath('//*[@id="myModal"]//span[@class="minus-item"]')
        el = s(by.xpath('//*[@id="myModal"]//span[@class="plus-item"]'))
        i = 1
        while i <= num:
            if el.is_displayed():
                c_actions.action_click_to_element(driver, element, '//*[@id="myModal"]//span[@class="minus-item"]')
            else:
                try:
                    c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                        '//*[@class="in-cart popup-in-cart"]'), '//*[@class="in-cart popup-in-cart"]')
                except NoSuchElementException:
                    c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
                        '//*[@class="in-cart popup-in-cart "]'), '//*[@class="in-cart popup-in-cart "]')
            i += 1
        #   Close pizza
        c_actions.action_click_to_element(driver, driver.find_element_by_xpath(
            '//*[@id="myModal"]//span[contains(text(),"Закрыть")]'),
                                          '//*[@id="myModal"]//span[contains(text(),"Закрыть")]')
        c_actions.custom_pause()
