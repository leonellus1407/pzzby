from flask import Flask
from selene import config
from selene.browsers import BrowserName

from myapplic.Tests.pzzBy import pzzBy

app = Flask(__name__)


@app.route("/")
def hello():
    return pzzBy.run_test(setup_browser())


if __name__ == "__main__":
    config.browser_name = BrowserName.FIREFOX
    app.debug = False
    app.run(host='0.0.0.0')
