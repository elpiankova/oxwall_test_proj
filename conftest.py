import time

import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.sign_in_page import SignInPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


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
def logged_user(driver):
    username = "admin"
    main_page = MainPage(driver)
    main_page.sign_in_click()
    sign_in_page = SignInPage(driver)
    sign_in_page.login(username=username, password="pass")
    time.sleep(5)
    yield username
    main_page.logout()
