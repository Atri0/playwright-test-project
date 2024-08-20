from pages.ProductListPage import ProductListPage
import attrs


@attrs.define
class LoginPage:
    page = attrs.field()
    _username = attrs.field(init=False, factory=lambda: None)
    _password = attrs.field(init=False, factory=lambda: None)
    _login_btn = attrs.field(init=False, factory=lambda: None)
    _error_message = attrs.field(init=False, factory=lambda: None)

    def __attrs_post_init__(self):
        self._username = self.page.get_by_placeholder("Username")
        self._password = self.page.get_by_placeholder("Password")
        self._login_btn = self.page.get_by_text("Login")
        self._error_message = self.page.locator("//h3[@data-test='error']")

    def enter_username(self, user_name):
        self._username.clear()
        self._username.fill(user_name)

    def enter_password(self, user_password):
        self._password.clear()
        self._password.fill(user_password)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return ProductListPage(self.page)

    @property
    def error_message_locator(self):
        return self._error_message

    @property
    def login_btn(self):
        return self._login_btn
