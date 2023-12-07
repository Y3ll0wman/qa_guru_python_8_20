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
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    browser.config.driver_options = options

    config.base_url = 'https://demowebshop.tricentis.com'
    config.window_width = 1920
    config.window_height = 1080
    config.reports_folder = './.reports'
    config.timeout = 5

    yield

    print("\nquit browser..")
    browser.quit()
