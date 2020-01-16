import os
import pytest

from selenium import webdriver

from vendor import VENDOR_DIR


@pytest.fixture(scope='session')
def driver(request):
    _driver = webdriver.Chrome(executable_path=os.path.join(VENDOR_DIR, 'chromedriver'))

    def _quit():
        _driver.quit()

    request.addfinalizer(_quit)

    return _driver