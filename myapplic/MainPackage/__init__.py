from flask import Flask
from selene import config, browser
from selene.browsers import BrowserName
from selenium import webdriver

from myapplic.Tests.GoogleSite import GoogleSite

app = Flask(__name__)


@app.route("/")
def hello():
    return GoogleSite.run_test(setup_browser())


def setup_browser():
    driver = webdriver.Firefox()
    browser.set_driver(driver)
    config.timeout = 2
    return driver


if __name__ == "__main__":
    config.browser_name = BrowserName.FIREFOX
    app.debug = True
    app.run(host='0.0.0.0')
