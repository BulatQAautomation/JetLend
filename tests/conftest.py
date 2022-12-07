import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='Chrome',
                     help="Choose browser: Chrome, Opera or Firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        print("\n\nStart Chrome browser for test ...")
        browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=ChromeOptions()
        )
    elif browser_name == "Firefox":
        print("\n\nStart Firefox browser for test ...")
        browser = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=FirefoxOptions()
        )
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print("\nQuit browser...")
    browser.quit()


@pytest.fixture(scope='session')
def base_url():
    return "https://demo.jetlend.ru/lend/v3/"
