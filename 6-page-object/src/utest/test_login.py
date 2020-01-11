import unittest

from mockito import mock, when, verify, unstub

from pageobject import Login


class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lib = Login()

    def tearDown(self):
        unstub()

    def test_01_login(self):
        username = 'demo'
        passowrd = 'mode'
        sl = mock()
        when(self.lib)._get_sl().thenReturn(sl)
        when(self.lib.sl).input_text('username_field', username)
        when(self.lib.sl).input_text('password_field', passowrd)
        when(self.lib.sl).click_button('login_button')
        when(self.lib)._wait_page_ready('http://localhost:7272/welcome.html')
        self.lib.login()
        verify(self.lib.sl).input_text('username_field', username)
        verify(self.lib.sl).input_text('password_field', passowrd)
        verify(self.lib.sl).click_button('login_button')
