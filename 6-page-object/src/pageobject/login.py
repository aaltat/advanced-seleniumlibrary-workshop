from robot.utils import is_truthy

from pageobject.error import Error
from pageobject.pageobject import CTX
from pageobject.welcome import Welcome


class Login(CTX):

    def __init__(self):
        CTX.__init__(self)
        self.page_url = '%sindex.html' % self.host
        self.welcome = Welcome()
        self.error = Error()

    def login(self, username='demo', passowrd='mode', error=False):
        """Login to to the page.

        `username` and `passowrd` arguments can be used to change
        the default login credentials. `error` argument can
        be used to change to login outcome to error when set
        to True.
        """
        self.sl.input_text('username_field', username)
        self.sl.input_password('password_field', passowrd)
        self.sl.click_button('login_button')
        if is_truthy(error):
            self._wait_page_ready(self.error.page_url)
        else:
            self._wait_page_ready(self.welcome.page_url)
