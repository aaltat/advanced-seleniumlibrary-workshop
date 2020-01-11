import unittest

from mockito import mock, when, unstub

from pageobject import PageObject


class PageObjectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lib = PageObject()

    def tearDown(self):
        unstub()

    def test_01_demo(self):
        page = mock()
        url = 'http://localhost:7272/index.html'
        page.page_url = url
        page_name = 'LoginPage'
        sl = mock()
        when(self.lib)._get_sl().thenReturn(sl)
        when(self.lib)._set_search_order('PageObject').thenReturn(True)
        when(self.lib)._get_url().thenReturn(url)
        when(self.lib)._get_page(page_name).thenReturn(page)
        when(self.lib.sl).go_to(url).thenReturn(True)
        self.lib.go_to(page_name)
