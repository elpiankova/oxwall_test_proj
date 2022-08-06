import json
import time

import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from value_objects.users import User


@pytest.fixture()
def driver(selenium):
    driver = selenium
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
    user = User(username="admin", password="pass")
    main_page = MainPage(driver)
    main_page.sign_in_click()
    sign_in_page = SignInPage(driver)
    sign_in_page.login(user)
    time.sleep(5)
    yield user
    main_page.logout()


with open("data/user.json", encoding="utf-8") as f:
    user_data = json.load(f)


@pytest.fixture(params=user_data, ids=[str(u) for u in user_data])
def user(request):
    u = User(**request.param)
    print(u)
    return u
