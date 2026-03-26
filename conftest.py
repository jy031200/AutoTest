import pytest
from driver.mobile_driver import get_driver

@pytest.fixture
def driver():
    driver = get_driver()


    yield driver
    driver.quit()