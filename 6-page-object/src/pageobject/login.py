from pageobject.pageobject import CTX


class Login(CTX):

    def __init__(self):
        CTX.__init__(self)
        self.page_url = '%sindex.html' % self.host

    def login(self, username='demo', passowrd='mode'):
        """Login to to the page.

        `username` and `passowrd` arguments can be used to change
        the default login credentials.
        """
        self.sl.input_text('username_field', username)
        self.sl.input_password('password_field', passowrd)
        self.sl.click_button('login_button')
