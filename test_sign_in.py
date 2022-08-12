import pytest

from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.dashboard_page import DashboardPage


@pytest.mark.nondestructive
def test_sign_in(driver, open_oxwall_site, user):
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
    sign_in_page = SignInPage(driver)
    sign_in_page.input_username(user.username)
    sign_in_page.input_password(user.password)
    sign_in_page.click_sign_in()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_this_page()


def test_sign_in_admin_submit(driver, open_oxwall_site):
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
    sign_in_page = SignInPage(driver)
    sign_in_page.input_username("admin")
    sign_in_page.input_password("pass")
    sign_in_page.submit()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_this_page()
