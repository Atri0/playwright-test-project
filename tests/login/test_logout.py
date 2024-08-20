from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage


def test_logout(set_up_tear_down) -> None:
    page = set_up_tear_down
    login_page = LoginPage(page)
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    products_p = login_page.do_login(credentials)
    products_p.click_burger_menu().click_logout()

    expect(login_page.login_btn).to_be_visible()
