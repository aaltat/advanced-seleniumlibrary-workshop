from pageobject.pageobject import CTX


class Welcome(CTX):

    def __init__(self):
        CTX.__init__(self)
        self.page_url = '%swelcome.html' % self.host

    def title_should_be_correct(self):
        title = self.driver.title
        assert title == 'Welcome Page'
