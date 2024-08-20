import attrs


@attrs.define
class ProductListPage:
    page = attrs.field()
    _product_header = attrs.field(init=False, factory=lambda: None)
    _burger_menu_btn = attrs.field(init=False, factory=lambda: None)
    _logout_btn = attrs.field(init=False, factory=lambda: None)

    def __attrs_post_init__(self):
        self._product_header = self.page.locator("span.title")
        self._burger_menu_btn = self.page.locator("button#react-burger-menu-btn")
        self._logout_btn = self.page.locator("//a[@id='logout_sidebar_link']")

    @property
    def product_header(self):
        return self._product_header

    @property
    def burger_menu_btn(self):
        return self._burger_menu_btn

    @property
    def logout_btn(self):
        return self._logout_btn

    @property
    def product_header(self):
        return self._product_header

    def click_burger_menu(self):
        self._burger_menu_btn.click()
        return ProductListPage(self.page)

    def click_logout(self):
        from pages.LoginPage import LoginPage
        self._logout_btn.click()
        return LoginPage(self.page)
