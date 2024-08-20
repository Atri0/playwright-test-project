import re
from Base_Page import BasePage
from playwright.async_api import expect


class PlaywrightDevPage(BasePage):
    async def goto(self):
        await self.page.goto("https://playwright.dev/")

    async def check_title(self):
        await expect(self.page).to_have_title(re.compile("Playwright"))



