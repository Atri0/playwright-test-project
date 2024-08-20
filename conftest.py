import pytest
from playwright.async_api import async_playwright

from pages.LoginPage import LoginPage

'''
@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
    await browser.close()

@pytest.fixture(scope="function")
async def page(browser):
    context = await browser.new_context()
    page = await context.new_page()
    return page
'''

@pytest.fixture(scope="function")
def set_up_tear_down(page) -> None:
    #page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("http://www.saucedemo.com")
    yield page

@pytest.fixture
def login_page(set_up_tear_down):
    page = set_up_tear_down
    return LoginPage(page)
