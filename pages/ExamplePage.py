import re
from Base_Page import BasePage
from playwright.async_api import expect


class ExamplePage(BasePage):
    async def goto(self):
        await self.page.goto("https://example.com")

    async def check_title(self):
        assert await self.page.title() == "Example Domain"
