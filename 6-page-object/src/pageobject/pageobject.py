import time

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.errors import NoOpenBrowser


class CTX:

    ROBOT_LIBRARY_SCOPE = "TEST SUITE"
    page_timeout = 5

    def __init__(self):
        self.builtin = BuiltIn()
        self.info = logger.info
        self.debug = logger.debug
        self.host = 'http://localhost:7272/'
        self.sl_string = 'SeleniumLibrary'

    @property
    def driver(self):
        try:
            return self.sl.driver
        except NoOpenBrowser:
            self.sl.open_browser(self.host, 'chrome')
            return self.sl.driver

    @property
    def sl(self) -> SeleniumLibrary:
        try:
            return self._get_sl()
        except RuntimeError:
            self.debug('Importing %s' % self.sl_string)
            self.builtin.import_library(self.sl_string)
            return self._get_sl()

    def _get_sl(self):  # Do to ease mocking
        return self.builtin.get_library_instance(self.sl_string)

    def _get_url(self):
        return self.driver.current_url

    def _wait_page_ready(self, url):
        wait_time = time.time() + self.page_timeout
        while time.time() < wait_time:
            if self._get_url() == url:
                self.info('Current page loaded.')
                return True
        raise AssertionError('Page %s was not found' % url)

    def close(self):
        """Closes all currently active browsers."""
        self.sl.close_all_browsers()


class PageObject(CTX):

    def go_to(self, page_lib: str):
        """Go To Given page.

        Opens browser is browser is not open.
        """
        self._set_search_order(self.__class__.__name__)
        page_lib = self._get_page(page_lib)
        location = self._get_url()
        if location != page_lib.page_url:
            self.sl.go_to(page_lib.page_url)

    def location_should_be(self, page_lib: str):
        self._set_search_order(self.__class__.__name__)
        page_lib = self._get_page(page_lib)
        location = self._get_url()
        assert location == page_lib.page_url

    def _get_page(self, page: str):
        """Returns the desired page object from Robot Framework library cache.

        If library is not found, will import the page object.
        """
        page = 'pageobject.%s' % page
        try:
            lib = self.builtin.get_library_instance(page)
        except RuntimeError:
            self.builtin.import_library(page)
            lib = self.builtin.get_library_instance(page)
        self._set_search_order(page)
        return lib

    def _set_search_order(self, page: str):
        """Currently active library is top of RF library search order."""
        if not page.startswith('pageobject'):
            page = 'pageobject.%s' % page
        old_order = self.builtin.set_library_search_order()
        if page in old_order:
            old_order = list(old_order)
            old_order.remove(page)
            old_order = tuple(old_order)
        new_order = (page,) + old_order
        self.debug('Setting library search order to %s' % str(new_order))
        self.builtin.set_library_search_order(*new_order)
