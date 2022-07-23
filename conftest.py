import time

import pytest
from selenium import webdriver

from oxwall_site import OwxallSite


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    return driver


@pytest.fixture()
def open_oxwall_site(driver):
    driver.get("http://localhost/oxwall/")
    # driver.get("https://demo.oxwall.com/")
    # driver.get("https://demos.softaculous.com/Oxwall")
    # driver.get("https://www.softaculous.com/softaculous/demos/Oxwall")

    # frame = driver.find_element(By.XPATH, "//iframe[2]")
    # driver.switch_to.frame(frame)
    return


@pytest.fixture()
def login(driver):
    app = OwxallSite(driver)
    app.login()
    time.sleep(5)
    yield
    app.logout()
