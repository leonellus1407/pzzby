import time

from selene.api import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait


class c_actions:

    @staticmethod
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

    @staticmethod
    def action_click_to_element(driver, element, xpath=None):
        action_chains = ActionChains(driver)
        c_actions.scroll_shim(driver, element)
        if xpath is not None:
            WebDriverWait(
                driver, config.timeout).until(
                    element_to_be_clickable(
                        by.xpath(
                            xpath)))
        action_chains.move_to_element(element).click().perform()

    @staticmethod
    def custom_pause(ctime=1):
        time.sleep(ctime)
