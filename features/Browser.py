from selenium import webdriver


class Browser(object):

    base_url = 'http://localhost/'
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = location if len(location) > 0 else self.base_url
        self.driver.get(url)