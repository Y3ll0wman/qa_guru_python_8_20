import pytest
from selene.api import config, browser
from selenium import webdriver


@pytest.fixture
def api_url():
    return 'https://demowebshop.tricentis.com'


@pytest.fixture(scope='function', autouse=True)
def browser_chrome(request):
    """
    Фикстура для настройки Chrome браузера.

    Настраивает окно браузера с заданными размерами, запускает браузер в headless режиме.
    """
    config.window_width = 1920
    config.window_height = 1080
    config.reports_folder = './.reports'
    config.base_url = 'https://demowebshop.tricentis.com'
    config.timeout = 5
    options = webdriver.ChromeOptions()
    options.browser_version = '118.0'
    options.add_argument('--no-sandbox')

    yield

    print("\nquit browser..")
    browser.quit()
