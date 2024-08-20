import pytest
from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.constants import LoginPageStrings


@pytest.mark.parametrize("credentials, expected_message, is_valid",[
                        (LoginPageStrings.CREDENTIALS, LoginPageStrings.PRODUCTS_TEXT, True),
                        (LoginPageStrings.INVALID_CREDENTIALS, LoginPageStrings.INVALID_LOGIN_ERROR_MESSAGE, False),
                        ({'username': '', 'password': ''}, LoginPageStrings.MISSING_USERNAME_ERROR_MESSAGE, False), ])

def test_login(login_page, credentials, expected_message, is_valid) -> None:
    if is_valid:
        product_p = login_page.do_login(credentials)
        expect(product_p.product_header).to_have_text(expected_message)
    else:
        login_page.do_login(credentials)
        expect(login_page.error_message_locator).to_contain_text(expected_message)


# def test_login_with_standard_user(login_page) -> None:
#     product_p = login_page.do_login(LoginPageStrings.CREDENTIALS)
#
#     expect(product_p.product_header).to_have_text(LoginPageStrings.PRODUCTS_TEXT)
#
#
# def test_login_with_invalid_user(login_page) -> None:
#     login_page.do_login(LoginPageStrings.INVALID_CREDENTIALS)
#
#     expect(login_page.error_message_locator).to_contain_text(LoginPageStrings.INVALID_LOGIN_ERROR_MESSAGE)
#
#
# def test_login_without_credentials(login_page) -> None:
#     login_page.click_login()
#
#     expect(login_page.error_message_locator).to_contain_text(LoginPageStrings.MISSING_USERNAME_ERROR_MESSAGE)


def test_access_inventory_without_login(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.goto(LoginPageStrings.INVENTORY_URL)
    login_page = LoginPage(page)

    expect(login_page.error_message_locator).to_contain_text(LoginPageStrings.ACCESS_DENIED_ERROR_MESSAGE)
